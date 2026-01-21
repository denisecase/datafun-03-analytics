"""app_yourname.py - Project script.

TODO: Replace "yourname" in the filename with your actual name or alias.

TODO: Read the examples carefully. Choose your data source of one of the provided types.
TODO: Create and implement a new Python file (module) in this folder following the associated example.
TODO: Your module should have:
- an appropriate name like yourname_type_pipeline.py (e.g., smith_csv_pipeline.py)
- start with a docstring similar to the examples
- add imports at the top.
- define an extract function (E that reads data from data/raw into memory)
- define a transform function (T that processes the extracted data)
- define a load function (L that writes output to data/processed)
- define a run_pipeline() function that calls E, T, L, and adds a new output file to data/processed/.
TODO: Import and call your new module run_pipeline function in this script.

Author: Your Name or Alias
Date: 2026-01

Practice key Python skills:
- pathlib for cross-platform paths
- logging (preferred over print)
- calling functions from modules
- clear ETL pipeline stages:
  E = Extract (read, get data from source into memory)
  T = Transform (process, change data in memory)
  L = Load (write results, to data/processed or other destination)

OBS:
  This is your file to practice and customize.
  Find the TODO comments, and as you complete each task, remove the TODO note.
"""


# === DECLARE IMPORTS (BRING IN FREE CODE) ===

# Imports from the Python standard library (free stuff that comes with Python).
import logging
from pathlib import Path
from typing import Final

# REQ: imports from external packages must be listed in pyproject.toml dependencies
from datafun_toolkit.logger import get_logger, log_header

# === IMPORT LOCAL MODULE FUNCTIONS ===
# REQ: imports from other modules in this project must use full package path
# TODO: create and import your own data pipeline module here. See the example code.


# === CONFIGURE LOGGER ONCE PER MODULE ===

LOG: logging.Logger = get_logger("P03", level="DEBUG")

# === DECLARE GLOBAL VARIABLES ===

ROOT_DIR: Final[Path] = Path.cwd()
DATA_DIR: Final[Path] = ROOT_DIR / "data"
RAW_DIR: Final[Path] = DATA_DIR / "raw"
PROCESSED_DIR: Final[Path] = DATA_DIR / "processed"

# === DEFINE THE MAIN FUNCTION THAT WILL CALL OUR FUNCTIONS ===


def main() -> None:
    """Entry point: run four simple ETVL pipelines."""
    log_header(LOG, "Pipelines: Read, Process, Verify, Write (ETVL)")
    LOG.info("START main()")

    # TODO: call your imported data pipeline that reads from data/raw and writes to data/processed.

    LOG.info("END main()")


# === CONDITIONAL EXECUTION GUARD ===

if __name__ == "__main__":
    main()
