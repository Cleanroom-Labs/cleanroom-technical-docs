Workflow: Large Directory Transfer
==================================

Scenario
--------

Transfer a large directory with mixed file sizes (e.g., software development environment with source code, dependencies, build artifacts) across an air-gap.

--------------

Prerequisites
-------------

- **Source machine:** Development machine with internet
- **Destination machine:** Air-gapped production system
- **Transfer media:** Two 32GB USB drives
- **Directory:** ``~/project/`` (40GB, 50,000 files)

--------------

Workflow Steps
--------------

Phase 1: Pack on Source Machine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Preview operation**

   .. code:: bash

      airgap-transfer pack ~/project/ /media/usb-drive --dry-run

   Shows: 2 chunks needed (32GB + 8GB)

2. **Execute pack**

   .. code:: bash

      airgap-transfer pack ~/project/ /media/usb-drive --verbose

   - Preserves directory structure in tar format
   - Writes ``chunk_000.tar`` (32GB) to USB #1
   - Progress: “15,000 files packed (30%)”

3. **Swap to USB #2**

   - Tool prompts for USB swap
   - Writes ``chunk_001.tar`` (8GB) to USB #2
   - Manifest written to both USBs

Phase 2: Physical Transfer
~~~~~~~~~~~~~~~~~~~~~~~~~~

- Transport USB drives across air-gap
- Verify physical chain of custody if required

Phase 3: Unpack on Destination Machine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Verify chunks**

   .. code:: bash

      airgap-transfer list /media/usb-1
      airgap-transfer list /media/usb-2

   Confirms both chunks present with valid checksums

2. **Unpack to destination**

   .. code:: bash

      airgap-transfer unpack /media/usb-drives ~/restored-project/ --verify

   - Verifies all chunk checksums
   - Extracts in order, preserving structure
   - Progress: “35,000 files extracted (70%)”
   - Final verification of directory structure

3. **Verify integrity**

   .. code:: bash

      cd ~/restored-project
      find . -type f | wc -l  # Should match source count

--------------

Success Criteria
----------------

- ✅ All 50,000 files present
- ✅ Directory structure preserved
- ✅ File permissions maintained
- ✅ All checksums verified
- ✅ Process takes < 30 minutes

--------------

Optimization Notes
------------------

+-------------------+-----------------------------+-----------------------------------+
| Factor            | Impact                      | Mitigation                        |
+===================+=============================+===================================+
| Many small files  | Slower tar creation         | Use compression in post-MVP       |
+-------------------+-----------------------------+-----------------------------------+
| Mixed file sizes  | Uneven chunk utilization    | Acceptable for MVP                |
+-------------------+-----------------------------+-----------------------------------+
| Symlinks          | May break if absolute paths | Document limitation, fix post-MVP |
+-------------------+-----------------------------+-----------------------------------+

--------------

Error Scenarios
---------------

+-----------------------+--------------------------------+-----------------------------+
| Error                 | Cause                          | Recovery                    |
+=======================+================================+=============================+
| “Permission denied”   | Insufficient permissions       | Run with appropriate user   |
+-----------------------+--------------------------------+-----------------------------+
| “Disk full on unpack” | Insufficient destination space | Free space, resume          |
+-----------------------+--------------------------------+-----------------------------+
| “Partial directory”   | Interrupted pack               | Resume from manifest        |
+-----------------------+--------------------------------+-----------------------------+

--------------

Related Documents
-----------------

- `SRS <../requirements/srs.md>`__ - Directory handling requirements
- `SDD <../design/sdd.md>`__ - Tar format and structure preservation
