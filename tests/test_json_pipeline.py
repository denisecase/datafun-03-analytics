"""tests/test_json_pipeline.py - Tests for case_json_pipeline.py.

WHY: Professional Python projects include tests to verify that code runs
     correctly and to catch problems early when changes are made.
     Running tests is part of the standard workflow in every module.

OBS: You do not need to read or modify this file.
     These tests create minimal JSON files in a temporary folder
     that is automatically cleaned up after each test.
"""

import json
from pathlib import Path

import pytest

from datafun.case_json_pipeline import (
    extract_people_list,
    load_counts_report,
    transform_count_by_craft,
    verify_counts,
)

# === extract_people_list ===


def test_extract_people_list_returns_dicts(tmp_path: Path) -> None:
    """extract_people_list() returns a list of dictionaries."""
    json_file = tmp_path / "test.json"
    json_file.write_text(
        json.dumps({"people": [{"name": "Alice", "craft": "ISS"}]}),
        encoding="utf-8",
    )
    result = extract_people_list(file_path=json_file, list_key="people")
    assert len(result) == 1
    assert result[0]["craft"] == "ISS"


def test_extract_people_list_missing_file(tmp_path: Path) -> None:
    """extract_people_list() raises FileNotFoundError for a missing file."""
    with pytest.raises(FileNotFoundError):
        extract_people_list(file_path=tmp_path / "missing.json", list_key="people")


def test_extract_people_list_not_a_dict(tmp_path: Path) -> None:
    """extract_people_list() raises TypeError if top-level JSON is not a dict."""
    json_file = tmp_path / "test.json"
    json_file.write_text(json.dumps([1, 2, 3]), encoding="utf-8")
    with pytest.raises(TypeError):
        extract_people_list(file_path=json_file, list_key="people")


def test_extract_people_list_missing_key_returns_empty(tmp_path: Path) -> None:
    """extract_people_list() returns empty list when key is missing."""
    json_file = tmp_path / "test.json"
    json_file.write_text(json.dumps({"other": []}), encoding="utf-8")
    result = extract_people_list(file_path=json_file, list_key="people")
    assert result == []


def test_extract_people_list_skips_non_dicts(tmp_path: Path) -> None:
    """extract_people_list() skips items that are not dictionaries."""
    json_file = tmp_path / "test.json"
    json_file.write_text(
        json.dumps({"people": [{"craft": "ISS"}, "not_a_dict", 42]}),
        encoding="utf-8",
    )
    result = extract_people_list(file_path=json_file, list_key="people")
    assert len(result) == 1


# === transform_count_by_craft ===


def test_transform_count_by_craft_counts_correctly() -> None:
    """transform_count_by_craft() returns correct counts per craft."""
    people = [
        {"craft": "ISS"},
        {"craft": "ISS"},
        {"craft": "Tiangong"},
    ]
    result = transform_count_by_craft(people_list=people, craft_key="craft")
    assert result["ISS"] == 2
    assert result["Tiangong"] == 1


def test_transform_count_by_craft_missing_key_uses_unknown() -> None:
    """transform_count_by_craft() uses 'Unknown' for missing craft key."""
    people = [{"name": "Alice"}]
    result = transform_count_by_craft(people_list=people, craft_key="craft")
    assert "Unknown" in result


def test_transform_count_by_craft_empty_list() -> None:
    """transform_count_by_craft() returns empty dict for empty input."""
    result = transform_count_by_craft(people_list=[], craft_key="craft")
    assert result == {}


# === verify_counts ===


def test_verify_counts_passes_valid() -> None:
    """verify_counts() does not raise for valid counts."""
    verify_counts(counts={"ISS": 3, "Tiangong": 2})


def test_verify_counts_raises_negative() -> None:
    """verify_counts() raises ValueError for a negative count."""
    with pytest.raises(ValueError):
        verify_counts(counts={"ISS": -1})


# === load_counts_report ===


def test_load_counts_report_creates_file(tmp_path: Path) -> None:
    """load_counts_report() creates a file at the given path."""
    out = tmp_path / "out.txt"
    load_counts_report(counts={"ISS": 3}, out_path=out)
    assert out.exists()


def test_load_counts_report_content(tmp_path: Path) -> None:
    """load_counts_report() writes craft names and counts to the output file."""
    out = tmp_path / "out.txt"
    load_counts_report(counts={"ISS": 3, "Tiangong": 2}, out_path=out)
    content = out.read_text(encoding="utf-8")
    assert "ISS: 3" in content
    assert "Tiangong: 2" in content


def test_load_counts_report_sorted(tmp_path: Path) -> None:
    """load_counts_report() writes craft names in alphabetical order."""
    out = tmp_path / "out.txt"
    load_counts_report(counts={"Tiangong": 2, "ISS": 3}, out_path=out)
    content = out.read_text(encoding="utf-8")
    assert content.index("ISS") < content.index("Tiangong")
