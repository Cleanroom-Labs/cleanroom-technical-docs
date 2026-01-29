Meta-Architecture
=================

**Purpose:** Document relationships, boundaries, and dependencies between the three Cleanroom Labs projects

Project Overview
----------------

The AirGap suite consists of three independent but complementary projects:

+-----------------------+----------------------+---------------------------------------------+-----------------------------------------------------------+
| Project               | Type                 | Purpose                                     | Primary Users                                             |
+=======================+======================+=============================================+===========================================================+
| **AirGap Transfer**   | Utility              | Transfer large files across air-gaps        | IT staff, users with large datasets                       |
+-----------------------+----------------------+---------------------------------------------+-----------------------------------------------------------+
| **AirGap Deploy**     | Developer tool       | Package applications for air-gap deployment | Developers, maintainers, release engineers                |
+-----------------------+----------------------+---------------------------------------------+-----------------------------------------------------------+
| **Cleanroom Whisper** | End-user application | Offline audio transcription                 | Privacy-conscious users, researchers, accessibility users |
+-----------------------+----------------------+---------------------------------------------+-----------------------------------------------------------+

Architecture Diagram
--------------------

.. code-block:: none

   ┌───────────────────────────────────────────────────────────────────────────────┐
   │                         Cleanroom Labs Project Suite                          │
   └───────────────────────────────────────────────────────────────────────────────┘

   ┌─────────────────────┐      ┌─────────────────────┐      ┌─────────────────────┐
   │  Cleanroom Whisper  │      │   AirGap Deploy     │      │  AirGap Transfer    │
   │                     │      │                     │      │                     │
   │  End-User App       │      │  Developer Tool     │      │  Utility            │
   │  ┌──────────────┐   │      │  ┌──────────────┐   │      │  ┌──────────────┐   │
   │  │ Audio Record │   │      │  │ Manifest     │   │      │  │ Pack/Chunk   │   │
   │  │ Transcribe   │   │      │  │ Parser       │   │      │  │ Files        │   │
   │  │ System Tray  │   │      │  │              │   │      │  │              │   │
   │  │ SQLite DB    │   │      │  │ Component    │   │      │  │ Verify       │   │
   │  └──────────────┘   │      │  │ Collectors   │   │      │  │ Checksums    │   │
   │                     │      │  │              │   │      │  │              │   │
   │  Dependencies:      │      │  │ Package      │   │      │  │ Unpack/      │   │
   │  - whisper.cpp      ├─────▶│  │ Generator    │   │      │  │ Reconstruct  │   │
   │  - Whisper models   │ (1)  │  │              │   │      │  └──────────────┘   │
   │                     │      │  │ Install      │   │      │                     │
   │  Can be deployed    │      │  │ Script Gen   │   │      │  Used for:          │
   │  using airgap-      │      │  └──────────────┘   │      │  - Large packages   │
   │  deploy             │      │         │           │      │  - Multi-USB        │
   │                     │      │         │ (2)       │      │  - Dataset transfer │
   └─────────────────────┘      │         ▼           │      └─────────────────────┘
                                │  ┌──────────────┐   │               ▲
                                │  │ Package too  │   │               │
                                │  │ large?       │───┼───────────────┘
                                │  └──────────────┘   │      (3)
                                │                     │   Integration
                                │  Output:            │   in workflows
                                │  - .tar.gz/.zip     │
                                │  - install.sh/ps1   │
                                └─────────────────────┘

   Legend:
     (1) Cleanroom Whisper can be packaged using AirGap Deploy for air-gap deployment
     (2) If package exceeds USB capacity, workflow suggests AirGap Transfer
     (3) AirGap Transfer handles chunked file transfer

Project Relationships
---------------------

Cleanroom Whisper ↔ AirGap Deploy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Relationship:** Cleanroom Whisper is a **reference implementation** and **primary use case** for AirGap Deploy.

**How they relate:**

- AirGap Deploy packages Cleanroom Whisper (with dependencies) for air-gapped systems
- Deployment use case documented in :doc:`airgap-deploy:use-cases/use-case-airgap-whisper`
- Cleanroom Whisper's ``AirGapDeploy.toml`` defines packaging requirements

**Independence:**

- Cleanroom Whisper can be built/deployed manually without AirGap Deploy
- AirGap Deploy can package any application, not just Cleanroom Whisper

**Code dependencies:** None (no compile-time or runtime dependency)

--------------

AirGap Deploy ↔ AirGap Transfer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Relationship:** AirGap Transfer is an **optional workflow enhancement** for AirGap Deploy.

**How they relate:**

- When AirGap Deploy creates packages larger than USB capacity, workflows suggest using AirGap Transfer
- AirGap Transfer chunks the deployment package for multi-USB transfer
- Integration is at the **workflow level**, not code level
- Use case documented in :doc:`airgap-deploy:use-cases/use-case-ollama`

**Example workflow:**

.. code:: bash

   # Developer creates large package (e.g., Ollama + multiple LLM models = 20GB)
   airgap-deploy prep --manifest AirGapDeploy.ollama.toml
   # Output: ollama-deploy-20GB.tar.gz

   # Package exceeds 16GB USB capacity
   # User employs airgap-transfer to chunk it
   airgap-transfer pack ollama-deploy-20GB.tar.gz /media/usb --chunk-size 16GB

   # Transfer chunks across air-gap with multiple USBs

   # Reconstruct on air-gapped system
   airgap-transfer unpack /media/usb ~/deployment/

   # Then install as normal
   cd ~/deployment/ollama-deploy
   sudo ./install.sh

**Independence:**

- AirGap Deploy works fine for packages that fit on single USB
- AirGap Transfer can be used for any large file transfer, not just deployment packages

**Code dependencies:** None (workflow integration only)

Cleanroom Whisper ↔ AirGap Transfer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Relationship:** No direct relationship.

**Indirect connection:**

- If Cleanroom Whisper is packaged with large models, the deployment package might need AirGap Transfer
- AirGap Transfer docs list integration with deployment workflows: :doc:`airgap-transfer:use-cases/overview`

**Code dependencies:** None

Use Cases
---------

Each project defines detailed use cases. For a full understanding
of how these tools are envisioned to work — individually and together — explore the
use case documentation below.

.. raw:: html

   <div style="margin-top: 1.5em;"></div>

**Use case counts by project:**

==================  =====
Project             Count
==================  =====
Cleanroom Whisper   :need_count:`type=='usecase' and 'whisper' in tags`
AirGap Deploy       :need_count:`type=='usecase' and 'deploy' in tags`
AirGap Transfer     :need_count:`type=='usecase' and 'transfer' in tags`
**Total**           :need_count:`type=='usecase'`
==================  =====

**Use case overview:**

.. raw:: html

   <div style="margin-top: 1.5em;"></div>

.. needtable::
   :types: usecase
   :columns: id, title, status, tags
   :style: table

**Explore the full use case documentation:**

- :doc:`airgap-transfer:use-cases/index` — File transfer use cases
- :doc:`airgap-deploy:use-cases/index` — Deployment packaging use cases
- :doc:`cleanroom-whisper:use-cases/index` — Transcription application use cases

Dependency Analysis
-------------------

Compile-Time Dependencies
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none

   Cleanroom Whisper dependencies:
     - whisper.cpp (external, build-time)
     - Rust crates: ~10 direct dependencies
     - NO dependency on AirGap Deploy or AirGap Transfer

   AirGap Deploy dependencies:
     - Rust crates: reqwest, serde, toml, tar, etc.
     - Dependency on AirGap Transfer
     - NO dependency on Cleanroom Whisper or AirGap Transfer

   AirGap Transfer dependencies:
     - Rust crates: sha2, minimal stdlib usage
     - NO dependency on Cleanroom Whisper or AirGap Deploy

**Result:** ✅ **Zero circular dependencies**.

Runtime Dependencies
~~~~~~~~~~~~~~~~~~~~

.. code-block:: none

   Cleanroom Whisper runtime:
     - Requires whisper.cpp binary (external process)
     - Requires at least one Whisper model file
     - NO runtime dependency on other AirGap tools

   AirGap Deploy runtime:
     - NO runtime dependencies on other AirGap tools
     - May invoke git, cargo vendor, wget/curl (system tools)

   AirGap Transfer runtime:
     - NO runtime dependencies on other AirGap tools
     - Pure Rust, uses only stdlib

**Result:** ✅ **Zero runtime dependencies** - Each project runs independently.

Workflow Dependencies
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none

   Developer deploying Cleanroom Whisper:
     1. Use AirGap Deploy to create package
     2. (Optional) Use AirGap Transfer if package is large
     3. Install Cleanroom Whisper on air-gapped system

   User transferring large dataset:
     1. Use AirGap Transfer directly
     2. NO need for other tools

   Developer deploying other applications:
     1. Use AirGap Deploy with custom manifest
     2. (Optional) Use AirGap Transfer if needed
     3. NO connection to Cleanroom Whisper

**Result:** ✅ **Workflow integration is optional** - Tools complement each other but work independently.

Project Boundaries
------------------

.. _cleanroom-whisper-1:

Cleanroom Whisper
~~~~~~~~~~~~~~~~~

**Value:** "Private, offline audio transcription you can trust"

**Target audience:** Privacy-conscious professionals, government/military users, researchers handling sensitive data, accessibility users

**Alternative to:** Cloud transcription services (Google, AWS Transcribe, Whisper API)

**Differentiator:** Complete offline operation, no data leaves your machine

**Scope:**

- ✅ Audio recording and transcription
- ✅ System tray interface
- ✅ Hotkey management
- ✅ Transcription history (SQLite)
- ✅ Privacy-focused, offline-first

**Out of scope:**

- ❌ Deployment packaging (that's AirGap Deploy)
- ❌ File transfer utilities (that's AirGap Transfer)
- ❌ Network communication (violates privacy principle)

.. _AirGap Deploy-1:

AirGap Deploy
~~~~~~~~~~~~~

**Value:** "Deploy any application to air-gapped systems with one manifest"

**Target audience:** Developers releasing software for air-gapped use, DevOps/release engineers, open-source maintainers targeting security-sensitive users

**Alternative to:** Manual packaging, custom deployment scripts per application

**Differentiator:** Declarative manifests, cross-platform, handles complex dependencies

**Scope:**

- ✅ Parse deployment manifests (TOML)
- ✅ Collect application components (source, binaries, models)
- ✅ Generate installation scripts (Bash, PowerShell)
- ✅ Package for air-gap deployment
- ✅ Generic, works for any application

**Out of scope:**

- ❌ Large file chunking/transfer (suggest AirGap Transfer in workflows)
- ❌ Application-specific logic (remains generic)
- ❌ Runtime dependencies on specific applications

.. _AirGap Transfer-1:

AirGap Transfer
~~~~~~~~~~~~~~~

**Value:** "Safely transfer multi-GB datasets across air-gaps"

**Target audience:** IT staff managing air-gapped infrastructure, users with large datasets (models, backups), anyone working with data that exceeds USB capacity

**Alternative to:** Manual chunking with ``split``, complex rsync workflows, proprietary tools

**Differentiator:** Built-in verification, resume capability, simple CLI

**Scope:**

- ✅ Chunk large files/directories
- ✅ SHA-256 verification
- ✅ Resume interrupted transfers
- ✅ Reconstruct files on destination
- ✅ Generic, works for any large data

**Out of scope:**

- ❌ Application packaging (that's AirGap Deploy)
- ❌ Deployment orchestration (users combine tools in workflows)
- ❌ Audio transcription or other application features


