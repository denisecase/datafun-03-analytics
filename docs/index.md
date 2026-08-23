# Project Documentation

> Use this hosted documentation site to tell your
> data story. Include a narrative telling your
> results, observations, and interpretations.
> Display visuals as needed for a compelling story.

## Professional Workflow

See [**Workflow B: Apply Example Project**](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/)
to get a project like this running on your machine.

## Professional Projects

- We code like the pros to help us **focus on the analytics**.
- Most files in this repository will never be touched.
- If curious about a file, check out the
  [Professional Python Project Explainer](https://denisecase.github.io/professional-python-project-explainer/).

## Documentation Index

- **Home** - this landing page
- [**Project Instructions**](./project-instructions.md)
- [**Concepts**](./concepts.md)
- [**Data Card**](./data-card.md)
- [**API**](./api.md)

## Initial Results

The project processes four different types of raw data
and writes the results to **data/processed/**.
Each pipeline follows the
**Extract / Transform / Verify / Load** structure.

- **CSV** - reads the world happiness CSV file,
  extracts the selected numeric column,
  calculates descriptive statistics,
  verifies the results,
  and writes the statistics to a text file.
  (TODO: link or disply results).

- **JSON** - reads the astronauts JSON file,
  extracts the list of people,
  counts people by spacecraft,
  verifies the results,
  and writes the counts to a text file.
  (TODO: link or disply results).

- **XLSX** - reads the feedback Excel file,
  extracts text from the selected column,
  counts occurrences of the selected word,
  verifies the result,
  and writes the count to a text file.
  (TODO: link or disply results).

- **TXT** - reads the Romeo and Juliet text file,
  counts its lines, words, and characters,
  verifies the results,
  and writes the summary to a text file.
  (TODO: link or disply results).
