"""tests/test_etvl_xlsx.py - Tests for etvl_xlsx.py.

WHY: Professional Python projects include tests to verify that code runs
     correctly and to catch problems early when changes are made.
     Running tests is part of the standard workflow in every module.

OBS: You do not need to read or modify this file.
     These tests create minimal XLSX files in a temporary folder
     that is automatically cleaned up after each test.
"""

import logging
from pathlib import Path

from openpyxl import Workbook

from datafun.etvl_xlsx import run_etvl_xlsx


def test_run_etvl_xlsx(tmp_path: Path) -> None:
    """Confirm the XLSX ETVL pipeline runs and creates output."""
    input_file = tmp_path / "input.xlsx"
    output_file = tmp_path / "output.txt"

    workbook = Workbook()
    worksheet = workbook.active
    worksheet["A1"] = "GitHub was useful."
    worksheet["A2"] = "I used GitHub for my project."
    worksheet["A3"] = "Python was useful."
    workbook.save(input_file)

    log = logging.getLogger("test_etvl_xlsx")

    run_etvl_xlsx(
        input_file=input_file,
        output_file=output_file,
        column_letter="A",
        word="GitHub",
        log=log,
    )

    assert output_file.exists()
    assert output_file.read_text(encoding="utf-8").strip()
