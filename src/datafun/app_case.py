"""app_case.py - Project script (example).

Author: Denise Case
Date: 2026-01

Practice key Python skills:
- pathlib for cross-platform paths
- logging (preferred over print)
- calling functions from modules
- clear ETVL pipeline stages:
  E = Extract (read, get data from source into memory)
  T = Transform (process, change data in memory)
  V = Verify (check, validate data in memory)
  L = Load (write results, to data/processed or other destination)

Terminal command to run this file from the root project folder:

    uv run python -m datafun.app_case

OBS:
  Don't edit this file - it should remain a working example.
  Copy it, rename it, and modify your copy.
"""


# === DECLARE IMPORTS (BRING IN FREE CODE) ===

# Imports from the Python standard library (free stuff that comes with Python).
import logging
from pathlib import Path
from typing import Final

# REQ: imports from external packages must be listed in pyproject.toml dependencies
from datafun_toolkit.logger import get_logger, log_header, log_path

# === IMPORT LOCAL MODULE FUNCTIONS ===
# REQ: imports from other modules in this project must use full package path
from datafun.case_csv_pipeline import run_csv_pipeline
from datafun.case_json_pipeline import run_json_pipeline
from datafun.case_text_pipeline import run_text_pipeline
from datafun.case_xlsx_pipeline import run_xlsx_pipeline

# === CONFIGURE LOGGER ONCE PER MODULE ===

LOG: logging.Logger = get_logger("P03", level="DEBUG")

# === DECLARE GLOBAL VARIABLES ===

ROOT_DIR: Final[Path] = Path.cwd()
DATA_DIR: Final[Path] = ROOT_DIR / "data"
RAW_DIR: Final[Path] = DATA_DIR / "raw"
PROCESSED_DIR: Final[Path] = DATA_DIR / "processed"

# === DEFINE THE MAIN FUNCTION THAT WILL CALL OUR FUNCTIONS ===


def main() -> None:
    """Entry point for the script.

    Entry point: run four simple ETVL pipelines.

    log_header() logs a standard run header.
    log_path() logs repo-relative paths (privacy-safe).

    Arguments: None.
    Returns: None.
    """
    log_header(LOG, "P03")

    LOG.info("========================")
    LOG.info("START main()")
    LOG.info("========================")

    log_path(LOG, "ROOT_DIR", ROOT_DIR)
    log_path(LOG, "PROCESSED_DIR", PROCESSED_DIR)

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    # Call each pipeline. Each reads from data/raw and writes to data/processed.
    run_csv_pipeline(raw_dir=RAW_DIR, processed_dir=PROCESSED_DIR, logger=LOG)
    run_xlsx_pipeline(raw_dir=RAW_DIR, processed_dir=PROCESSED_DIR, logger=LOG)
    run_json_pipeline(raw_dir=RAW_DIR, processed_dir=PROCESSED_DIR, logger=LOG)
    run_text_pipeline(raw_dir=RAW_DIR, processed_dir=PROCESSED_DIR, logger=LOG)

    LOG.info("========================")
    LOG.info("Executed successfully!")
    LOG.info("========================")


# === CONDITIONAL EXECUTION GUARD ===

# WHY: If running this file as a script, then call main() function.
# OBS: This is standard Python "boilerplate".

if __name__ == "__main__":
    main()
