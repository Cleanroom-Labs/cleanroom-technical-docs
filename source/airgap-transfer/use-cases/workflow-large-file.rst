Workflow: Large File Transfer
=============================

Scenario
--------

Transfer a single large file (e.g., 50GB VM image) across an air-gap using 16GB USB drives.

--------------

Prerequisites
-------------

- **Source machine:** Connected system with internet access
- **Destination machine:** Air-gapped system
- **Transfer media:** Three 16GB USB drives
- **File:** ``vm-image.qcow2`` (50GB)

--------------

Workflow Steps
--------------

Phase 1: Pack on Source Machine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Connect USB drive #1**

   .. code:: bash

      airgap-transfer pack vm-image.qcow2 /media/usb-drive --dry-run

   Preview: Shows 4 chunks needed (3x 16GB + 1x 2GB)

2. **Execute pack operation**

   .. code:: bash

      airgap-transfer pack vm-image.qcow2 /media/usb-drive

   - Writes ``chunk_000.tar`` (16GB)
   - Generates SHA-256 checksum
   - Updates manifest

3. **Swap USB drives**

   - Tool prompts: “Insert next USB drive”
   - Eject USB #1 safely
   - Connect USB #2
   - Tool continues with ``chunk_001.tar``

4. **Repeat for remaining chunks**

   - USB #3 contains ``chunk_002.tar`` and ``chunk_003.tar``
   - All USBs contain copy of manifest: ``airgap-transfer-manifest.json``

Phase 2: Physical Transfer
~~~~~~~~~~~~~~~~~~~~~~~~~~

- Physically move USB drives across air-gap boundary
- No network connectivity required

Phase 3: Unpack on Destination Machine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Connect USB drive #1**

   .. code:: bash

      airgap-transfer list /media/usb-drive

   Shows chunks present on this USB (chunk_000)

2. **Connect all USB drives**

   - Mount USB #1, #2, #3
   - All chunks now accessible

3. **Execute unpack operation**

   .. code:: bash

      airgap-transfer unpack /media/usb-drives ~/restored/ --verify

   - Verifies checksums for all chunks
   - Reconstructs ``vm-image.qcow2``
   - Verifies final file integrity
   - Reports: “Success: 50GB transferred, verified”

--------------

Success Criteria
----------------

- ✅ File reconstructed matches original
- ✅ All checksums verified
- ✅ No data loss or corruption
- ✅ Process completable by non-technical user

--------------

Error Scenarios
---------------

==================== ===================== ======================
Error                Cause                 Recovery
==================== ===================== ======================
“Chunk missing”      USB #2 not connected  Connect missing USB
“Checksum mismatch”  Corrupted chunk       Re-pack affected chunk
“Insufficient space” Destination disk full Free space, retry
==================== ===================== ======================

--------------

Related Documents
-----------------

- `SRS <../requirements/srs.md>`__ - Pack/Unpack requirements
- `SDD <../design/sdd.md>`__ - Chunking architecture
