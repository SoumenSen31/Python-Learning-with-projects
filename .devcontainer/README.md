# Python Learning with Projects - Devcontainer Setup

## Overview
This repository uses a **devcontainer** configuration for consistent Python development environments in GitHub Codespaces and VS Code Dev Containers.

## Features
- **Python 3.11** environment
- **Pre-installed tools**: Black (formatter), Flake8 (linter), Pylint (analyzer)
- **VS Code Extensions**: Python, Pylance, GitHubCopilot, and debugging tools
- **Auto-formatting**: Code is automatically formatted on save using Black

## Quick Start
1. Open the repo in GitHub Codespaces
2. VS Code will detect the `.devcontainer` configuration and suggest rebuilding
3. Click "Rebuild Container" to set up the environment
4. Your environment is ready with all Python tools installed

## Install Additional Dependencies
```bash
# Install from requirements.txt
pip install -r requirements.txt

# Or install individual packages
pip install <package-name>
```

## Running Python Files
```bash
# Run a Python script
python project1.py

# Run with debugging
python -m pdb project1.py

# Run tests
pytest
```

## Formatting & Linting
```bash
# Format code with Black
black .

# Check style with Flake8
flake8 .

# Lint with Pylint
pylint *.py
```

## File Structure
```
Python-Learning-with-projects/
├── .devcontainer/
│   ├── devcontainer.json     # Main devcontainer config
│   └── Dockerfile            # Container image definition
├── requirements.txt          # Python dependencies
├── project1.py              # Your Python projects
└── README.md                # This file
```

## Rebuilding the Container
If you modify the `devcontainer.json` or `Dockerfile`:
1. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac)
2. Search for "Dev Containers: Rebuild Container"
3. Wait for the rebuild to complete

## Tips
- Your environment persists across Codespaces sessions
- All Python packages are installed in the container
- Changes to your code are automatically saved
- The container includes debugging tools for VS Code

Happy coding! 🐍
