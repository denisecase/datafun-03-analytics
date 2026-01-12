# INSTRUCTORS.md

This file is for instructors and maintainers of the **DataFun** project series.
Students do **not** need to read this file to complete assignments.

Its purpose is to explain _why_ the repository is structured the way it is, and to
document policies that keep projects consistent, repeatable, and low-friction.

## Instructional Intent

This repository is a teaching template, not a production system.

Design priorities are:

- clarity and stability
- repeatability across projects
- professional habits with minimal cognitive load
- useful tools that behave the same on Windows, macOS, and Linux

Anything that increases confusion, noise, or maintenance burden is intentionally avoided.

## Workflow Consistency Policy

All DataFun repositories use the same three-phase workflow:

1. **Set Up Machine** (once per machine)
2. **Set Up Project** (once per repository)
3. **Daily Workflow** (repeated each session)

Commands, ordering, and expectations are intentionally uniform across projects so students can
focus on _learning Python_, not relearning tooling.

## Tooling Philosophy

This project models modern, professional Python practice using:

- `uv` for Python versioning and dependency management
- `src/` layout for import clarity
- automated formatting and checks where appropriate
- GitHub for version control and collaboration

Tools are included to model good practice, regardless of the project focus.

## Dependency and Update Policy

- Security alerts and fixes are enabled to model responsible maintenance.
- Automatic version update `pull requests (PR)` may be disabled in downstream repos to reduce noise and confusion.
- Configuration lives in (`pyproject.toml` and `.github/dependabot.yml`) so behavior is explicit and reproducible.

## Keywords and Metadata Policy

To prevent drift across systems, metadata responsibilities are intentionally separated:

- **CITATION.cff** - Canonical source of keywords for citation, indexing, and scholarly use.
- **GitHub repository topics** - A small, curated, search-oriented subset of keywords.
- **SE_MANIFEST.toml** - Structural metadata only; keywords are omitted or kept intentionally broad.

Policy: `CITATION.cff` is the canonical source of keywords; GitHub topics are a curated subset,
and `SE_MANIFEST.toml` omits keywords to prevent drift.

## Troubleshooting Placement

Critical blocking issues (for example, getting stuck at the `>>>` Python prompt)
must appear in the **root README.md**, not only in documentation.

## When to Change This Template

Changes should be made when they:

- reduce confusion
- improve cross-platform reliability
- strengthen alignment with professional practice
- apply uniformly across related projects

Avoid changes that add novelty without instructional value.

## Maintainer Note

This file exists to avoid having to reverse-engineer decisions later.

If you are reading this while teaching:
you are encouraged to reuse, adapt, and extend this template as you like.
