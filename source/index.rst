AirGap Project Suite Documentation
===================================

Welcome to the AirGap Project Suite documentation. This suite consists of three independent Rust projects designed for secure, air-gapped environments:

- **AirGap Whisper**: End-user transcription application
- **AirGap Deploy**: Developer deployment packaging tool
- **AirGap Transfer**: Large file transfer utility

All projects follow strict privacy-first design principles with zero network communication and minimal dependencies.

.. toctree::
   :maxdepth: 1
   :caption: Meta Documentation

   meta/index

.. toctree::
   :maxdepth: 2
   :caption: Projects

   airgap-whisper/index
   airgap-deploy/index
   airgap-transfer/index

Quick Links
===========

**Getting Started:**

- :doc:`meta/principles` - Core design principles for all projects
- :doc:`meta/meta-architecture` - Cross-project architecture overview

**Requirements:**

- :doc:`AirGap Whisper <airgap-whisper/requirements/srs>`
- :doc:`AirGap Deploy <airgap-deploy/requirements/srs>`
- :doc:`AirGap Transfer <airgap-transfer/requirements/srs>`

**Traceability:**

- :doc:`meta/traceability-matrix` - Requirements ↔ Tests traceability
- :doc:`meta/gap-analysis` - Gap analysis across all projects

Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
