Test Plan
=========

AirGap Whisper
--------------

**Version:** 1.0.0 **Date:** 2026-01-04 **Standard:** IEEE 829 (simplified for MVP)

--------------

Introduction
---------------

This test plan covers MVP requirements (FR-001 through FR-036, NFR-001 through NFR-006).

--------------

Test Strategy
----------------

Test Levels
~~~~~~~~~~~

=========== ====================== ======================
Level       Scope                  Tools
=========== ====================== ======================
Unit        Individual functions   Rust ``#[test]``
Integration Component interactions Rust integration tests
System      End-to-end workflows   Manual testing
=========== ====================== ======================

Features Not Tested
~~~~~~~~~~~~~~~~~~~

===================== ====================
Feature               Reason
===================== ====================
whisper.cpp internals Third-party software
OS audio APIs         Platform dependency
SQLite engine         Third-party software
===================== ====================

Test Automation Approach
~~~~~~~~~~~~~~~~~~~~~~~~

**MVP:** Manual testing only. Automation deferred until post-MVP stabilization.

**Unit tests (automatable):**

+------------------+----------------------------------+---------------------------------+
| Component        | What to Test                     | Mock Strategy                   |
+==================+==================================+=================================+
| db.rs            | CRUD operations                  | In-memory SQLite (``:memory:``) |
+------------------+----------------------------------+---------------------------------+
| whisper.rs       | Command building, output parsing | Mock ``Command`` output         |
+------------------+----------------------------------+---------------------------------+
| audio.rs         | WAV file format validation       | Pre-recorded test files         |
+------------------+----------------------------------+---------------------------------+

**Integration tests (partially automatable):**

======================= ====================
Test                    Automation Notes
======================= ====================
Database + file storage Use temp directories
Settings persistence    In-memory database
Path validation         Unit testable
======================= ====================

**System tests (manual only):**

================ =============================
Test             Why Manual
================ =============================
Tray icon states Requires visual verification
Global hotkeys   Requires OS-level interaction
Audio recording  Requires microphone hardware
Notifications    Platform-specific behavior
================ =============================

**Mock whisper.cpp:** For CI, create a simple binary that echoes test input:

.. code:: bash

   #!/bin/bash
   # mock-whisper.sh - Returns predictable output for testing
   echo "This is a test transcription."

--------------

Test Cases by Category
-------------------------

Recording Tests
~~~~~~~~~~~~~~~

.. needtable::
   :types: test
   :filter: id.startswith('TC-REC')
   :columns: id,title,tests,priority
   :colwidths: 20,40,20,20
   :style: table
   :sort: id

**Traceable Test Cases (sphinx-needs directives):**

.. test:: Hotkey Starts Recording
   :id: TC-REC-001
   :status: approved
   :tags: whisper, recording, hotkey
   :tests: FR-WHISPER-001
   :priority: high

   **Steps:**

   1. Configure global hotkey in settings
   2. Press configured hotkey
   3. Verify recording starts

   **Expected:** Tray icon shows recording state, audio buffer initializes

.. test:: Hotkey Stops Recording
   :id: TC-REC-002
   :status: approved
   :tags: whisper, recording, hotkey
   :tests: FR-WHISPER-001
   :priority: high

   **Steps:**

   1. Start recording via hotkey
   2. Press hotkey again
   3. Verify recording stops

   **Expected:** WAV file saved, transcription begins

.. test:: Tray Icon Recording State
   :id: TC-REC-003
   :status: approved
   :tags: whisper, recording, ui
   :tests: FR-WHISPER-002
   :priority: high

   **Steps:**

   1. Start recording
   2. Observe tray icon

   **Expected:** Icon changes color/appearance to indicate recording state

.. test:: Default Microphone Capture
   :id: TC-REC-004
   :status: approved
   :tags: whisper, recording, audio
   :tests: FR-WHISPER-003
   :priority: high

   **Steps:**

   1. Start recording with default settings
   2. Speak into system default microphone
   3. Stop recording

   **Expected:** Audio captured from correct device

.. test:: WAV File Format Validation
   :id: TC-REC-005
   :status: approved
   :tags: whisper, recording, audio
   :tests: FR-WHISPER-004
   :priority: high

   **Steps:**

   1. Complete a recording
   2. Inspect generated WAV file

   **Expected:** 16kHz mono WAV format

.. test:: Whisper.cpp Invocation
   :id: TC-TRS-001
   :status: approved
   :tags: whisper, transcription
   :tests: FR-WHISPER-008
   :priority: high

   **Steps:**

   1. Stop recording
   2. Monitor system processes

   **Expected:** whisper.cpp binary executed with correct model path

.. test:: Transcription Text Extraction
   :id: TC-TRS-002
   :status: approved
   :tags: whisper, transcription
   :tests: FR-WHISPER-009
   :priority: high

   **Steps:**

   1. Complete transcription
   2. Check stored text

   **Expected:** Text correctly parsed from whisper.cpp stdout

.. test:: Transcription Notification
   :id: TC-TRS-003
   :status: approved
   :tags: whisper, transcription, ui
   :tests: FR-WHISPER-010
   :priority: high

   **Steps:**

   1. Complete transcription
   2. Observe system notification

   **Expected:** Notification shows preview of transcribed text

.. test:: Transcription Progress Icon
   :id: TC-TRS-004
   :status: approved
   :tags: whisper, transcription, ui
   :tests: FR-WHISPER-011
   :priority: medium

   **Steps:**

   1. Stop recording (transcription starts)
   2. Observe tray icon

   **Expected:** Icon indicates transcription in progress

.. test:: Transcription Error Notification
   :id: TC-TRS-005
   :status: approved
   :tags: whisper, transcription, error
   :tests: FR-WHISPER-012
   :priority: high

   **Steps:**

   1. Simulate whisper.cpp failure (invalid model path)
   2. Attempt transcription

   **Expected:** Error notification displayed with helpful message

.. test:: Tray Menu Shows Recording Duration
   :id: TC-REC-006
   :status: approved
   :tags: whisper, recording, ui
   :tests: FR-WHISPER-005
   :priority: medium

   Verify tray menu displays recording duration while active

.. test:: Recording Duration Limit
   :id: TC-REC-007
   :status: approved
   :tags: whisper, recording
   :tests: FR-WHISPER-006
   :priority: medium

   Verify recording stops at configured duration limit

.. test:: Custom Audio Device
   :id: TC-REC-008
   :status: approved
   :tags: whisper, recording, audio
   :tests: FR-WHISPER-007
   :priority: medium

   Verify custom audio input device selection works correctly

.. test:: Transcription Saved to Database
   :id: TC-HIS-001
   :status: approved
   :tags: whisper, history, database
   :tests: FR-WHISPER-013
   :priority: high

   Verify all transcriptions are saved to SQLite database

.. test:: Tray Menu Shows Recent Items
   :id: TC-HIS-002
   :status: approved
   :tags: whisper, history, ui
   :tests: FR-WHISPER-014
   :priority: high

   Verify tray menu displays recent transcriptions (newest first)

.. test:: Menu Items Show Timestamp and Preview
   :id: TC-HIS-003
   :status: approved
   :tags: whisper, history, ui
   :tests: FR-WHISPER-015
   :priority: medium

   Verify menu items display timestamp and text preview

.. test:: Click Menu Item Copies to Clipboard
   :id: TC-HIS-004
   :status: approved
   :tags: whisper, history, clipboard
   :tests: FR-WHISPER-016
   :priority: high

   Verify clicking menu item copies full transcription to clipboard

.. test:: View History Dialog
   :id: TC-HIS-005
   :status: approved
   :tags: whisper, history, ui
   :tests: FR-WHISPER-017
   :priority: medium

   Verify "View History" opens native dialog with full list

.. test:: Delete Transcription
   :id: TC-HIS-006
   :status: approved
   :tags: whisper, history
   :tests: FR-WHISPER-018
   :priority: medium

   Verify transcription can be deleted from history dialog

.. test:: Hotkey Copies Last Transcription
   :id: TC-OUT-001
   :status: approved
   :tags: whisper, output, hotkey, clipboard
   :tests: FR-WHISPER-019
   :priority: high

   Verify global hotkey copies most recent transcription to clipboard

.. test:: Export to Text File
   :id: TC-OUT-002
   :status: approved
   :tags: whisper, output, file
   :tests: FR-WHISPER-020
   :priority: medium

   Verify transcription can be exported as .txt file from history dialog

.. test:: Settings Dialog Opens
   :id: TC-SET-001
   :status: approved
   :tags: whisper, settings, ui
   :tests: FR-WHISPER-021
   :priority: high

   Verify "Settings" menu item opens native settings dialog

.. test:: Configure Whisper Path
   :id: TC-SET-002
   :status: approved
   :tags: whisper, settings, configuration
   :tests: FR-WHISPER-022
   :priority: high

   Verify whisper.cpp binary path can be configured with file picker

.. test:: Configure Model Path
   :id: TC-SET-003
   :status: approved
   :tags: whisper, settings, configuration
   :tests: FR-WHISPER-023
   :priority: high

   Verify model file path can be configured with file picker

.. test:: Path Validation
   :id: TC-SET-004
   :status: approved
   :tags: whisper, settings, validation
   :tests: FR-WHISPER-024
   :priority: high

   Verify paths are validated to exist before save

.. test:: Configure Hotkeys
   :id: TC-SET-005
   :status: approved
   :tags: whisper, settings, hotkey
   :tests: FR-WHISPER-025
   :priority: high

   Verify global hotkeys can be configured with conflict detection

.. test:: First-Run Prompt
   :id: TC-SET-006
   :status: approved
   :tags: whisper, settings, ux
   :tests: FR-WHISPER-026
   :priority: medium

   Verify first-run prompt appears when paths not configured

.. test:: Tray Icon Shows Status
   :id: TC-TRY-001
   :status: approved
   :tags: whisper, tray, ui
   :tests: FR-WHISPER-027
   :priority: high

   Verify tray icon shows app status (idle/recording/transcribing)

.. test:: Left-Click Toggles Recording
   :id: TC-TRY-002
   :status: approved
   :tags: whisper, tray, ui
   :tests: FR-WHISPER-028
   :priority: high

   Verify left-click on tray icon toggles recording

.. test:: Right-Click Shows Menu
   :id: TC-TRY-003
   :status: approved
   :tags: whisper, tray, ui
   :tests: FR-WHISPER-029
   :priority: high

   Verify right-click shows menu with Recent items, Settings, Quit

.. test:: App Starts Minimized to Tray
   :id: TC-TRY-004
   :status: approved
   :tags: whisper, tray, ui
   :tests: FR-WHISPER-030
   :priority: high

   Verify app starts minimized to tray (no main window)

.. test:: Path Traversal Rejected
   :id: TC-SEC-001
   :status: approved
   :tags: whisper, security
   :tests: FR-WHISPER-031
   :priority: critical

   Verify file paths with ``..`` are rejected

.. test:: SQL Injection Prevention
   :id: TC-SEC-002
   :status: approved
   :tags: whisper, security, database
   :tests: FR-WHISPER-032
   :priority: critical

   Verify parameterized queries prevent SQL injection

.. test:: No Network Calls (Firewall Test)
   :id: TC-SEC-003
   :status: approved
   :tags: whisper, security, privacy
   :tests: FR-WHISPER-033
   :priority: critical

   Verify no network calls using firewall monitoring

.. test:: No Network Calls (Packet Capture)
   :id: TC-SEC-004
   :status: approved
   :tags: whisper, security, privacy
   :tests: FR-WHISPER-033
   :priority: critical

   Verify no network calls using packet capture analysis

.. test:: App Works Offline
   :id: TC-SEC-005
   :status: approved
   :tags: whisper, security, privacy, offline
   :tests: FR-WHISPER-033, NFR-WHISPER-004
   :priority: critical

   Verify app is 100% functional offline (airplane mode test)

.. test:: Cargo Vendor Directory Present
   :id: TC-DEP-001
   :status: approved
   :tags: whisper, deployment
   :tests: FR-WHISPER-034
   :priority: high

   Verify cargo vendor directory is present for offline build

.. test:: Build Succeeds Without Internet
   :id: TC-DEP-002
   :status: approved
   :tags: whisper, deployment
   :tests: FR-WHISPER-035
   :priority: critical

   Verify build process works without internet after initial setup

.. test:: Single-Directory Deployment
   :id: TC-DEP-003
   :status: approved
   :tags: whisper, deployment
   :tests: FR-WHISPER-036
   :priority: medium

   Verify single-directory deployment works (app + whisper.cpp + model)

.. test:: App Launch Time
   :id: TC-NFR-001
   :status: approved
   :tags: whisper, performance
   :tests: NFR-WHISPER-001
   :priority: high

   Verify app launches in < 2 seconds

.. test:: Memory Footprint
   :id: TC-NFR-002
   :status: approved
   :tags: whisper, performance
   :tests: NFR-WHISPER-002
   :priority: high

   Verify memory usage < 100 MB (excluding whisper.cpp)

.. test:: Build on Air-Gapped System
   :id: TC-NFR-003
   :status: approved
   :tags: whisper, deployment, offline
   :tests: NFR-WHISPER-005
   :priority: high

   Verify build succeeds on air-gapped system with no internet

.. test:: System Theme Support
   :id: TC-NFR-004
   :status: approved
   :tags: whisper, ui, accessibility
   :tests: NFR-WHISPER-006
   :priority: medium

   Verify app follows system theme (dark/light)

.. test:: Privacy Guarantee Verification
   :id: TC-NFR-005
   :status: approved
   :tags: whisper, privacy, security
   :tests: NFR-WHISPER-003
   :priority: critical

   Verify no network calls under any circumstance (monitor with network sniffer)

.. test:: Offline Functionality Test
   :id: TC-NFR-006
   :status: approved
   :tags: whisper, offline
   :tests: NFR-WHISPER-004
   :priority: critical

   Verify 100% functionality with network disconnected

.. test:: Transcription Performance
   :id: TC-NFR-007
   :status: approved
   :tags: whisper, performance, transcription
   :tests: NFR-WHISPER-007
   :priority: medium

   Verify transcription completes within 2x recording duration

.. test:: Audio File Integrity Check
   :id: TC-NFR-008
   :status: approved
   :tags: whisper, reliability, audio
   :tests: NFR-WHISPER-008
   :priority: high

   Verify WAV file integrity verified before transcription

.. test:: Database Transaction Safety
   :id: TC-NFR-009
   :status: approved
   :tags: whisper, reliability, database
   :tests: NFR-WHISPER-009
   :priority: high

   Verify database operations use transactions preventing data loss

.. test:: Whisper.cpp Crash Handling
   :id: TC-NFR-010
   :status: approved
   :tags: whisper, reliability, error-handling
   :tests: NFR-WHISPER-010
   :priority: high

   Verify whisper.cpp crashes handled gracefully without audio loss

.. test:: Hotkey Registration Recovery
   :id: TC-NFR-011
   :status: approved
   :tags: whisper, reliability, hotkeys
   :tests: NFR-WHISPER-011
   :priority: medium

   Verify detection and recovery from hotkey registration failures

.. test:: Notification Clarity
   :id: TC-NFR-012
   :status: approved
   :tags: whisper, usability, notifications
   :tests: NFR-WHISPER-012
   :priority: high

   Verify notifications include clear status and transcription preview

.. test:: Tray Icon State Indication
   :id: TC-NFR-013
   :status: approved
   :tags: whisper, usability, tray
   :tests: NFR-WHISPER-013
   :priority: high

   Verify tray icon clearly indicates state (idle/recording/transcribing)

.. test:: Settings Dialog Usability
   :id: TC-NFR-014
   :status: approved
   :tags: whisper, usability, settings
   :tests: NFR-WHISPER-014
   :priority: medium

   Verify settings dialog provides clear labels and validation feedback

.. test:: First-Time Setup Experience
   :id: TC-NFR-015
   :status: approved
   :tags: whisper, usability, setup
   :tests: NFR-WHISPER-015
   :priority: medium

   Verify first-time users guided to configure whisper.cpp path

.. test:: Test Coverage Verification
   :id: TC-NFR-016
   :status: approved
   :tags: whisper, maintainability, testing
   :tests: NFR-WHISPER-016
   :priority: high

   Verify codebase achieves ≥80% test coverage via cargo tarpaulin

.. test:: API Documentation Completeness
   :id: TC-NFR-017
   :status: approved
   :tags: whisper, maintainability, documentation
   :tests: NFR-WHISPER-017
   :priority: high

   Verify all public APIs have rustdoc documentation

.. test:: Clippy Compliance Check
   :id: TC-NFR-018
   :status: approved
   :tags: whisper, maintainability, code-quality
   :tests: NFR-WHISPER-018
   :priority: high

   Verify cargo clippy passes with zero warnings

.. test:: Code Formatting Check
   :id: TC-NFR-019
   :status: approved
   :tags: whisper, maintainability, code-quality
   :tests: NFR-WHISPER-019
   :priority: high

   Verify code formatted with rustfmt (cargo fmt --check)

.. test:: Platform-Specific Tray Support
   :id: TC-NFR-020
   :status: approved
   :tags: whisper, portability, tray
   :tests: NFR-WHISPER-020
   :priority: high

   Verify native tray icons on macOS, Windows, Linux with GNOME AppIndicator

.. test:: Audio Device Compatibility
   :id: TC-NFR-021
   :status: approved
   :tags: whisper, portability, audio
   :tests: NFR-WHISPER-021
   :priority: high

   Verify compatibility with standard audio input devices across platforms

.. test:: Database Growth Performance
   :id: TC-NFR-022
   :status: approved
   :tags: whisper, scalability, database
   :tests: NFR-WHISPER-022
   :priority: medium

   Verify performance with 10,000+ transcriptions without degradation

.. test:: Long Audio Recording Support
   :id: TC-NFR-023
   :status: approved
   :tags: whisper, scalability, audio
   :tests: NFR-WHISPER-023
   :priority: medium

   Verify support for audio recordings up to 120 minutes

.. test:: Large Transcription Handling
   :id: TC-NFR-024
   :status: approved
   :tags: whisper, scalability, transcription
   :tests: NFR-WHISPER-024
   :priority: medium

   Verify handling of transcriptions with 50,000+ characters

.. test:: Optional Database Encryption
   :id: TC-NFR-025
   :status: approved
   :tags: whisper, security, database
   :tests: NFR-WHISPER-025
   :priority: low

   Verify optional SQLite encryption for sensitive transcriptions (if implemented)

Transcription Tests
~~~~~~~~~~~~~~~~~~~

.. needtable::
   :types: test
   :filter: id.startswith('TC-TRS')
   :columns: id,title,tests,priority
   :colwidths: 20,40,20,20
   :style: table
   :sort: id

History Tests
~~~~~~~~~~~~~

.. needtable::
   :types: test
   :filter: id.startswith('TC-HIS')
   :columns: id,title,tests,priority
   :colwidths: 20,40,20,20
   :style: table
   :sort: id

Output Tests
~~~~~~~~~~~~

.. needtable::
   :types: test
   :filter: id.startswith('TC-OUT')
   :columns: id,title,tests,priority
   :colwidths: 20,40,20,20
   :style: table
   :sort: id

Settings Tests
~~~~~~~~~~~~~~

.. needtable::
   :types: test
   :filter: id.startswith('TC-SET')
   :columns: id,title,tests,priority
   :colwidths: 20,40,20,20
   :style: table
   :sort: id

System Tray Tests
~~~~~~~~~~~~~~~~~

.. needtable::
   :types: test
   :filter: id.startswith('TC-TRY')
   :columns: id,title,tests,priority
   :colwidths: 20,40,20,20
   :style: table
   :sort: id

Security Tests
~~~~~~~~~~~~~~

.. needtable::
   :types: test
   :filter: id.startswith('TC-SEC')
   :columns: id,title,tests,priority
   :colwidths: 20,40,20,20
   :style: table
   :sort: id

Deployment Tests
~~~~~~~~~~~~~~~~

.. needtable::
   :types: test
   :filter: id.startswith('TC-DEP')
   :columns: id,title,tests,priority
   :colwidths: 20,40,20,20
   :style: table
   :sort: id

Non-Functional Tests
~~~~~~~~~~~~~~~~~~~~

.. needtable::
   :types: test
   :filter: id.startswith('TC-NFR')
   :columns: id,title,tests,priority
   :colwidths: 20,40,20,20
   :style: table
   :sort: id

--------------

Test Procedures
------------------

Network Isolation Test (TC-SEC-003)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Preconditions:** - App installed - Firewall configured to block all app connections

**Steps:** 1. Enable firewall blocking for app 2. Launch app 3. Record audio (30 seconds) 4. Stop and transcribe 5. View history 6. Check firewall logs

**Pass Criteria:** Zero blocked connection attempts in logs.

Offline Operation Test (TC-SEC-005)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Preconditions:** - App installed with configured whisper.cpp - Network disconnected (airplane mode)

**Steps:** 1. Disconnect network 2. Launch app 3. Record → transcribe → copy 4. Verify all features work

**Pass Criteria:** All operations complete successfully.

Air-Gap Build Test (TC-DEP-002)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Preconditions:** - Fresh clone of repository with vendored dependencies - Network disconnected (airplane mode or air-gapped VM)

**Steps:** 1. Clone repository to air-gapped system 2. Run ``cargo build --release --offline`` 3. Verify binary is produced

**Pass Criteria:** Build completes successfully with no network access.

--------------

Requirements Traceability
-------------------------

This section demonstrates bidirectional traceability between requirements and test cases for AirGap Whisper.

Requirements to Tests Matrix
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following table shows all requirements and their associated test cases.

.. needtable::
   :types: req, nfreq, test
   :columns: id, title, status, type
   :filter: "whisper" in tags
   :style: table

Requirements Coverage
~~~~~~~~~~~~~~~~~~~~~

This table shows only requirements, making it easy to verify coverage completeness.

.. needtable::
   :types: req, nfreq
   :columns: id, title, priority, status
   :filter: "whisper" in tags
   :style: table

.. note::

   To see which tests validate each requirement, refer to the Requirements to Tests Matrix above, or check the individual test case definitions in Section 3.

Test Cases
~~~~~~~~~~

This table lists all test cases with their validation links.

.. needtable::
   :types: test
   :columns: id, title, priority, status, tests
   :filter: "whisper" in tags
   :style: table

The "Tests" column shows which requirements each test case validates (via the :tests: link).

--------------

Pass/Fail Criteria
---------------------

- **All Critical tests must pass** before release
- **All High priority tests must pass** before release
- **Medium priority tests:** 90% pass rate acceptable

--------------

Revision History
----------------

+----------------------+--------------+-----------------------------------------------------+
| Version              | Date         | Description                                         |
+======================+==============+=====================================================+
| 1.0.0                | 2026-01-04   | MVP test cases (36 tests covering FR-001 to FR-036) |
+----------------------+--------------+-----------------------------------------------------+
