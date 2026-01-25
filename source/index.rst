Technical Documentation
=======================

Welcome to the Cleanroom Labs technical documentation. This documentation covers three **foundation Rust projects** designed for secure, air-gapped environments, with room for future expansion:

- **Cleanroom Whisper**: End-user transcription application
- **AirGap Deploy**: Developer deployment packaging tool
- **AirGap Transfer**: Large file transfer utility

These three projects represent our near-term development focus and demonstrate core patterns for privacy-first, offline computing. All projects follow strict privacy-first design principles with zero network communication and minimal dependencies, establishing a foundation that can support future air-gapped tools.

.. toctree::
   :maxdepth: 2
   :caption: Project Overview

   meta/index

.. toctree::
   :maxdepth: 2
   :caption: Projects

   projects/whisper
   projects/deploy
   projects/transfer

Quick Links
===========

**Getting Started:**

- :doc:`meta/principles` - Core design principles for all projects
- :doc:`meta/meta-architecture` - Cross-project architecture overview

**Requirements:**

- `Cleanroom Whisper <cleanroom-whisper/requirements/srs.html>`_
- `AirGap Deploy <airgap-deploy/requirements/srs.html>`_
- `AirGap Transfer <airgap-transfer/requirements/srs.html>`_

**Traceability:**

- :doc:`meta/requirements-overview` - Project statistics and requirements overview

Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
