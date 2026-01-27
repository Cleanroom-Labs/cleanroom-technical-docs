AirGap Deploy |status-active|
=============================

**Universal Deployment Packaging Tool**

AirGap Deploy is a Rust tool for preparing software deployments for air-gapped systems. It automates the collection, packaging, and installation of Rust applications, external binaries, model files, and system packages.

Quick Links
-----------

* `View Full Documentation <../airgap-deploy/index.html>`_
* `Requirements Specification <../airgap-deploy/requirements/srs.html>`_
* `Design Document <../airgap-deploy/design/sdd.html>`_
* `Implementation Roadmap <../airgap-deploy/roadmap.html>`_
* `Use Cases <../airgap-deploy/use-cases/index.html>`_

Key Features
------------

* **Declarative manifests**: Define deployments in ``AirGapDeploy.toml`` files
* **Automated collection**: Gather all dependencies automatically
* **Verification**: Checksum validation for all components
* **Installation scripts**: Generate bash installers for target systems
* **Extensible**: Plugin system for custom components

Project Status
--------------

See the :doc:`roadmap <airgap-deploy:roadmap>` for the complete 7-phase implementation plan.

Core Principles
---------------

AirGap Deploy follows the :doc:`/meta/principles` established for all AirGap projects:

* Privacy through data locality (no network code in deployed apps)
* Minimal dependencies (tool itself has minimal deps)
* Simple architecture (clear, maintainable code)
* Air-gap ready (designed for offline environments)

Example Use Cases
-----------------

* Deploy Cleanroom Whisper with whisper.cpp models
* Deploy Ollama with language models
* Deploy custom Rust applications with vendored dependencies

Related Projects
----------------

* :doc:`whisper` - Example application that can be deployed
* :doc:`transfer` - Transfer deployment packages to air-gapped systems
