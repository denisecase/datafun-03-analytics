"""case_csv_pipeline.py - CSV ETVL pipeline.

Author: Denise Case
Date: 2026-04

  Practice key Python skills related to:
    - ETVL pipeline structure (Extract, Transform, Verify, Load)
    - reading CSV files using the csv module
    - keyword-only function arguments
    - error handling with raise
    - calculating statistics with the statistics module
    - writing results to a text file

  Paths (relative to repo root):

    INPUT FILE:  data/raw/2020_happiness.csv
    OUTPUT FILE: data/processed/csv_ladder_score_stats.txt

  Terminal command to run this file from the root project folder:

    uv run python -m datafun.case_csv_pipeline

OBS:
  Don't edit this file - it should remain a working example.
  Copy it, rename it, and modify your copy.
"""

# === DECLARE IMPORTS (BRING IN FREE CODE) ===

import csv
import statistics
from pathlib import Path
from typing import Any

# === SKILL: KEYWORD-ONLY ARGUMENTS ===

# In the functions below, you will see a bare asterisk (*,) in the parameter list.
# EVERY parameter listed AFTER the asterisk must be passed by NAME when calling the function.
# This is called a keyword-only argument (or kwarg).
#
# Example:
#   def my_func(*, name: str, count: int) -> None: ...
#
#   my_func(name="case", count=3)   # correct - named arguments
#   my_func("case", 3)              # TypeError - positional not allowed
#
# WHY: In data pipelines, argument order mistakes are hard to debug.
# Named arguments make every call self-documenting.


# === SKILL: ETVL PIPELINE STRUCTURE ===

# An ETVL pipeline processes data in four steps:
#   E = Extract  - read raw data from a source (file, database, API)
#   T = Transform - clean, filter, or calculate from the raw data
#   V = Verify   - check that results are valid before writing
#   L = Load     - write the results to an output file
#
# Each step is a separate function with a single responsibility.
# This makes each step easy to test, debug, and reuse.


# === E: EXTRACT ===

# csv.DictReader reads each row as a dictionary keyed by column name.
# This makes it easy to access columns by name rather than by index.
#
# Defensive programming: always check that a file exists before reading it.
# Always check that the expected column is present before accessing it.
# Use raise to signal an error the caller must handle.


def extract_csv_scores(*, file_path: Path, column_name: str) -> list[float]:
    """E: Read CSV and extract one numeric column as floats.

    Arguments:
        file_path: Path to input CSV file.
        column_name: Name of the column to extract.

    Returns:
        List of float values from the specified column.
    """
    # Handle known possible error: no file at the path provided.
    if not file_path.exists():
        raise FileNotFoundError(f"Missing input file: {file_path}")

    scores: list[float] = []
    with file_path.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        # Handle known possible error: missing expected column.
        if reader.fieldnames is None or column_name not in reader.fieldnames:
            raise KeyError(
                f"CSV missing expected column '{column_name}'. "
                f"Found: {reader.fieldnames}"
            )

        for row in reader:
            raw_value = (row.get(column_name) or "").strip()
            # Skip empty cells rather than failing the whole pipeline.
            if not raw_value:
                continue
            try:
                scores.append(float(raw_value))
            except ValueError:
                # Skip rows that do not convert cleanly to float.
                continue

    return scores


# === T: TRANSFORM ===

# The statistics module provides mean() and stdev().
# stdev() requires at least two values - guard against a single-value list.


def transform_scores_to_stats(*, scores: list[float]) -> dict[str, float]:
    """T: Calculate basic statistics for a list of floats.

    Arguments:
        scores: List of float values.

    Returns:
        Dictionary with keys: count, min, max, mean, stdev.
    """
    if not scores:
        raise ValueError("No numeric values found for analysis.")

    return {
        "count": float(len(scores)),
        "min": min(scores),
        "max": max(scores),
        "mean": statistics.mean(scores),
        # stdev() requires at least 2 values; return 0.0 for a single value.
        "stdev": statistics.stdev(scores) if len(scores) > 1 else 0.0,
    }


# === V: VERIFY ===

# Verification catches problems between Transform and Load.
# It is cheaper to detect a bad result before writing it to disk.
# Use raise to signal an error the caller must handle.


def verify_stats(*, stats: dict[str, float]) -> None:
    """V: Sanity-check the stats dictionary.

    Arguments:
        stats: Dictionary with statistics to verify.

    Returns:
        None
    """
    required = {"count", "min", "max", "mean", "stdev"}
    missing = required - set(stats.keys())
    # Handle known possible error: missing required keys.
    if missing:
        raise KeyError(f"Missing stats keys: {sorted(missing)}")

    # Handle known possible error: count must be positive.
    if stats["count"] <= 0:
        raise ValueError("Count must be positive.")

    # Handle known possible error: min cannot be greater than max.
    if stats["min"] > stats["max"]:
        raise ValueError("Min cannot be greater than max.")


# === L: LOAD ===

# Path.open("w") creates or overwrites a file.
# Always create parent directories before writing with mkdir(parents=True, exist_ok=True).
# Use f-strings to format numeric output to a consistent number of decimal places.


def load_stats_report(*, stats: dict[str, float], out_path: Path) -> None:
    """L: Write stats to a text file in data/processed.

    Arguments:
        stats: Dictionary with statistics to write.
        out_path: Path to output text file.

    Returns:
        None
    """
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with out_path.open("w", encoding="utf-8") as f:
        f.write("CSV Ladder Score Statistics\n")
        f.write(f"Count: {int(stats['count'])}\n")
        f.write(f"Minimum: {stats['min']:.2f}\n")
        f.write(f"Maximum: {stats['max']:.2f}\n")
        f.write(f"Mean: {stats['mean']:.2f}\n")
        f.write(f"Standard Deviation: {stats['stdev']:.2f}\n")


# === FULL PIPELINE ===

# This function composes the four steps into a single callable pipeline.
# Each step receives the output of the previous step.
# The logger is passed in as an argument so this function works in any context.


def run_csv_pipeline(*, raw_dir: Path, processed_dir: Path, logger: Any) -> None:
    """Run the full ETVL pipeline.

    Arguments:
        raw_dir: Path to data/raw directory.
        processed_dir: Path to data/processed directory.
        logger: Logger for logging messages.

    Returns:
        None
    """
    logger.info("CSV: START")

    input_file = raw_dir / "2020_happiness.csv"
    output_file = processed_dir / "csv_ladder_score_stats.txt"

    # E: Read raw data.
    scores = extract_csv_scores(file_path=input_file, column_name="Ladder score")

    # T: Calculate statistics.
    stats = transform_scores_to_stats(scores=scores)

    # V: Verify results before writing.
    verify_stats(stats=stats)

    # L: Write results to disk.
    load_stats_report(stats=stats, out_path=output_file)

    logger.info("CSV: wrote %s", output_file)
    logger.info("CSV: END")
