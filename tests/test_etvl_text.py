"""tests/test_etvl_text.py - Tests for etvl_text.py.

WHY: Professional Python projects include tests to verify that code runs
     correctly and to catch problems early when changes are made.
     Running tests is part of the standard workflow in every module.

OBS: You do not need to read or modify this file.
     These tests create minimal text files in a temporary folder
     that is automatically cleaned up after each test.
"""

import logging
from pathlib import Path

from datafun.etvl_text import run_etvl_text


def test_run_etvl_text(tmp_path: Path) -> None:
    """Confirm the text ETVL pipeline runs and creates output."""
    input_file = tmp_path / "input.txt"
    output_file = tmp_path / "output.txt"

    input_file.write_text(
        "First line.\nSecond line.\nThird line.\n",
        encoding="utf-8",
    )

    log = logging.getLogger("test_etvl_text")

    run_etvl_text(
        input_file=input_file,
        output_file=output_file,
        log=log,
    )

    assert output_file.exists()
    assert output_file.read_text(encoding="utf-8").strip()
