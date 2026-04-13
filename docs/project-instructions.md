# Project Instructions (Module 3: Data Analytics Pipelines)

## WEDNESDAY: Complete Workflow Phase 1

Follow the instructions in
[⭐ **Workflow: Apply Example**](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/)
to complete:

1. Phase 1. **Start & Run** - copy the project and confirm it runs

## FRIDAY/SUNDAY: Complete Workflow Phases 2-4

Again, follow the instructions above to complete:

1. Phase 2. **Change Authorship** - update the project to your name and GitHub account
2. Phase 3. **Read & Understand** - review the project structure and code
3. Phase 4. **Make a Technical Modification** - make a change and verify it still runs

## Phase 4 Suggestions

Make a small technical change that does not break the pipeline.
Choose any one of these (or a different modification as you like):

- Change the target word in the XLSX pipeline to a different word
  (e.g., search for "Python" or "data" instead of "GitHub")
- Add a new derived field in the CSV Transform stage
  (e.g., a normalized score, or a label based on whether the value is above the mean)
- Add a line to any Load stage that writes the current date to the output file
- Adjust logging messages in any pipeline to provide more detail about what was found

Confirm the pipeline still runs successfully after your change.

## Phase 5 Suggestions

### Phase 5 Suggestion 1. New Data File, Same Format (Directed)

Apply one of the existing pipelines to a different data file of the same type.

Steps:

- Choose one pipeline: CSV, JSON, text, or XLSX
- Find or create a new data file of that type
  - CSV: any dataset with at least one numeric column
    (e.g., from https://www.kaggle.com or https://data.gov)
  - JSON: any JSON file with a list of objects
    (e.g., from a public API or https://github.com/jdorfman/awesome-json-datasets)
  - Text: any plain text file with readable content
    (e.g., from https://www.gutenberg.org)
  - XLSX: any Excel file with text content in a column
- Copy and rename the relevant pipeline file
- Update the input filename and column/key names to match your new data
- Update the output filename to reflect your data
- Run the pipeline and confirm success

Then:

- Describe your data source and what it contains
- Identify the column or key you extracted and why you chose it
- Describe one challenge you encountered adapting the pipeline and how you resolved it

### Phase 5 Suggestion 2. New Format Pipeline (Original)

Write a new ETVL pipeline for a data format not yet covered in the example.

Good options include:

- A second CSV file with different columns and a different Transform (e.g., filtering rows)
- A nested JSON file with a different structure (e.g., multiple levels of nesting)
- A text file from a different source with different counting logic
  (e.g., count sentences instead of words)

Steps:

- Place your raw data file in `data/raw/`
- Create a new pipeline file named `yourname_<format>_pipeline.py`
- Implement all four ETVL steps as separate functions
- Use keyword-only arguments (`*,`) in all function definitions
- Call the pipeline from `main()` in `app_yourname.py`
- Write at least one test for your Extract function and one for your Transform function
- Run the full pipeline and confirm output appears in `data/processed/`

Then:

- Describe the data format and structure of your file
- Explain what your Transform step computes and why it is useful
- Describe what your Verify step checks and why those checks matter

## Key Skill Focus

As you work, focus on:

- how each ETVL step has a single, clear responsibility
- how keyword-only arguments prevent argument-order mistakes
- how defensive programming handles missing files and unexpected values
- how `raise` signals an error that the caller must handle
- how the Verify step catches problems before writing results to disk

Your goal is to reuse the same pipeline pattern on new data sources.

## Professional Communication

Make sure the title and narrative reflect your work.
Verify key files:

- README.md
- docs/ (source and hosted on GitHub Pages)
- src/ (your pipeline files)
- data/processed/ (output files committed to Git)

Ensure your project clearly demonstrates:

- a complete ETVL pipeline with all four steps
- successful execution with output written to `data/processed/`
- understanding of the data format you chose
- at least one test for your pipeline functions
