# Glossary (Module 3: Data Analytics Pipelines)

## Pipeline

A sequence of processing steps where data flows from a source to an output.
Each step has a single responsibility.
Separating steps makes pipelines easier to test, debug, and reuse.

## ETVL (Extract, Transform, Verify, Load)

The four-step pipeline model used in this module.

- **Extract** - read raw data from a file
- **Transform** - compute or reshape the data into a useful form
- **Verify** - check that results are valid before writing
- **Load** - write the results to an output file

The Verify step is added between Transform and Load to catch problems
before they are written to disk.

## Extract

The pipeline step that reads raw data from a source file.
The Extract function checks that the file exists before opening it
and raises an error if it does not.

## Transform

The pipeline step that processes the extracted data.
Examples: calculating statistics from numbers,
counting occurrences of a word, or grouping records by a category.

## Verify

The pipeline step that checks the transformed result for known problems
before writing it to disk.
Examples: checking that required keys are present,
that counts are non-negative, and that minimum is not greater than maximum.

## Load

The pipeline step that writes the verified result to an output file.
The Load function creates any missing parent folders
before writing using `mkdir(parents=True, exist_ok=True)`.

## Raw Data

Data in its original, unprocessed form.
Raw data files are stored in `data/raw/` and are not modified by the pipeline.

## Processed Data

Data that has been extracted, transformed, verified, and written by the pipeline.
Processed output files are stored in `data/processed/`.

## Artifact

A file produced by running a script that is committed to Git
as evidence of successful execution.
In this module, the files written to `data/processed/` are artifacts.

## CSV (Comma-Separated Values)

A plain text file format where each row is a record
and values within a row are separated by commas.
Python's built-in `csv` module reads CSV files without any installation.
`csv.DictReader` reads each row as a dictionary keyed by column name.

## JSON (JavaScript Object Notation)

A structured text format commonly used to exchange data over the web.
JSON maps directly to Python types:
objects become `dict`, arrays become `list`, strings become `str`.
Python's built-in `json` module reads JSON files without any installation.

## Plain Text File

A file containing unstructured text with no special formatting.
`file.readlines()` reads the file into a list of strings, one per line.
Each line includes the newline character at the end.

## XLSX (Excel Spreadsheet)

A binary spreadsheet format used by Microsoft Excel.
The `openpyxl` package reads XLSX files in Python.
`openpyxl` is an external package and must be listed in `pyproject.toml`.

## Keyword-Only Argument

A function parameter that must be passed by name, not by position.
A bare asterisk (`*,`) in the parameter list makes all following parameters keyword-only.

```python
def my_func(*, file_path: Path, column_name: str) -> list[float]: ...

my_func(file_path=path, column_name="score")   # correct
my_func(path, "score")                          # TypeError
```

WHY: Named arguments prevent argument-order mistakes
and make function calls self-documenting.

## Defensive Programming

Writing code that anticipates and handles known failure cases
rather than assuming inputs are always valid.
In data pipelines, defensive programming means checking
that files exist, keys are present, and values are the expected type
before using them.

## raise

A Python statement that signals an error and stops execution of the current function.
The calling code must either handle the error or allow it to propagate.

```python
if not file_path.exists():
    raise FileNotFoundError(f"Missing input file: {file_path}")
```

Using `raise` with a descriptive message makes errors easier to debug.

## isinstance()

A Python built-in function that checks whether a value is an instance of a given type.
Used in defensive programming to verify types at runtime
before using a value that came from untrusted input such as a JSON file.

```python
if not isinstance(value, list):
    raise TypeError(f"Expected a list, got {type(value)}")
```

## Fallback Value

A default value used when expected data is missing or cannot be read.
Using a fallback prevents the pipeline from crashing on incomplete input.

```python
craft = person.get("craft", "Unknown")
```

## dict.get()

A Python dictionary method that returns the value for a key
if the key exists, or a default value if it does not.
This avoids a `KeyError` when a key may be missing.

```python
counts[craft] = counts.get(craft, 0) + 1
```

## statistics module

A Python standard library module that provides functions
for calculating descriptive statistics from a list of numbers.
No installation is needed.
Common functions: `statistics.mean()`, `statistics.stdev()`.
`stdev()` requires at least two values.
