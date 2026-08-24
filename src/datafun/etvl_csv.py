"""etvl_csv.py - CSV ETVL pipeline.

Author: Denise Case
Date: 2026-08-23

Practice key Python skills related to:
    - ETVL pipeline structure (Extract, Transform, Verify, Load)
    - reading CSV files using the csv module
    - keyword-only function arguments
    - error handling with raise
    - calculating statistics with the statistics module
    - writing results to a text file

OBS:
  This file is part of the working example project.
  First, run and understand the example as provided.
  When you take ownership of the project, adapt this pipeline
  to process data for your new problem.

RUN:
  No need.
  We don't usually run supporting modules like this one directly.
"""

# === DECLARE IMPORTS (BRING IN FREE CODE) ===

import logging
from pathlib import Path

from datafun.utils_etvl import (
    extract_csv_rows,
    load_stats_report,
    transform_column_to_floats,
    transform_column_to_stats,
    verify_stats,
)

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
#   E = Extract   - read raw data from a source (file, database, API)
#   T = Transform - clean, filter, or calculate from the raw data
#   V = Verify    - check that results are valid before writing
#   L = Load      - write the results to an output file
#
# Each step is a separate function with a single responsibility.
# This makes each step easy to test, debug, and reuse.
#
# The reusable ETVL functions are imported from utils_etvl.py.
# This module composes those functions into the CSV pipeline.


# === CALL THIS PIPELINE FROM app.py ===

# The main app.py file declares the data-specific choices:
#
#   CSV_INPUT   = data/raw/2020_happiness.csv
#   CSV_OUTPUT  = data/processed/csv_ladder_score_stats.txt
#   CSV_COLUMN  = Ladder score
#   CSV_GRAIN   = one country
#
# app.py calls this function and passes those values in:
#
#   run_etvl_csv(
#       input_file=CSV_INPUT,
#       output_file=CSV_OUTPUT,
#       column_name=CSV_COLUMN,
#       grain=CSV_GRAIN,
#       log=LOG,
#   )
#
# Each named argument provides one value this function needs:
#
#   input_file  = the CSV file to read
#   output_file = the text file to write
#   column_name = the numeric column to analyze
#   grain       = what one row represents
#   log         = where to send progress messages
#
# Notice that the names on the LEFT belong to this function.
# The values on the RIGHT are declared in app.py.
#
# These are keyword-only arguments.
# The * below means each argument must be passed by name.


# === FULL PIPELINE ===

# This function composes the four steps into a single callable pipeline.
# Each step receives the output of the previous step.
# The logger is passed in as an argument so this function works in any context.


def run_etvl_csv(
    *,
    input_file: Path,
    output_file: Path,
    column_name: str,
    log: logging.Logger,
) -> None:
    """Run the full CSV ETVL pipeline.

    Arguments:
        input_file: Path to the input CSV file.
        output_file: Path to the output text file.
        column_name: Name of the numeric column to summarize.
        log: Logger for logging messages.

    Returns:
        None.
    """
    log.info("CSV: START")

    # === E: EXTRACT ===

    # csv.DictReader reads each row as a dictionary keyed by column name.
    # This makes it easy to access columns by name rather than by index.
    #
    # Defensive programming: always check that a file exists before reading it.
    # Always check that expected data is available before accessing it.
    # Use raise to signal an error the caller must handle.

    rows = extract_csv_rows(
        file_path=input_file,
        log=log,
    )

    # === T: TRANSFORM ===

    # First convert the selected column from raw strings to numeric values.
    # Empty and non-numeric values are skipped.

    values = transform_column_to_floats(
        rows=rows,
        column_name=column_name,
        log=log,
    )

    # The statistics module provides mean() and stdev().
    # stdev() requires at least two values - guard against a single-value list.

    stats = transform_column_to_stats(
        values=values,
        log=log,
    )

    # === V: VERIFY ===

    # Verification catches problems between Transform and Load.
    # It is cheaper to detect a bad result before writing it to disk.
    # Use raise to signal an error the caller must handle.

    verify_stats(
        stats=stats,
        log=log,
    )

    # === L: LOAD ===

    # Path.open("w") creates or overwrites a file.
    # Always create parent directories before writing
    # with mkdir(parents=True, exist_ok=True).
    # Use f-strings to format numeric output
    # to a consistent number of decimal places.

    load_stats_report(
        stats=stats,
        column_name=column_name,
        out_path=output_file,
        log=log,
    )

    log.info("CSV: wrote %s", output_file)
    log.info("CSV: END")
