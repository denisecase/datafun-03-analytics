"""case_text_pipeline.py - Text ETVL pipeline.

Author: Denise Case
Date: 2026-04

  Practice key Python skills related to:
    - ETVL pipeline structure (Extract, Transform, Verify, Load)
    - reading text files line by line
    - counting lines, words, and characters
    - keyword-only function arguments
    - error handling with raise
    - writing results to a text file

  Paths (relative to repo root):

    INPUT FILE:  data/raw/romeo_and_juliet.txt
    OUTPUT FILE: data/processed/txt_summary.txt

  Terminal command to run this file from the root project folder:

    uv run python -m datafun.case_text_pipeline

OBS:
  Don't edit this file - it should remain a working example.
  Copy it, rename it, and modify your copy.
"""

# === DECLARE IMPORTS (BRING IN FREE CODE) ===

from pathlib import Path
from typing import Any

# === SKILL: READING A TEXT FILE LINE BY LINE ===

# file.readlines() reads the entire file and returns a list of strings.
# Each string is one line, including the newline character at the end.
# len(line.split()) counts the words in a line by splitting on whitespace.
# len(line) counts every character including spaces and newlines.


# === E: EXTRACT ===


def extract_lines(*, file_path: Path) -> list[str]:
    """E: Read a text file into a list of lines.

    Arguments:
        file_path: Path to input text file.

    Returns:
        List of lines from the text file.
    """
    # Handle known possible error: no file at the path provided.
    if not file_path.exists():
        raise FileNotFoundError(f"Missing input file: {file_path}")

    with file_path.open("r", encoding="utf-8") as f:
        return f.readlines()


# === T: TRANSFORM ===

# Iterate over the list of lines to accumulate counts.
# str.split() splits on any whitespace and returns a list of words.
# len() counts items in any sequence - lines, words, or characters.


def transform_line_word_char_counts(*, lines: list[str]) -> dict[str, int]:
    """T: Summarize a list of lines: line count, word count, character count.

    Arguments:
        lines: List of lines from the text file.

    Returns:
        Dictionary with counts for 'lines', 'words', and 'chars'.
    """
    line_count = len(lines)
    word_count = 0
    char_count = 0

    for line in lines:
        char_count += len(line)
        word_count += len(line.split())

    return {
        "lines": line_count,
        "words": word_count,
        "chars": char_count,
    }


# === V: VERIFY ===

# Check all expected keys are present and all counts are non-negative.
# Catching this before Load prevents writing a corrupt result to disk.


def verify_summary(*, summary: dict[str, int]) -> None:
    """V: Verify the summary has expected keys and non-negative values.

    Arguments:
        summary: Dictionary with counts for 'lines', 'words', and 'chars'.

    Returns:
        None
    """
    for key in ("lines", "words", "chars"):
        # Handle known possible error: the key is missing.
        if key not in summary:
            raise KeyError(f"Missing summary key: {key}")
        # Handle known possible error: count is negative.
        if summary[key] < 0:
            raise ValueError(f"Invalid {key} count: {summary[key]}")


# === L: LOAD ===


def load_summary_report(*, summary: dict[str, int], out_path: Path) -> None:
    """L: Write summary to a text file in data/processed.

    Arguments:
        summary: Dictionary with counts for 'lines', 'words', and 'chars'.
        out_path: Path to output text file.

    Returns:
        None
    """
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with out_path.open("w", encoding="utf-8") as f:
        f.write("Text File Summary\n")
        f.write(f"Lines: {summary['lines']}\n")
        f.write(f"Words: {summary['words']}\n")
        f.write(f"Characters: {summary['chars']}\n")


# === FULL PIPELINE ===

# This function composes the four steps into a single callable pipeline.
# The logger is passed in as an argument so this function works in any context.


def run_text_pipeline(*, raw_dir: Path, processed_dir: Path, logger: Any) -> None:
    """Run the full ETVL pipeline.

    Arguments:
        raw_dir: Path to data/raw directory.
        processed_dir: Path to data/processed directory.
        logger: Logger for logging messages.

    Returns:
        None
    """
    logger.info("TXT: START")

    input_file = raw_dir / "romeo_and_juliet.txt"
    output_file = processed_dir / "txt_summary.txt"

    # E: Read raw data.
    lines = extract_lines(file_path=input_file)

    # T: Calculate counts.
    summary = transform_line_word_char_counts(lines=lines)

    # V: Verify results before writing.
    verify_summary(summary=summary)

    # L: Write results to disk.
    load_summary_report(summary=summary, out_path=output_file)

    logger.info("TXT: wrote %s", output_file)
    logger.info("TXT: END")
