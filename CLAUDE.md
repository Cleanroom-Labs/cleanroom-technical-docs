# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a **Sphinx documentation repository** for the **AirGap project suite** - a collection of tools for deploying and using software in air-gapped (offline) environments. The repository contains planning documents, requirements, design specifications, and use case analyses for three related projects:

1. **Cleanroom Whisper** - Offline audio transcription app using whisper.cpp
2. **AirGap Deploy** - Universal Rust tool for preparing software deployments for air-gapped systems
3. **AirGap Transfer** - Tool for transferring files to air-gapped systems

## Project Structure

```
technical-docs/
├── cleanroom-whisper-docs/            # Submodule: Whisper transcription app docs
│   ├── readme.rst                     # Project overview
│   ├── roadmap.rst                    # Current status and milestones
│   ├── requirements/srs.rst           # Software Requirements Specification
│   ├── design/sdd.rst                 # Software Design Document
│   ├── testing/plan.rst               # Test plan with traceability
│   └── use-cases/                     # Use case workflows
│
├── airgap-deploy-docs/                # Submodule: Deployment packaging tool docs
│   ├── readme.rst
│   ├── roadmap.rst
│   ├── requirements/srs.rst
│   ├── design/sdd.rst
│   ├── testing/plan.rst
│   └── use-cases/
│
├── airgap-transfer-docs/              # Submodule: File transfer tool docs
│   ├── readme.rst
│   ├── roadmap.rst
│   ├── requirements/srs.rst
│   ├── design/sdd.rst
│   ├── testing/plan.rst
│   └── use-cases/
│
├── source/
│   ├── meta/                          # Cross-project documentation
│   │   ├── principles.rst             # Core design principles (READ THIS FIRST)
│   │   ├── meta-architecture.rst      # Project relationships and dependencies
│   │   ├── release-roadmap.rst        # Release planning and milestones
│   │   ├── specification-overview.rst # Aggregate statistics and traceability
│   │   ├── rust-integration-guide.rst # Future Rust API integration
│   │   └── sphinx-needs-guide.rst     # How to use sphinx-needs
│   │
│   ├── projects/                      # Landing pages for each project
│   │   ├── whisper.rst                # Cleanroom Whisper landing page
│   │   ├── deploy.rst                 # AirGap Deploy landing page
│   │   └── transfer.rst               # AirGap Transfer landing page
│   │
│   ├── cleanroom-theme/               # Submodule: Theme configuration
│   ├── conf.py                        # Sphinx configuration
│   └── index.rst                      # Documentation home page
│
├── PROJECT_TEMPLATE.md                # Template for creating new project docs
├── Makefile                           # Build commands (make html, make clean)
├── requirements.txt                   # Python dependencies for Sphinx
└── build/html/                        # Generated HTML documentation
```

**Note:** Project documentation is in separate submodules at root level, not inside `source/`. The `source/projects/` directory contains landing pages that link to the project submodules.

## Core Design Philosophy

**READ `source/meta/principles.rst` FIRST** - It defines the non-negotiable design principles that guide all projects:

1. **Privacy Through Data Locality** - No network code, all data stays local
2. **Minimal Dependencies** - Target ≤10 direct Rust dependencies
3. **Simple Architecture** - Write obvious code, avoid premature abstraction
4. **Air-Gap Ready** - Must work on systems with zero internet access

### Key Constraints

- **No network code** in applications (no `std::net`, `tokio::net`, `hyper`, `reqwest`)
- **Vendored dependencies** for air-gapped builds
- **Pure Rust** where possible, minimal system dependencies
- **Flat file structure** (e.g., 5 files max for Cleanroom Whisper)
- **No WebView/GUI frameworks** - Use system tray and native APIs

## Working with Sphinx Documentation

### Document Format

This repository uses **reStructuredText (.rst)** and **Sphinx** for professional documentation:

- **sphinx-needs** extension provides traceability directives (`:req:`, `:test:`, `:usecase:`)
- **needtable** directives create dynamic traceability matrices
- **need_count** directives provide automatic statistics
- Supports both RST and Markdown (via myst_parser extension)

### Building Documentation

```bash
# First-time setup (if virtual environment doesn't exist)
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Subsequent sessions (activate existing environment)
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Building documentation
make html          # Build HTML documentation
make clean         # Clean build artifacts
make help          # Show all available build targets
```

Generated documentation appears in `build/html/index.html`.

**Note:** The virtual environment is stored in `.venv/` and is excluded from git. If using direnv (detected via `.envrc`), the virtual environment activates automatically when entering the directory.

### GitHub Actions Deployment

Documentation is automatically built and deployed to GitHub Pages when changes are pushed to `main`:

- **Workflow:** `.github/workflows/sphinx-docs.yml`
- **Triggers:** Push to main branch (when `source/**`, `requirements.txt`, or `Makefile` changes)
- **Deploy target:** GitHub Pages (requires repository Settings > Pages > Source set to "GitHub Actions")
- **Build dependencies:** Python 3.11, Graphviz (for needflow diagrams)
- **Deployment URL pattern:** `https://[username].github.io/[repo-name]/`

The workflow runs `make html` and deploys `build/html/` to GitHub Pages. The build and deploy are separate jobs - PRs only build (don't deploy) to catch errors early. Check the Actions tab for build status and errors.

### Document Types

This repository contains:

- **Requirements (SRS)** - IEEE 830 simplified format with sphinx-needs directives, defines WHAT to build
- **Design (SDD)** - IEEE 1016 simplified format, defines HOW to build
- **Roadmaps** - Phase-by-phase implementation plans and milestones
- **Use Case Analysis** - Workflow scenarios and examples
- **Test Plans** - Test cases with traceability links to requirements
- **Traceability** - Requirements Overview page shows aggregate statistics; detailed traceability in each project's test plan

### Making Changes to Documentation

When updating documentation:

1. **Maintain consistency** with `source/meta/principles.rst` - It is the source of truth
2. **Keep it concise** - These are MVP-focused docs, avoid over-engineering
3. **Update cross-references** - Many docs reference each other using `:doc:` directive
4. **Follow existing structure** - Use the same heading levels and formats
5. **Use sphinx-needs directives** - For requirements (`:req:`), test cases (`:test:`), use cases (`:usecase:`)
6. **Update traceability** - Test cases should link to requirements via `:tests:` field
7. **Build and verify** - Run `make html` to ensure no errors
8. **Check warnings** - Sphinx warnings indicate broken links, missing references, or syntax errors

**Common build errors:**
- `WARNING: undefined label` - Missing or incorrect `:ref:` target
- `WARNING: unknown document` - Incorrect `:doc:` path (use relative paths)
- `WARNING: duplicate label` - Need IDs must be unique across all projects

### Common Tasks

**Adding a new feature to Cleanroom Whisper:**
1. Check if it violates principles in `source/meta/principles.rst` (section: "Features We Don't Build")
2. Add requirement to `source/cleanroom-whisper/requirements/srs.rst` using `.. req::` directive
3. Update `source/cleanroom-whisper/design/sdd.rst` with implementation approach
4. Add test cases to `source/cleanroom-whisper/testing/plan.rst` using `.. test::` directive with `:tests:` link
5. Update `source/cleanroom-whisper/roadmap.rst` milestones if needed
6. Build docs and verify traceability tables update automatically

**Clarifying a use case:**
1. Read existing use case analyses in relevant project's `use-cases/` directory
2. Follow the same structure (Overview, Workflow, Technical Details, Success Criteria)
3. Reference specific technical components from SDD
4. Optionally add `.. usecase::` directive for traceability

## Cleanroom Whisper Specifics

### Architecture

- **Language:** Pure Rust
- **Target dependencies:** 8 direct crates (see `source/meta/principles.rst`)
- **File structure:** `main.rs`, `audio.rs`, `whisper.rs`, `db.rs`, `tray.rs` (5 files total)
- **External dependency:** whisper.cpp (user-managed binary)
- **Storage:** SQLite with bundled library

### MVP Development Status

Check `source/cleanroom-whisper/roadmap.rst` for current milestone status.

### Key Technologies

- `tray-icon` + `global-hotkey` (not Tauri)
- `cpal` for audio recording
- `hound` for WAV file writing
- `rusqlite` with bundled SQLite
- Shell execution to whisper.cpp binary

## AirGap Deploy Specifics

This is a **separate Rust tool** (not yet implemented) for automating air-gap deployments.

### Core Concept

Declarative manifests (`AirGapDeploy.toml`) that define:
- Rust applications with vendored dependencies
- External binaries (like whisper.cpp)
- Model files with checksums
- System packages

### Architecture

See `source/airgap-deploy/roadmap.rst` for the complete 7-phase implementation plan:
1. Core Infrastructure
2. Built-in Components (RustApp, ExternalBinary, ModelFile, SystemPackage)
3. Collection & Packaging
4. Installation Script Generation
5. CLI Interface
6. Testing & Documentation
7. Plugin System (optional)

## Sphinx-Needs Directives

### Requirement Directive

```rst
.. req:: Requirement Title
   :id: FR-WHISPER-001
   :status: approved
   :tags: whisper, recording, audio
   :priority: must

   The system SHALL record audio from the default microphone.
```

### Test Directive

```rst
.. test:: Test Case Title
   :id: TC-REC-001
   :status: approved
   :tags: whisper, recording
   :tests: FR-WHISPER-001
   :priority: critical

   **Preconditions:** Microphone connected
   **Steps:** 1. Press record hotkey 2. Speak into microphone 3. Press stop
   **Pass Criteria:** Audio file created with non-zero size
```

### Use Case Directive

```rst
.. usecase:: Quick Voice Memo
   :id: UC-WHISPER-001
   :status: approved
   :tags: whisper, recording, transcription
```

## Common Documentation Patterns

### Referencing Other Documents

Use Sphinx cross-reference directives:
- `:doc:`/meta/principles`` - Link to principles document
- `:doc:`../design/sdd`` - Relative path to design document
- `:ref:`section-label`` - Link to specific section

### Traceability Tables

Use needtable directives to show requirements and tests:

```rst
.. needtable::
   :types: req, test
   :columns: id, title, status, priority
   :filter: "whisper" in tags
   :style: table
```

### Statistics

Use need_count for automatic counting:

```rst
Requirements: :need_count:`type=='req' and 'whisper' in tags`
```

## Tools and Workflow

This is a **Sphinx documentation repository** that generates professional HTML documentation with traceability.

### Build System

- **Sphinx** - Documentation generator
- **sphinx-needs** - Requirements traceability extension (critical for traceability matrices)
- **sphinx_rtd_theme** - Read the Docs theme
- **myst-parser** - Markdown support (optional, RST preferred)
- **Graphviz** - Required for needflow diagrams and visualizations
- **Python 3.11+** - Required for Sphinx

### Dependencies

See `requirements.txt` for exact versions. Key dependencies:
- `Sphinx>=7.0.0,<8.0.0` - Documentation generator
- `sphinx-rtd-theme>=3.0.0` - Read the Docs theme
- `sphinx-needs>=6.3.0` - Traceability directives (`:req:`, `:test:`, `:usecase:`)
- `graphviz>=0.20.0` - Diagram generation (also requires system Graphviz: `brew install graphviz` on macOS)
- `myst-parser>=3.0.0` - Optional Markdown support
- `sphinxcontrib-rust>=1.0.0` - Future Rust API documentation support

### Git Workflow

- Work on `main` branch
- Use descriptive commit messages
- Build docs before committing to check for errors
- Commit generated HTML is optional (can be built by CI/CD)

### File Organization

- Keep related documents together in project subdirectories
- Use consistent naming: lowercase with hyphens (e.g., `traceability-dashboard.rst`)
- Place cross-project documents in `source/meta/`
- Each project has same structure: readme, roadmap, requirements/, design/, testing/, use-cases/

## Important Notes

1. **This is planning documentation** - The actual code repositories for these projects are separate
2. **MVP-focused** - All specs are simplified for minimum viable product
3. **Principles-driven** - When in doubt, refer to `source/meta/principles.rst`
4. **No speculation** - Don't add hypothetical features or "future considerations" beyond what's documented
5. **Air-gap constraint** - Always consider: "Does this work with zero network access?"
6. **Traceability is automated** - Use sphinx-needs directives; tables and statistics update automatically
7. **Build before committing** - Run `make html` to verify no errors or warnings

## Questions About Design Decisions

If you need to understand why something is designed a certain way:
1. Check `source/meta/principles.rst` first
2. Then check the project's `readme.rst`
3. Then check the SRS (Software Requirements Specification) in `requirements/srs.rst`
4. Then check the SDD (Software Design Document) in `design/sdd.rst`
5. If still unclear, review the use case analysis documents in `use-cases/`
6. Check `source/meta/specification-overview.rst` for aggregate statistics and traceability overview
