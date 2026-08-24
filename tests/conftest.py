# tests/conftest.py

"""Test configuration so tests can run without displaying plots."""

import matplotlib

matplotlib.use("Agg")
