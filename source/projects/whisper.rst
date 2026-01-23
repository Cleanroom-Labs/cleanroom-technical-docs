AirGap Whisper
==============

**Offline Audio Transcription Application**

AirGap Whisper is an end-user desktop application for offline audio transcription using whisper.cpp. It provides a simple, privacy-first way to transcribe audio recordings without any network connection.

Quick Links
-----------

* `View Full Documentation <../airgap-whisper/index.html>`_
* `Requirements Specification <../airgap-whisper/requirements/srs.html>`_
* `Design Document <../airgap-whisper/design/sdd.html>`_
* `Implementation Roadmap <../airgap-whisper/roadmap.html>`_
* `Use Cases <../airgap-whisper/use-cases/overview.html>`_

Key Features
------------

* **Privacy-first**: All transcription happens locally, no data leaves your computer
* **Simple UI**: System tray icon with global hotkey support
* **Persistent storage**: SQLite database for transcription history
* **Minimal dependencies**: Pure Rust with whisper.cpp integration

Project Status
--------------

See the :doc:`roadmap <airgap-whisper:roadmap>` for current implementation status and milestones.

Core Principles
---------------

AirGap Whisper follows the :doc:`/meta/principles` established for all AirGap projects:

* Privacy through data locality (no network code)
* Minimal dependencies (≤10 direct Rust crates)
* Simple architecture (obvious, maintainable code)
* Air-gap ready (works with zero internet access)

Related Projects
----------------

* :doc:`deploy` - Deploy AirGap Whisper to air-gapped systems
* :doc:`transfer` - Transfer large model files to air-gapped machines
