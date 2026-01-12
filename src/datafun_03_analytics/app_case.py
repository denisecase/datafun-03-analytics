"""app_case.py - Project script (example).

Author: Denise Case
Date: 2026-01

Practice key Python skills:


OBS:
  Don't edit this file - it should remain a working example.
"""

# === DECLARE IMPORTS (BRING IN FREE CODE) ===

import logging
from pathlib import Path
from typing import Final

# External (must be listed in pyproject.toml)
from datafun_toolkit.logger import get_logger, log_header

# === CONFIGURE LOGGER ONCE PER MODULE (FILE) ===

LOG: logging.Logger = get_logger("P03", level="DEBUG")

# === DECLARE GLOBAL CONSTANTS ===

# Find the current working directory (cwd) using pathlib.
# Use UPPER_SNAKE_CASE for constant names.
# Use `type hints` with Final for constants.

ROOT_DIR: Final[Path] = Path.cwd()


# === DEFINE THE MAIN FUNCTION ===


def main() -> None:
    """Entry point for the script. Creates files as visible artifacts for Git."""
    log_header(LOG, "Analytics: Read, Process, and Write Data")

    LOG.info("START main()")

    LOG.info("END main()")


# === CONDITIONAL EXECUTION GUARD ===

if __name__ == "__main__":
    main()
