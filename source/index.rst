AirGap Project Suite Documentation
===================================

Welcome to the AirGap Project Suite documentation. This suite consists of three **foundation Rust projects** designed for secure, air-gapped environments, with room for future expansion:

- **AirGap Whisper**: End-user transcription application
- **AirGap Deploy**: Developer deployment packaging tool
- **AirGap Transfer**: Large file transfer utility

These three projects represent our near-term development focus and demonstrate core patterns for privacy-first, offline computing. All projects follow strict privacy-first design principles with zero network communication and minimal dependencies, establishing a foundation that can support future air-gapped tools.

.. toctree::
   :maxdepth: 2
   :caption: Meta Documentation

   meta/index

.. toctree::
   :maxdepth: 2
   :caption: Projects

   airgap-whisper/index
   airgap-deploy/index
   airgap-transfer/index

.. toctree::
   :maxdepth: 1
   :caption: Blog

   blog/index

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

- :doc:`meta/requirements-overview` - Project statistics and requirements overview

Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
