"""etvl_text.py - Text ETVL pipeline.

Author: Denise Case
Date: 2026-08-23

Practice key Python skills related to:
    - ETVL pipeline structure (Extract, Transform, Verify, Load)
    - reading text files line by line
    - counting lines, words, and characters
    - keyword-only function arguments
    - error handling with raise
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
        None.
    """
    for key in ("lines", "words", "chars"):
        # Handle known possible error: the key is missing.
        if key not in summary:
            raise KeyError(f"Missing summary key: {key}")

        # Handle known possible error: count is negative.
        if summary[key] < 0:
            raise ValueError(f"Invalid {key} count: {summary[key]}")


# === L: LOAD ===


def load_summary_report(
    *,
    summary: dict[str, int],
    out_path: Path,
) -> None:
    """L: Write summary to a text file in data/processed.

    Arguments:
        summary: Dictionary with counts for 'lines', 'words', and 'chars'.
        out_path: Path to output text file.

    Returns:
        None.
    """
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with out_path.open("w", encoding="utf-8") as f:
        f.write("Text File Summary\n")
        f.write(f"Lines: {summary['lines']}\n")
        f.write(f"Words: {summary['words']}\n")
        f.write(f"Characters: {summary['chars']}\n")


# === CALL THIS PIPELINE FROM app.py ===

# The main app.py file declares the data-specific choices:
#
#   TXT_INPUT  = data/raw/romeo_and_juliet.txt
#   TXT_OUTPUT = data/processed/txt_summary.txt
#
# app.py calls this function and passes those values in:
#
#   run_etvl_text(
#       input_file=TXT_INPUT,
#       output_file=TXT_OUTPUT,
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


def run_etvl_text(
    *,
    input_file: Path,
    output_file: Path,
    log: logging.Logger,
) -> None:
    """Run the full text ETVL pipeline.

    Arguments:
        input_file: Path to the input text file.
        output_file: Path to the output text file.
        log: Logger for logging messages.

    Returns:
        None.
    """
    log.info("TXT: START")

    # E: Read raw data.
    lines = extract_lines(
        file_path=input_file,
    )

    # T: Calculate counts.
    summary = transform_line_word_char_counts(
        lines=lines,
    )

    # V: Verify results before writing.
    verify_summary(
        summary=summary,
    )

    # L: Write results to disk.
    load_summary_report(
        summary=summary,
        out_path=output_file,
    )

    log.info("TXT: wrote %s", output_file)
    log.info("TXT: END")
