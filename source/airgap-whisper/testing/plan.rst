Test Plan
=========

Whisper Lite
------------

**Version:** 1.0.0 **Date:** 2026-01-04 **Standard:** IEEE 829 (simplified for MVP)

--------------

1. Introduction
---------------

This test plan covers MVP requirements (FR-001 through FR-036, NFR-001 through NFR-006).

--------------

2. Test Strategy
----------------

2.1 Test Levels
~~~~~~~~~~~~~~~

=========== ====================== ======================
Level       Scope                  Tools
=========== ====================== ======================
Unit        Individual functions   Rust ``#[test]``
Integration Component interactions Rust integration tests
System      End-to-end workflows   Manual testing
=========== ====================== ======================

2.2 Features Not Tested
~~~~~~~~~~~~~~~~~~~~~~~

===================== ====================
Feature               Reason
===================== ====================
whisper.cpp internals Third-party software
OS audio APIs         Platform dependency
SQLite engine         Third-party software
===================== ====================

2.3 Test Automation Approach
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

3. Test Cases by Category
-------------------------

3.1 Recording Tests
~~~~~~~~~~~~~~~~~~~

========== ================================== =========== ========
ID         Description                        Requirement Priority
========== ================================== =========== ========
TC-REC-001 Hotkey starts recording            FR-001      High
TC-REC-002 Hotkey stops recording             FR-001      High
TC-REC-003 Tray icon shows recording state    FR-002      High
TC-REC-004 Audio captured from default mic    FR-003      High
TC-REC-005 WAV file created (16kHz mono)      FR-004      High
TC-REC-006 Tray menu shows recording duration FR-005      Medium
TC-REC-007 Recording stops at duration limit  FR-006      Medium
TC-REC-008 Custom audio device works          FR-007      Medium
========== ================================== =========== ========

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

3.2 Transcription Tests
~~~~~~~~~~~~~~~~~~~~~~~

+------------+------------------------------------------+----------------------+-----------------+
| ID         | Description                              | Requirement          | Priority        |
+============+==========================================+======================+=================+
| TC-TRS-001 | whisper.cpp invoked on stop              | FR-008               | High            |
+------------+------------------------------------------+----------------------+-----------------+
| TC-TRS-002 | Text extracted from stdout               | FR-009               | High            |
+------------+------------------------------------------+----------------------+-----------------+
| TC-TRS-003 | Notification shows transcription preview | FR-010               | High            |
+------------+------------------------------------------+----------------------+-----------------+
| TC-TRS-004 | Tray icon shows transcribing state       | FR-011               | Medium          |
+------------+------------------------------------------+----------------------+-----------------+
| TC-TRS-005 | Error notification on whisper failure    | FR-012               | High            |
+------------+------------------------------------------+----------------------+-----------------+

3.3 History Tests
~~~~~~~~~~~~~~~~~

========== ===================================== =========== ========
ID         Description                           Requirement Priority
========== ===================================== =========== ========
TC-HIS-001 Transcription saved to database       FR-013      High
TC-HIS-002 Tray menu shows recent items          FR-014      High
TC-HIS-003 Menu items show timestamp and preview FR-015      Medium
TC-HIS-004 Click menu item copies to clipboard   FR-016      High
TC-HIS-005 View History opens native dialog      FR-017      Medium
TC-HIS-006 Delete transcription from dialog      FR-018      Medium
========== ===================================== =========== ========

3.4 Output Tests
~~~~~~~~~~~~~~~~

========== ================================ =========== ========
ID         Description                      Requirement Priority
========== ================================ =========== ========
TC-OUT-001 Hotkey copies last transcription FR-019      High
TC-OUT-002 Export to .txt file              FR-020      Medium
========== ================================ =========== ========

3.5 Settings Tests
~~~~~~~~~~~~~~~~~~

========== ================================== =========== ========
ID         Description                        Requirement Priority
========== ================================== =========== ========
TC-SET-001 Settings menu opens dialog         FR-021      High
TC-SET-002 Configure whisper path with picker FR-022      High
TC-SET-003 Configure model path with picker   FR-023      High
TC-SET-004 Path validation (exists)           FR-024      High
TC-SET-005 Configure hotkeys                  FR-025      High
TC-SET-006 First-run prompt appears           FR-026      Medium
========== ================================== =========== ========

3.6 System Tray Tests
~~~~~~~~~~~~~~~~~~~~~

========== ============================ =========== ========
ID         Description                  Requirement Priority
========== ============================ =========== ========
TC-TRY-001 Tray icon shows status       FR-027      High
TC-TRY-002 Left-click toggles recording FR-028      High
TC-TRY-003 Right-click shows menu       FR-029      High
TC-TRY-004 App starts minimized to tray FR-030      High
========== ============================ =========== ========

3.7 Security Tests
~~~~~~~~~~~~~~~~~~

========== ================================= =============== ========
ID         Description                       Requirement     Priority
========== ================================= =============== ========
TC-SEC-001 Path with ``..`` rejected         FR-031          Critical
TC-SEC-002 SQL injection prevented           FR-032          Critical
TC-SEC-003 No network calls (firewall test)  FR-033          Critical
TC-SEC-004 No network calls (packet capture) FR-033          Critical
TC-SEC-005 App works offline                 FR-033, NFR-004 Critical
========== ================================= =============== ========

3.8 Deployment Tests
~~~~~~~~~~~~~~~~~~~~

========== ================================= =========== ========
ID         Description                       Requirement Priority
========== ================================= =========== ========
TC-DEP-001 Cargo vendor directory present    FR-034      High
TC-DEP-002 Build succeeds without internet   FR-035      Critical
TC-DEP-003 Single-directory deployment works FR-036      Medium
========== ================================= =========== ========

3.9 Non-Functional Tests
~~~~~~~~~~~~~~~~~~~~~~~~

========== ========================== =========== =========
ID         Description                Requirement Target
========== ========================== =========== =========
TC-NFR-001 App launch time            NFR-001     < 2 sec
TC-NFR-002 Memory usage               NFR-002     < 100 MB
TC-NFR-003 Build on air-gapped system NFR-005     Pass/Fail
TC-NFR-004 Theme follows system       NFR-006     Pass/Fail
========== ========================== =========== =========

--------------

4. Test Procedures
------------------

4.1 Network Isolation Test (TC-SEC-003)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Preconditions:** - App installed - Firewall configured to block all app connections

**Steps:** 1. Enable firewall blocking for app 2. Launch app 3. Record audio (30 seconds) 4. Stop and transcribe 5. View history 6. Check firewall logs

**Pass Criteria:** Zero blocked connection attempts in logs.

4.2 Offline Operation Test (TC-SEC-005)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Preconditions:** - App installed with configured whisper.cpp - Network disconnected (airplane mode)

**Steps:** 1. Disconnect network 2. Launch app 3. Record → transcribe → copy 4. Verify all features work

**Pass Criteria:** All operations complete successfully.

4.3 Air-Gap Build Test (TC-DEP-002)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Preconditions:** - Fresh clone of repository with vendored dependencies - Network disconnected (airplane mode or air-gapped VM)

**Steps:** 1. Clone repository to air-gapped system 2. Run ``cargo build --release --offline`` 3. Verify binary is produced

**Pass Criteria:** Build completes successfully with no network access.

--------------

5. Pass/Fail Criteria
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
