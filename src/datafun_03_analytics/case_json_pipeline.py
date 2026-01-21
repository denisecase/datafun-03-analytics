"""p3_json_pipeline.py - JSON ETVL pipeline.

ETVL:
  E = Extract (read)
  T = Transform (process)
  V = Verify (check)
  L = Load (write results to data/processed)

This example is intentionally explicit about *walking JSON*:

- json.load(file) returns a Python dictionary (top-level object)
- dict.get("people", []) safely retrieves a nested list
- iteration is used to walk arrays (lists)
- each list element is expected to be a dictionary with keys such as "craft"

Core JSON Data Concepts:

- JSON is hierarchical (tree-structured)
- JSON arrays map to Python lists
- JSON objects map to Python dictionaries (key-value pairs)
- JSON is nested (lists and dictionaries can appear within each other)
- JSON is untrusted input (keys may be missing, values may be wrong types)
- JSON values are optional (no required keys)
- JSON types are runtime facts, not promises (no static typing or schema)

Runtime Validation and Defensive Access:

- Use isinstance() to verify value types at runtime
- Use dict.get(key, default) to handle missing keys safely
- Use iteration to walk arrays (lists)
- Apply defensive programming for unexpected or missing data
- Verify file existence before attempting to read JSON

CUSTOM: We turn off some of our PyRight type checks when working with raw data pipelines.
WHY: We don't know what types things are until after we read them.
OBS: See pyproject.toml and the [tool.pyright] section for details.

CUSTOM: We use keyword-only function arguments.
In our functions, you'll see a `*,`.
The asterisk can appear anywhere in the list of parameters.
EVERY argument AFTER the asterisk must be passed
using the named keyword argument (also called kwarg), rather than by position.

WHY: Requiring named arguments prevents argument-order mistakes.
It also makes our function calls self-documenting, which can be especially helpful in
data-processing pipelines.

Example JSON Data:

{
    "people": [
        {
            "craft": "ISS",
            "name": "Oleg Kononenko"
        }, ...
"""

import json
from pathlib import Path
from typing import Any

# === DEFINE ETL STEP FUNCTIONS ===
# === We add a VERIFY step to check data integrity ===


def extract_people_list(
    *, file_path: Path, list_key: str = "people"
) -> list[dict[str, Any]]:
    """E/V: Read JSON file and extract a list of dictionaries under list_key.

    Args:
        file_path: Path to input JSON file.
        list_key: Top-level key expected to map to a list (default: "people").

    Returns:
        A list of dictionaries from the JSON file.
    """
    if not file_path.exists():
        raise FileNotFoundError(f"Missing input file: {file_path}")

    with file_path.open("r", encoding="utf-8") as f:
        data: Any = json.load(f)

    if not isinstance(data, dict):
        raise TypeError("Expected JSON top-level object to be a dictionary.")

    value: Any = data.get(list_key, [])
    if not isinstance(value, list):
        raise TypeError(f"Expected {list_key!r} to be a list.")

    people_list: list[dict[str, Any]] = []
    for item in value:
        if isinstance(item, dict):
            # If it passes the right type check, add it to the list.
            # Just add a type ignore to silence the warnings - we have already checked the type.
            people_list.append(item)  # type: ignore[arg-type]

    return people_list


def transform_count_by_craft(
    *, people_list: list[dict[str, Any]], craft_key: str = "craft"
) -> dict[str, int]:
    """T/V: Count people by craft.

    Args:
        people_list: List of person dictionaries.
        craft_key: Key to read craft name from (default: "craft").

    Returns:
        Dictionary mapping craft names to counts.
    """
    counts: dict[str, int] = {}

    for person in people_list:
        craft: Any = person.get(craft_key, "Unknown")
        if not isinstance(craft, str) or not craft.strip():
            craft = "Unknown"
        counts[craft] = counts.get(craft, 0) + 1

    return counts


def verify_counts(*, counts: dict[str, int]) -> None:
    """V: Verify counts are non-negative and craft names are not empty.

    Args:
        counts: Dictionary mapping craft names to counts.

    Raises:
        ValueError: If any count is negative or craft name is invalid.

    Returns:
        None
    """
    for craft, count in counts.items():
        # Handle known possible error: invalid craft name after stripping off white space.
        if not craft.strip():
            raise ValueError(f"Invalid craft name: {craft!r}")
        # Handle known possible error: count is negative.
        if count < 0:
            raise ValueError(f"Invalid count for craft {craft!r}: {count}")


def load_counts_report(*, counts: dict[str, int], out_path: Path) -> None:
    """L: Write craft counts to a text file in data/processed.

    Args:
        counts: Dictionary mapping craft names to counts.
        out_path: Path to output text file.

    Returns:
        None
    """
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with out_path.open("w", encoding="utf-8") as f:
        f.write("Astronauts by spacecraft:\n")
        for craft in sorted(counts):
            f.write(f"{craft}: {counts[craft]}\n")


# === DEFINE THE FULL PIPELINE FUNCTION ===


def run_json_pipeline(*, raw_dir: Path, processed_dir: Path, logger: Any) -> None:
    """Run the full ETVL pipeline.

    Args:
        raw_dir: Path to data/raw directory.
        processed_dir: Path to data/processed directory.
        logger: Logger for logging messages.

    Returns:
        None

    """
    logger.info("JSON: START")

    input_file = raw_dir / "astros.json"
    output_file = processed_dir / "json_astronauts_by_craft.txt"

    # E
    people_list = extract_people_list(file_path=input_file, list_key="people")

    # T
    craft_counts = transform_count_by_craft(people_list=people_list, craft_key="craft")

    # V
    verify_counts(counts=craft_counts)

    # L
    load_counts_report(counts=craft_counts, out_path=output_file)

    logger.info("JSON: wrote %s", output_file)
    logger.info("JSON: END")
