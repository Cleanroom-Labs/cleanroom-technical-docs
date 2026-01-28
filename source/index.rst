Technical Documentation
=======================

Welcome to the Cleanroom Labs technical documentation. This documentation covers three **foundation Rust projects** designed for secure, air-gapped environments, with room for future expansion:

- **AirGap Transfer**: Large file transfer utility
- **AirGap Deploy**: Developer deployment packaging tool
- **Cleanroom Whisper**: End-user transcription application

These three projects represent our near-term development focus and demonstrate core patterns for privacy-first, offline computing. All projects follow strict privacy-first design principles with zero network communication and minimal dependencies, establishing a foundation that can support future air-gapped tools.

.. toctree::
   :maxdepth: 2
   :caption: Cross-Project Information

   meta/principles
   meta/meta-architecture
   meta/release-roadmap
   meta/specification-overview

.. toctree::
   :maxdepth: 2
   :caption: Developer Resources

   meta/sphinx-needs-guide
   meta/rust-integration-guide

.. toctree::
   :maxdepth: 1
   :caption: Projects

   projects/transfer
   projects/deploy
   projects/whisper

Quick Links
===========

**Getting Started:**

- :doc:`meta/principles` - Core design principles for all projects
- :doc:`meta/meta-architecture` - Cross-project architecture overview

**Requirements:**

- `Cleanroom Whisper <cleanroom-whisper/requirements/srs.html>`_
- `AirGap Deploy <airgap-deploy/requirements/srs.html>`_
- `AirGap Transfer <airgap-transfer/requirements/srs.html>`_

**Specification Overview:**

- :doc:`meta/specification-overview` - Project statistics and traceability overview

Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
