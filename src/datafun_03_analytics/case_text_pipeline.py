"""p3_text_pipeline.py - Text ETVL pipeline.

ETVL:
  E = Extract (read)
  T = Transform (process)
  V = Verify (check)
  L = Load (write results to data/processed)

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
"""

from pathlib import Path
from typing import Any

# === DEFINE ETL STEP FUNCTIONS ===
# === We add a VERIFY step to check data integrity ===


def extract_lines(*, file_path: Path) -> list[str]:
    """E: Read a text file into a list of lines.

    Args:
        file_path: Path to input text file.

    Returns:
            List of lines from the text file.
    """
    # Handle known possible error: no file at the path provided.
    if not file_path.exists():
        raise FileNotFoundError(f"Missing input file: {file_path}")

    with file_path.open("r", encoding="utf-8") as f:
        return f.readlines()


def transform_line_word_char_counts(*, lines: list[str]) -> dict[str, int]:
    """T: Create a simple summary: line count, word count, character count.

    Args:
        lines: List of lines from the text file.

    Returns:
        Dictionary with counts for 'lines', 'words', and 'chars'.
    """
    line_count = len(lines)
    word_count = 0
    char_count = 0

    for line in lines:
        char_count += len(line)
        word_count += len(line.split())

    return {
        "lines": line_count,
        "words": word_count,
        "chars": char_count,
    }


def verify_summary(*, summary: dict[str, int]) -> None:
    """V: Verify the summary has expected keys and non-negative values.

    Args:
        summary: Dictionary with counts for 'lines', 'words', and 'chars'.

    Raises:
        KeyError: If expected keys are missing.
        ValueError: If any count is negative.

    Returns:
        None
    """
    for key in ("lines", "words", "chars"):
        # Handle known possible error: the key is missing.
        if key not in summary:
            raise KeyError(f"Missing summary key: {key}")
        # Handle known possible error: count is negative.
        if summary[key] < 0:
            raise ValueError(f"Invalid {key} count: {summary[key]}")


def load_summary_report(*, summary: dict[str, int], out_path: Path) -> None:
    """L: Write summary to a text file in data/processed.

    Args:
        summary: Dictionary with counts for 'lines', 'words', and 'chars'.
        out_path: Path to output text file.

    Returns:
        None
    """
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with out_path.open("w", encoding="utf-8") as f:
        f.write("Text File Summary\n")
        f.write(f"Lines: {summary['lines']}\n")
        f.write(f"Words: {summary['words']}\n")
        f.write(f"Characters: {summary['chars']}\n")


# === DEFINE THE FULL PIPELINE FUNCTION ===


def run_text_pipeline(*, raw_dir: Path, processed_dir: Path, logger: Any) -> None:
    """Run the full ETVL pipeline.

    Args:
        raw_dir: Path to data/raw directory.
        processed_dir: Path to data/processed directory.
        logger: Logger for logging messages.

    Returns:
        None

    """
    logger.info("TXT: START")

    input_file = raw_dir / "romeo_and_juliet.txt"
    output_file = processed_dir / "txt_summary.txt"

    # E
    lines = extract_lines(file_path=input_file)

    # T
    summary = transform_line_word_char_counts(lines=lines)

    # V
    verify_summary(summary=summary)

    # L
    load_summary_report(summary=summary, out_path=output_file)

    logger.info("TXT: wrote %s", output_file)
    logger.info("TXT: END")
