Software Requirements Specification
===================================

AirGap Transfer
---------------

**Version:** 1.0.0 **Date:** 2026-01-04 **Standard:** IEEE 830 (simplified for MVP)

--------------

1. Introduction
---------------

1.1 Purpose
~~~~~~~~~~~

This SRS defines MVP requirements for AirGap Transfer, a command-line utility for safely transferring large files across air-gap boundaries.

1.2 Scope
~~~~~~~~~

**Product:** AirGap Transfer — a minimal CLI tool for chunked file transfers via removable media.

**In Scope:** - Split large datasets into chunks for USB transfer - Reconstruct files from chunks with integrity verification - Resume interrupted transfers - Cross-platform support (macOS, Windows, Linux)

**Out of Scope (per** `principles.md <../../principles.md>`__\ **):** - Network transfers, cloud sync, auto-updates - Compression or encryption (defer to post-MVP) - GUI interface - Real-time synchronization - Ollama-specific logic (general-purpose only)

1.3 Definitions
~~~~~~~~~~~~~~~

+-----------------------+------------------------------------------------------------------+
| Term                  | Definition                                                       |
+=======================+==================================================================+
| Air-gap               | Physical separation between systems with no network connectivity |
+-----------------------+------------------------------------------------------------------+
| Chunk                 | A fixed-size portion of source data that fits on removable media |
+-----------------------+------------------------------------------------------------------+
| Pack                  | Operation to split source files into chunks                      |
+-----------------------+------------------------------------------------------------------+
| Unpack                | Operation to reconstruct files from chunks                       |
+-----------------------+------------------------------------------------------------------+
| Manifest              | Metadata file describing chunk inventory and checksums           |
+-----------------------+------------------------------------------------------------------+

--------------

2. Overall Description
----------------------

2.1 Product Perspective
~~~~~~~~~~~~~~~~~~~~~~~

Standalone CLI tool for transferring data across air-gap boundaries using removable media.

All operations occur locally with no network connectivity.

See `SDD <../design/sdd.md>`__ for architecture diagrams and component details.

2.2 Constraints
~~~~~~~~~~~~~~~

============= ==========================================================
Constraint    Description
============= ==========================================================
Offline-only  Zero network calls at runtime
Air-gap ready Deployable without internet access
Platforms     macOS, Windows, Linux
UI model      Command-line interface only (no GUI)
Media         Works with standard removable media (USB, external drives)
============= ==========================================================

--------------

3. Functional Requirements
--------------------------

Priority: **M**\ ust / **S**\ hould / **C**\ ould

3.1 Pack Operation
~~~~~~~~~~~~~~~~~~

+---------+-------------------------+-------------------------------------------------------------+
| ID      | Priority                | Requirement                                                 |
+=========+=========================+=============================================================+
| FR-001  | M                       | Split source files/directories into fixed-size chunks       |
+---------+-------------------------+-------------------------------------------------------------+
| FR-002  | M                       | Auto-detect USB capacity and set chunk size accordingly     |
+---------+-------------------------+-------------------------------------------------------------+
| FR-003  | M                       | Generate SHA-256 checksums for each chunk                   |
+---------+-------------------------+-------------------------------------------------------------+
| FR-004  | M                       | Create manifest file with chunk metadata and checksums      |
+---------+-------------------------+-------------------------------------------------------------+
| FR-005  | M                       | Stream data directly to USB without intermediate temp files |
+---------+-------------------------+-------------------------------------------------------------+
| FR-006  | S                       | Support manual chunk size specification                     |
+---------+-------------------------+-------------------------------------------------------------+
| FR-007  | S                       | Show progress during chunk creation                         |
+---------+-------------------------+-------------------------------------------------------------+
| FR-008  | S                       | Prompt for USB swapping when multiple chunks needed         |
+---------+-------------------------+-------------------------------------------------------------+

3.2 Unpack Operation
~~~~~~~~~~~~~~~~~~~~

+---------+-------------------------+----------------------------------------------------------+
| ID      | Priority                | Requirement                                              |
+=========+=========================+==========================================================+
| FR-009  | M                       | Reconstruct original files from chunks                   |
+---------+-------------------------+----------------------------------------------------------+
| FR-010  | M                       | Verify chunk checksums before reconstruction             |
+---------+-------------------------+----------------------------------------------------------+
| FR-011  | M                       | Place reconstructed files in specified destination       |
+---------+-------------------------+----------------------------------------------------------+
| FR-012  | M                       | Validate chunk completeness (all chunks present)         |
+---------+-------------------------+----------------------------------------------------------+
| FR-013  | S                       | Resume partial unpacks if interrupted                    |
+---------+-------------------------+----------------------------------------------------------+
| FR-014  | S                       | Optionally delete chunks after successful reconstruction |
+---------+-------------------------+----------------------------------------------------------+
| FR-015  | S                       | Show progress during reconstruction                      |
+---------+-------------------------+----------------------------------------------------------+

3.3 List Operation
~~~~~~~~~~~~~~~~~~

====== ======== =================================================
ID     Priority Requirement
====== ======== =================================================
FR-016 M        Display chunk inventory from manifest
FR-017 M        Show chunk sizes and verification status
FR-018 S        Identify missing or corrupted chunks
FR-019 S        Display estimated total size after reconstruction
====== ======== =================================================

3.4 Integrity Verification
~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------+-------------------------+-----------------------------------------------------------+
| ID      | Priority                | Requirement                                               |
+=========+=========================+===========================================================+
| FR-020  | M                       | Generate SHA-256 checksums during pack                    |
+---------+-------------------------+-----------------------------------------------------------+
| FR-021  | M                       | Verify checksums during unpack                            |
+---------+-------------------------+-----------------------------------------------------------+
| FR-022  | M                       | Detect corrupted chunks and report errors                 |
+---------+-------------------------+-----------------------------------------------------------+
| FR-023  | S                       | Verify final reconstructed file against original checksum |
+---------+-------------------------+-----------------------------------------------------------+

3.5 State Management
~~~~~~~~~~~~~~~~~~~~

====== ======== ================================================
ID     Priority Requirement
====== ======== ================================================
FR-024 M        Maintain operation state in manifest file
FR-025 M        Track chunk completion status
FR-026 S        Support resume for interrupted pack operations
FR-027 S        Support resume for interrupted unpack operations
====== ======== ================================================

3.6 Command Interface
~~~~~~~~~~~~~~~~~~~~~

+--------+----------+-----------------------------------------------------------+
| ID     | Priority | Requirement                                               |
+========+==========+===========================================================+
| FR-028 | M        | ``airgap-transfer pack <source> <dest>`` command          |
+--------+----------+-----------------------------------------------------------+
| FR-029 | M        | ``airgap-transfer unpack <source> <dest>`` command        |
+--------+----------+-----------------------------------------------------------+
| FR-030 | M        | ``airgap-transfer list <chunk-location>`` command         |
+--------+----------+-----------------------------------------------------------+
| FR-031 | M        | ``--dry-run`` flag for all operations                     |
+--------+----------+-----------------------------------------------------------+
| FR-032 | M        | ``--verify`` flag to enable/disable checksum verification |
+--------+----------+-----------------------------------------------------------+
| FR-033 | S        | ``--chunk-size`` flag for manual chunk size specification |
+--------+----------+-----------------------------------------------------------+
| FR-034 | S        | ``--verbose`` flag for detailed output                    |
+--------+----------+-----------------------------------------------------------+

3.7 Error Handling
~~~~~~~~~~~~~~~~~~

====== ======== ===================================================
ID     Priority Requirement
====== ======== ===================================================
FR-035 M        Detect and report insufficient USB capacity
FR-036 M        Handle missing chunks gracefully
FR-037 M        Detect and report checksum verification failures
FR-038 M        Provide clear error messages with suggested actions
====== ======== ===================================================

3.8 Safety Features
~~~~~~~~~~~~~~~~~~~

====== ======== ============================================
ID     Priority Requirement
====== ======== ============================================
FR-039 M        Confirm overwrite of existing files
FR-040 M        Validate destination paths and permissions
FR-041 M        Safely sync USB before prompting for removal
FR-042 S        Atomic operations where possible
====== ======== ============================================

3.9 Deployment
~~~~~~~~~~~~~~

+---------+-------------------------+----------------------------------------------------------+
| ID      | Priority                | Requirement                                              |
+=========+=========================+==========================================================+
| FR-043  | M                       | All dependencies available for offline build             |
+---------+-------------------------+----------------------------------------------------------+
| FR-044  | M                       | Build process works without internet after initial setup |
+---------+-------------------------+----------------------------------------------------------+
| FR-045  | S                       | Single-binary deployment                                 |
+---------+-------------------------+----------------------------------------------------------+

--------------

4. Non-Functional Requirements
------------------------------

+----------+------------------------------------+-----------------------------------------------------------+
| ID       | Requirement                        | Target                                                    |
+==========+====================================+===========================================================+
| NFR-001  | Chunk creation time                | < 10 minutes for 10GB dataset                             |
+----------+------------------------------------+-----------------------------------------------------------+
| NFR-002  | Memory footprint                   | < 100 MB during streaming operations                      |
+----------+------------------------------------+-----------------------------------------------------------+
| NFR-003  | Privacy                            | All data stays on local/removable media; no network calls |
+----------+------------------------------------+-----------------------------------------------------------+
| NFR-004  | Offline functionality              | 100% functional offline                                   |
+----------+------------------------------------+-----------------------------------------------------------+
| NFR-005  | Air-gap deployment                 | Build and run on systems with no internet access          |
+----------+------------------------------------+-----------------------------------------------------------+
| NFR-006  | Cross-platform                     | Support macOS, Windows, Linux                             |
+----------+------------------------------------+-----------------------------------------------------------+

--------------

.. _error-handling-1:

5. Error Handling
-----------------

+-----------------------------------+--------------------------------------------------------+
| Scenario                          | Behavior                                               |
+===================================+========================================================+
| Insufficient USB capacity         | Warn user, suggest smaller chunk size or larger USB    |
+-----------------------------------+--------------------------------------------------------+
| Missing chunks during unpack      | List missing chunks, abort with clear error            |
+-----------------------------------+--------------------------------------------------------+
| Checksum mismatch                 | Identify corrupted chunk, abort with error             |
+-----------------------------------+--------------------------------------------------------+
| Disk full during pack             | Stop operation, clean up partial chunk                 |
+-----------------------------------+--------------------------------------------------------+
| Permission denied                 | Clear error message with required permissions          |
+-----------------------------------+--------------------------------------------------------+
| USB disconnected during operation | Detect failure, allow resume from last completed chunk |
+-----------------------------------+--------------------------------------------------------+

--------------

Appendix: Chunk Format Specification
------------------------------------

Manifest Structure
~~~~~~~~~~~~~~~~~~

.. code:: json

   {
     "version": "1.0",
     "source": "/path/to/source",
     "total_size": 10737418240,
     "chunk_size": 1073741824,
     "chunks": [
       {
         "index": 0,
         "filename": "chunk_000.tar",
         "size": 1073741824,
         "checksum": "sha256:abc123...",
         "status": "completed"
       }
     ],
     "created": "2026-01-04T12:00:00Z"
   }

Chunk Naming Convention
~~~~~~~~~~~~~~~~~~~~~~~

- Format: ``chunk_XXX.tar`` where XXX is zero-padded chunk index
- Manifest: ``airgap-transfer-manifest.json``

--------------

Revision History
----------------

+----------------------+--------------+----------------------------------------------------+
| Version              | Date         | Description                                        |
+======================+==============+====================================================+
| 1.0.0                | 2026-01-04   | MVP requirements (45 functional, 6 non-functional) |
+----------------------+--------------+----------------------------------------------------+
