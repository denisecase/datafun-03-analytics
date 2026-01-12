"""app_yourname.py - Project script.

TODO: Replace "yourname" in the filename with your actual name or alias.

Author: Your Name or Alias
Date: 2026-01

  Practice key Python skills:


OBS:
  This is your file to practice and customize.
  Find the TODO comments, and as you complete each task, remove the TODO note.
"""


# === DECLARE IMPORTS (BRING IN FREE CODE) ===

# Imports from the Python standard library (free stuff that comes with Python).
import logging

# Imports from external libraries (these must be listed in pyproject.toml).
from datafun_toolkit.logger import get_logger

# === CONFIGURE LOGGER ONCE PER MODULE (FILE) ===

LOG: logging.Logger = get_logger("P03", level="DEBUG")

# === DECLARE SOME GLOBAL VARIABLES ===


# === DEFINE THE MAIN FUNCTION THAT WILL CALL OUR FUNCTIONS ===


def main() -> None:
    """Entry point for the script.

    Arguments: None (nothing is passed in the parentheses after the `main`).

    Returns: None (nothing is returned when this function runs).

    This function creates what we call `side effects` -
    like logging output to the console and a file.
    """
    LOG.info("END main()")


# === CONDITIONAL EXECUTION GUARD ===

# WHY: If running this file as a script, then call main() function.
# OBS: This is just standard Python boilerplate.
# OBS: We copy and paste it and do not bother to memorize it.

if __name__ == "__main__":
    main()
