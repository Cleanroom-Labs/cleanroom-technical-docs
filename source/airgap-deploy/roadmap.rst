Project Roadmap
===============

Build a deployment tool that makes air-gap packaging simple. Ship it. See what happens.

--------------

Current Focus
-------------

**Phase:** Documentation Complete, Ready for Development

**Goal:** Implement MVP that can package AirGap Whisper for air-gapped systems.

**Plan:** `development-plan.md <development-plan.md>`__

--------------

MVP Milestones (v0.1.0)
-----------------------

= ========================= ===========
# Phase                     Status
= ========================= ===========
1 Core Infrastructure       Not Started
2 Built-in Components       Not Started
3 Collection & Packaging    Not Started
4 Install Script Generation Not Started
5 CLI Interface             Not Started
6 Testing & Documentation   Not Started
= ========================= ===========

**Done when:** Successfully packages and deploys AirGap Whisper to air-gapped VM.

--------------

Phase Details
-------------

Phase 1: Core Infrastructure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Goal:** Project setup, manifest parsing, component registry

**Key Deliverables:** - Cargo workspace setup - Manifest parser (TOML) - Component trait definition - Platform abstraction

**Status:** Not Started

--------------

Phase 2: Built-in Components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Goal:** Implement essential component types

**Key Deliverables:** - RustAppComponent (cargo vendor, toolchain) - ExternalBinaryComponent (git clone, build instructions) - ModelFileComponent (download, checksum verification) - SystemPackageComponent (deferred to v0.2)

**Status:** Not Started

--------------

Phase 3: Collection & Packaging
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Goal:** Orchestrate component collection, create archives

**Key Deliverables:** - Collector engine (parallel collection) - Packager (tar.gz/zip) - Metadata generation

**Status:** Not Started

--------------

Phase 4: Install Script Generation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Goal:** Generate platform-specific installation scripts

**Key Deliverables:** - Bash template (install.sh) - PowerShell template (install.ps1) - Dependency checking logic - Interactive/automatic modes

**Status:** Not Started

--------------

Phase 5: CLI Interface
~~~~~~~~~~~~~~~~~~~~~~

**Goal:** User-friendly command-line tool

**Key Deliverables:** - ``airgap-deploy prep`` command - ``airgap-deploy validate`` command - ``airgap-deploy init`` command - Progress bars, colored output

**Status:** Not Started

--------------

Phase 6: Testing & Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Goal:** Comprehensive testing and documentation

**Key Deliverables:** - Unit tests (80%+ coverage) - Integration tests (end-to-end) - CI/CD pipeline - User guide

**Status:** Not Started

--------------

Success Criteria
----------------

MVP is complete when:

- ✅ Can package AirGap Whisper with all dependencies
- ✅ Generated install script works on air-gapped Ubuntu VM
- ✅ Cross-platform support (Linux, macOS, Windows)
- ✅ 80%+ test coverage
- ✅ Documentation complete (user guide, examples)

--------------

After MVP (v0.2.0+)
-------------------

v0.2.0: System Dependencies
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- SystemPackageComponent implementation
- ALSA, build tools packaging
- Dependency resolution

v0.3.0: Cross-Platform Packaging
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Cross-compilation support
- Single-command multi-platform builds
- Prebuilt binary option

v1.0.0: Production Ready
~~~~~~~~~~~~~~~~~~~~~~~~

- Plugin system for custom components
- Digital signatures (GPG)
- SBOM generation
- Enterprise features

--------------

Non-Goals
---------

**Never plan to build:** - GUI interface (CLI-only philosophy) - Cloud-based distribution - Automatic updates (contradicts air-gap) - Network-based installation

--------------

Integration Roadmap
-------------------

With AirGap Whisper
~~~~~~~~~~~~~~~~~~~

- **v0.1.0:** Package AirGap Whisper (reference implementation)
- **v0.2.0:** Simplify deployment in AirGap Whisper README

With airgap-transfer
~~~~~~~~~~~~~~~~~~~~

- **v0.1.0:** Document large package workflow
- **v0.2.0:** Detect large packages, suggest airgap-transfer automatically

--------------

Key Documents
-------------

+-----------------------------------------------+---------------------------------+
| Document                                      | Purpose                         |
+===============================================+=================================+
| `principles.md <../principles.md>`__          | Design principles (read first)  |
+-----------------------------------------------+---------------------------------+
| `development-plan.md <development-plan.md>`__ | What to build (7 phases)        |
+-----------------------------------------------+---------------------------------+
| `requirements/srs.md <requirements/srs.md>`__ | 57 functional requirements      |
+-----------------------------------------------+---------------------------------+
| `design/sdd.md <design/sdd.md>`__             | Architecture and design         |
+-----------------------------------------------+---------------------------------+

--------------

Progress Log
------------

========== ================================================
Date       Activity
========== ================================================
2026-01-04 Created complete specification and documentation
2026-01-04 Gap analysis complete - ready for development
========== ================================================

--------------

Decision Log
------------

Why TOML for Manifests?
~~~~~~~~~~~~~~~~~~~~~~~

**Date:** 2026-01-04 **Decision:** Use TOML (not YAML or JSON) **Rationale:** Human-readable, strongly-typed, familiar to Rust developers (Cargo.toml)

Why Build on Target System?
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Date:** 2026-01-04 **Decision:** Build from source on air-gapped system (not prebuilt binaries) **Rationale:** Trust (user can inspect), flexibility (system-specific configs), simplicity (no cross-compilation)

Why Defer SystemPackageComponent?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Date:** 2026-01-04 **Decision:** Defer to v0.2.0 **Rationale:** Complex (distro detection, dependency resolution), workaround exists (document in README), not blocking MVP

--------------

Metrics
-------

Development Metrics
~~~~~~~~~~~~~~~~~~~

- **Target:** v0.1.0 in 6-8 weeks
- **Test coverage:** 80%+ required
- **Code quality:** Zero clippy warnings

User Metrics
~~~~~~~~~~~~

- **Time to first package:** < 10 minutes
- **Package creation time:** < 5 minutes (typical app)
- **Installation time:** < 20 minutes (including build)

--------------

Release Strategy
----------------

v0.1.0 (MVP)
~~~~~~~~~~~~

1. Complete all 6 phases
2. Test with AirGap Whisper deployment
3. Publish to crates.io
4. Announce in Rust community

v0.2.0+
~~~~~~~

- Iterative releases
- Community feedback incorporation
- Feature additions based on usage

--------------

Community
---------

**Status:** Pre-release (documentation phase)

**When ready:** - Publish to crates.io - Create GitHub repository - Accept issues and PRs - Build community around air-gap deployment

--------------

See Also
--------

- `Meta-Architecture <../meta-architecture.md>`__ - How airgap-deploy fits in the AirGap suite
- `Requirements Overview <../meta/requirements-overview.rst>`__ - Project statistics and requirements overview
- `AirGap Whisper <../airgap-whisper/README.md>`__ - Primary use case
- `airgap-transfer <../airgap-transfer/README.md>`__ - Large file transfer companion tool
