# Cleanroom Labs Technical Documentation

Aggregated Sphinx documentation for all AirGap projects.

## Structure

```
cleanroom-technical-docs/
├── shared/                      # Shared theme configuration
│   ├── theme-config.py         # Common Sphinx settings
│   └── extensions.txt          # Shared dependencies
├── source/                      # Master documentation
│   ├── index.rst               # Master landing page
│   ├── conf.py                 # Master Sphinx config
│   └── _static/
│       └── custom.css          # Shared styling
├── project-1-docs/             # Submodule (project docs)
├── project-2-docs/             # Submodule (project docs)
└── project-3-docs/             # Submodule (project docs)
```

## Quick Start

### Building Documentation

```bash
# Create virtual environment (first time only)
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Build HTML documentation
make html

# Open in browser
open build/html/index.html
```

### Working with Submodules

```bash
# Initialize all project submodules
git submodule update --init --recursive

# Update all submodules to latest
git submodule update --remote

# Check submodule status
git submodule status
```

## Shared Theme Configuration

All project documentation imports the shared theme from `shared/theme-config.py`.

### Using Shared Theme in Project Docs

Each project's `source/conf.py` should include:

```python
import sys
import os

# Add shared config to path
sys.path.insert(0, os.path.abspath('../../shared'))

# Import all shared settings
from theme_config import *

# Project-specific settings
project = 'Your Project Name'
version = '1.0.0'
copyright = '2024, Cleanroom Labs'

# Extend shared extensions if needed
extensions.extend([
    'sphinx.ext.viewcode',  # Example project-specific extension
])

# Add project-specific intersphinx mapping
intersphinx_mapping.update({
    'project2': ('https://cleanroomlabs.dev/docs/project-2/', None),
})
```

## Adding a New Project

1. Create the project documentation repository
2. Add it as a submodule:
   ```bash
   git submodule add <repo-url> <project-name>-docs
   ```
3. Update `source/index.rst` to include the project
4. Configure the project's `conf.py` to use shared theme
5. Build and verify

## Cross-Project References

Use Sphinx intersphinx for cross-references:

```rst
See :doc:`project2:installation` for details.
Reference :class:`project3:ClassName` for API.
```

## Development

### Building Specific Projects

```bash
cd project-1-docs
source ../.venv/bin/activate
sphinx-build -M html source build
```

### Cleaning Build Output

```bash
make clean
```

### Checking for Warnings

```bash
make html 2>&1 | grep WARNING
```

## CI/CD

Documentation is automatically built and deployed when:
- Changes pushed to main branch
- Tags created (for versioned releases)

See `.github/workflows/` for CI configuration.

## Resources

- [Sphinx Documentation](https://www.sphinx-doc.org/)
- [Read the Docs Theme](https://sphinx-rtd-theme.readthedocs.io/)
- [Sphinx Needs Extension](https://sphinx-needs.readthedocs.io/)
- [Git Submodules Guide](../docs/SUBMODULES_GUIDE.md)
