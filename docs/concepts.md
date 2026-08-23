# Concepts

> Key concepts introduced in this module.

<!--
Only the first sentence/paragraph of h3 entries
are used for the integrated quiz.
Wrap code terms in double asterisks
rather than single backtics so they can be read aloud.
-->

## Data Pipeline

A sequence of steps that moves data from a source toward a useful result.

Each step has a single responsibility, and the steps run in order,
with each one receiving the output of the one before it.

## ETVL

Organizes a pipeline into four stages: Extract, Transform, Verify, and Load.

The Verify stage sits between Transform and Load
to catch potential problems.
This is a variation on the older ETL abbreviation,
which omitted explicit verification.

### Extract

**Extract** reads raw data from a source.

A source might be a delimited file, a spreadsheet, a database,
an API, a sensor, or another application.
Extraction preserves the source data long enough to determine what is present,
and typically confirms the source exists before reading it.

### Transform

**Transform** changes data into a form useful for the current purpose.

Common transformations include converting text to numbers,
selecting or cleaning values, grouping records, and calculating summary statistics.

### Verify

Checks that the transformed result meets expectations before it is used or saved.

Typical checks confirm that required values exist, that counts are non-negative,
that expected fields are present,
and that numeric results fall within a reasonable range,
such as a minimum not exceeding a maximum.

### Load

**Load** writes the verified result to its destination
(often called a **sink**).

A destination might be a text file, a delimited file,
a database, a report, or another analytical process.

## Raw Data

The source data in its original, unprocessed form.

Raw data may be kept in a Data Lake or a Data Lake House.

## Processed Data

Data that has been extracted, transformed, verified,
and written for an analytical purpose.

## Summary Statistics

Describe the important characteristics of a collection of numeric values.

### Count

How many observations contributed to a calculation.

### Minimum and Maximum

The minimum is the smallest observed value and the maximum is the largest.
Together they describe the range of the observations.

### Mean

The mean is the sum of the values divided by the count,
and it summarizes the center of the collection.
For values 8, 10, and 12, the mean is (8 + 10 + 12) / 3, which is 10.

### Standard Deviation

**Standard deviation** describes how far observations
tend to fall from the mean.

A small standard deviation indicates that values cluster
near the mean, and a larger one indicates greater spread.

## File Formats

Data arrives in different formats, and the reading tool
changes with the format even though the pipeline stages do not.

### Delimited Text (CSV)

A **CSV (comma-separated values) file** stores one record per row,
with values separated by commas.

Python reads it with the standard-library **csv** module,
no installation required, and **csv.DictReader**
returns each row as a dictionary keyed by column name.

### JSON

JavaScript Object Notation is a structured text format widely
used to exchange data over the web.

It maps directly onto Python types:
objects become dictionaries
(a set of key-value pairs that provide a string or label with each value),
arrays become lists, and strings stay strings.
Python reads it with the standard-library **json** module.

### Plain Text

A plain-text file contains unstructured text with no defined fields.

The **readlines()** method returns the file as a list of strings,
one per line, each ending in a newline character.
A newline character is not typically visible,
and may be different by operating system.

### Spreadsheet (XLSX)

An XLSX file is the binary spreadsheet format used by Microsoft Excel.

Reading it requires the external **openpyxl** package,
which must be declared as a project dependency in **pyproject.toml**.

## Keyword-Only Argument

A **keyword-only argument** is a function parameter that must be passed
by name rather than by position.

A bare **asterisk in the parameter list** makes every parameter
after it keyword-only,
which prevents argument-order mistakes and makes each call self-documenting.

```python
def summarize(*, file_path: Path, column_name: str) -> list[float]: ...


summarize(file_path=path, column_name="score")  # passed by name

summarize(path, "score")  # TypeError
```

## Defensive Programming

Defensive programming anticipates and handles known failure cases
instead of assuming inputs are valid.

In a pipeline this means confirming that files exist,
that expected keys are present, and that values
hold the expected type before being used.

## raise

The **raise** statement signals an error and stops the current function.

The calling code must either handle the error or allow it to propagate,
and a descriptive message makes the cause easier to diagnose.

```python
if not file_path.exists():
    raise FileNotFoundError(f"Missing input file: {file_path}")
```

## isinstance()

The **isinstance()** function reports
whether a value is an instance of a given type.

It supports defensive programming by confirming a value's type
at runtime before the value is used,
essential for input from untrusted sources.

```python
if not isinstance(value, list):
    raise TypeError(f"Expected a list, got {type(value)}")
```

## dict.get() and Fallback Values

The **get()** method returns the value for a key when it exists
and a fallback value when it does not, avoiding an error on a missing key.
A fallback is a default substituted
for missing data so processing can continue on incomplete input.

```python
craft = person.get("craft", "Unknown")
```

## statistics Module

The standard-library **statistics** module provides
descriptive-statistic functions for a list of numbers,
with no installation required.

It includes **mean()** and **stdev()**, where **stdev()**
requires at least two values.
