# datafun-03-analytics

> Professional Python project: working with data files for analytics.

## Project Planning

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

---

## Three Workflows

There are three workflows for analytics projects.

- 01: Set Up Machine (Once Per Machine)
- 02: Set Up Project (Once Per Project)
- 03: Daily Workflow (Working With Python Project Code)

## 01: Set Up Machine (Once Per Machine)

Follow the detailed instructions at:
[**01. Set Up Your Machine**](https://denisecase.github.io/pro-analytics-02/01-set-up-machine/)

🛑 All steps must be completed and verified successfully.

## 02: Set Up Project (Once Per Project)

1. Get Repository: Sign in to GitHub, open this repository in your browser, and click **Copy this template** to get a copy in **YOURACCOUNT**.

2. Configure Repository Settings:
   - Select your repository **Settings** (the gear icon way on the right).
   -  Go to **Pages** tab / Enable GitHub Pages / Build and deployment / set **Source** to **GitHub Actions**
   -  Go to **Advanced Security** tab / Dependabot / **Dependabot security updates** / **Enable**
   -  Go to **Advanced Security** tab / Dependabot / **Grouped security updates** / **Enable**

3. Clone to local: Open a **machine terminal** in your **`Repos`** folder and clone your new repo.

  ```shell
  git clone https://github.com/YOURACCOUNT/datafun-03-analytics
  ```

4. Open project in VS Code: Change directory into the repo and open the project in VS Code by running `code .` ("code dot"):

  ```shell
  cd datafun-03-analytics
  code .
  ```

5. Install recommended extensions.

   - When VS Code opens, accept the Extension Recommendations (click **`Install All`** or similar when asked).

6. Set up a project Python environment (managed by `uv`) and align VS Code with it.

   - Use VS Code menu option `Terminal` / `New Terminal` to open a **VS Code terminal** in the root project folder.
   - Run the following commands, one at a time, hitting ENTER after each:

    ```shell
    uv self update
    uv python pin 3.14
    uv sync --extra dev --extra docs --upgrade
    ```

If asked: "We noticed a new environment has been created. Do you want to select it for the workspace folder?" Click **"Yes"**.

If successful, you'll see a new `.venv` folder appear in the root project folder.

Optional (recommended): install and run pre-commit checks:

```shell
uvx pre-commit install
git add -A
uvx pre-commit run --all-files
```

Fore more detailed instructions and troubleshooting, see the pro guide at:
[**02. Set Up Your Project**](https://denisecase.github.io/pro-analytics-02/02-set-up-project/)

🛑 Do not continue until all REQUIRED steps are complete and verified.

## 03: Daily Workflow (Working With Python Project Code)

Follow the detailed instructions at:
[**03. Daily Workflow**](https://denisecase.github.io/pro-analytics-02/03-daily-workflow/)

Commands are provided below to:

1. Git pull
2. Run and check the Python files
3. Build and serve docs
4. Save progress with Git add-commit-push
5. Update project files

VS Code should have only this project (datafun-03-analytics) open.
Use VS Code menu option `Terminal` / `New Terminal` and run the following commands:

```shell
git pull
```

In the same VS Code terminal, run any Python source files:

```shell
uv run python src/datafun_03_analytics/app_case.py
uv run python src/datafun_03_analytics/app_yourname.py
```

OR: Run them as modules (preferred):

```shell
uv run python -m datafun_03_analytics.app_case
uv run python -m datafun_03_analytics.app_yourname
```

For more see: [Running Python Reliably](https://denisecase.github.io/pro-analytics-02/06-python/running-python/).

If a command fails, verify:

- Only this project is open in VS Code.
- The terminal is open in the project root folder.
- The `uv sync --extra dev --extra docs --upgrade` command completed successfully.

Hint: if you run `ls` in the terminal, you should see files including `pyproject.toml`, `README.md`, and `uv.lock`.

Run Python checks and tests (as available):

```shell
uv run ruff format .
uv run ruff check . --fix
uv run pytest --cov=src --cov-report=term-missing
```

Build and serve docs (hit **CTRL+c** in the VS Code terminal to quit serving):

```shell
uv run mkdocs build --strict
uv run mkdocs serve
```

While editing project code and docs, repeat the commands above to run files, check them, and rebuild docs as needed.

Save progress frequently (some tools may make changes; you may need to **re-run git `add` and `commit`** to ensure everything gets committed before pushing):

```shell
git add -A
git commit -m "update"
git push -u origin main
```

Additional details and troubleshooting are available in the [Pro-Analytics-02 Documentation](https://denisecase.github.io/pro-analytics-02/).

---

## Project Objectives

### Project Task 1. Personalize Your Documentation Links

Open [mkdocs.yaml](./mkdocs.yaml).
This file configures the associated project documentation website (powered by MkDocs)
Use CTRL+f to find each occurrence of the source GitHub account (e.g. `denisecase`).
Change each occurrence to point to your GitHub account instead (spacing and capitalization MUST match the URL of your GitHub account **exactly**.)

### Project Task 2. Personalize Your Python File

1. Rename `app_yourname.py` to reflect your name or alias.

- Find the file the file in the VS Code Explorer window (top icon on the left).
- Right-click / Rename.
- Follow conventions: name Python files in lower_snake_case, words joined with underscores, and using `.py` extension.

2. Edit this README.md file to change the run command to call your file instead.
   Use CTRL+f to search for `app_yourname.py` and replace all occurrences exactly.
3. Preview this README.md to make sure it still appears correctly.
   - Find README.md in the VS Code Explorer window (top icon on the left)
   - Right-click / Preview
   - Fix any issues.
4. Run the updated command to execute **your** Python script.

### Project Task 3. Implement Your Python File

1. Read the example code carefully **before** starting.
2. Open your file. Search for "TODO" items. VS Code has icons down the left. Use either TODO Tree (tree, at the bottom) or Search (second from top).
3. Complete each TODO carefully, one at a time.
4. After implementing a TODO, paste your run command in the terminal and hit Enter to re-run it.
5. When it runs without errors, delete the associated TODO command.
6. Keep working through each TODO.
7. When you finish, there should be **zero TODO occurrences** in your project.

**Save often**: After making any useful progress, follow the steps to git add-commit-push.

---

## Notes

- You do not need to add to or modify `tests/`. They are provided for example only.
- You do not need to view or modify any of the supporting **config files**.
- Many of the repo files are silent helpers. Explore as you like, but nothing is required.
- You do NOT need to understand everything. Understanding builds naturally over time.
- Use the **UP ARROW** and **DOWN ARROW** in the terminal to scroll through past commands.
- Use `CTRL+f` to find (and replace) with in a file.

## Troubleshooting >>> or ...

If you see something like this in your terminal: `>>>` or `...`
You accidentally started Python interactive mode.
It happens.
Press `Ctrl+c` (both keys together) or `Ctrl+Z` then `Enter` on Windows.

## Resources

- [Pro-Analytics-02](https://denisecase.github.io/pro-analytics-02/) - guide to professional Python
- [ANNOTATIONS.md](./ANNOTATIONS.md) - REQ/WHY/OBS annotations used
- [INSTRUCTORS.md](./docs/root/INSTRUCTORS.md) - guidance and notes for instructors and maintainers
- [POLICIES.md](./docs/root/POLICIES.md) - project rules and expectations that apply to all contributors
- [SKILLS.md](./docs/root/SKILLS.md) - skills, concepts, and professional practices (there are many)
- [SE_MANIFEST.toml](./SE_MANIFEST.toml) - project intent, scope, and role

## Citation

[CITATION.cff](./CITATION.cff) - TODO: update author and repository fields to reflect your creative work

<!--
WHY: Support correct citation and attribution.
-->

## License

[MIT](./LICENSE)

<!--
WHY: Provide terms of reuse and limits of liability.
-->
