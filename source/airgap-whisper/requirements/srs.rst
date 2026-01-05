Software Requirements Specification
===================================

AirGap Whisper
--------------

**Version:** 1.0.0 **Date:** 2026-01-04 **Standard:** IEEE 830 (simplified for MVP)

--------------

1. Introduction
---------------

1.1 Purpose
~~~~~~~~~~~

This SRS defines MVP requirements for AirGap Whisper, an offline audio transcription app.

1.2 Scope
~~~~~~~~~

**Product:** AirGap Whisper — a minimal desktop app for voice-to-text using whisper.cpp.

**In Scope:** - Record audio from microphone - Transcribe using whisper.cpp - Store history in SQLite - Global hotkeys for hands-free operation - System tray for background operation

**Out of Scope (per** `principles.md <../../principles.md>`__\ **):** - Cloud sync, telemetry, auto-updates - FLAC compression, MP3/M4A import - Audio playback, streaming transcription - Word timestamps, speaker diarization

1.3 Definitions
~~~~~~~~~~~~~~~

+-----------------------+--------------------------------------------------------------------+
| Term                  | Definition                                                         |
+=======================+====================================================================+
| whisper.cpp           | C++ implementation of OpenAI’s Whisper model                       |
+-----------------------+--------------------------------------------------------------------+
| System tray           | OS notification area (menu bar on macOS, taskbar on Windows/Linux) |
+-----------------------+--------------------------------------------------------------------+

--------------

2. Overall Description
----------------------

2.1 Product Perspective
~~~~~~~~~~~~~~~~~~~~~~~

Standalone desktop app that shells out to user-installed whisper.cpp. All processing occurs locally with no network connectivity.

See `SDD <../design/sdd.md>`__ for architecture diagrams and component details.

2.2 Constraints
~~~~~~~~~~~~~~~

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

3. Functional Requirements
--------------------------

Priority: **M**\ ust / **S**\ hould / **C**\ ould

3.1 Recording
~~~~~~~~~~~~~

+---------+-------------------------+----------------------------------------------------------+
| ID      | Priority                | Requirement                                              |
+=========+=========================+==========================================================+
| FR-001  | M                       | Global hotkey toggles recording (start/stop)             |
+---------+-------------------------+----------------------------------------------------------+
| FR-002  | M                       | Tray icon changes color/state when recording             |
+---------+-------------------------+----------------------------------------------------------+
| FR-003  | M                       | Audio captured from system default microphone            |
+---------+-------------------------+----------------------------------------------------------+
| FR-004  | M                       | Audio saved as WAV (16kHz mono)                          |
+---------+-------------------------+----------------------------------------------------------+
| FR-005  | S                       | Tray menu shows recording duration while active          |
+---------+-------------------------+----------------------------------------------------------+
| FR-006  | S                       | Configurable recording duration limit (default: 120 min) |
+---------+-------------------------+----------------------------------------------------------+
| FR-007  | S                       | Audio input device selection in settings                 |
+---------+-------------------------+----------------------------------------------------------+

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

3.2 Transcription
~~~~~~~~~~~~~~~~~

+---------+-------------------------+------------------------------------------------------------+
| ID      | Priority                | Requirement                                                |
+=========+=========================+============================================================+
| FR-008  | M                       | On stop, invoke whisper.cpp with configured model          |
+---------+-------------------------+------------------------------------------------------------+
| FR-009  | M                       | Parse whisper.cpp stdout for text                          |
+---------+-------------------------+------------------------------------------------------------+
| FR-010  | M                       | Show notification with transcription preview on completion |
+---------+-------------------------+------------------------------------------------------------+
| FR-011  | M                       | Tray icon indicates transcription in progress              |
+---------+-------------------------+------------------------------------------------------------+
| FR-012  | M                       | Handle transcription errors with system notification       |
+---------+-------------------------+------------------------------------------------------------+

3.3 History
~~~~~~~~~~~

====== ======== ======================================================
ID     Priority Requirement
====== ======== ======================================================
FR-013 M        Save all transcriptions to SQLite
FR-014 M        Tray menu shows recent transcriptions (newest first)
FR-015 M        Menu items show: timestamp and text preview
FR-016 M        Click menu item copies full transcription to clipboard
FR-017 S        “View History” opens native dialog with full list
FR-018 S        Delete transcription from history dialog
====== ======== ======================================================

3.4 Output
~~~~~~~~~~

====== ======== =====================================================
ID     Priority Requirement
====== ======== =====================================================
FR-019 M        Global hotkey copies most recent transcription
FR-020 S        Export transcription as .txt file from history dialog
====== ======== =====================================================

3.5 Settings
~~~~~~~~~~~~

====== ======== ==================================================
ID     Priority Requirement
====== ======== ==================================================
FR-021 M        “Settings” menu item opens native settings dialog
FR-022 M        Configure whisper.cpp binary path with file picker
FR-023 M        Configure model file path with file picker
FR-024 M        Validate paths exist before save
FR-025 M        Configure global hotkeys with conflict detection
FR-026 S        First-run prompt when paths not configured
====== ======== ==================================================

3.6 System Tray
~~~~~~~~~~~~~~~

+---------+-------------------------+----------------------------------------------------------+
| ID      | Priority                | Requirement                                              |
+=========+=========================+==========================================================+
| FR-027  | M                       | Tray icon shows app status (idle/recording/transcribing) |
+---------+-------------------------+----------------------------------------------------------+
| FR-028  | M                       | Left-click tray icon toggles recording                   |
+---------+-------------------------+----------------------------------------------------------+
| FR-029  | M                       | Right-click shows menu: Recent items, Settings, Quit     |
+---------+-------------------------+----------------------------------------------------------+
| FR-030  | M                       | App starts minimized to tray (no main window)            |
+---------+-------------------------+----------------------------------------------------------+

3.7 Security
~~~~~~~~~~~~

====== ======== =======================================
ID     Priority Requirement
====== ======== =======================================
FR-031 M        Sanitize file paths (reject ``..``)
FR-032 M        Use parameterized database queries
FR-033 M        No network calls under any circumstance
====== ======== =======================================

3.8 Deployment
~~~~~~~~~~~~~~

+---------+-------------------------+----------------------------------------------------------+
| ID      | Priority                | Requirement                                              |
+=========+=========================+==========================================================+
| FR-034  | M                       | All dependencies available for offline build             |
+---------+-------------------------+----------------------------------------------------------+
| FR-035  | M                       | Build process works without internet after initial setup |
+---------+-------------------------+----------------------------------------------------------+
| FR-036  | S                       | Single-directory deployment (app + whisper.cpp + model)  |
+---------+-------------------------+----------------------------------------------------------+

--------------

4. Non-Functional Requirements
------------------------------

+----------+------------------------------------+------------------------------------------------------------------+
| ID       | Requirement                        | Target                                                           |
+==========+====================================+==================================================================+
| NFR-001  | App launch time                    | < 2 seconds                                                      |
+----------+------------------------------------+------------------------------------------------------------------+
| NFR-002  | Memory footprint                   | < 100 MB (excluding whisper.cpp)                                 |
+----------+------------------------------------+------------------------------------------------------------------+
| NFR-003  | Privacy                            | All data stays on user’s machine; no network calls, no telemetry |
+----------+------------------------------------+------------------------------------------------------------------+
| NFR-004  | Offline functionality              | 100% functional offline                                          |
+----------+------------------------------------+------------------------------------------------------------------+
| NFR-005  | Air-gap deployment                 | Build and run on systems with no internet access                 |
+----------+------------------------------------+------------------------------------------------------------------+
| NFR-006  | Theme support                      | Follow system (dark/light)                                       |
+----------+------------------------------------+------------------------------------------------------------------+

**Traceable Non-Functional Requirements (sphinx-needs directives):**

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

.. nfreq:: Privacy Guarantee
   :id: NFR-WHISPER-003
   :status: approved
   :tags: whisper, privacy, security
   :priority: must

   All data stays on user's machine; no network calls, no telemetry

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

.. nfreq:: System Theme Support
   :id: NFR-WHISPER-006
   :status: approved
   :tags: whisper, ui, accessibility
   :priority: should

   Follow system theme (dark/light)

--------------

5. Error Handling
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
