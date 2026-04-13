# datafun-03-analytics

[![Python 3.14+](https://img.shields.io/badge/python-3.14%2B-blue?logo=python)](#)
[![MIT](https://img.shields.io/badge/license-see%20LICENSE-yellow.svg)](./LICENSE)

> Professional Python project: working with data files for analytics.

Data analytics requires a variety of skills.
This course builds capabilities through working projects.

In the age of generative AI, durable skills are grounded in real work:
setting up a professional environment,
reading and running code,
understanding the logic,
and pushing work to a shared repository.
Each project follows the structure of professional Python projects.
We learn by doing.

## This Project

This project illustrates ETL data pipelines processing raw data with the following types:

- CSV (comma separated values)
- JSON (structured data commonly used to exchange information over the web)
- Text (excerpt from _Romeo and Juliet_)
- Excel file (using the `openpyxl` package added to `pyproject.toml`)

The working example illustrates a complete pipeline.
Use the working example and your resources to create your own processing pipelines.

Think about some raw data you would like to process.

- What format is the data? Choose from csv, json, text, or xlsx.
- Choose static data (e.g., in files), rather than data in motion (e.g., social media streams)
- Being able to read and process a wide variety of data files is critical in professional analytics.
- Python is popular partly because it makes building data pipelines relatively easy.

## Project Specific Choices for Data Pipeline projects

We've turned off some PyRight type checks since we are working with raw data pipelines.

- WHY: We don't know what types things are until after we read them.
- See pyproject.toml and the [tool.pyright] section for details.

We use keyword-only function arguments when defining our ETL functions.

- In our functions, you'll see a `*,`.
- The asterisk can appear anywhere in the list of parameters.
- EVERY argument AFTER the asterisk must be passed using the named keyword argument (also called kwarg), rather than by position.
- WHY: Requiring named arguments prevents argument-order mistakes.
- It also makes our function calls self-documenting, which can be especially helpful in data-processing pipelines.

## Large Project File

This repo includes a 2.2 MB Excel data file.
We have increased the size of the "large file" check in our pre-commit hooks.

## DEBUG HELP: If you see "import block is unsorted",

Mouse over, click lightbulb icon for suggestions. and select "Organize Imports".

## DEBUG HELP: If you see "Type of run_csv_pipeline is unknown",

Ensure you have set up your .venv.
View / Command Palette: Python: Select Interpreter.
Select the .venv in this project folder.
View / Command Palette: Developer: Reload Window.

## Working Files

You'll work with just these areas:

- **docs/** - the project narrative and documentation
- **src/datafun** - where the magic happens
- **pyproject.toml** - update authorship & links
- **zensical.toml** - update authorship & links

## Instructions

Follow the [step-by-step workflow guide](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/) to complete:

1. Phase 1. **Start & Run**
2. Phase 2. **Change Authorship**
3. Phase 3. **Read & Understand**
4. Phase 4. **Modify**
5. Phase 5. **Apply**

## Challenges

Challenges are expected.
Sometimes instructions may not quite match your operating system.
When issues occur, share screenshots, error messages, and details about what you tried.
Working through issues is part of implementing professional projects.

## Success

After completing Phase 1. **Start & Run**, you'll have your own GitHub project,
running on your machine, and running the example will print out:

```shell
========================
Executed successfully!
========================
```

## Command Reference

The commands below are used in the workflow guide above.
They are provided here for convenience.

Follow the guide for the **full instructions**.

<details>
<summary>Show command reference</summary>

### In a machine terminal (open in your `Repos` folder)

After you get a copy of this repo in your own GitHub account,
open a machine terminal in your `Repos` folder:

```shell
# Replace username with YOUR GitHub username.
git clone https://github.com/username/datafun-03-analytics

cd datafun-03-analytics
code .
```

### In a VS Code terminal

```shell
uv self update
uv python pin 3.14
uv sync --extra dev --extra docs --upgrade

uvx pre-commit install

git add -A
uvx pre-commit run --all-files
# repeat if changes were made
git add -A
uvx pre-commit run --all-files

# run the module
uv run python -m datafun.app_case

# do chores
uv run ruff format .
uv run ruff check . --fix
uv run python -m pyright
uv run pytest
uv run zensical build

# save progress
git add -A
git commit -m "update"
git push -u origin main
```

</details>

## Notes

- Use the **UP ARROW** and **DOWN ARROW** in the terminal to scroll through past commands.
- Use `CTRL+f` to find (and replace) text within a file.

## Example Output

```text
| INFO | P03 | ========================
| INFO | P03 | START main()
| INFO | P03 | ========================
| INFO | P03 | ROOT_DIR = .
| INFO | P03 | PROCESSED_DIR = data\processed
| INFO | P03 | CSV: START
| INFO | P03 | CSV: wrote C:\Repos\datafun\datafun-03-analytics\data\processed\csv_ladder_score_stats.txt
| INFO | P03 | CSV: END
| INFO | P03 | XLSX: START
| INFO | P03 | XLSX: wrote C:\Repos\datafun\datafun-03-analytics\data\processed\xlsx_feedback_github_count.txt
| INFO | P03 | XLSX: END
| INFO | P03 | JSON: START
| INFO | P03 | JSON: wrote C:\Repos\datafun\datafun-03-analytics\data\processed\json_astronauts_by_craft.txt
| INFO | P03 | JSON: END
| INFO | P03 | TXT: START
| INFO | P03 | TXT: wrote C:\Repos\datafun\datafun-03-analytics\data\processed\txt_summary.txt
| INFO | P03 | TXT: END
| INFO | P03 | ========================
| INFO | P03 | Executed successfully!
| INFO | P03 | ========================
```
