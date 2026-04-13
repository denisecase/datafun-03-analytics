"""case_json_pipeline.py - JSON ETVL pipeline.

Author: Denise Case
Date: 2026-04

  Practice key Python skills related to:
    - ETVL pipeline structure (Extract, Transform, Verify, Load)
    - reading JSON files using the json module
    - walking JSON: dictionaries, lists, and nested structures
    - keyword-only function arguments
    - defensive programming for untrusted input
    - runtime type checking with isinstance()
    - writing results to a text file

  Paths (relative to repo root):

    INPUT FILE:  data/raw/astros.json
    OUTPUT FILE: data/processed/json_astronauts_by_craft.txt

  Terminal command to run this file from the root project folder:

    uv run python -m datafun.case_json_pipeline

OBS:
  Don't edit this file - it should remain a working example.
  Copy it, rename it, and modify your copy.
"""

# === DECLARE IMPORTS (BRING IN FREE CODE) ===

import json
from pathlib import Path
from typing import Any

# === SKILL: JSON DATA STRUCTURE ===

# JSON is a common format for exchanging data over the web.
# Python's json module reads JSON into native Python types:
#
#   JSON object  → Python dict   { "key": value }
#   JSON array   → Python list   [ value, value ]
#   JSON string  → Python str    "hello"
#   JSON number  → Python int or float
#   JSON boolean → Python bool   true → True
#   JSON null    → Python None
#
# JSON is hierarchical: lists and dicts can be nested inside each other.
# Example:
#   {
#     "people": [
#       { "name": "Oleg Kononenko", "craft": "ISS" },
#       { "name": "Jasmin Moghbeli", "craft": "ISS" }
#     ]
#   }
#
# json.load(file) returns the top-level structure - usually a dict.
# Use dict.get(key, default) to safely access keys that may be missing.


# === SKILL: DEFENSIVE PROGRAMMING FOR UNTRUSTED INPUT ===

# JSON is untrusted input: keys may be missing, values may be wrong types.
# Never assume a key exists. Never assume a value is the expected type.
# Use isinstance() to check types at runtime before using a value.
# Use dict.get(key, default) to handle missing keys without crashing.


# === E: EXTRACT ===


def extract_people_list(
    *, file_path: Path, list_key: str = "people"
) -> list[dict[str, Any]]:
    """E/V: Read JSON file and extract a list of dictionaries under list_key.

    Arguments:
        file_path: Path to input JSON file.
        list_key: Top-level key expected to map to a list (default: "people").

    Returns:
        A list of dictionaries from the JSON file.
    """
    # Handle known possible error: no file at the path provided.
    if not file_path.exists():
        raise FileNotFoundError(f"Missing input file: {file_path}")

    with file_path.open("r", encoding="utf-8") as f:
        # json.load() reads the entire file and returns a Python object.
        data: Any = json.load(f)

    # JSON top level should be a dict - verify before accessing keys.
    if not isinstance(data, dict):
        raise TypeError("Expected JSON top-level object to be a dictionary.")

    # Use dict.get() to safely retrieve the list - default to empty list if missing.
    value: Any = data.get(list_key, [])

    # Verify the value is actually a list before iterating.
    if not isinstance(value, list):
        raise TypeError(f"Expected {list_key!r} to be a list.")

    # Walk the list and keep only items that are dictionaries.
    # Each person record should be a dict with keys like "name" and "craft".
    people_list: list[dict[str, Any]] = []
    for item in value:
        if isinstance(item, dict):
            people_list.append(item)  # type: ignore[arg-type]

    return people_list


# === T: TRANSFORM ===

# dict.get(key, default) returns the default if the key is missing.
# counts.get(craft, 0) + 1 increments the count for each craft name seen.
# This is a common pattern for counting occurrences in a list.


def transform_count_by_craft(
    *, people_list: list[dict[str, Any]], craft_key: str = "craft"
) -> dict[str, int]:
    """T: Count people by craft.

    Arguments:
        people_list: List of person dictionaries.
        craft_key: Key to read craft name from (default: "craft").

    Returns:
        Dictionary mapping craft names to counts.
    """
    counts: dict[str, int] = {}

    for person in people_list:
        # Use dict.get() to safely access the craft key.
        craft: Any = person.get(craft_key, "Unknown")
        # Guard against non-string or empty values.
        if not isinstance(craft, str) or not craft.strip():
            craft = "Unknown"
        # Increment the count for this craft, starting at 0 if not yet seen.
        counts[craft] = counts.get(craft, 0) + 1

    return counts


# === V: VERIFY ===


def verify_counts(*, counts: dict[str, int]) -> None:
    """V: Verify counts are non-negative and craft names are not empty.

    Arguments:
        counts: Dictionary mapping craft names to counts.

    Returns:
        None
    """
    for craft, count in counts.items():
        # Handle known possible error: invalid craft name.
        if not craft.strip():
            raise ValueError(f"Invalid craft name: {craft!r}")
        # Handle known possible error: count is negative.
        if count < 0:
            raise ValueError(f"Invalid count for craft {craft!r}: {count}")


# === L: LOAD ===

# sorted() returns a new list in alphabetical order.
# This makes output consistent and predictable regardless of input order.


def load_counts_report(*, counts: dict[str, int], out_path: Path) -> None:
    """L: Write craft counts to a text file in data/processed.

    Arguments:
        counts: Dictionary mapping craft names to counts.
        out_path: Path to output text file.

    Returns:
        None
    """
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with out_path.open("w", encoding="utf-8") as f:
        f.write("Astronauts by spacecraft:\n")
        # Sort craft names alphabetically for consistent, readable output.
        for craft in sorted(counts):
            f.write(f"{craft}: {counts[craft]}\n")


# === FULL PIPELINE ===

# This function composes the four steps into a single callable pipeline.
# The logger is passed in as an argument so this function works in any context.


def run_json_pipeline(*, raw_dir: Path, processed_dir: Path, logger: Any) -> None:
    """Run the full ETVL pipeline.

    Arguments:
        raw_dir: Path to data/raw directory.
        processed_dir: Path to data/processed directory.
        logger: Logger for logging messages.

    Returns:
        None
    """
    logger.info("JSON: START")

    input_file = raw_dir / "astros.json"
    output_file = processed_dir / "json_astronauts_by_craft.txt"

    # E: Read raw data.
    people_list = extract_people_list(file_path=input_file, list_key="people")

    # T: Count people by craft.
    craft_counts = transform_count_by_craft(people_list=people_list, craft_key="craft")

    # V: Verify results before writing.
    verify_counts(counts=craft_counts)

    # L: Write results to disk.
    load_counts_report(counts=craft_counts, out_path=output_file)

    logger.info("JSON: wrote %s", output_file)
    logger.info("JSON: END")
