Meta-Architecture
=================

**Purpose:** Document relationships, boundaries, and dependencies between the three AirGap projects

--------------

Project Overview
----------------

The AirGap suite consists of three independent but complementary projects:

+---------------------+----------------------+---------------------------------------------+-----------------------------------------------------------+
| Project             | Type                 | Purpose                                     | Primary Users                                             |
+=====================+======================+=============================================+===========================================================+
| **AirGap Whisper**  | End-user application | Offline audio transcription                 | Privacy-conscious users, researchers, accessibility users |
+---------------------+----------------------+---------------------------------------------+-----------------------------------------------------------+
| **AirGap Deploy**   | Developer tool       | Package applications for air-gap deployment | Developers, maintainers, release engineers                |
+---------------------+----------------------+---------------------------------------------+-----------------------------------------------------------+
| **AirGap Transfer** | Utility              | Transfer large files across air-gaps        | IT staff, users with large datasets                       |
+---------------------+----------------------+---------------------------------------------+-----------------------------------------------------------+

--------------

Architecture Diagram
--------------------

.. code-block:: none

   ┌───────────────────────────────────────────────────────────────────────────────┐
   │                             AirGap Project Suite                              │
   └───────────────────────────────────────────────────────────────────────────────┘

   ┌─────────────────────┐      ┌─────────────────────┐      ┌─────────────────────┐
   │   AirGap Whisper    │      │   AirGap Deploy     │      │  AirGap Transfer    │
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
     (1) AirGap Whisper is packaged using AirGap Deploy for air-gap deployment
     (2) If package exceeds USB capacity, workflow suggests AirGap Transfer
     (3) AirGap Transfer handles chunked file transfer

--------------

Project Relationships
---------------------

AirGap Whisper ↔ AirGap Deploy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Relationship:** AirGap Whisper is a **reference implementation** and **primary use case** for AirGap Deploy.

**How they relate:**

- AirGap Deploy packages AirGap Whisper (with dependencies) for air-gapped systems
- Deployment workflow documented in :doc:`airgap-deploy:use-cases/workflow-airgap-whisper`
- AirGap Whisper's ``AirGapDeploy.toml`` defines packaging requirements

**Independence:**

- AirGap Whisper can be built/deployed manually without AirGap Deploy
- AirGap Deploy can package any application, not just AirGap Whisper

**Code dependencies:** None (no compile-time or runtime dependency)

--------------

AirGap Deploy ↔ AirGap Transfer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Relationship:** AirGap Transfer is an **optional workflow enhancement** for AirGap Deploy.

**How they relate:**

- When AirGap Deploy creates packages larger than USB capacity, workflows suggest using AirGap Transfer
- AirGap Transfer chunks the deployment package for multi-USB transfer
- Integration is at the **workflow level**, not code level

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

--------------

AirGap Whisper ↔ AirGap Transfer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Relationship:** No direct relationship.

**Indirect connection:**

- If AirGap Whisper is packaged with large models, the deployment package might need AirGap Transfer
- AirGap Whisper mentioned in AirGap Transfer docs as example use case

**Code dependencies:** None

--------------

Dependency Analysis
-------------------

Compile-Time Dependencies
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none

   AirGap Whisper dependencies:
     - whisper.cpp (external, build-time)
     - Rust crates: ~10 direct dependencies
     - NO dependency on AirGap Deploy or AirGap Transfer

   AirGap Deploy dependencies:
     - Rust crates: reqwest, serde, toml, tar, etc.
     - Dependency on AirGap Transfer
     - NO dependency on AirGap Whisper or AirGap Transfer

   AirGap Transfer dependencies:
     - Rust crates: sha2, minimal stdlib usage
     - NO dependency on AirGap Whisper or AirGap Deploy

**Result:** ✅ **Zero circular dependencies**.

--------------

Runtime Dependencies
~~~~~~~~~~~~~~~~~~~~

.. code-block:: none

   AirGap Whisper runtime:
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

--------------

Workflow Dependencies
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none

   Developer deploying AirGap Whisper:
     1. Use AirGap Deploy to create package
     2. (Optional) Use AirGap Transfer if package is large
     3. Install AirGap Whisper on air-gapped system

   User transferring large dataset:
     1. Use AirGap Transfer directly
     2. NO need for other tools

   Developer deploying other applications:
     1. Use AirGap Deploy with custom manifest
     2. (Optional) Use AirGap Transfer if needed
     3. NO connection to AirGap Whisper

**Result:** ✅ **Workflow integration is optional** - Tools complement each other but work independently.

--------------

Project Boundaries
------------------

AirGap Whisper
~~~~~~~~~~~~~~

**Scope:**

- ✅ Audio recording and transcription
- ✅ System tray interface
- ✅ Hotkey management
- ✅ Transcription history (SQLite)
- ✅ Privacy-focused, offline-first

**Out of scope:**

- ❌ Deployment packaging (that’s AirGap Deploy)
- ❌ File transfer utilities (that’s AirGap Transfer)
- ❌ Network communication (violates privacy principle)

**Boundaries:**

- End-user application, not a library or framework
- Focused on single use case: offline transcription
- Does NOT reuse code from AirGap Deploy or AirGap Transfer

--------------

AirGap Deploy
~~~~~~~~~~~~~

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

**Boundaries:**

- Developer tool, not end-user application
- Generic packaging framework, not AirGap Whisper-specific
- Does NOT include chunking logic (delegates to AirGap Transfer)

--------------

AirGap Transfer
~~~~~~~~~~~~~~~

**Scope:**

- ✅ Chunk large files/directories
- ✅ SHA-256 verification
- ✅ Resume interrupted transfers
- ✅ Reconstruct files on destination
- ✅ Generic, works for any large data

**Out of scope:**

- ❌ Application packaging (that’s AirGap Deploy)
- ❌ Deployment orchestration (users combine tools in workflows)
- ❌ Audio transcription or other application features

**Boundaries:**

- Utility for file transfer, not a packaging framework
- Generic, not specific to AirGap Whisper or deployment workflows
- Single responsibility: move large data across air-gaps safely

--------------

Value Propositions
------------------

Each project serves a distinct audience with a unique value proposition:

.. _airgap-whisper-1:

AirGap Whisper
~~~~~~~~~~~~~~

**Value:** “Private, offline audio transcription you can trust”

**Target audience:**

- Privacy-conscious professionals
- Government/military users in air-gapped environments
- Researchers handling sensitive data
- Accessibility users needing offline voice-to-text

**Alternative to:** Cloud transcription services (Google, AWS Transcribe, Whisper API)

**Differentiator:** Complete offline operation, no data leaves your machine

--------------

.. _AirGap Deploy-1:

AirGap Deploy
~~~~~~~~~~~~~

**Value:** “Deploy any application to air-gapped systems with one manifest”

**Target audience:**

- Developers releasing software for air-gapped use
- DevOps/release engineers
- Open-source maintainers targeting security-sensitive users

**Alternative to:** Manual packaging, custom deployment scripts per application

**Differentiator:** Declarative manifests, cross-platform, handles complex dependencies

--------------

.. _AirGap Transfer-1:

AirGap Transfer
~~~~~~~~~~~~~~~

**Value:** “Safely transfer multi-GB datasets across air-gaps”

**Target audience:**

- IT staff managing air-gapped infrastructure
- Users needing to transfer large datasets (models, datasets, backups)
- Anyone working with data that exceeds USB capacity

**Alternative to:** Manual chunking with ``split``, complex rsync workflows, proprietary tools

**Differentiator:** Built-in verification, resume capability, simple CLI

--------------

User Journeys
-------------

Journey 1: Developer Releasing AirGap Whisper
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Actors:** AirGap Whisper maintainer, end user

**Scenario:** Create a release package for end users to install on air-gapped systems

**Steps:**

**Developer** creates ``AirGapDeploy.toml`` manifest for AirGap Whisper
**Developer** runs ``airgap-deploy prep`` → generates package (~300MB)
Package fits on single USB, no need for airgap-transfer
**Developer** uploads package to GitHub releases
**End user** downloads package, transfers via USB
**End user** extracts and runs ``./install.sh``
**End user** uses AirGap Whisper for transcription

**Tools used:** AirGap Deploy (packaging), AirGap Whisper (end use)

--------------

Journey 2: Deploying Ollama with Large Models
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Actors:** Developer, air-gapped user

**Scenario:** Deploy Ollama with multiple LLM models (20GB total) to air-gapped system

**Steps:**

**Developer** creates ``AirGapDeploy.ollama.toml`` with 3 models
**Developer** runs ``airgap-deploy prep`` → 20GB package
Package exceeds 16GB USB capacity
**Developer** runs ``airgap-transfer pack`` → chunks into 2x 10GB chunks
**Developer** uploads chunks to file server
**User** downloads chunks, transfers with 2x USB drives
**User** runs ``airgap-transfer unpack`` → reconstructs 20GB package
**User** extracts and runs ``./install.sh`` → installs Ollama + models

**Tools used:** AirGap Deploy (packaging), AirGap Transfer (chunking), Ollama (end use)

--------------

Journey 3: Transferring Research Dataset
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Actors:** Researcher with dataset

**Scenario:** Transfer 500GB research dataset from connected lab to air-gapped analysis system

**Steps:**

**Researcher** has dataset in ``/data/research/``
**Researcher** runs ``airgap-transfer pack /data/research /media/usb1``
Fills USB1 (16GB), prompts for USB2
Continues filling USB2, USB3, …, USB32 (32x 16GB USBs)
Physically transfers USBs to air-gapped system
**Researcher** runs ``airgap-transfer unpack /media/usb1 /data/restored``
Inserts each USB in sequence, airgap-transfer reconstructs dataset
Verifies checksums, data integrity confirmed

**Tools used:** AirGap Transfer only (no deployment, no transcription)

--------------

Integration Points
------------------

Documented Integration
~~~~~~~~~~~~~~~~~~~~~~

**AirGap Deploy workflows mention AirGap Transfer:**

- :doc:`airgap-deploy:use-cases/workflow-ollama` - Shows chunking large Ollama packages
- :doc:`airgap-deploy:use-cases/workflow-airgap-whisper` - Notes option for large packages

**AirGap Transfer docs mention AirGap Deploy:**

- :doc:`airgap-transfer:use-cases/overview` - Lists integration with deployment workflows

**Cross-references maintained** in use case documentation.

--------------

No Integration (By Design)
~~~~~~~~~~~~~~~~~~~~~~~~~~

**AirGap Whisper does NOT integrate with the other tools:**

- No awareness of AirGap Deploy or AirGap Transfer
- Can be packaged manually, with AirGap Deploy, or by other means
- Maintains complete independence

**This is intentional:** AirGap Whisper is an end-user application with its own value, not a component of a larger system.

--------------

Design Principles Alignment
---------------------------

All three projects follow the same core principles from :doc:`/meta/principles`:

+---------------------------+-----------------------------+-------------------------------------+--------------------------+
| Principle                 | AirGap Whisper              | AirGap Deploy                       | AirGap Transfer          |
+===========================+=============================+=====================================+==========================+
| **Privacy/Data Locality** | ✅ No network code          | ✅ No network in generated packages | ✅ No network code       |
+---------------------------+-----------------------------+-------------------------------------+--------------------------+
| **Minimal Dependencies**  | ✅ ~10 crates               | ✅ Essential packaging crates only  | ✅ Minimal stdlib usage  |
+---------------------------+-----------------------------+-------------------------------------+--------------------------+
| **Simple Architecture**   | ✅ Flat structure, ~5 files | ✅ Clear component separation       | ✅ Single responsibility |
+---------------------------+-----------------------------+-------------------------------------+--------------------------+
| **Air-gap Ready**         | ✅ Vendored deps            | ✅ Entire purpose                   | ✅ Designed for air-gaps |
+---------------------------+-----------------------------+-------------------------------------+--------------------------+

--------------

Competitive Advantages of the Integrated Suite
-----------------------------------------------

The AirGap suite occupies a **unique position** in the market by providing an integrated, privacy-first, minimal-dependency solution for air-gapped environments. While component-level competitors exist, no alternative offers the same combination of features.

Why the AirGap Suite?
~~~~~~~~~~~~~~~~~~~~~

**Unique Integration**: The AirGap suite is the only open-source project providing:

1. **Offline voice transcription** (Whisper) - Cross-platform, system tray workflow
2. **Application packaging** (Deploy) - Declarative manifests for desktop apps + ML models
3. **Large file transfer** (Transfer) - Multi-USB chunking with cryptographic verification

**No other project integrates these three capabilities** in a privacy-first, air-gap-ready architecture.

**End-to-End Workflow Example**:

.. code-block:: none

   Developer (Connected System)
     ↓
     1. Create AirGap Whisper deployment manifest
     2. Run airgap-deploy prep → packages app + whisper.cpp + models (~300-400MB)
     3. Package exceeds USB capacity → use airgap-transfer pack to chunk
     4. Transfer USB drives to air-gapped system
     ↓
   Air-Gapped User
     1. Run airgap-transfer unpack to reconstruct package
     2. Run ./install.sh from AirGap Deploy package
     3. Use AirGap Whisper for offline transcription

This complete workflow has **no equivalent** in the open source or commercial space.

Shared Competitive Advantages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All three projects share these differentiators:

**1. Offline-First Architecture**

- ✅ Zero network code (architecture-level guarantee, not just a setting)
- ✅ No analytics, telemetry, crash reporting, or update checks
- ✅ All data stays on local or removable media
- ✅ Works in completely isolated environments (government, healthcare, finance)

**2. Cross-Platform Support**

- ✅ macOS, Windows, and Linux with consistent behavior
- ✅ Single codebase, platform-native integration (system tray, notifications, scripts)
- ✅ No platform-specific tools or frameworks required

**3. Minimal Dependencies**

- ✅ AirGap Whisper: 8 Rust crates
- ✅ AirGap Deploy: Essential packaging crates only
- ✅ AirGap Transfer: Minimal stdlib usage
- ✅ Compare to typical apps: 20-50+ dependencies

**4. Air-Gap Deployment Ready**

- ✅ Vendored dependencies for offline builds
- ✅ No network access required for installation or operation
- ✅ USB transfer workflows built-in
- ✅ Complete documentation for air-gap deployment

**5. Open Source with Permissive Licensing**

- ✅ Dual-licensed MIT OR Apache-2.0 (your choice)
- ✅ No vendor lock-in, no subscription costs
- ✅ Full source code available for security audits
- ✅ Community-driven development

vs Competition
~~~~~~~~~~~~~~

**Individual Project Comparisons** (detailed analysis with competitors):

- **AirGap Whisper**: See :ref:`competitive analysis <airgap-whisper-readme-competition>`

  - vs macOS-only tools (MacWhisper, VoiceInk, Superwhisper)
  - vs cloud services (Otter.ai, Fireflies, Whisper API)
  - vs file transcription tools (Vibe Transcribe, Speech Note)
  - **Unique**: Only cross-platform, air-gap-ready voice transcription tool

- **AirGap Deploy**: See :ref:`competitive analysis <airgap-deploy-readme-competition>`

  - vs Kubernetes tools (Zarf, UDS, KOSI)
  - vs container platforms (Docker, Podman)
  - vs enterprise tools (JFrog, NetBox, Commvault)
  - vs language-specific tools (pip download, cargo-vendor)
  - **Unique**: Only tool for packaging Rust apps + ML models for air-gap desktop deployment

- **AirGap Transfer**: See :ref:`competitive analysis <airgap-transfer-readme-competition>`

  - vs manual processes (tar + split, manual copying)
  - vs rsync (no multi-USB orchestration)
  - vs enterprise backup (Commvault, Veeam, BigFix)
  - vs hardware solutions (data diodes, Owl Defense)
  - **Unique**: Only lightweight, manifest-driven multi-USB chunking tool

**Integrated Suite Advantages**:

+-------------------------------+-------------------+-------------------+----------------------+
| Feature                       | AirGap Suite      | Individual Tools  | Enterprise Solutions |
+===============================+===================+===================+======================+
| Complete air-gap workflow     | ✅ All-in-one     | ❌ Piece together | ⚠️  Complex setup    |
+-------------------------------+-------------------+-------------------+----------------------+
| Privacy-first architecture    | ✅ Zero network   | ⚠️  Varies        | ❌ Cloud-dependent   |
+-------------------------------+-------------------+-------------------+----------------------+
| Cross-platform                | ✅ Full support   | ⚠️  Limited       | ⚠️  Varies           |
+-------------------------------+-------------------+-------------------+----------------------+
| Minimal dependencies          | ✅ <10 crates     | ❌ 20-50+ deps    | ❌ Heavy stack       |
+-------------------------------+-------------------+-------------------+----------------------+
| Cost                          | ✅ Free (MIT/APL) | ⚠️  Mixed         | ❌ Expensive         |
+-------------------------------+-------------------+-------------------+----------------------+
| Offline documentation         | ✅ Sphinx docs    | ⚠️  Online only   | ⚠️  Varies           |
+-------------------------------+-------------------+-------------------+----------------------+

Target Markets
~~~~~~~~~~~~~~

The AirGap suite is designed for organizations and individuals requiring **secure, offline, reproducible software deployment**:

**Government & Defense**

- Classified environments (DoD, intelligence agencies)
- Air-gapped networks for national security
- Compliance: FedRAMP, NIST SP 800-171, CMMC

**Healthcare**

- HIPAA-compliant offline systems
- Patient data privacy requirements
- Medical research with sensitive data

**Finance**

- Isolated trading systems
- Payment processing networks
- Regulatory compliance (PCI-DSS, SOX)

**Industrial Control Systems**

- SCADA/ICS networks
- Critical infrastructure (power, water, transportation)
- Safety-critical systems requiring isolation

**Research Institutions**

- Sensitive data processing
- Reproducible research environments
- Data sovereignty requirements

Market Opportunity
~~~~~~~~~~~~~~~~~~

**Gap in the market**: Existing solutions either:

1. Target Kubernetes/cloud-native (Zarf, UDS) - too complex for desktop apps
2. Platform-specific (MacWhisper, VoiceInk) - limited platform support
3. Commercial/expensive (JFrog, Commvault) - cost prohibitive for many users
4. Manual processes (tar+split, rsync) - error-prone, no automation

**AirGap suite fills this gap** by providing lightweight, open-source, cross-platform tools for the complete air-gap workflow.

--------------

Summary
-------

Three Independent Projects
~~~~~~~~~~~~~~~~~~~~~~~~~~

**AirGap Whisper** - End-user application for offline transcription
**AirGap Deploy** - Developer tool for packaging applications
**AirGap Transfer** - Utility for large file transfer

Relationships
~~~~~~~~~~~~~

- **Code level:** Zero dependencies (completely independent)
- **Workflow level:** Optional integration (AirGap Deploy + AirGap Transfer for large packages)
- **Conceptual level:** Complementary tools in the air-gap ecosystem

Key Insights
~~~~~~~~~~~~

✅ **No circular dependencies**

- Clean separation of concerns ✅ **Each project has distinct value**
- Can be used independently ✅ **Optional workflow integration**
- Users choose when to combine tools ✅ **Shared design principles**
- Consistent philosophy across projects

