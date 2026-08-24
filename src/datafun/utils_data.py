"""src/datafun/data_utils.py - Utility functions for the project.

These functions do the reusable work:

- load a file,
- look at the data,
- describe it.

Each one receives everything it needs when the calling code
"passes in" information via the parentheses (think of them as the
only doorway into a function).

To reuse the function, just pass in different "arguments".

OBS: You should read, but should not need to modify this file.

RUN:
  No need.
  We don't usually run supporting modules like this one directly.
  This file exists to move messy repeatable instructions
  out of the main script.
"""


# === DECLARE IMPORTS (BRING IN FREE CODE) ===

import logging

import pandas as pd

# === DECLARE A FUNCTION TO INSPECT THE DATA ===


def inspect(df: pd.DataFrame, grain: str, log: logging.Logger) -> str:
    """Get a formatted inspection string from the data.

    Ask the data about itself.
    No need to type column names by hand - the data knows.

    Arguments:
        df: the loaded pandas DataFrame (a 2-dimensional table like an Excel sheet).
        grain: what one row represents.
        log: the logger to send progress messages to.

    Returns:
        a formatted multi-line string.
    """
    log.info("START inspect")

    # Get the count of rows.
    row_count: int = len(df)

    # Get the count of columns.
    column_count: int = len(df.columns)

    # Get a list of column names.
    column_names: list[str] = list(df.columns)

    # Get the first few rows of data
    first_rows: pd.DataFrame = df.head()

    # Log the facts Python discovered about the data.
    log.info("   row_count:    %s", row_count)
    log.info("   column_count: %s", column_count)
    log.info("   column_names: %s", column_names)

    # Build a readable string to return to the calling code.
    # Use a multi-line string (triple quotes) to make it easy to read.
    # Use a formatted string (f before the opening) so we can pass in information
    inspection_string: str = f"""
----------------
Data Inspection:
----------------
    One row means: {grain}
    Row count: {row_count}
    Column count: {column_count}
    Column names: {column_names}

---------------
First Few Rows:
---------------
{first_rows}
"""

    log.info("END inspect. Returning inspection_string.")
    return inspection_string


# === DECLARE A FUNCTION TO DESCRIBE THE DATA ===


def get_analyst_description(
    grain: str,
    target: str,
    feature: str,
    why: str,
    log: logging.Logger,
) -> str:
    """Get a formatted summary string of the analyst description.

    These are the analyst's declarations, written after looking at the data.
    This is critical analyst work: look, then say what one row means,
    which of the columns might be a target we could predict,
    which of the columns might be a feature we could use if we
    were to build a model to predict the target,
    and why we think that feature might be related to the target.

    Arguments:
        grain: what one row means.
        target: a thing we could try to predict.
        feature: a feature (clue / indicator / column) that might help.
        why: why this feature might help predict the target.
        log: the logger to write progress to.

    Returns:
        a formatted multi-line string.
    """
    log.info("START get_analyst_description")

    summary_string: str = f"""
--------------------------------------------------------
Analyst Data Description (and Possible Prediction Plan):
--------------------------------------------------------
    A row represents:           {grain}
    A target we might predict:  {target}
    A feature that might help:  {feature}
    Why the feature might help: {why}
"""

    log.info("END get_analyst_description. Returning summary_string.")
    return summary_string
