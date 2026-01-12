# Optional: Cloud Development Environment (GitHub Codespaces)

This repository includes an **optional development container** configuration
intended for use with **GitHub Codespaces**.

It provides a ready-to-run Linux-based development environment in the cloud.
The workflow inside Codespaces mirrors the local workflow used in the project.

**Local development is still recommended and is the primary learning path.**
This cloud option exists only as a fallback when:

- local installation is not possible
- working on a restricted or shared machine
- a temporary, browser-based environment is needed

## Dev Container (Conceptual Overview)

A dev container:

- runs a Linux environment in the cloud
- includes Python (version specified in the configuration file)
- installs project dependencies using the **same commands** used locally
- allows running code, tests, and tools in a terminal

A dev container is **not**:

- required
- a replacement for learning local Python setup
- part of the preferred workflow

## This Dev Container

This configuration:

- uses a standard Python base image
- runs the same dependency install command used locally
- does **not** add databases, services, or exposed ports
- is intentionally minimal and predictable

There is no Codespaces-specific build system.

## Important Windows Note

Using containers locally typically requires Docker and/or WSL on Windows.

**We do not support or recommend local Dev Containers on Windows.**

## How to Use (Optional, Cloud Only)

This option is disabled to keep the project local-first.

If you choose to try GitHub Codespaces:

1. Rename `.devcontainer/devcontainer_OPTION.json` to `.devcontainer/devcontainer.json`
2. Git add-commit-push the repository to your GitHub account
3. Open the repository on GitHub
4. Select **Code / Codespaces / Create codespace**
5. Wait for the environment to build
6. Use the same commands shown in `README.md`

No additional configuration is required.

## GitHub Codespaces

GitHub Codespaces provides a cloud-based development environment that runs
in a web browser (or in VS Code), hosted by GitHub.

- Free usage may be available for verified students
- Usage limits may apply
- Because users may incur charges, this option is not recommended.
- If you choose to explore Codespaces, monitor costs and use external documentation or support resources.
