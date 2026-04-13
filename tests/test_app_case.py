"""tests/test_app_case.py - Smoke test for the example.

WHY: Professional Python projects include tests to verify that code runs
     correctly and to catch problems early when changes are made.
     Running tests is part of the standard workflow in every module.

OBS: You do not need to read or modify this file in Module 1.
     It exists so that `uv run pytest` passes on a clean project.
"""


def test_app_case_runs():
    """Confirm the example module runs without error."""
    from datafun.app_case import main

    main()
