# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a **Sphinx documentation repository** for the **AirGap project suite** - a collection of tools for deploying and using software in air-gapped (offline) environments. The repository contains planning documents, requirements, design specifications, and use case analyses for three related projects:

1. **AirGap Whisper** - Offline audio transcription app using whisper.cpp
2. **AirGap Deploy** - Universal Rust tool for preparing software deployments for air-gapped systems
3. **AirGap Transfer** - Tool for transferring files to air-gapped systems

## Project Structure

```
sphinx-docs/
├── source/
│   ├── meta/                           # Cross-project documentation
│   │   ├── principles.rst              # Core design principles (READ THIS FIRST)
│   │   ├── meta-architecture.rst       # Project relationships and dependencies
│   │   ├── requirements-overview.rst   # Aggregate statistics and traceability overview
│   │   ├── rust-integration-guide.rst  # Future Rust API integration
│   │   └── sphinx-needs-guide.rst      # How to use sphinx-needs
│   │
│   ├── airgap-whisper/                 # Whisper transcription app
│   │   ├── readme.rst                  # Project overview
│   │   ├── roadmap.rst                 # Current status and milestones
│   │   ├── requirements/srs.rst        # Software Requirements Specification (with sphinx-needs directives)
│   │   ├── design/sdd.rst              # Software Design Document
│   │   ├── testing/plan.rst            # Test plan with traceability tables
│   │   └── use-cases/overview.rst      # Use case workflows
│   │
│   ├── airgap-deploy/                  # Deployment packaging tool
│   │   ├── readme.rst
│   │   ├── roadmap.rst
│   │   ├── requirements/srs.rst        # Requirements with sphinx-needs directives
│   │   ├── design/sdd.rst
│   │   ├── testing/plan.rst            # Test plan with traceability tables
│   │   └── use-cases/                  # Deployment workflows
│   │
│   ├── airgap-transfer/                # File transfer tool
│   │   ├── readme.rst
│   │   ├── roadmap.rst
│   │   ├── requirements/srs.rst        # Requirements with sphinx-needs directives
│   │   ├── design/sdd.rst
│   │   ├── testing/plan.rst            # Test plan with traceability tables
│   │   └── use-cases/                  # Transfer workflows
│   │
│   ├── conf.py                         # Sphinx configuration
│   └── index.rst                       # Documentation home page
│
├── Makefile                            # Build commands (make html, make clean)
├── requirements.txt                    # Python dependencies for Sphinx
└── build/html/                         # Generated HTML documentation
```

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
- **Flat file structure** (e.g., 5 files max for AirGap Whisper)
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
cd sphinx-docs
make html          # Build HTML documentation
make clean         # Clean build artifacts
```

Generated documentation appears in `build/html/index.html`

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

### Common Tasks

**Adding a new feature to AirGap Whisper:**
1. Check if it violates principles in `source/meta/principles.rst` (section: "Features We Don't Build")
2. Add requirement to `source/airgap-whisper/requirements/srs.rst` using `.. req::` directive
3. Update `source/airgap-whisper/design/sdd.rst` with implementation approach
4. Add test cases to `source/airgap-whisper/testing/plan.rst` using `.. test::` directive with `:tests:` link
5. Update `source/airgap-whisper/roadmap.rst` milestones if needed
6. Build docs and verify traceability tables update automatically

**Clarifying a use case:**
1. Read existing use case analyses in relevant project's `use-cases/` directory
2. Follow the same structure (Overview, Workflow, Technical Details, Success Criteria)
3. Reference specific technical components from SDD
4. Optionally add `.. usecase::` directive for traceability

## AirGap Whisper Specifics

### Architecture

- **Language:** Pure Rust
- **Target dependencies:** 8 direct crates (see `source/meta/principles.rst`)
- **File structure:** `main.rs`, `audio.rs`, `whisper.rs`, `db.rs`, `tray.rs` (5 files total)
- **External dependency:** whisper.cpp (user-managed binary)
- **Storage:** SQLite with bundled library

### MVP Development Status

Check `source/airgap-whisper/roadmap.rst` for current milestone status.

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
- **sphinx-needs** - Requirements traceability extension
- **sphinx_rtd_theme** - Read the Docs theme
- **Python 3.x** - Required for Sphinx

### Git Workflow

- Work on `main` branch
- Use descriptive commit messages
- Build docs before committing to check for errors
- Commit generated HTML is optional (can be built by CI/CD)

### File Organization

- Keep related documents together in project subdirectories
- Use consistent naming: lowercase with hyphens (e.g., `requirements-overview.rst`)
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
6. Check `source/meta/requirements-overview.rst` for aggregate statistics and traceability overview
