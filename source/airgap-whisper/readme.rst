Whisper Lite
============

A minimal, keyboard-driven desktop application for offline audio transcription using `whisper.cpp <https://github.com/ggerganov/whisper.cpp>`__.

Features
--------

- **Private** - All data stays on your machine. No network calls, no telemetry.
- **Air-gap ready** - Deployable on systems with no internet access
- **Keyboard-driven** - Global hotkeys for recording and copying transcriptions
- **System tray** - Runs in background, no main window required
- **Lightweight** - Pure Rust, single binary (~10-15 MB)

How It Works
------------

1. Press hotkey → start recording (tray icon turns red)
2. Press hotkey → stop and transcribe with whisper.cpp
3. Result appears in tray menu
4. Press hotkey → copy to clipboard

No main window required.

Quick Start
-----------

Prerequisites
~~~~~~~~~~~~~

- **whisper.cpp**: Build whisper.cpp and download a model (base.en recommended for ~140MB)
- **System requirements**: macOS, Windows, or Linux

  - Linux (GNOME): Requires `AppIndicator extension <https://extensions.gnome.org/extension/615/appindicator-support/>`__

Installation
~~~~~~~~~~~~

Build from source with Cargo, or use a pre-built binary for your platform.

First Run
~~~~~~~~~

1. The app appears in your system tray (menu bar on macOS)
2. Right-click and select “Settings”
3. Set paths to whisper.cpp binary and model file

Usage
-----

Recording
~~~~~~~~~

1. Press ``Ctrl+Alt+R`` (or ``⌃⌥R`` on macOS) to start recording
2. Tray icon turns red while recording
3. Press the hotkey again to stop and transcribe
4. Notification shows transcription result

Quick Copy
~~~~~~~~~~

Press ``Ctrl+Alt+C`` (or ``⌃⌥C`` on macOS) to copy your most recent transcription to the clipboard.

Viewing History
~~~~~~~~~~~~~~~

Right-click the tray icon to see recent transcriptions. Click any item to copy it to clipboard.

Default Hotkeys
---------------

- Toggle recording: ``Ctrl+Alt+R`` (or ``⌃⌥R`` on macOS)
- Copy last transcription: ``Ctrl+Alt+C`` (or ``⌃⌥C`` on macOS)

See `SRS <requirements/srs.md>`__ for complete hotkey specifications.

Building
--------

Requires Rust toolchain and platform-specific build tools (C compiler, audio libraries).

See `Development Plan <development-plan.md>`__ for complete build instructions and architecture details.

Air-Gapped Deployment
---------------------

Whisper Lite supports deployment on systems with no internet access. All dependencies can be vendored and transferred offline via USB or other secure methods.

For detailed air-gap deployment procedures, see the airgap-deploy project documentation.

--------------

Privacy
-------

Whisper Lite is **private by architecture**:

- Zero network code in the application
- No analytics, telemetry, or crash reporting
- No update checks or external API calls
- All audio and transcriptions stay on your machine

Platform Support
----------------

+-------------------------+--------------------+---------------------------------+
| Platform                | Support            | Notes                           |
+=========================+====================+=================================+
| macOS                   | Full               | Menu bar app                    |
+-------------------------+--------------------+---------------------------------+
| Windows                 | Full               | System tray app                 |
+-------------------------+--------------------+---------------------------------+
| Linux (KDE, XFCE, etc.) | Full               | System tray app                 |
+-------------------------+--------------------+---------------------------------+
| Linux (GNOME)           | Requires extension | AppIndicator extension          |
+-------------------------+--------------------+---------------------------------+
| Linux (Wayland)         | Limited hotkeys    | Global hotkeys require XWayland |
+-------------------------+--------------------+---------------------------------+

License
-------

Dual-licensed under MIT OR Apache-2.0 (your choice). See `LICENSE.md <LICENSE.md>`__ for details.

Documentation
-------------

This README covers installation and usage. For development and technical specifications, see the documents below.

Start Here
~~~~~~~~~~

+---------------------------------------------+-------------------------------------+
| Document                                    | Purpose                             |
+=============================================+=====================================+
| `principles.md <../principles.md>`__        | Core design principles (read first) |
+---------------------------------------------+-------------------------------------+
| `project-roadmap.md <project-roadmap.md>`__ | Project status and direction        |
+---------------------------------------------+-------------------------------------+

Technical Documentation
~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------+-------------------------------------------------+
| Document                                     | Purpose                                         |
+==============================================+=================================================+
| `Requirements (SRS) <requirements/srs.md>`__ | Detailed functional requirements                |
+----------------------------------------------+-------------------------------------------------+
| `Design (SDD) <design/sdd.md>`__             | Architecture, database schema, component design |
+----------------------------------------------+-------------------------------------------------+
| `Test Plan <testing/plan.md>`__              | Test cases and procedures                       |
+----------------------------------------------+-------------------------------------------------+
| `CLAUDE.md <../CLAUDE.md>`__                 | AI assistant development guidelines             |
+----------------------------------------------+-------------------------------------------------+

Project Planning
~~~~~~~~~~~~~~~~

+--------------------------------------------+---------------------------------+
| Document                                   | Purpose                         |
+============================================+=================================+
| `Development Plan <development-plan.md>`__ | MVP implementation milestones   |
+--------------------------------------------+---------------------------------+
