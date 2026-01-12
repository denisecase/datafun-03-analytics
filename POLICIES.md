# Project Policies

> Documents project-wide standards and expectations.

## All Projects

The following files are considered **foundational** and
are typically included in professional repositories.

- `.gitignore` - Defines files and artifacts that must not be committed (e.g., virtual environments, build outputs)
- `.gitattributes` - Defines how Git normalizes files across platforms (e.g., line endings)
- `.editorconfig` - Defines editor-agnostic formatting rules (e.g., indentation, whitespace)

These files:

- reduce cross-platform issues
- prevent accidental commits
- keep diffs small and predictable

## VS Code Configuration

- `.vscode/` contains optional VS Code configuration
- Settings and extensions are recommendations, not requirements
- Some VS Code configuration files allow comments despite using `.json`
  - This is a **VS Code–specific exception**
  - Standard JSON does **not** allow comments
  - These files are parsed using JSONC (JSON with Comments)
  - Outside `.vscode/`, use `.jsonc` when comments are required

## Python Dependency Management

- REQ: `uv.lock` MUST be committed to the repository.
- WHY: The lock file provides a reproducible, known-good dependency baseline.
- OBS: Dependencies are regularly updated with `uv sync --upgrade`.

## Project Automation

- REQ: Different tools serve different purposes.
- WHY: Separation prevents slow commits and unpredictable CI failures

  1. **manual checks**: quick checks
  2. **pre-commit**: fast, local hygiene (formatting, linting)
  3. **GitHub Actions**: verification (tests, builds, baseline checks)

### 1. Manual Quality Checks (Before Pre-commit)

These commands verify code quality before enabling automated hooks.
Before installing pre-commit hooks, run checks manually:

- `uv run ruff check --fix .`
- `uv run ruff format .`

### 2. Pre-commit Quality Checks

- **First time:** Run `uv run pre-commit install` after cloning
- **Every commit:** Hooks run automatically
- **Manual check:** `uv run pre-commit run --all-files`

### 3. GitHub Actions

Action: Dependency Updates (dependabot.yml)

- OBS: Dependabot is used to automatically update versions used in Actions workflows.
- WHY: CI infrastructure should remain current with minimal effort.
- OBS:
  - Python dependencies are upgraded manually using `uv sync --upgrade`
  - Dependabot is intentionally not used for Python packages

Action: Continuous Integration (ci.yml)

- REQ: CI enforces baseline correctness only.
- WHY: CI should be predictable, fast, and low-noise.
- CUSTOM: Stricter quality checks are available but optional

Action: Link Checking (links.yml)

- OBS: Automated link checks are run using Lychee.
- WHY: Broken links reduce documentation quality and trust.
- OBS:
  - Link checks apply to Markdown and documentation files
  - Failures indicate broken or unreachable links
  - This check is informational and low-noise when configured correctly

## Optional Tools and Workflows

### Strict Tooling

Stricter configurations (e.g., `ruff.strict.toml`, strict type checking) are provided for instructors, maintainers, and advanced users. These are opt-in and not required.

### Development Containers

- A dev container configuration may be provided as a fallback option
- Local development using `uv` is preferred and recommended
- The dev container uses the same commands and workflow as local setup
- **WHEN:** Only if local Python setup is problematic

### Quick Edits in the Browser

- When viewing your project repo in a web browser, quick edits can be made in a VS Code-like environment
- **How:** Change `github.com` in the URL to `github.dev`
- **Limitations:** No terminal access, no local file execution
- **Best for:** Quick README fixes, typo corrections, reviewing files
