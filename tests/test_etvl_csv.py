"""tests/test_etvl_csv.py - Tests for etvl_csv.py.

WHY: Professional Python projects include tests to verify that code runs
     correctly and to catch problems early when changes are made.
     Running tests is part of the standard workflow in every module.

OBS: You do not need to read or modify this file.
     These tests create minimal CSV files in a temporary folder
     that is automatically cleaned up after each test.
"""

from pathlib import Path

"""tests/test_etvl_csv.py - Tests for etvl_csv.py.

WHY: Professional Python projects include tests to verify that code runs
     correctly and to catch problems early when changes are made.
     Running tests is part of the standard workflow in every module.

OBS: You do not need to read or modify this file.
     These tests create minimal CSV files in a temporary folder
     that is automatically cleaned up after each test.
"""

import csv
import logging

from datafun.etvl_csv import run_etvl_csv


def test_run_etvl_csv(tmp_path: Path) -> None:
    """Confirm the CSV ETVL pipeline runs and creates output."""
    input_file = tmp_path / "input.csv"
    output_file = tmp_path / "output.txt"

    with input_file.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["Ladder score"])
        writer.writeheader()
        writer.writerow({"Ladder score": "5.0"})
        writer.writerow({"Ladder score": "6.0"})
        writer.writerow({"Ladder score": "7.0"})

    log = logging.getLogger("test_etvl_csv")

    run_etvl_csv(
        input_file=input_file,
        output_file=output_file,
        column_name="Ladder score",
        log=log,
    )

    assert output_file.exists()
    assert output_file.read_text(encoding="utf-8").strip()
