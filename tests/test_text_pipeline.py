"""tests/test_text_pipeline.py - Tests for case_text_pipeline.py.

WHY: Professional Python projects include tests to verify that code runs
     correctly and to catch problems early when changes are made.
     Running tests is part of the standard workflow in every module.

OBS: You do not need to read or modify this file.
     These tests create minimal text files in a temporary folder
     that is automatically cleaned up after each test.
"""

from pathlib import Path

import pytest

from datafun.case_text_pipeline import (
    extract_lines,
    load_summary_report,
    transform_line_word_char_counts,
    verify_summary,
)

# === extract_lines ===


def test_extract_lines_returns_list(tmp_path: Path) -> None:
    """extract_lines() returns a list of strings."""
    txt_file = tmp_path / "test.txt"
    txt_file.write_text("line one\nline two\n", encoding="utf-8")
    result = extract_lines(file_path=txt_file)
    assert isinstance(result, list)
    assert len(result) == 2


def test_extract_lines_preserves_content(tmp_path: Path) -> None:
    """extract_lines() preserves the text content of each line."""
    txt_file = tmp_path / "test.txt"
    txt_file.write_text("hello world\n", encoding="utf-8")
    result = extract_lines(file_path=txt_file)
    assert "hello world" in result[0]


def test_extract_lines_missing_file(tmp_path: Path) -> None:
    """extract_lines() raises FileNotFoundError for a missing file."""
    with pytest.raises(FileNotFoundError):
        extract_lines(file_path=tmp_path / "missing.txt")


# === transform_line_word_char_counts ===


def test_transform_counts_keys() -> None:
    """transform_line_word_char_counts() returns all expected keys."""
    result = transform_line_word_char_counts(lines=["hello world\n"])
    assert set(result.keys()) == {"lines", "words", "chars"}


def test_transform_counts_line_count() -> None:
    """transform_line_word_char_counts() counts lines correctly."""
    result = transform_line_word_char_counts(lines=["one\n", "two\n", "three\n"])
    assert result["lines"] == 3


def test_transform_counts_word_count() -> None:
    """transform_line_word_char_counts() counts words across all lines."""
    result = transform_line_word_char_counts(lines=["one two\n", "three\n"])
    assert result["words"] == 3


def test_transform_counts_empty_input() -> None:
    """transform_line_word_char_counts() returns zeros for empty input."""
    result = transform_line_word_char_counts(lines=[])
    assert result["lines"] == 0
    assert result["words"] == 0
    assert result["chars"] == 0


# === verify_summary ===


def test_verify_summary_passes_valid() -> None:
    """verify_summary() does not raise for valid summary."""
    verify_summary(summary={"lines": 10, "words": 50, "chars": 300})


def test_verify_summary_raises_missing_key() -> None:
    """verify_summary() raises KeyError when a required key is missing."""
    with pytest.raises(KeyError):
        verify_summary(summary={"lines": 10, "words": 50})


def test_verify_summary_raises_negative() -> None:
    """verify_summary() raises ValueError for a negative count."""
    with pytest.raises(ValueError):
        verify_summary(summary={"lines": -1, "words": 50, "chars": 300})


# === load_summary_report ===


def test_load_summary_report_creates_file(tmp_path: Path) -> None:
    """load_summary_report() creates a file at the given path."""
    out = tmp_path / "out.txt"
    load_summary_report(summary={"lines": 10, "words": 50, "chars": 300}, out_path=out)
    assert out.exists()


def test_load_summary_report_content(tmp_path: Path) -> None:
    """load_summary_report() writes lines, words, and chars to the output file."""
    out = tmp_path / "out.txt"
    load_summary_report(summary={"lines": 10, "words": 50, "chars": 300}, out_path=out)
    content = out.read_text(encoding="utf-8")
    assert "Lines: 10" in content
    assert "Words: 50" in content
    assert "Characters: 300" in content
