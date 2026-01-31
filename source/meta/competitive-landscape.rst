Competitive Landscape
=====================

**Purpose:** Summarize the competitive positioning of each Cleanroom Labs project and the integrated suite.

Per-Project Competitive Analysis
---------------------------------

AirGap Transfer
~~~~~~~~~~~~~~~

See :ref:`competitive analysis <airgap-transfer-readme-competition>`

- vs manual processes (tar + split, manual copying)
- vs rsync (no multi-USB orchestration)
- vs enterprise backup (Commvault, Veeam, BigFix)
- vs hardware solutions (data diodes, Owl Defense)
- **Unique**: Only lightweight, manifest-driven multi-USB chunking tool

AirGap Deploy
~~~~~~~~~~~~~

See :ref:`competitive analysis <airgap-deploy-readme-competition>`

- vs Kubernetes tools (Zarf, UDS, KOSI)
- vs container platforms (Docker, Podman)
- vs enterprise tools (JFrog, NetBox, Commvault)
- vs language-specific tools (pip download, cargo-vendor)
- vs build systems (Bazel, CMake)
- vs package managers (Nix, Homebrew, Flatpak)
- **Unique**: Only tool for packaging Rust apps + ML models for air-gap desktop deployment

Cleanroom Whisper
~~~~~~~~~~~~~~~~~

See :ref:`competitive analysis <cleanroom-whisper-readme-competition>`

- vs macOS-only tools (MacWhisper, VoiceInk, Superwhisper)
- vs cloud services (Otter.ai, Fireflies, Whisper API)
- vs file transcription tools (Vibe Transcribe, Speech Note)
- **Unique**: Only cross-platform, air-gap-ready voice transcription tool

--------------

Integrated Suite Comparison
---------------------------

+-------------------------------+--------------------------------+-------------------+----------------------+
| Feature                       | AirGap Suite                   | Individual Tools  | Enterprise Solutions |
+===============================+================================+===================+======================+
| Complete air-gap workflow     | ✅ All-in-one                  | ❌ Piece together | ⚠️  Complex setup    |
+-------------------------------+--------------------------------+-------------------+----------------------+
| Privacy-first architecture    | ✅ Zero network                | ⚠️  Varies        | ❌ Cloud-dependent   |
+-------------------------------+--------------------------------+-------------------+----------------------+
| Cross-platform                | ✅ Full support                | ⚠️  Limited       | ⚠️  Varies           |
+-------------------------------+--------------------------------+-------------------+----------------------+
| Minimal dependencies          | ✅ <10 crates                  | ❌ 20-50+ deps    | ❌ Heavy stack       |
+-------------------------------+--------------------------------+-------------------+----------------------+
| Cost                          | ✅ AGPL (commercial available) | ⚠️  Mixed         | ❌ Expensive         |
+-------------------------------+--------------------------------+-------------------+----------------------+
| Offline documentation         | ✅ Sphinx docs                 | ⚠️  Online only   | ⚠️  Varies           |
+-------------------------------+--------------------------------+-------------------+----------------------+
