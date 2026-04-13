"""case_xlsx_pipeline.py - XLSX ETVL pipeline.

Author: Denise Case
Date: 2026-04

  Practice key Python skills related to:
    - ETVL pipeline structure (Extract, Transform, Verify, Load)
    - reading Excel files using the openpyxl package
    - accessing cells by column letter
    - keyword-only function arguments
    - runtime type checking with isinstance()
    - counting word occurrences across strings
    - writing results to a text file

  Paths (relative to repo root):

    INPUT FILE:  data/raw/Feedback.xlsx
    OUTPUT FILE: data/processed/xlsx_feedback_github_count.txt

  Terminal command to run this file from the root project folder:

    uv run python -m datafun.case_xlsx_pipeline

OBS:
  Don't edit this file - it should remain a working example.
  Copy it, rename it, and modify your copy.
"""

# === DECLARE IMPORTS (BRING IN FREE CODE) ===

from pathlib import Path
from typing import Any, cast

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


def extract_xlsx_column_strings(*, file_path: Path, column_letter: str) -> list[str]:
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


def transform_count_word(*, values: list[str], word: str) -> int:
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
        None
    """
    # Handle known possible error: count is negative.
    if count < 0:
        raise ValueError("Count cannot be negative.")


# === L: LOAD ===


def load_count_report(
    *, count: int, out_path: Path, word: str, column_letter: str
) -> None:
    """L: Write the word count result to a text file in data/processed.

    Arguments:
        count: The word count to write.
        out_path: Path to output text file.
        word: The word that was counted.
        column_letter: The column letter that was processed.

    Returns:
        None
    """
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with out_path.open("w", encoding="utf-8") as f:
        f.write("XLSX Word Count Result\n")
        f.write(f"Word: {word}\n")
        f.write(f"Column: {column_letter}\n")
        f.write(f"Count: {count}\n")


# === FULL PIPELINE ===

# This function composes the four steps into a single callable pipeline.
# The logger is passed in as an argument so this function works in any context.


def run_xlsx_pipeline(*, raw_dir: Path, processed_dir: Path, logger: Any) -> None:
    """Run the full ETVL pipeline.

    Arguments:
        raw_dir: Path to data/raw directory.
        processed_dir: Path to data/processed directory.
        logger: Logger for logging messages.

    Returns:
        None
    """
    logger.info("XLSX: START")

    input_file = raw_dir / "Feedback.xlsx"
    output_file = processed_dir / "xlsx_feedback_github_count.txt"

    column_letter = "A"
    word = "GitHub"

    # E: Read string values from column A.
    values = extract_xlsx_column_strings(
        file_path=input_file,
        column_letter=column_letter,
    )

    # T: Count occurrences of the target word.
    count = transform_count_word(values=values, word=word)

    # V: Verify the count before writing.
    verify_count(count=count)

    # L: Write results to disk.
    load_count_report(
        count=count,
        out_path=output_file,
        word=word,
        column_letter=column_letter,
    )

    logger.info("XLSX: wrote %s", output_file)
    logger.info("XLSX: END")
