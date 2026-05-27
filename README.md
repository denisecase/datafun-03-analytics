# datafun-03-analytics

[![Workflow Guide](https://img.shields.io/badge/Pro--Guide-pro--analytics--02-green)](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/)
[![Python 3.14](https://img.shields.io/badge/python-3.14%2B-blue?logo=python)](./pyproject.toml)
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

This project illustrates **ETL data pipelines** for extracting raw data,
transforming it, and loading results.

Think about some raw data you would like to process:

- **CSV** (comma-separated values, common tabular format)
- **JSON** (structured data commonly used to exchange information over the web)
- **Text** (unstructured, e.g., a literary excerpt or a log file)
- **Excel** (widely used in business and research)

You will run the working example pipelines, read the code,
and build your own pipeline to process a dataset you choose.

## Working Files

You'll work with just these areas:

- **docs/** - the project narrative and documentation
- **src/datafun** - where the magic happens
- **data/raw/** - input data files
- **pyproject.toml** - update authorship & links
- **zensical.toml** - update authorship & links

## Instructions

Follow the
[step-by-step workflow guide](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/)
to complete:

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

A new file `project.log` will appear in the root project folder.

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
# reset uv cache only after suspected cache corruption or strange dependency errors
# uv cache clean

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
uv run python -m pytest
uv run python -m zensical build

# save progress
git add -A
git commit -m "update"
git push -u origin main
```

</details>

## Notes

- Use the **UP ARROW** and **DOWN ARROW** in the terminal to scroll through past commands.
- Use `CTRL+f` to find (and replace) text within a file.
- You do not need to add to or modify `tests/`. They are provided for example only.
- Many files are silent helpers. Explore as you like, but nothing is required.
- You do NOT not to understand everything; understanding builds naturally over time.

## Troubleshooting >>>

If you see something like this in your terminal: `>>>` or `...`
You accidentally started Python interactive mode.
It happens.
Press `Ctrl+c` (both keys together) or `Ctrl+Z` then `Enter` on Windows.

## Example Output

```shell
| INFO | P03 | ========================
| INFO | P03 | START main()
| INFO | P03 | ========================
| INFO | P03 | ROOT_DIR = .
| INFO | P03 | PROCESSED_DIR = data\processed
| INFO | P03 | CSV: START
| INFO | P03 | CSV: wrote data\processed\csv_ladder_score_stats.txt
| INFO | P03 | CSV: END
| INFO | P03 | XLSX: START
| INFO | P03 | XLSX: wrote data\processed\xlsx_feedback_github_count.txt
| INFO | P03 | XLSX: END
| INFO | P03 | JSON: START
| INFO | P03 | JSON: wrote data\processed\json_astronauts_by_craft.txt
| INFO | P03 | JSON: END
| INFO | P03 | TXT: START
| INFO | P03 | TXT: wrote data\processed\txt_summary.txt
| INFO | P03 | TXT: END
| INFO | P03 | ========================
| INFO | P03 | Executed successfully!
| INFO | P03 | ========================
```
