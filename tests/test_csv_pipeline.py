"""tests/test_p3_csv_pipeline.py - Tests for case_csv_pipeline.py.

WHY: Professional Python projects include tests to verify that code runs
     correctly and to catch problems early when changes are made.
     Running tests is part of the standard workflow in every module.

OBS: You do not need to read or modify this file.
     These tests create minimal CSV files in a temporary folder
     that is automatically cleaned up after each test.
"""

from pathlib import Path

import pytest

from datafun.case_csv_pipeline import (
    extract_csv_scores,
    load_stats_report,
    transform_scores_to_stats,
    verify_stats,
)

# === extract_csv_scores ===


def test_extract_csv_scores_returns_floats(tmp_path: Path) -> None:
    """extract_csv_scores() returns a list of floats from the named column."""
    csv_file = tmp_path / "test.csv"
    csv_file.write_text("score\n7.5\n6.0\n8.2\n", encoding="utf-8")
    result = extract_csv_scores(file_path=csv_file, column_name="score")
    assert result == [7.5, 6.0, 8.2]


def test_extract_csv_scores_skips_empty_rows(tmp_path: Path) -> None:
    """extract_csv_scores() skips empty cells without failing."""
    csv_file = tmp_path / "test.csv"
    csv_file.write_text("score\n7.5\n\n6.0\n", encoding="utf-8")
    result = extract_csv_scores(file_path=csv_file, column_name="score")
    assert len(result) == 2


def test_extract_csv_scores_skips_non_numeric(tmp_path: Path) -> None:
    """extract_csv_scores() skips rows that cannot be converted to float."""
    csv_file = tmp_path / "test.csv"
    csv_file.write_text("score\n7.5\nnot_a_number\n6.0\n", encoding="utf-8")
    result = extract_csv_scores(file_path=csv_file, column_name="score")
    assert len(result) == 2


def test_extract_csv_scores_missing_file(tmp_path: Path) -> None:
    """extract_csv_scores() raises FileNotFoundError for a missing file."""
    with pytest.raises(FileNotFoundError):
        extract_csv_scores(file_path=tmp_path / "missing.csv", column_name="score")


def test_extract_csv_scores_missing_column(tmp_path: Path) -> None:
    """extract_csv_scores() raises KeyError when the column is not found."""
    csv_file = tmp_path / "test.csv"
    csv_file.write_text("other_col\n1.0\n", encoding="utf-8")
    with pytest.raises(KeyError):
        extract_csv_scores(file_path=csv_file, column_name="score")


# === transform_scores_to_stats ===


def test_transform_scores_to_stats_keys(tmp_path: Path) -> None:
    """transform_scores_to_stats() returns all expected keys."""
    stats = transform_scores_to_stats(scores=[1.0, 2.0, 3.0])
    assert set(stats.keys()) == {"count", "min", "max", "mean", "stdev"}


def test_transform_scores_to_stats_values() -> None:
    """transform_scores_to_stats() calculates correct values."""
    stats = transform_scores_to_stats(scores=[2.0, 4.0, 6.0])
    assert stats["count"] == 3.0
    assert stats["min"] == 2.0
    assert stats["max"] == 6.0
    assert stats["mean"] == pytest.approx(4.0)


def test_transform_scores_to_stats_empty_raises() -> None:
    """transform_scores_to_stats() raises ValueError for an empty list."""
    with pytest.raises(ValueError):
        transform_scores_to_stats(scores=[])


def test_transform_scores_to_stats_single_value() -> None:
    """transform_scores_to_stats() returns stdev of 0.0 for a single value."""
    stats = transform_scores_to_stats(scores=[5.0])
    assert stats["stdev"] == 0.0


# === verify_stats ===


def test_verify_stats_passes_valid_stats() -> None:
    """verify_stats() does not raise for valid stats."""
    verify_stats(
        stats={"count": 3.0, "min": 1.0, "max": 5.0, "mean": 3.0, "stdev": 1.0}
    )


def test_verify_stats_raises_missing_key() -> None:
    """verify_stats() raises KeyError when a required key is missing."""
    with pytest.raises(KeyError):
        verify_stats(stats={"count": 3.0, "min": 1.0, "max": 5.0, "mean": 3.0})


def test_verify_stats_raises_zero_count() -> None:
    """verify_stats() raises ValueError when count is zero."""
    with pytest.raises(ValueError):
        verify_stats(
            stats={"count": 0.0, "min": 1.0, "max": 5.0, "mean": 3.0, "stdev": 1.0}
        )


def test_verify_stats_raises_min_greater_than_max() -> None:
    """verify_stats() raises ValueError when min is greater than max."""
    with pytest.raises(ValueError):
        verify_stats(
            stats={"count": 3.0, "min": 9.0, "max": 1.0, "mean": 3.0, "stdev": 1.0}
        )


# === load_stats_report ===


def test_load_stats_report_creates_file(tmp_path: Path) -> None:
    """load_stats_report() creates a file at the given path."""
    out = tmp_path / "out.txt"
    load_stats_report(
        stats={"count": 3.0, "min": 1.0, "max": 5.0, "mean": 3.0, "stdev": 1.0},
        out_path=out,
    )
    assert out.exists()


def test_load_stats_report_content(tmp_path: Path) -> None:
    """load_stats_report() writes expected keys to the output file."""
    out = tmp_path / "out.txt"
    load_stats_report(
        stats={"count": 3.0, "min": 1.0, "max": 5.0, "mean": 3.0, "stdev": 1.0},
        out_path=out,
    )
    content = out.read_text(encoding="utf-8")
    assert "Count" in content
    assert "Mean" in content
