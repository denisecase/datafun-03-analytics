"""tests/test_etvl_json.py - Tests for etvl_json.py.

WHY: Professional Python projects include tests to verify that code runs
     correctly and to catch problems early when changes are made.
     Running tests is part of the standard workflow in every module.

OBS: You do not need to read or modify this file.
     These tests create minimal JSON files in a temporary folder
     that is automatically cleaned up after each test.
"""

import json
import logging
from pathlib import Path

from datafun.etvl_json import run_etvl_json


def test_run_etvl_json(tmp_path: Path) -> None:
    """Confirm the JSON ETVL pipeline runs and creates output."""
    input_file = tmp_path / "input.json"
    output_file = tmp_path / "output.txt"

    data = {
        "people": [
            {"name": "Ada", "craft": "ISS"},
            {"name": "Grace", "craft": "ISS"},
            {"name": "Katherine", "craft": "Tiangong"},
        ]
    }
    input_file.write_text(json.dumps(data), encoding="utf-8")

    log = logging.getLogger("test_etvl_json")

    run_etvl_json(
        input_file=input_file,
        output_file=output_file,
        list_key="people",
        craft_key="craft",
        log=log,
    )

    assert output_file.exists()
    assert output_file.read_text(encoding="utf-8").strip()
