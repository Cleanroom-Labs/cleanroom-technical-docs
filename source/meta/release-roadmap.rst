Release Roadmap
===============

This document coordinates release planning across the three foundation projects: Cleanroom Whisper, AirGap Deploy, and AirGap Transfer.

Release Philosophy
------------------

The AirGap suite follows a **synchronized release strategy** for major versions:

- **v1.0.0**: Coordinated release across all three projects
- **Scope**: Minimum Viable Product (MVP) for each project
- **Goal**: Demonstrate integrated workflows (e.g., Deploy → Transfer → Install)
- **Target Date**: June 30, 2026
- **Development Window**: February 3 - June 27, 2026 (22 weeks)

Individual projects may have independent patch releases (v1.0.1, v1.0.2) for bug fixes, but major feature releases (v1.1, v2.0) will be coordinated.

--------------

v1.0.0 Release Criteria
-----------------------

AirGap Transfer v1.0.0
~~~~~~~~~~~~~~~~~~~~~~

**Definition of Done:**

- All MVP features implemented (see `Transfer Roadmap <../airgap-transfer/roadmap.html>`_)
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

AirGap Deploy v1.0.0
~~~~~~~~~~~~~~~~~~~~

**Definition of Done:**

- All MVP components implemented (see `Deploy Roadmap <../airgap-deploy/roadmap.html>`_)
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


Cleanroom Whisper v1.0.0
~~~~~~~~~~~~~~~~~~~~~~~~

**Definition of Done:**

- All MVP features implemented (see `Whisper Roadmap <../cleanroom-whisper/roadmap.html>`_)
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

--------------

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
**Target Validation Date:** June 20, 2026

--------------

v1.0.0 Release Timeline
-----------------------

**Development Schedule (22 weeks: Feb 3 - June 27, 2026)**

.. list-table::
   :header-rows: 1
   :widths: 10 30 15 25

   * - Phase
     - Project
     - Duration
     - Dates
   * - 1
     - AirGap Transfer MVP
     - 8 weeks
     - Feb 3 - Mar 28
   * - 2
     - AirGap Deploy MVP
     - 8 weeks
     - Mar 31 - May 23
   * - 3
     - Cleanroom Whisper MVP
     - 5 weeks
     - May 26 - June 27
   * - 4
     - Integration Testing
     - 2 weeks
     - June 16 - June 27 (overlap)
   * - 5
     - v1.0.0 Release
     - \-
     - Week of June 30, 2026

**Time Budget:** ~15 hours/week average development time

--------------

**Phase 1: MVP Development** (Status: Not Started)

- **Dates:** February 3 - June 27, 2026
- **Goal:** Complete all MVP features for all three projects
- **Milestone:** All roadmap checkboxes complete
- **Project Order:**

  1. AirGap Transfer (Feb 3 - Mar 28) - Foundation for file transfer
  2. AirGap Deploy (Mar 31 - May 23) - Packaging tool
  3. Cleanroom Whisper (May 26 - June 27) - Transcription app

**Phase 2: Integration Testing** (Status: Not Started)

- **Dates:** June 16 - June 27, 2026 (overlaps with Whisper M4-M6)
- **Goal:** Validate Ollama deployment workflow end-to-end
- **Milestone:** Integration scenario passes on all platforms
- **Key Validation:** June 20, 2026 - Ollama deployment scenario validated

**Phase 3: Documentation and Content** (Status: In Progress - Planning)

- **Parallel with development**
- **Complete by:** June 23, 2026
- Demo blog posts written
- User documentation reviewed
- Release notes drafted

**Phase 4: Release Preparation** (Status: Not Started)

- **Dates:** June 23 - June 27, 2026
- Pre-built binaries created for all platforms (target: June 25)
- GitHub releases prepared
- Blog posts finalized
- Marketing materials ready (if applicable)

**Phase 5: Coordinated Launch** (Status: Not Started)

- **Target Date:** June 30, 2026
- All three projects release v1.0.0 simultaneously
- Blog posts published (intro + 3 demos)
- Announcement on relevant channels
- YouTube videos (if time permits)

**Phase 6: Post-Launch** (Status: Not Started)

- **Dates:** July 2026 onwards
- Monitor for bug reports
- Patch releases as needed (v1.0.1, v1.0.2, etc.)
- Community feedback incorporation

--------------

Individual Project Roadmaps
----------------------------

For detailed MVP implementation plans, see:

- `AirGap Transfer Roadmap <../airgap-transfer/roadmap.html>`_
- `AirGap Deploy Roadmap <../airgap-deploy/roadmap.html>`_
- `Cleanroom Whisper Roadmap <../cleanroom-whisper/roadmap.html>`_

Each roadmap documents:

- MVP feature scope
- Implementation milestones
- Definition of done
- What's NOT in MVP (deferred features)
- Progress tracking
