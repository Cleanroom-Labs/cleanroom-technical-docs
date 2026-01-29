# Cleanroom Labs Technical Documentation

Aggregated Sphinx documentation for all AirGap projects.

## Structure

```
cleanroom-technical-docs/
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
│   ├── projects/                        # Landing pages for each project
│   │   ├── whisper.rst
│   │   ├── deploy.rst
│   │   └── transfer.rst
│   └── cleanroom-theme/                 # Submodule: shared theme config
│       ├── theme_config.py              # Common Sphinx settings
│       ├── tokens/                      # Design tokens (colors, nav)
│       ├── css/                         # Generated CSS
│       ├── icons/                       # Project icon SVGs
│       ├── sphinx/                      # Templates and static assets
│       └── scripts/                     # Build and validation scripts
├── cleanroom-whisper-docs/              # Submodule: Whisper docs
├── airgap-deploy-docs/                  # Submodule: Deploy docs
├── airgap-transfer-docs/                # Submodule: Transfer docs
├── Makefile                             # Build commands
└── requirements.txt                     # Python dependencies
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

All project documentation imports the shared theme from the `cleanroom-theme` submodule. Each project has its own copy of the submodule at `source/cleanroom-theme/`.

### Using Shared Theme in Project Docs

Each project's `source/conf.py` should include:

```python
import sys
import os

# Add cleanroom-theme submodule to path (local to this repo)
sys.path.insert(0, os.path.abspath('cleanroom-theme'))

# Import all shared settings
from theme_config import *

# Project-specific settings
project = 'Your Project Name'
version = '1.0.0'
copyright = '2024, Cleanroom Labs'

# Extend shared extensions if needed
extensions.extend([
    'sphinx.ext.viewcode',
])

# Configure sphinx-needs types with project prefix
needs_types = make_needs_types('YOURPROJECT-')
```

## Adding a New Project

1. Create the project documentation repository locally
2. Add it as a submodule (using local path):
   ```bash
   git submodule add /path/to/local/project-docs <project-name>-docs
   ```
3. Add the `cleanroom-theme` submodule inside the new project's `source/` directory
4. Update `source/index.rst` to include the project
5. Configure the project's `conf.py` to use shared theme (see above)
6. Build and verify

## Cross-Project References

The master `source/conf.py` maps intersphinx to local build paths:

```python
intersphinx_mapping.update({
    'cleanroom-whisper': ('../cleanroom-whisper-docs/build/html/', None),
    'airgap-deploy': ('../airgap-deploy-docs/build/html/', None),
    'airgap-transfer': ('../airgap-transfer-docs/build/html/', None),
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
