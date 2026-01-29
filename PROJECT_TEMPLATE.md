# Project Documentation Template

Use this template when creating a new project-docs repository.

## Repository Structure

```
project-name-docs/
├── .github/
│   └── workflows/
│       └── build-docs.yml
├── source/
│   ├── index.rst
│   ├── conf.py
│   ├── requirements/
│   ├── design/
│   ├── testing/
│   └── use-cases/
├── requirements.txt
├── Makefile
├── make.bat
└── README.md
```

## conf.py Template

See the shared theme configuration in the nested theme submodule:
`source/cleanroom-theme/theme_config.py` (and the repo-level `cleanroom-technical-docs/source/cleanroom-theme/` copy).

Project conf.py should import shared configuration:

- Import sys and os modules
- Add shared directory to Python path
- Import from theme_config
- Set project-specific variables (project, version, copyright)
- Extend extensions list if needed
- Configure intersphinx_mapping for cross-references
- Set HTML context and title

## requirements.txt

Keep dependencies aligned with the aggregator baseline in `cleanroom-technical-docs/requirements.txt`.

Add project-specific dependencies below if needed.

## Setup Instructions

1. Create new repository for project docs
2. Copy Makefile and make.bat from cleanroom-technical-docs
3. Create source/ directory structure
4. Write conf.py with shared theme import
5. Create index.rst
6. Add as submodule to cleanroom-technical-docs
7. Update master index.rst
8. Test build locally
9. Configure CI/CD
