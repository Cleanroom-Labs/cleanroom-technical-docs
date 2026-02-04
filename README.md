# Cleanroom Labs Technical Documentation

Aggregated Sphinx documentation for all AirGap projects.

## Structure

```
technical-docs/
├── source/                              # Master documentation
│   ├── index.rst                        # Master landing page
│   ├── conf.py                          # Master Sphinx config
│   ├── meta/                            # Cross-project documentation
│   │   ├── principles.rst               # Core design principles
│   │   ├── meta-architecture.rst        # Project relationships
│   │   ├── specification-overview.rst   # Aggregate statistics
│   │   ├── release-roadmap.rst          # Release planning
│   │   ├── rust-integration-guide.rst   # Future Rust API integration
│   │   └── sphinx-needs-guide.rst       # sphinx-needs usage guide
│   └── projects/                        # Landing pages for each project
│       ├── whisper.rst
│       ├── deploy.rst
│       └── transfer.rst
├── common/                              # Submodule: shared theme & build tools
│   ├── theme_config.py                  # Common Sphinx settings
│   ├── requirements.txt                 # Shared Python dependencies
│   ├── tokens/                          # Design tokens (colors, nav)
│   ├── css/                             # Generated CSS
│   ├── icons/                           # Project icon SVGs
│   ├── sphinx/                          # Templates and static assets
│   └── scripts/                         # Build and validation scripts
│       └── check-sphinx-warnings.sh     # Shared warning checker
├── whisper/                             # Submodule: Whisper docs
├── deploy/                              # Submodule: Deploy docs
├── transfer/                            # Submodule: Transfer docs
├── Makefile                             # Build commands
└── requirements.txt                     # References common/requirements.txt
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

All project documentation imports the shared theme from the `common` submodule at each repo's root level. Each project has its own copy of the submodule at `common/` (the `cleanroom-website-common` repository).

### Using Shared Theme in Project Docs

Each project's `source/conf.py` should include:

```python
import sys
import os

# Add theme submodule to path (one level up from source/)
sys.path.insert(0, os.path.abspath('../common'))

# Import all shared settings
from theme_config import *

# Override paths for theme directory relative to source/
html_static_path = ['../common/sphinx/_static']
templates_path = ['../common/sphinx/_templates']
html_favicon = '../common/sphinx/_static/favicon.ico'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Project-specific settings
project = 'Your Project Name'
version = '1.0.0'
copyright = '2026, Cleanroom Labs'

# Extend shared extensions if needed
extensions.extend([
    'sphinx.ext.viewcode',
])

# Configure sphinx-needs types with project prefix
needs_types = make_needs_types('YOURPROJECT-')
```

## Adding a New Project

1. Create the project documentation repository
2. Add it as a submodule:
   ```bash
   git submodule add git@github.com:<org>/<project>.git <project-name>
   ```
3. Add the `common` submodule at the new project's root level:
   ```bash
   cd <project-name>
   git submodule add git@github.com:Cleanroom-Labs/cleanroom-website-common.git common
   ```
4. Update `source/index.rst` to include the project
5. Configure the project's `conf.py` to use the shared theme (see above)
6. Add the project name to the `PROJECTS` variable in the `Makefile`
7. Build and verify

## Cross-Project References

The master `source/conf.py` maps intersphinx to local build paths:

```python
intersphinx_mapping.update({
    'cleanroom-whisper': ('/docs/whisper/', '../whisper/build/html/objects.inv'),
    'airgap-deploy': ('/docs/deploy/', '../deploy/build/html/objects.inv'),
    'airgap-transfer': ('/docs/transfer/', '../transfer/build/html/objects.inv'),
})
```

Use Sphinx intersphinx for cross-references:

```rst
See :doc:`cleanroom-whisper:requirements/srs` for details.
See :doc:`airgap-deploy:design/sdd` for architecture.
```

## Development

### Building Specific Projects

```bash
cd whisper  # or deploy, transfer
source ../.venv/bin/activate
sphinx-build -M html source build
```

### Cleaning Build Output

```bash
make clean
```

### Checking for Warnings

```bash
make html        # Build all documentation (output captured to build.log)
make html-check  # Check build.log for errors/warnings
```

The `html-check` target ignores intersphinx inventory warnings (expected when building offline) and fails on all other warnings or errors.

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
