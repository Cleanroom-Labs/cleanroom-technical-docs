# Project Documentation Template

Use this template when creating a new project-docs repository.

## Repository Structure

```
project-name/
├── common/                    # Submodule: shared design system & build tools
├── source/
│   ├── index.rst
│   ├── conf.py
│   ├── requirements/
│   ├── design/
│   ├── testing/
│   └── use-cases/
├── requirements.txt           # References common/requirements.txt
├── Makefile
├── make.bat
└── README.md
```

## conf.py Template

See the shared configuration in the common submodule:
`common/theme_config.py` (at the repo root level).

Project conf.py should import shared configuration:

- Import sys and os modules
- Add shared directory to Python path
- Import from theme_config
- Set project-specific variables (project, version, copyright)
- Extend extensions list if needed
- Configure intersphinx_mapping for cross-references
- Set HTML context and title

## requirements.txt

Use `-r common/requirements.txt` to reference the shared common dependencies. Add project-specific dependencies below if needed.

## Setup Instructions

1. Create new repository for project docs
2. Copy Makefile and make.bat from technical-docs
3. Create source/ directory structure
4. Write conf.py with shared config import
5. Create index.rst
6. Add as submodule to technical-docs
7. Update master index.rst
8. Test build locally
9. Configure CI/CD
