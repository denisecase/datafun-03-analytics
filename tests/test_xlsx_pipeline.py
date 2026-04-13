"""tests/test_xlsx_pipeline.py - Tests for case_xlsx_pipeline.py.

WHY: Professional Python projects include tests to verify that code runs
     correctly and to catch problems early when changes are made.
     Running tests is part of the standard workflow in every module.

OBS: You do not need to read or modify this file.
     These tests create minimal Excel files using openpyxl in a temporary
     folder that is automatically cleaned up after each test.
"""

from pathlib import Path

import openpyxl
import pytest

from datafun.case_xlsx_pipeline import (
    extract_xlsx_column_strings,
    load_count_report,
    transform_count_word,
    verify_count,
)

# === Fixtures ===


def make_xlsx(path: Path, column_a_values: list) -> Path:
    """Create a minimal Excel file with values in column A."""
    wb = openpyxl.Workbook()
    ws = wb.active
    if ws is None:
        raise RuntimeError("Failed to create active worksheet")
    for value in column_a_values:
        ws.append([value])
    wb.save(path)
    return path


# === extract_xlsx_column_strings ===


def test_extract_xlsx_column_strings_returns_strings(tmp_path: Path) -> None:
    """extract_xlsx_column_strings() returns non-empty string values."""
    xlsx_file = make_xlsx(tmp_path / "test.xlsx", ["hello", "world", "python"])
    result = extract_xlsx_column_strings(file_path=xlsx_file, column_letter="A")
    assert result == ["hello", "world", "python"]


def test_extract_xlsx_column_strings_skips_non_strings(tmp_path: Path) -> None:
    """extract_xlsx_column_strings() skips non-string cell values."""
    xlsx_file = make_xlsx(tmp_path / "test.xlsx", ["hello", 42, None, "world"])
    result = extract_xlsx_column_strings(file_path=xlsx_file, column_letter="A")
    assert result == ["hello", "world"]


def test_extract_xlsx_column_strings_skips_empty_strings(tmp_path: Path) -> None:
    """extract_xlsx_column_strings() skips empty or whitespace-only strings."""
    xlsx_file = make_xlsx(tmp_path / "test.xlsx", ["hello", "   ", "", "world"])
    result = extract_xlsx_column_strings(file_path=xlsx_file, column_letter="A")
    assert result == ["hello", "world"]


def test_extract_xlsx_column_strings_missing_file(tmp_path: Path) -> None:
    """extract_xlsx_column_strings() raises FileNotFoundError for a missing file."""
    with pytest.raises(FileNotFoundError):
        extract_xlsx_column_strings(
            file_path=tmp_path / "missing.xlsx", column_letter="A"
        )


# === transform_count_word ===


def test_transform_count_word_basic() -> None:
    """transform_count_word() counts occurrences of a word."""
    result = transform_count_word(
        values=["I use GitHub", "GitHub is great", "no match here"],
        word="GitHub",
    )
    assert result == 2


def test_transform_count_word_case_insensitive() -> None:
    """transform_count_word() matches regardless of case."""
    result = transform_count_word(values=["github GITHUB GitHub"], word="github")
    assert result == 3


def test_transform_count_word_no_matches() -> None:
    """transform_count_word() returns 0 when word is not found."""
    result = transform_count_word(values=["hello world"], word="python")
    assert result == 0


def test_transform_count_word_empty_word_raises() -> None:
    """transform_count_word() raises ValueError for an empty word."""
    with pytest.raises(ValueError):
        transform_count_word(values=["hello"], word="")


# === verify_count ===


def test_verify_count_passes_zero() -> None:
    """verify_count() does not raise for a count of zero."""
    verify_count(count=0)


def test_verify_count_passes_positive() -> None:
    """verify_count() does not raise for a positive count."""
    verify_count(count=42)


def test_verify_count_raises_negative() -> None:
    """verify_count() raises ValueError for a negative count."""
    with pytest.raises(ValueError):
        verify_count(count=-1)


# === load_count_report ===


def test_load_count_report_creates_file(tmp_path: Path) -> None:
    """load_count_report() creates a file at the given path."""
    out = tmp_path / "out.txt"
    load_count_report(count=5, out_path=out, word="GitHub", column_letter="A")
    assert out.exists()


def test_load_count_report_content(tmp_path: Path) -> None:
    """load_count_report() writes word, column, and count to the output file."""
    out = tmp_path / "out.txt"
    load_count_report(count=5, out_path=out, word="GitHub", column_letter="A")
    content = out.read_text(encoding="utf-8")
    assert "GitHub" in content
    assert "Count: 5" in content
    assert "Column: A" in content
