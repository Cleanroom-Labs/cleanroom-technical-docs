AirGap Transfer
===============

**Large File Transfer Utility**

AirGap Transfer is a tool for efficiently transferring large files and directories to air-gapped systems using USB drives or other removable media. It handles chunking, reassembly, verification, and progress tracking.

Quick Links
-----------

* `View Full Documentation <../airgap-transfer/index.html>`_
* `Requirements Specification <../airgap-transfer/requirements/srs.html>`_
* `Design Document <../airgap-transfer/design/sdd.html>`_
* `Implementation Roadmap <../airgap-transfer/roadmap.html>`_
* `Use Cases <../airgap-transfer/use-cases/index.html>`_

Key Features
------------

* **Smart chunking**: Split large files to fit on USB drives
* **Automatic reassembly**: Reconstruct files on target system
* **Verification**: Checksum validation for data integrity
* **Progress tracking**: Visual feedback for transfers
* **Resume support**: Continue interrupted transfers

Project Status
--------------

See the :doc:`roadmap <airgap-transfer:roadmap>` for current implementation status and milestones.

Core Principles
---------------

AirGap Transfer follows the :doc:`/meta/principles` established for all AirGap projects:

* Privacy through data locality (no network code)
* Minimal dependencies (≤10 direct Rust crates)
* Simple architecture (obvious, maintainable code)
* Air-gap ready (designed for offline environments)

Common Scenarios
----------------

* Transfer multi-GB language models for Ollama
* Move large datasets to air-gapped machines
* Deploy software packages prepared by AirGap Deploy

Related Projects
----------------

* :doc:`whisper` - Application that may need large model files transferred
* :doc:`deploy` - Creates deployment packages that may need transfer
