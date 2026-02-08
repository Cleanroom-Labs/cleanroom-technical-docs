Technical Documentation
=======================

Welcome to the Cleanroom Labs technical documentation. This documentation covers three **foundation Rust projects** designed for secure, air-gapped environments, with room for future expansion:

- **AirGap Transfer**: Large file transfer utility
- **AirGap Deploy**: Developer deployment packaging tool
- **Cleanroom Whisper**: End-user transcription application

These three projects represent our near-term development focus and demonstrate core patterns for privacy-first, offline computing. All projects follow strict privacy-first design principles with zero network communication and minimal dependencies, establishing a foundation that can support future air-gapped tools.

.. toctree::
   :maxdepth: 1
   :caption: Projects

   projects/transfer
   projects/deploy
   projects/whisper

.. toctree::
   :maxdepth: 2
   :caption: Cross-Project Information

   meta/licensing
   meta/scope-and-limitations
   meta/competitive-landscape
   meta/principles
   meta/meta-architecture
   meta/specification-overview
   meta/release-philosophy
   meta/release-roadmap

.. toctree::
   :maxdepth: 2
   :caption: Developer Resources

   meta/sphinx-needs-guide
   meta/rust-integration-guide
   meta/developer-guidelines


Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
