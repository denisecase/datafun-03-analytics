"""p3_xlsx_pipeline.py - XLSX ETVL pipeline.

ETVL:
  E = Extract (read)
  T = Transform (process)
  V = Verify (check)
  L = Load (write results to data/processed)

CUSTOM: We turn off some of our PyRight type checks when working with raw data pipelines.
WHY: We don't know what types things are until after we read them.
OBS: See pyproject.toml and the [tool.pyright] section for details.

CUSTOM: We use keyword-only function arguments.
In our functions, you'll see a `*,`.
The asterisk can appear anywhere in the list of parameters.
EVERY argument AFTER the asterisk must be passed
using the named keyword argument (also called kwarg), rather than by position.

WHY: Requiring named arguments prevents argument-order mistakes.
It also makes our function calls self-documenting, which can be especially helpful in
data-processing pipelines.
"""

from pathlib import Path
from typing import Any, cast

# DEBUG HELP: If you see "import "openpyxl" could not be resolved from source"
# Open pyproject.toml, find `dependencies` section,
# Ensure the package (openpyxl) is listed there.
# Set up your environment with the uv commands from the README.
import openpyxl
from openpyxl.cell.cell import Cell

# === DEFINE ETL STEP FUNCTIONS ===
# === We add a VERIFY step to check data integrity ===


def extract_xlsx_column_strings(*, file_path: Path, column_letter: str) -> list[str]:
    """E: Read an Excel file and extract string values from a column.

    Args:
        file_path: Path to input XLSX file.
        column_letter: Letter of the column to extract (e.g., 'A').

    Returns:
        List of string values from the specified column.
    """
    # Handle known possible error: no file at the path provided.
    if not file_path.exists():
        raise FileNotFoundError(f"Missing input file: {file_path}")

    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    values: list[str] = []

    for cell in sheet[column_letter]:
        cell = cast(Cell, cell)
        value = cell.value
        if isinstance(value, str) and value.strip():
            values.append(value)
    return values


def transform_count_word(*, values: list[str], word: str) -> int:
    """T: Count occurrences of a word across strings (case-insensitive).

    Args:
        values: List of strings to search.
        word: Word to count.

    Returns:
        Count of occurrences of the word.
    """
    # Handle known possible error: no word provided by caller.
    if not word:
        raise ValueError("Word to count cannot be empty.")

    target = word.lower()
    count = 0
    for text in values:
        count += text.lower().count(target)
    return count


def verify_count(*, count: int) -> None:
    """V: Verify the count is valid.

    Args:
        count: The count to verify.

    Raises:
        ValueError: If the count is negative.

    Returns:
        None
    """
    # Handle known possible error: count is negative.
    if count < 0:
        raise ValueError("Count cannot be negative.")


def load_count_report(
    *, count: int, out_path: Path, word: str, column_letter: str
) -> None:
    """L: Write the result to a text file in data/processed.

    Args:
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


# === DEFINE THE FULL PIPELINE FUNCTION ===


def run_xlsx_pipeline(*, raw_dir: Path, processed_dir: Path, logger: Any) -> None:
    """Run the full ETVL pipeline.

    Args:
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

    # E
    values = extract_xlsx_column_strings(
        file_path=input_file,
        column_letter=column_letter,
    )

    # T
    count = transform_count_word(values=values, word=word)

    # V
    verify_count(count=count)

    # L
    load_count_report(
        count=count, out_path=output_file, word=word, column_letter=column_letter
    )

    logger.info("XLSX: wrote %s", output_file)
    logger.info("XLSX: END")
