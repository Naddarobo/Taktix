# Taktix
A tactics based game for your terminal

## Python & Virtualenv (pyenv + Poetry)

- **Python version**: `3.14` (pinned in `.python-version`). Change this file if you prefer a different installed Python.
- **Tooling**: this repository uses `pyenv` to manage local Python versions and `poetry` for virtual environments and dependency management.

Quick setup (recommended):

```bash
# 1) Install pyenv if you don't have it (follow the project README):
#    https://github.com/pyenv/pyenv#installation

# 2) Run the helper script to install Python, configure pyenv, and install dependencies
bash scripts/setup_env.sh

# 3) Enter the poetry shell (optional)
poetry shell

# 4) Run tests
poetry run pytest
```

Notes:
- The script `scripts/setup_env.sh` will try to install the Python version listed in `.python-version` using `pyenv` and will install Poetry if it is not available.
- If you already use a different Python manager or virtualenv workflow, you can still use `poetry` directly: `poetry env use <python-path>` and `poetry install`.
# Taktix
A tactics based game for your terminal
