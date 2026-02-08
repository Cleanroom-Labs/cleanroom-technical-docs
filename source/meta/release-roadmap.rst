Release Roadmap
===============

This document tracks active release planning across the three foundation projects. For the versioning strategy and coordination rules, see :doc:`release-philosophy`.

v1.0.0 Release Criteria
-----------------------

AirGap Deploy v1.0.0
~~~~~~~~~~~~~~~~~~~~

**Definition of Done:**

- All MVP features implemented (see `Deploy Roadmap <../deploy/roadmap.html>`_)
- Core components: RustApp, ExternalBinary, ModelFile working
- Manifest validation working
- Install script generation (Linux/macOS Bash, Windows PowerShell)
- Cross-platform packaging support
- Documentation complete
- Ollama deployment workflow validated

**Deliverables:**

- Source code on GitHub
- Pre-built binary
- Demo blog post (Ollama scenario)
- Manifest templates
- User documentation

AirGap Transfer v1.0.0
~~~~~~~~~~~~~~~~~~~~~~

**Definition of Done:**

- All MVP features implemented (see `Transfer Roadmap <../transfer/roadmap.html>`_)
- Pack/unpack/list operations working
- SHA-256 verification functional
- Resume capability working
- Cross-platform support
- Documentation complete
- Integration with Deploy validated (Ollama scenario)

**Deliverables:**

- Source code on GitHub
- Pre-built binary
- Demo blog post (Ollama + models scenario)
- User documentation

Cleanroom Whisper v1.0.0
~~~~~~~~~~~~~~~~~~~~~~~~

**Definition of Done:**

- All MVP features implemented (see `Whisper Roadmap <../whisper/roadmap.html>`_)
- Cross-platform support (macOS, Windows, Linux)
- SQLite history storage working
- Global hotkeys functional
- System tray integration complete
- Documentation complete

**Deliverables:**

- Source code on GitHub
- Pre-built binaries for all platforms
- Demo blog post
- User documentation

v1.0.0 Quality Bar
~~~~~~~~~~~~~~~~~~~

**For MVP:**

- **Works:** Core flow functions without crashing
- **Usable:** It can be used on a daily basis without frustration
- **Stable:** No data loss

**Not required for MVP:**

- Performance optimization (make it work first)
- Fully fleshed-out requirements and corresponding implementation
- Comprehensive test suite covering all branches aside from the happy paths

v1.0.0 Milestone Plan
----------------------

Development is organized into 6 milestones over 12 months. The order front-loads foundational work (AirGap Deploy) since downstream projects depend on its packaging capabilities.

.. list-table::
   :header-rows: 1
   :widths: 12 12 76

   * - Milestone
     - Target
     - Deliverables
   * - M1
     - Month 2
     - Specification refinement complete; AirGap Deploy core infrastructure (manifest parsing, component abstractions, CLI skeleton)
   * - M2
     - Month 4
     - AirGap Deploy Rust packaging complete (cargo vendoring, toolchain bundling, install script generation)
   * - M3
     - Month 6
     - AirGap Deploy complete (external binaries, model files); AirGap Transfer core started
   * - M4
     - Month 8
     - AirGap Transfer complete (chunking, verification, multi-USB recovery)
   * - M5
     - Month 10
     - Cleanroom Whisper MVP complete (system tray, hotkeys, transcription, history)
   * - M6
     - Month 12
     - Cross-platform testing, integration validation (Deploy → Whisper workflow), documentation

Milestone Details
~~~~~~~~~~~~~~~~~

**M1: Foundations** (Status: Not Started)

- **Goal:** Refine specifications across all projects; stand up AirGap Deploy core
- **Key outputs:** Finalized SRS/SDD for all projects, working manifest parser, CLI skeleton

**M2: Deploy Packaging** (Status: Not Started)

- **Goal:** Complete Rust application packaging pipeline
- **Key outputs:** Cargo vendoring, toolchain bundling, install script generation for Linux/macOS/Windows

**M3: Deploy Complete + Transfer Started** (Status: Not Started)

- **Goal:** Finish AirGap Deploy (external binaries, model files); begin AirGap Transfer
- **Key outputs:** AirGap Deploy v1.0.0-rc, AirGap Transfer scaffolding

**M4: Transfer Complete** (Status: Not Started)

- **Goal:** Complete AirGap Transfer with chunking, verification, resume capability, and recovery
- **Key outputs:** AirGap Transfer v1.0.0-rc

**M5: Whisper MVP** (Status: Not Started)

- **Goal:** Complete Cleanroom Whisper with system tray, hotkeys, transcription, and history
- **Key outputs:** Cleanroom Whisper v1.0.0-rc

**M6: Integration & Release** (Status: Not Started)

- **Goal:** Cross-platform testing, integration validation, documentation, coordinated launch
- **Key outputs:** All three projects release v1.0.0 simultaneously, blog posts, demo content

Cross-Project Integration Milestones
-------------------------------------

The v1.0.0 release validates that the three projects work together seamlessly.

Integration Scenario: Ollama Deployment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This end-to-end workflow must work for v1.0.0 release:

1. **AirGap Deploy** packages Ollama + llama2-7b model (~20GB)
2. **AirGap Transfer** chunks package across multiple USB drives
3. **AirGap Transfer** reconstructs package on air-gapped system
4. **AirGap Deploy** install script successfully installs Ollama offline
5. Ollama runs successfully with downloaded model

**Validation Criteria:**

- Zero manual intervention required after initial manifest creation
- Cryptographic integrity verification passes
- Cross-platform compatibility (test on macOS, Linux, Windows)
- Process documented in demo blog post

**Status:** Not Started
**Target:** Milestone 6

Individual Project Roadmaps
----------------------------

For detailed, project roadmaps, see:

- `AirGap Deploy Roadmap <../deploy/roadmap.html>`_
- `AirGap Transfer Roadmap <../transfer/roadmap.html>`_
- `Cleanroom Whisper Roadmap <../whisper/roadmap.html>`_

For planning of development not covered by this roadmap, see :doc:`planning`.

Progress Log
~~~~~~~~~~~~

========== ================================================================
Date       Activity
========== ================================================================
2026-01-28 Created release roadmap and coordinated project specifications
2026-01-31 Restructured from 22-week/5-phase plan to 6-milestone/12-month plan
2026-02-08 Added v1.1 planning (SBOM/CBOM/vuln-scan requirements and use
           cases); reorganized cross-project docs
========== ================================================================
