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

3.7 Error Handling Tests
~~~~~~~~~~~~~~~~~~~~~~~~

========== =============================== =========== ========
ID         Description                     Requirement Priority
========== =============================== =========== ========
TC-ERR-001 Insufficient USB capacity error FR-035      High
TC-ERR-002 Missing chunks error            FR-036      High
TC-ERR-003 Checksum mismatch error         FR-037      Critical
TC-ERR-004 Clear error messages            FR-038      High
========== =============================== =========== ========

3.8 Safety Tests
~~~~~~~~~~~~~~~~

========== ========================== =========== ========
ID         Description                Requirement Priority
========== ========================== =========== ========
TC-SAF-001 Confirm file overwrite     FR-039      High
TC-SAF-002 Validate destination paths FR-040      High
TC-SAF-003 USB sync before removal    FR-041      High
========== ========================== =========== ========

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

Revision History
----------------

+----------------------+--------------+------------------------------------------------------+
| Version              | Date         | Description                                          |
+======================+==============+======================================================+
| 1.0.0                | 2026-01-04   | MVP test cases (35+ tests covering FR-001 to FR-045) |
+----------------------+--------------+------------------------------------------------------+
