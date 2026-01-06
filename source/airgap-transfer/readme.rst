AirGap Transfer
===============

A minimal command-line utility for safely transferring large files and datasets across air-gap boundaries using removable media.

Features
--------

- **Air-gap ready** - Designed for systems with no network access
- **Chunked transfers** - Split large datasets across multiple USB drives
- **Integrity verification** - SHA-256 checksums for all transfers
- **Resume capability** - Continue interrupted transfers
- **Cross-platform** - macOS, Windows, and Linux support
- **Lightweight** - Pure Rust, single binary

How It Works
------------

Transfer large datasets that exceed single USB drive capacity:

1. **Pack**: Split source files into chunks that fit on available USB drives
2. **Transfer**: Move USB drives across air-gap boundary
3. **Unpack**: Reconstruct original files on destination machine with verification

All operations maintain data integrity through cryptographic checksums.

Quick Start
-----------

Prerequisites
~~~~~~~~~~~~~

- Rust toolchain (for building from source)
- USB drives with sufficient combined capacity
- Write access to source and destination directories

Installation
~~~~~~~~~~~~

Build from source with Cargo, or use a pre-built binary for your platform.

First Transfer
~~~~~~~~~~~~~~

.. code:: bash

   # On source machine (connected side):
   airgap-transfer pack ~/large-dataset /media/usb-drive --chunk-size 16GB

   # Physically transfer USB drive(s) across air-gap

   # On destination machine (air-gapped side):
   airgap-transfer unpack /media/usb-drive ~/restored-dataset

Usage
-----

Pack Operation
~~~~~~~~~~~~~~

Split source files into chunks:

.. code:: bash

   airgap-transfer pack <source> <usb-mount> [options]

**Options:**

- ``--chunk-size <SIZE>`` - Maximum chunk size (default: auto-detect USB capacity)
- ``--dry-run`` - Preview operations without writing
- ``--verify`` - Generate checksums during packing

Unpack Operation
~~~~~~~~~~~~~~~~

Reconstruct files from chunks:

.. code:: bash

   airgap-transfer unpack <chunk-location> <destination> [options]

**Options:**

- ``--verify`` - Verify all checksums before unpacking
- ``--keep-chunks`` - Don’t delete chunks after successful reconstruction

List Operation
~~~~~~~~~~~~~~

Analyze chunk status:

.. code:: bash

   airgap-transfer list <chunk-location>

Shows chunk inventory, sizes, and verification status.

Building
--------

Requires Rust toolchain and platform-specific build tools.

See :doc:`Roadmap <roadmap>` for complete build instructions and architecture details.

Air-Gapped Deployment
---------------------

AirGap Transfer supports deployment on systems with no internet access. All dependencies can be vendored and transferred offline via USB.

For detailed air-gap deployment procedures, see the AirGap Deploy project documentation.

--------------

Use Cases
---------

- Transfer large datasets (hundreds of GB) across air-gap boundaries
- Backup critical data to removable media with verification
- Deploy software and models to isolated systems
- Migrate data between air-gapped environments

Privacy
-------

AirGap Transfer is **private by architecture**:

- Zero network code in the application
- No analytics, telemetry, or external API calls
- All data stays on local or removable media
- Cryptographic verification ensures integrity

Platform Support
----------------

======== ======= ================================
Platform Support Notes
======== ======= ================================
macOS    Full    Tested on macOS 10.15+
Linux    Full    Tested on Ubuntu, Fedora, Debian
Windows  Full    Tested on Windows 10/11
======== ======= ================================

Documentation
-------------

This README covers installation and usage. For development and technical specifications, see the documents below.

Start Here
~~~~~~~~~~

+---------------------------------------------+-------------------------------------+
| Document                                    | Purpose                             |
+=============================================+=====================================+
| :doc:`Principles <../meta/principles>`      | Core design principles (read first) |
+---------------------------------------------+-------------------------------------+
| :doc:`Roadmap <roadmap>`                    | Project status and direction        |
+---------------------------------------------+-------------------------------------+

Technical Documentation
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------+-------------------------------------------------+
| Document                                        | Purpose                                         |
+=================================================+=================================================+
| :doc:`Software Requirements <requirements/srs>` | Detailed functional requirements                |
+-------------------------------------------------+-------------------------------------------------+
| :doc:`Software Design <design/sdd>`             | Architecture, data structures, component design |
+-------------------------------------------------+-------------------------------------------------+
| :doc:`Test Plan <testing/plan>`                 | Test cases and procedures                       |
+-------------------------------------------------+-------------------------------------------------+

Project Planning
~~~~~~~~~~~~~~~~

+--------------------------------------------+---------------------------------+
| Document                                   | Purpose                         |
+============================================+=================================+
| :doc:`Roadmap <roadmap>`                   | MVP implementation milestones   |
+--------------------------------------------+---------------------------------+
| :doc:`Use Case Analysis <use-cases/index>` | Workflow documentation          |
+--------------------------------------------+---------------------------------+
