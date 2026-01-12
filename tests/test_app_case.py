# tests/test_app_case.py
#
# Simple, clear pytest examples.
# Show how to test file-writing functions without touching
# the real project folder, and how to avoid slow sleeps.
#
# Assumptions:
# - module is importable
# - pytest running from project root
#
# Run:
#   uv run pytest


from datafun_03_analytics import app_case


def test_ok():
    assert True


def test_app_case_exists():
    assert app_case is not None
