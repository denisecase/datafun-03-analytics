"""etvl_xlsx.py - XLSX ETVL pipeline.

Author: Denise Case
Date: 2026-08-23

Practice key Python skills related to:
    - ETVL pipeline structure (Extract, Transform, Verify, Load)
    - reading Excel files using the openpyxl package
    - accessing cells by column letter
    - keyword-only function arguments
    - runtime type checking with isinstance()
    - counting word occurrences across strings
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
from typing import cast

# openpyxl is an external package - it must be listed in pyproject.toml dependencies.
# OBS: If you see "import openpyxl could not be resolved", open pyproject.toml,
#      find the dependencies section, and confirm openpyxl is listed there.
#      Then run: uv sync --extra dev --extra docs --upgrade
import openpyxl
from openpyxl.cell.cell import Cell

# === SKILL: READING AN EXCEL FILE WITH openpyxl ===

# openpyxl.load_workbook() opens an Excel file and returns a Workbook object.
# workbook.active returns the first (active) worksheet.
# sheet["A"] returns all cells in column A as a tuple.
# Each cell has a .value attribute containing the cell's contents.
# Cell values can be str, int, float, None, or other types.
# Use isinstance() to check the type before using the value.
# cast() tells the type checker what type to expect - it has no effect at runtime.


# === E: EXTRACT ===


def extract_xlsx_column_strings(
    *,
    file_path: Path,
    column_letter: str,
) -> list[str]:
    """E: Read an Excel file and extract string values from a column.

    Arguments:
        file_path: Path to input XLSX file.
        column_letter: Letter of the column to extract (e.g., 'A').

    Returns:
        List of non-empty string values from the specified column.
    """
    # Handle known possible error: no file at the path provided.
    if not file_path.exists():
        raise FileNotFoundError(f"Missing input file: {file_path}")

    workbook = openpyxl.load_workbook(file_path)

    # active returns the first worksheet - the one visible when the file opens.
    sheet = workbook.active

    values: list[str] = []

    for cell in sheet[column_letter]:
        # cast() narrows the type for the type checker - no runtime effect.
        cell = cast(Cell, cell)
        value = cell.value

        # Only keep non-empty string values.
        if isinstance(value, str) and value.strip():
            values.append(value)

    return values


# === T: TRANSFORM ===

# str.lower() converts a string to lowercase for case-insensitive comparison.
# str.count(target) returns how many times target appears in the string.
# Accumulate counts across all values with +=.


def transform_count_word(
    *,
    values: list[str],
    word: str,
) -> int:
    """T: Count occurrences of a word across all strings (case-insensitive).

    Arguments:
        values: List of strings to search.
        word: Word to count.

    Returns:
        Total count of occurrences of the word across all strings.
    """
    # Handle known possible error: no word provided by caller.
    if not word:
        raise ValueError("Word to count cannot be empty.")

    target = word.lower()
    count = 0

    for text in values:
        # Convert both to lowercase for case-insensitive matching.
        count += text.lower().count(target)

    return count


# === V: VERIFY ===


def verify_count(*, count: int) -> None:
    """V: Verify the count is valid.

    Arguments:
        count: The count to verify.

    Returns:
        None.
    """
    # Handle known possible error: count is negative.
    if count < 0:
        raise ValueError("Count cannot be negative.")


# === L: LOAD ===


def load_count_report(
    *,
    count: int,
    out_path: Path,
    word: str,
    column_letter: str,
) -> None:
    """L: Write the word count result to a text file in data/processed.

    Arguments:
        count: The word count to write.
        out_path: Path to output text file.
        word: The word that was counted.
        column_letter: The column letter that was processed.

    Returns:
        None.
    """
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with out_path.open("w", encoding="utf-8") as f:
        f.write("XLSX Word Count Result\n")
        f.write(f"Word: {word}\n")
        f.write(f"Column: {column_letter}\n")
        f.write(f"Count: {count}\n")


# === CALL THIS PIPELINE FROM app.py ===

# The main app.py file declares the data-specific choices:
#
#   XLSX_INPUT  = data/raw/Feedback.xlsx
#   XLSX_OUTPUT = data/processed/xlsx_feedback_github_count.txt
#   XLSX_COLUMN = A
#   XLSX_WORD   = GitHub
#
# app.py calls this function and passes those values in:
#
#   run_etvl_xlsx(
#       input_file=XLSX_INPUT,
#       output_file=XLSX_OUTPUT,
#       column_letter=XLSX_COLUMN,
#       word=XLSX_WORD,
#       log=LOG,
#   )
#
# Each named argument provides one value this function needs.
# The parameter name is on the LEFT of =.
# The value declared in app.py is on the RIGHT.
#
# The * below means each argument must be passed by name.


# === FULL PIPELINE ===

# This function composes the four steps into a single callable pipeline.
# Each step receives the output of the previous step.
# The logger is passed in as an argument so this function works in any context.


def run_etvl_xlsx(
    *,
    input_file: Path,
    output_file: Path,
    column_letter: str,
    word: str,
    log: logging.Logger,
) -> None:
    """Run the full XLSX ETVL pipeline.

    Arguments:
        input_file: Path to the input XLSX file.
        output_file: Path to the output text file.
        column_letter: Letter of the column to process.
        word: Word to count.
        log: Logger for logging messages.

    Returns:
        None.
    """
    log.info("XLSX: START")

    # E: Read string values from the selected column.
    values = extract_xlsx_column_strings(
        file_path=input_file,
        column_letter=column_letter,
    )

    # T: Count occurrences of the target word.
    count = transform_count_word(
        values=values,
        word=word,
    )

    # V: Verify the count before writing.
    verify_count(
        count=count,
    )

    # L: Write results to disk.
    load_count_report(
        count=count,
        out_path=output_file,
        word=word,
        column_letter=column_letter,
    )

    log.info("XLSX: wrote %s", output_file)
    log.info("XLSX: END")
