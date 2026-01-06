Software Requirements Specification
===================================

AirGap Whisper
--------------

**Version:** 1.0.0 **Date:** 2026-01-04 **Standard:** IEEE 830 (simplified for MVP)

--------------

Introduction
---------------

Purpose
~~~~~~~

This SRS defines MVP requirements for AirGap Whisper, an offline audio transcription app.

Scope
~~~~~

**Product:** AirGap Whisper — a minimal desktop app for voice-to-text using whisper.cpp.

**In Scope:**

- Record audio from microphone
- Transcribe using whisper.cpp
- Store history in SQLite
- Global hotkeys for hands-free operation
- System tray for background operation

**Out of Scope (per** :doc:`Principles </meta/principles>`\ **):**

- Cloud sync, telemetry, auto-updates
- FLAC compression, MP3/M4A import
- Audio playback, streaming transcription
- Word timestamps, speaker diarization

Definitions
~~~~~~~~~~~

+-----------------------+--------------------------------------------------------------------+
| Term                  | Definition                                                         |
+=======================+====================================================================+
| whisper.cpp           | C++ implementation of OpenAI’s Whisper model                       |
+-----------------------+--------------------------------------------------------------------+
| System tray           | OS notification area (menu bar on macOS, taskbar on Windows/Linux) |
+-----------------------+--------------------------------------------------------------------+

--------------

Overall Description
----------------------

Product Perspective
~~~~~~~~~~~~~~~~~~~

Standalone desktop app that shells out to user-installed whisper.cpp. All processing occurs locally with no network connectivity.

See :doc:`SDD <../design/sdd>` for architecture diagrams and component details.

Constraints
~~~~~~~~~~~

+---------------------------------+---------------------------------------------------------------+
| Constraint                      | Description                                                   |
+=================================+===============================================================+
| Offline-only                    | Zero network calls at runtime                                 |
+---------------------------------+---------------------------------------------------------------+
| Air-gap ready                   | Deployable without internet access                            |
+---------------------------------+---------------------------------------------------------------+
| Platforms                       | macOS, Windows, Linux (GNOME requires AppIndicator extension) |
+---------------------------------+---------------------------------------------------------------+
| UI model                        | System tray app with native dialogs (no main window)          |
+---------------------------------+---------------------------------------------------------------+
| Dependencies                    | User installs whisper.cpp and models                          |
+---------------------------------+---------------------------------------------------------------+

--------------

Functional Requirements
--------------------------

Priority: **M**\ ust / **S**\ hould / **C**\ ould

Recording
~~~~~~~~~

.. needtable::
   :types: req
   :filter: "whisper" in tags and "recording" in tags
   :columns: id,priority,title
   :colwidths: 20,20,60
   :style: table
   :sort: id

**Traceable Requirements (sphinx-needs directives):**

.. req:: Global Hotkey Toggle
   :id: FR-WHISPER-001
   :status: approved
   :tags: whisper, recording, hotkey
   :priority: must

   Global hotkey toggles recording (start/stop)

.. req:: Tray Icon Recording State
   :id: FR-WHISPER-002
   :status: approved
   :tags: whisper, recording, ui
   :priority: must

   Tray icon changes color/state when recording

.. req:: Default Microphone Input
   :id: FR-WHISPER-003
   :status: approved
   :tags: whisper, recording, audio
   :priority: must

   Audio captured from system default microphone

.. req:: WAV Audio Format
   :id: FR-WHISPER-004
   :status: approved
   :tags: whisper, recording, audio
   :priority: must

   Audio saved as WAV (16kHz mono)

.. req:: Recording Duration Display
   :id: FR-WHISPER-005
   :status: approved
   :tags: whisper, recording, ui
   :priority: should

   Tray menu shows recording duration while active

.. req:: Recording Duration Limit
   :id: FR-WHISPER-006
   :status: approved
   :tags: whisper, recording
   :priority: should

   Configurable recording duration limit (default: 120 min)

.. req:: Audio Input Device Selection
   :id: FR-WHISPER-007
   :status: approved
   :tags: whisper, recording, audio
   :priority: should

   Audio input device selection in settings

Transcription
~~~~~~~~~~~~~

.. needtable::
   :types: req
   :filter: "whisper" in tags and "transcription" in tags
   :columns: id,priority,title
   :colwidths: 20,20,60
   :style: table
   :sort: id

.. req:: Invoke Whisper.cpp
   :id: FR-WHISPER-008
   :status: approved
   :tags: whisper, transcription
   :priority: must

   On stop, invoke whisper.cpp with configured model

.. req:: Parse Transcription Output
   :id: FR-WHISPER-009
   :status: approved
   :tags: whisper, transcription
   :priority: must

   Parse whisper.cpp stdout for text

.. req:: Transcription Notification
   :id: FR-WHISPER-010
   :status: approved
   :tags: whisper, transcription, ui
   :priority: must

   Show notification with transcription preview on completion

.. req:: Transcription Progress Indicator
   :id: FR-WHISPER-011
   :status: approved
   :tags: whisper, transcription, ui
   :priority: must

   Tray icon indicates transcription in progress

.. req:: Transcription Error Handling
   :id: FR-WHISPER-012
   :status: approved
   :tags: whisper, transcription, error
   :priority: must

   Handle transcription errors with system notification

History
~~~~~~~

.. needtable::
   :types: req
   :filter: "whisper" in tags and "history" in tags
   :columns: id,priority,title
   :colwidths: 20,20,60
   :style: table
   :sort: id

.. req:: Save Transcriptions to Database
   :id: FR-WHISPER-013
   :status: approved
   :tags: whisper, history, database
   :priority: must

   Save all transcriptions to SQLite

.. req:: Show Recent Transcriptions
   :id: FR-WHISPER-014
   :status: approved
   :tags: whisper, history, ui
   :priority: must

   Tray menu shows recent transcriptions (newest first)

.. req:: Transcription Menu Preview
   :id: FR-WHISPER-015
   :status: approved
   :tags: whisper, history, ui
   :priority: must

   Menu items show: timestamp and text preview

.. req:: Copy Transcription on Click
   :id: FR-WHISPER-016
   :status: approved
   :tags: whisper, history, clipboard
   :priority: must

   Click menu item copies full transcription to clipboard

.. req:: View History Dialog
   :id: FR-WHISPER-017
   :status: approved
   :tags: whisper, history, ui
   :priority: should

   "View History" opens native dialog with full list

.. req:: Delete Transcription
   :id: FR-WHISPER-018
   :status: approved
   :tags: whisper, history
   :priority: should

   Delete transcription from history dialog

Output
~~~~~~

.. needtable::
   :types: req
   :filter: "whisper" in tags and "output" in tags
   :columns: id,priority,title
   :colwidths: 20,20,60
   :style: table
   :sort: id

.. req:: Copy Last Transcription Hotkey
   :id: FR-WHISPER-019
   :status: approved
   :tags: whisper, output, hotkey, clipboard
   :priority: must

   Global hotkey copies most recent transcription

.. req:: Export Transcription to File
   :id: FR-WHISPER-020
   :status: approved
   :tags: whisper, output, file
   :priority: should

   Export transcription as .txt file from history dialog

Settings
~~~~~~~~

.. needtable::
   :types: req
   :filter: "whisper" in tags and "settings" in tags
   :columns: id,priority,title
   :colwidths: 20,20,60
   :style: table
   :sort: id

.. req:: Settings Dialog
   :id: FR-WHISPER-021
   :status: approved
   :tags: whisper, settings, ui
   :priority: must

   "Settings" menu item opens native settings dialog

.. req:: Configure Whisper Binary Path
   :id: FR-WHISPER-022
   :status: approved
   :tags: whisper, settings, configuration
   :priority: must

   Configure whisper.cpp binary path with file picker

.. req:: Configure Model Path
   :id: FR-WHISPER-023
   :status: approved
   :tags: whisper, settings, configuration
   :priority: must

   Configure model file path with file picker

.. req:: Path Validation
   :id: FR-WHISPER-024
   :status: approved
   :tags: whisper, settings, validation
   :priority: must

   Validate paths exist before save

.. req:: Hotkey Configuration
   :id: FR-WHISPER-025
   :status: approved
   :tags: whisper, settings, hotkey
   :priority: must

   Configure global hotkeys with conflict detection

.. req:: First-Run Prompt
   :id: FR-WHISPER-026
   :status: approved
   :tags: whisper, settings, ux
   :priority: should

   First-run prompt when paths not configured

System Tray
~~~~~~~~~~~

.. needtable::
   :types: req
   :filter: "whisper" in tags and "tray" in tags
   :columns: id,priority,title
   :colwidths: 20,20,60
   :style: table
   :sort: id

.. req:: Tray Icon Status Display
   :id: FR-WHISPER-027
   :status: approved
   :tags: whisper, tray, ui
   :priority: must

   Tray icon shows app status (idle/recording/transcribing)

.. req:: Tray Icon Click Toggle
   :id: FR-WHISPER-028
   :status: approved
   :tags: whisper, tray, ui
   :priority: must

   Left-click tray icon toggles recording

.. req:: Tray Menu
   :id: FR-WHISPER-029
   :status: approved
   :tags: whisper, tray, ui
   :priority: must

   Right-click shows menu: Recent items, Settings, Quit

.. req:: Minimized Tray Start
   :id: FR-WHISPER-030
   :status: approved
   :tags: whisper, tray, ui
   :priority: must

   App starts minimized to tray (no main window)

Security
~~~~~~~~

.. needtable::
   :types: req
   :filter: "whisper" in tags and "security" in tags
   :columns: id,priority,title
   :colwidths: 20,20,60
   :style: table
   :sort: id

.. req:: Path Sanitization
   :id: FR-WHISPER-031
   :status: approved
   :tags: whisper, security
   :priority: must

   Sanitize file paths (reject `..`)

.. req:: Parameterized Queries
   :id: FR-WHISPER-032
   :status: approved
   :tags: whisper, security, database
   :priority: must

   Use parameterized database queries

.. req:: No Network Calls
   :id: FR-WHISPER-033
   :status: approved
   :tags: whisper, security, privacy
   :priority: must

   No network calls under any circumstance

Deployment
~~~~~~~~~~

.. needtable::
   :types: req
   :filter: "whisper" in tags and "deployment" in tags
   :columns: id,priority,title
   :colwidths: 20,20,60
   :style: table
   :sort: id

.. req:: Offline Build Dependencies
   :id: FR-WHISPER-034
   :status: approved
   :tags: whisper, deployment
   :priority: must

   All dependencies available for offline build

.. req:: Internet-Free Build
   :id: FR-WHISPER-035
   :status: approved
   :tags: whisper, deployment
   :priority: must

   Build process works without internet after initial setup

.. req:: Single-Directory Deployment
   :id: FR-WHISPER-036
   :status: approved
   :tags: whisper, deployment
   :priority: should

   Single-directory deployment (app + whisper.cpp + model)

--------------

Non-Functional Requirements
------------------------------

.. needtable::
   :types: nfreq
   :filter: "whisper" in tags
   :columns: id,priority,title
   :colwidths: 20,20,60
   :style: table
   :sort: id

Performance
~~~~~~~~~~~

.. nfreq:: App Launch Time
   :id: NFR-WHISPER-001
   :status: approved
   :tags: whisper, performance
   :priority: must

   App launch time < 2 seconds

.. nfreq:: Memory Footprint
   :id: NFR-WHISPER-002
   :status: approved
   :tags: whisper, performance
   :priority: must

   Memory footprint < 100 MB (excluding whisper.cpp)

.. nfreq:: Transcription Performance
   :id: NFR-WHISPER-007
   :status: approved
   :tags: whisper, performance, transcription
   :priority: should

   Transcription completion time SHALL be within 2x the recording duration

Reliability
~~~~~~~~~~~

.. nfreq:: Audio File Integrity
   :id: NFR-WHISPER-008
   :status: approved
   :tags: whisper, reliability, audio
   :priority: must

   The system SHALL verify WAV file integrity before transcription

.. nfreq:: Database Transaction Safety
   :id: NFR-WHISPER-009
   :status: approved
   :tags: whisper, reliability, database
   :priority: must

   Database operations SHALL use transactions to prevent data loss

.. nfreq:: Graceful Whisper.cpp Failure
   :id: NFR-WHISPER-010
   :status: approved
   :tags: whisper, reliability, error-handling
   :priority: must

   The system SHALL handle whisper.cpp crashes gracefully without losing audio

.. nfreq:: Hotkey Registration Recovery
   :id: NFR-WHISPER-011
   :status: approved
   :tags: whisper, reliability, hotkeys
   :priority: should

   The system SHALL detect and recover from hotkey registration failures

Usability
~~~~~~~~~

.. nfreq:: System Theme Support
   :id: NFR-WHISPER-006
   :status: approved
   :tags: whisper, ui, accessibility
   :priority: should

   Follow system theme (dark/light)

.. nfreq:: Notification Clarity
   :id: NFR-WHISPER-012
   :status: approved
   :tags: whisper, usability, notifications
   :priority: must

   System notifications SHALL include clear status and transcription preview

.. nfreq:: Tray Icon State Visibility
   :id: NFR-WHISPER-013
   :status: approved
   :tags: whisper, usability, tray
   :priority: must

   Tray icon SHALL clearly indicate app state (idle/recording/transcribing)

.. nfreq:: Settings Discoverability
   :id: NFR-WHISPER-014
   :status: approved
   :tags: whisper, usability, settings
   :priority: should

   Settings dialog SHALL provide clear labels and validation feedback

.. nfreq:: First-Time Setup
   :id: NFR-WHISPER-015
   :status: approved
   :tags: whisper, usability, setup
   :priority: should

   First-time users SHALL be guided to configure whisper.cpp path via clear prompts

Maintainability
~~~~~~~~~~~~~~~

.. nfreq:: Test Coverage
   :id: NFR-WHISPER-016
   :status: approved
   :tags: whisper, maintainability, testing
   :priority: must

   The codebase SHALL achieve at least 80% test coverage

.. nfreq:: API Documentation
   :id: NFR-WHISPER-017
   :status: approved
   :tags: whisper, maintainability, documentation
   :priority: must

   All public APIs SHALL have rustdoc documentation

.. nfreq:: Clippy Compliance
   :id: NFR-WHISPER-018
   :status: approved
   :tags: whisper, maintainability, code-quality
   :priority: must

   The code SHALL pass cargo clippy with zero warnings

.. nfreq:: Code Formatting
   :id: NFR-WHISPER-019
   :status: approved
   :tags: whisper, maintainability, code-quality
   :priority: must

   The code SHALL be formatted with rustfmt

Portability
~~~~~~~~~~~

.. nfreq:: Platform-Specific Tray Support
   :id: NFR-WHISPER-020
   :status: approved
   :tags: whisper, portability, tray
   :priority: must

   The system SHALL support native tray icons on macOS, Windows, Linux (GNOME with AppIndicator)

.. nfreq:: Audio Device Compatibility
   :id: NFR-WHISPER-021
   :status: approved
   :tags: whisper, portability, audio
   :priority: must

   The system SHALL work with standard audio input devices across all platforms

Scalability
~~~~~~~~~~~

.. nfreq:: Database Growth Handling
   :id: NFR-WHISPER-022
   :status: approved
   :tags: whisper, scalability, database
   :priority: should

   The system SHALL handle databases with 10,000+ transcriptions without performance degradation

.. nfreq:: Long Audio Support
   :id: NFR-WHISPER-023
   :status: approved
   :tags: whisper, scalability, audio
   :priority: should

   The system SHALL support audio recordings up to 120 minutes

.. nfreq:: Large Transcription Handling
   :id: NFR-WHISPER-024
   :status: approved
   :tags: whisper, scalability, transcription
   :priority: should

   The system SHALL handle transcriptions with 50,000+ characters

Security & Privacy
~~~~~~~~~~~~~~~~~~

.. nfreq:: Privacy Guarantee
   :id: NFR-WHISPER-003
   :status: approved
   :tags: whisper, privacy, security
   :priority: must

   All data stays on user's machine; no network calls, no telemetry

.. nfreq:: Local Data Encryption
   :id: NFR-WHISPER-025
   :status: approved
   :tags: whisper, security, database
   :priority: could

   The system COULD support optional SQLite encryption for sensitive transcriptions

Deployment
~~~~~~~~~~

.. nfreq:: Offline Functionality
   :id: NFR-WHISPER-004
   :status: approved
   :tags: whisper, offline
   :priority: must

   100% functional offline

.. nfreq:: Air-Gap Deployment
   :id: NFR-WHISPER-005
   :status: approved
   :tags: whisper, deployment, offline
   :priority: must

   Build and run on systems with no internet access

--------------

Error Handling
-----------------

+-----------------------------------+--------------------------------------------------------+
| Scenario                          | Behavior                                               |
+===================================+========================================================+
| Whisper binary not found          | Open settings dialog with path field focused           |
+-----------------------------------+--------------------------------------------------------+
| Model file not found              | Open settings dialog with path field focused           |
+-----------------------------------+--------------------------------------------------------+
| Whisper process crashes           | System notification with error, menu option to retry   |
+-----------------------------------+--------------------------------------------------------+
| Microphone permission denied      | System notification explaining how to grant permission |
+-----------------------------------+--------------------------------------------------------+
| Disk full during recording        | Stop recording, save partial, system notification      |
+-----------------------------------+--------------------------------------------------------+
| Hotkey registration failed        | System notification, app continues without that hotkey |
+-----------------------------------+--------------------------------------------------------+
| Hotkey conflict with system       | Warning in settings, allow override with confirmation  |
+-----------------------------------+--------------------------------------------------------+

--------------

Appendix: Default Hotkeys
-------------------------

================ ======= ==============
Action           macOS   Windows/Linux
================ ======= ==============
Toggle recording ``⌃⌥R`` ``Ctrl+Alt+R``
Copy last        ``⌃⌥C`` ``Ctrl+Alt+C``
================ ======= ==============

--------------

Revision History
----------------

+----------------------+--------------+----------------------------------------------------+
| Version              | Date         | Description                                        |
+======================+==============+====================================================+
| 1.0.0                | 2026-01-04   | MVP requirements (36 functional, 6 non-functional) |
+----------------------+--------------+----------------------------------------------------+
