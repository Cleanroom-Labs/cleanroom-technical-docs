Test Plan
=========

AirGap Transfer
---------------

**Version:** 1.0.0 **Date:** 2026-01-04 **Standard:** IEEE 829 (simplified for MVP)

--------------

1. Introduction
---------------

This test plan covers MVP requirements (FR-001 through FR-045, NFR-001 through NFR-006).

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

===================== ===================
Feature               Reason
===================== ===================
USB hardware failures External dependency
Filesystem internals  Platform dependency
Tar format compliance Third-party library
===================== ===================

2.3 Test Automation Approach
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**MVP:** Manual testing primarily. Unit tests for core logic.

**Unit tests (automatable):**

=========== ========================================
Component   What to Test
=========== ========================================
chunker.rs  Chunk size calculations, streaming logic
verifier.rs Checksum generation and verification
manifest.rs JSON serialization, state management
=========== ========================================

**Integration tests (partially automatable):**

====================== ====================
Test                   Automation Notes
====================== ====================
Pack + Unpack workflow Use temp directories
Manifest persistence   In-memory filesystem
Checksum verification  Known test vectors
====================== ====================

**System tests (manual only):**

========================= ===================================
Test                      Why Manual
========================= ===================================
USB detection             Requires physical USB hardware
Cross-platform behavior   Requires multiple test machines
Large file handling       Time-intensive, requires disk space
Resume after interruption Requires manual interruption
========================= ===================================

--------------

3. Test Cases by Category
-------------------------

3.1 Pack Operation Tests
~~~~~~~~~~~~~~~~~~~~~~~~

========== =============================== =========== ========
ID         Description                     Requirement Priority
========== =============================== =========== ========
TC-PCK-001 Pack single file into chunks    FR-001      High
TC-PCK-002 Pack directory into chunks      FR-001      High
TC-PCK-003 Auto-detect USB capacity        FR-002      High
TC-PCK-004 Generate chunk checksums        FR-003      High
TC-PCK-005 Create manifest file            FR-004      High
TC-PCK-006 Stream without temp files       FR-005      High
TC-PCK-007 Manual chunk size specification FR-006      Medium
TC-PCK-008 Progress reporting              FR-007      Medium
========== =============================== =========== ========

.. test:: Pack Single File into Chunks
   :id: TC-PCK-001
   :status: approved
   :tags: transfer, pack, chunking
   :tests: FR-TRANSFER-001
   :priority: high

   Verify pack operation splits single file into chunks

.. test:: Pack Directory into Chunks
   :id: TC-PCK-002
   :status: approved
   :tags: transfer, pack, directory
   :tests: FR-TRANSFER-001
   :priority: high

   Verify pack operation handles directory with multiple files

.. test:: Auto-Detect USB Capacity
   :id: TC-PCK-003
   :status: approved
   :tags: transfer, pack, usb
   :tests: FR-TRANSFER-002
   :priority: high

   Verify automatic detection of USB drive capacity

.. test:: Generate Chunk Checksums
   :id: TC-PCK-004
   :status: approved
   :tags: transfer, pack, checksum
   :tests: FR-TRANSFER-003
   :priority: high

   Verify SHA-256 checksums generated for each chunk

.. test:: Create Manifest File
   :id: TC-PCK-005
   :status: approved
   :tags: transfer, pack, manifest
   :tests: FR-TRANSFER-004
   :priority: high

   Verify manifest file creation with chunk metadata

.. test:: Stream Without Temp Files
   :id: TC-PCK-006
   :status: approved
   :tags: transfer, pack, streaming
   :tests: FR-TRANSFER-005
   :priority: high

   Verify pack operation streams data without intermediate temp files

.. test:: Manual Chunk Size Specification
   :id: TC-PCK-007
   :status: approved
   :tags: transfer, pack, chunk-size
   :tests: FR-TRANSFER-006
   :priority: medium

   Verify manual chunk size override functionality

.. test:: Progress Reporting
   :id: TC-PCK-008
   :status: approved
   :tags: transfer, pack, progress
   :tests: FR-TRANSFER-007
   :priority: medium

   Verify progress reporting during pack operation

3.2 Unpack Operation Tests
~~~~~~~~~~~~~~~~~~~~~~~~~~

========== ============================= =========== ========
ID         Description                   Requirement Priority
========== ============================= =========== ========
TC-UNP-001 Reconstruct files from chunks FR-009      High
TC-UNP-002 Verify chunk checksums        FR-010      High
TC-UNP-003 Place files in destination    FR-011      High
TC-UNP-004 Validate chunk completeness   FR-012      High
TC-UNP-005 Resume partial unpack         FR-013      Medium
TC-UNP-006 Delete chunks after unpack    FR-014      Medium
========== ============================= =========== ========

.. test:: Reconstruct Files from Chunks
   :id: TC-UNP-001
   :status: approved
   :tags: transfer, unpack, reconstruction
   :tests: FR-TRANSFER-009
   :priority: high

   Verify unpack reconstructs original files from chunks

.. test:: Verify Chunk Checksums
   :id: TC-UNP-002
   :status: approved
   :tags: transfer, unpack, checksum
   :tests: FR-TRANSFER-010
   :priority: high

   Verify chunk checksums before reconstruction

.. test:: Place Files in Destination
   :id: TC-UNP-003
   :status: approved
   :tags: transfer, unpack, destination
   :tests: FR-TRANSFER-011
   :priority: high

   Verify files placed in correct destination directory

.. test:: Validate Chunk Completeness
   :id: TC-UNP-004
   :status: approved
   :tags: transfer, unpack, validation
   :tests: FR-TRANSFER-012
   :priority: high

   Verify all required chunks present before unpack

.. test:: Resume Partial Unpack
   :id: TC-UNP-005
   :status: approved
   :tags: transfer, unpack, resume
   :tests: FR-TRANSFER-013
   :priority: medium

   Verify unpack can resume after interruption

.. test:: Delete Chunks After Unpack
   :id: TC-UNP-006
   :status: approved
   :tags: transfer, unpack, cleanup
   :tests: FR-TRANSFER-014
   :priority: medium

   Verify optional chunk deletion after successful unpack

3.3 List Operation Tests
~~~~~~~~~~~~~~~~~~~~~~~~

========== =========================== =========== ========
ID         Description                 Requirement Priority
========== =========================== =========== ========
TC-LST-001 Display chunk inventory     FR-016      High
TC-LST-002 Show chunk sizes and status FR-017      High
TC-LST-003 Identify missing chunks     FR-018      Medium
TC-LST-004 Show estimated total size   FR-019      Medium
========== =========================== =========== ========

.. test:: Display Chunk Inventory
   :id: TC-LST-001
   :status: approved
   :tags: transfer, list, inventory
   :tests: FR-TRANSFER-016
   :priority: high

   Verify list command displays all available chunks

.. test:: Show Chunk Sizes and Status
   :id: TC-LST-002
   :status: approved
   :tags: transfer, list, status
   :tests: FR-TRANSFER-017
   :priority: high

   Verify list shows chunk sizes and completion status

.. test:: Identify Missing Chunks
   :id: TC-LST-003
   :status: approved
   :tags: transfer, list, missing
   :tests: FR-TRANSFER-018
   :priority: medium

   Verify list identifies missing chunks from manifest

.. test:: Show Estimated Total Size
   :id: TC-LST-004
   :status: approved
   :tags: transfer, list, size
   :tests: FR-TRANSFER-019
   :priority: medium

   Verify list shows estimated total transfer size

3.4 Integrity Tests
~~~~~~~~~~~~~~~~~~~

========== ============================== =========== ========
ID         Description                    Requirement Priority
========== ============================== =========== ========
TC-INT-001 Generate SHA-256 checksums     FR-020      Critical
TC-INT-002 Verify checksums during unpack FR-021      Critical
TC-INT-003 Detect corrupted chunks        FR-022      Critical
TC-INT-004 Verify final file integrity    FR-023      High
========== ============================== =========== ========

.. test:: Generate SHA-256 Checksums
   :id: TC-INT-001
   :status: approved
   :tags: transfer, integrity, checksum
   :tests: FR-TRANSFER-020
   :priority: critical

   Verify SHA-256 checksums generated for all chunks

.. test:: Verify Checksums During Unpack
   :id: TC-INT-002
   :status: approved
   :tags: transfer, integrity, verification
   :tests: FR-TRANSFER-021
   :priority: critical

   Verify checksums validated during unpack operation

.. test:: Detect Corrupted Chunks
   :id: TC-INT-003
   :status: approved
   :tags: transfer, integrity, corruption
   :tests: FR-TRANSFER-022
   :priority: critical

   Verify corrupted chunks detected via checksum mismatch

.. test:: Verify Final File Integrity
   :id: TC-INT-004
   :status: approved
   :tags: transfer, integrity, final
   :tests: FR-TRANSFER-023
   :priority: high

   Verify final reconstructed file integrity matches original

3.5 State Management Tests
~~~~~~~~~~~~~~~~~~~~~~~~~~

========== ========================= =========== ========
ID         Description               Requirement Priority
========== ========================= =========== ========
TC-STA-001 Persist operation state   FR-024      High
TC-STA-002 Track chunk completion    FR-025      High
TC-STA-003 Resume interrupted pack   FR-026      Medium
TC-STA-004 Resume interrupted unpack FR-027      Medium
========== ========================= =========== ========

.. test:: Persist Operation State
   :id: TC-STA-001
   :status: approved
   :tags: transfer, state, persistence
   :tests: FR-TRANSFER-024
   :priority: high

   Verify operation state persisted to disk

.. test:: Track Chunk Completion
   :id: TC-STA-002
   :status: approved
   :tags: transfer, state, tracking
   :tests: FR-TRANSFER-025
   :priority: high

   Verify chunk completion tracked in state file

.. test:: Resume Interrupted Pack
   :id: TC-STA-003
   :status: approved
   :tags: transfer, state, resume, pack
   :tests: FR-TRANSFER-026
   :priority: medium

   Verify pack operation can resume after interruption

.. test:: Resume Interrupted Unpack
   :id: TC-STA-004
   :status: approved
   :tags: transfer, state, resume, unpack
   :tests: FR-TRANSFER-027
   :priority: medium

   Verify unpack operation can resume after interruption

3.6 Command Interface Tests
~~~~~~~~~~~~~~~~~~~~~~~~~~~

========== ===================== =========== ========
ID         Description           Requirement Priority
========== ===================== =========== ========
TC-CLI-001 Pack command syntax   FR-028      High
TC-CLI-002 Unpack command syntax FR-029      High
TC-CLI-003 List command syntax   FR-030      High
TC-CLI-004 Dry-run mode          FR-031      High
TC-CLI-005 Verify flag           FR-032      High
========== ===================== =========== ========

.. test:: Pack Command Syntax
   :id: TC-TRANSFER-CLI-001
   :status: approved
   :tags: transfer, cli, pack
   :tests: FR-TRANSFER-028
   :priority: high

   Verify pack command accepts correct syntax and arguments

.. test:: Unpack Command Syntax
   :id: TC-TRANSFER-CLI-002
   :status: approved
   :tags: transfer, cli, unpack
   :tests: FR-TRANSFER-029
   :priority: high

   Verify unpack command accepts correct syntax and arguments

.. test:: List Command Syntax
   :id: TC-TRANSFER-CLI-003
   :status: approved
   :tags: transfer, cli, list
   :tests: FR-TRANSFER-030
   :priority: high

   Verify list command accepts correct syntax and arguments

.. test:: Dry-Run Mode
   :id: TC-TRANSFER-CLI-004
   :status: approved
   :tags: transfer, cli, dry-run
   :tests: FR-TRANSFER-031
   :priority: high

   Verify dry-run mode previews operation without execution

.. test:: Verify Flag
   :id: TC-TRANSFER-CLI-005
   :status: approved
   :tags: transfer, cli, verify
   :tests: FR-TRANSFER-032
   :priority: high

   Verify --verify flag enables checksum verification

3.7 Error Handling Tests
~~~~~~~~~~~~~~~~~~~~~~~~

========== =============================== =========== ========
ID         Description                     Requirement Priority
========== =============================== =========== ========
TC-ERR-001 Insufficient USB capacity error FR-035      High
TC-ERR-002 Missing chunks error            FR-036      High
TC-ERR-004 Clear error messages            FR-038      High
========== =============================== =========== ========

.. test:: Insufficient USB Capacity Error
   :id: TC-TRANSFER-ERR-001
   :status: approved
   :tags: transfer, error, usb
   :tests: FR-TRANSFER-035
   :priority: high

   Verify error when USB capacity insufficient for chunk

.. test:: Missing Chunks Error
   :id: TC-TRANSFER-ERR-002
   :status: approved
   :tags: transfer, error, missing
   :tests: FR-TRANSFER-036
   :priority: high

   Verify error when required chunks missing during unpack

.. test:: Clear Error Messages
   :id: TC-TRANSFER-ERR-004
   :status: approved
   :tags: transfer, error, usability
   :tests: FR-TRANSFER-038
   :priority: high

   Verify all error messages clear and actionable

3.8 Safety Tests
~~~~~~~~~~~~~~~~

========== ========================== =========== ========
ID         Description                Requirement Priority
========== ========================== =========== ========
TC-SAF-001 Confirm file overwrite     FR-039      High
TC-SAF-002 Validate destination paths FR-040      High
TC-SAF-003 USB sync before removal    FR-041      High
========== ========================== =========== ========

.. test:: Confirm File Overwrite
   :id: TC-SAF-001
   :status: approved
   :tags: transfer, safety, overwrite
   :tests: FR-TRANSFER-039
   :priority: high

   Verify confirmation required before overwriting existing files

.. test:: Validate Destination Paths
   :id: TC-SAF-002
   :status: approved
   :tags: transfer, safety, validation
   :tests: FR-TRANSFER-040
   :priority: high

   Verify destination paths validated before write

.. test:: USB Sync Before Removal
   :id: TC-SAF-003
   :status: approved
   :tags: transfer, safety, sync
   :tests: FR-TRANSFER-041
   :priority: high

   Verify USB synced before prompting for removal

3.9 Non-Functional Tests
~~~~~~~~~~~~~~~~~~~~~~~~

========== ========================= =========== =========
ID         Description               Requirement Target
========== ========================= =========== =========
TC-NFR-001 Pack 10GB in < 10 minutes NFR-001     < 10 min
TC-NFR-002 Memory usage              NFR-002     < 100 MB
TC-NFR-003 Offline functionality     NFR-004     100%
TC-NFR-004 Cross-platform            NFR-006     Pass/Fail
========== ========================= =========== =========

.. test:: Pack 10GB in < 10 Minutes
   :id: TC-TRANSFER-NFR-001
   :status: approved
   :tags: transfer, performance, pack
   :tests: NFR-TRANSFER-001
   :priority: high

   Verify 10GB file packs in under 10 minutes

.. test:: Memory Usage < 100 MB
   :id: TC-TRANSFER-NFR-002
   :status: approved
   :tags: transfer, performance, memory
   :tests: NFR-TRANSFER-002
   :priority: medium

   Verify memory usage stays under 100 MB during operations

.. test:: Offline Functionality
   :id: TC-TRANSFER-NFR-003
   :status: approved
   :tags: transfer, offline, privacy
   :tests: NFR-TRANSFER-004
   :priority: critical

   Verify 100% functionality with network disconnected

.. test:: Cross-Platform Compatibility
   :id: TC-TRANSFER-NFR-004
   :status: approved
   :tags: transfer, portability, cross-platform
   :tests: NFR-TRANSFER-006
   :priority: high

   Verify functionality on Linux, macOS, Windows

--------------

4. Test Procedures
------------------

4.1 Offline Operation Test (TC-NFR-003)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Preconditions:** - App installed - Network disconnected (airplane mode or air-gapped system)

**Steps:** 1. Disconnect network 2. Pack 1GB test dataset 3. Unpack and verify 4. Check all operations completed

**Pass Criteria:** All operations complete successfully with no network.

4.2 Checksum Verification Test (TC-INT-003)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Preconditions:** - Valid chunk files - Manifest with checksums

**Steps:** 1. Corrupt one chunk file (modify 1 byte) 2. Run unpack operation 3. Verify error is reported 4. Confirm unpack aborts

**Pass Criteria:** Corrupted chunk detected, unpack aborted with clear error.

--------------

5. Pass/Fail Criteria
---------------------

- **All Critical tests must pass** before release
- **All High priority tests must pass** before release
- **Medium priority tests:** 90% pass rate acceptable

--------------

Requirements Traceability
-------------------------

This section demonstrates bidirectional traceability between requirements and test cases for AirGap Transfer.

Requirements to Tests Matrix
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following table shows all requirements and their associated test cases.

.. needtable::
   :types: req, nfreq, test
   :columns: id, title, status, type
   :filter: "transfer" in tags
   :style: table

Requirements Coverage
~~~~~~~~~~~~~~~~~~~~~

This table shows only requirements for AirGap Transfer.

.. needtable::
   :types: req, nfreq
   :columns: id, title, priority, status
   :filter: "transfer" in tags
   :style: table

.. note::

   To see which tests validate each requirement, refer to the Requirements to Tests Matrix above, or check the individual test case definitions in Section 3.

Test Cases
~~~~~~~~~~

This table lists all test cases with their validation links.

.. needtable::
   :types: test
   :columns: id, title, priority, status, tests
   :filter: "transfer" in tags
   :style: table

The "Tests" column shows which requirements each test case validates (via the :tests: link).

--------------

Revision History
----------------

+----------------------+--------------+------------------------------------------------------+
| Version              | Date         | Description                                          |
+======================+==============+======================================================+
| 1.0.0                | 2026-01-04   | MVP test cases (35+ tests covering FR-001 to FR-045) |
+----------------------+--------------+------------------------------------------------------+
