Release Roadmap
===============

This document coordinates release planning across the three AirGap foundation projects: Whisper, Deploy, and Transfer.

Release Philosophy
------------------

The AirGap suite follows a **synchronized release strategy** for major versions:

- **v1.0.0**: Coordinated release across all three projects
- **Scope**: Minimum Viable Product (MVP) for each project
- **Goal**: Demonstrate integrated workflows (e.g., Deploy → Transfer → Install)
- **Timeline**: [TBD - add when development begins]

Individual projects may have independent patch releases (v1.0.1, v1.0.2) for bug fixes, but major feature releases (v1.1, v2.0) will be coordinated.

--------------

v1.0.0 Release Criteria
-----------------------

AirGap Whisper v1.0.0
~~~~~~~~~~~~~~~~~~~~~

**Definition of Done:**

- All MVP features implemented (see :doc:`Whisper Roadmap <airgap-whisper:roadmap>`)
- Cross-platform support (macOS, Windows, Linux)
- SQLite history storage working
- Global hotkeys functional
- System tray integration complete
- Documentation complete (README, SRS, SDD, Test Plan)

**Deliverables:**

- Source code on GitHub
- Pre-built binaries for all platforms
- Demo blog post
- User documentation

AirGap Deploy v1.0.0
~~~~~~~~~~~~~~~~~~~~

**Definition of Done:**

- All MVP components implemented (see :doc:`Deploy Roadmap <airgap-deploy:roadmap>`)
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

- All MVP features implemented (see :doc:`Transfer Roadmap <airgap-transfer:roadmap>`)
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

**Status:** [Not Started]

--------------

v1.0.0 Release Timeline
-----------------------

.. note::
   This timeline will be updated as development progresses.

**Phase 1: MVP Development** (Status: [TBD])

- Start Date: [TBD]
- Goal: Complete all MVP features for all three projects
- Milestone: All roadmap checkboxes complete

**Phase 2: Integration Testing** (Status: Not Started)

- Start Date: [After Phase 1]
- Goal: Validate Ollama deployment workflow end-to-end
- Milestone: Integration scenario passes on all platforms

**Phase 3: Documentation and Content** (Status: In Progress - Planning)

- Demo blog posts written (can be parallel with Phase 1-2)
- User documentation reviewed
- Release notes drafted

**Phase 4: Release Preparation** (Status: Not Started)

- Pre-built binaries created for all platforms
- GitHub releases prepared
- Blog posts finalized
- Marketing materials ready (if applicable)

**Phase 5: Coordinated Launch** (Status: Not Started)

- Target Date: [TBD]
- All three projects release v1.0.0 simultaneously
- Blog posts published (intro + 3 demos)
- Announcement on relevant channels
- YouTube videos (if time permits)

**Phase 6: Post-Launch** (Status: Not Started)

- Monitor for bug reports
- Patch releases as needed (v1.0.1, v1.0.2, etc.)
- Community feedback incorporation

--------------

Individual Project Roadmaps
----------------------------

For detailed MVP implementation plans, see:

- :doc:`AirGap Whisper Roadmap <airgap-whisper:roadmap>`
- :doc:`AirGap Deploy Roadmap <airgap-deploy:roadmap>`
- :doc:`AirGap Transfer Roadmap <airgap-transfer:roadmap>`

Each roadmap documents:

- MVP feature scope
- Implementation milestones
- Definition of done
- What's NOT in MVP (deferred features)
- Progress tracking
