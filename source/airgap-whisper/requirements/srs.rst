Software Requirements Specification
===================================

Whisper Lite
------------

**Version:** 1.0.0 **Date:** 2026-01-04 **Standard:** IEEE 830 (simplified for MVP)

--------------

1. Introduction
---------------

1.1 Purpose
~~~~~~~~~~~

This SRS defines MVP requirements for Whisper Lite, an offline audio transcription app.

1.2 Scope
~~~~~~~~~

**Product:** Whisper Lite — a minimal desktop app for voice-to-text using whisper.cpp.

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
