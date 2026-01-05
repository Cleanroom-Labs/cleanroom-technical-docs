AirGap Deploy
=============

A command-line tool for packaging applications and their dependencies for deployment on air-gapped systems.

Features
--------

- **Declarative manifests** - Define deployments in simple TOML files
- **Cross-platform** - Works on Linux, macOS, and Windows
- **Component-based** - Package Rust apps, binaries, models, and system packages
- **Automated installation** - Generates platform-specific install scripts
- **Offline-ready** - Everything needed for air-gap deployment in one package

How It Works
------------

Deploy any application to air-gapped systems in two phases:

**Phase 1 - Preparation (Connected System):** 1. Create ``AirGapDeploy.toml`` manifest defining your application 2. Run ``airgap-deploy prep`` to download and package everything 3. Transfer package via USB or other physical media

**Phase 2 - Installation (Air-Gapped System):** 1. Extract package on air-gapped system 2. Run generated ``install.sh`` (or ``install.ps1`` on Windows) 3. Installation script builds and installs everything offline

No network required on the air-gapped system.

Quick Start
-----------

Prerequisites
~~~~~~~~~~~~~

- Rust toolchain (for building airgap-deploy)
- Internet access (for preparation phase)
- Git (for cloning external repositories)

Installation
~~~~~~~~~~~~

Build from source with Cargo:

.. code:: bash

   cargo install airgap-deploy

Or use a pre-built binary for your platform.

First Deployment
~~~~~~~~~~~~~~~~

Create a manifest for your application:

.. code:: toml

   # AirGapDeploy.toml
   [package]
   name = "my-app"
   version = "1.0.0"
   description = "My application for air-gap deployment"

   [[components]]
   type = "rust-app"
   source = "."
   vendor = true
   include_toolchain = true

   [install]
   method = "build-from-source"
   install_to = "user"
   mode = "interactive"

Prepare the deployment package:

.. code:: bash

   airgap-deploy prep --output dist/my-app.tar.gz

Transfer to air-gapped system and install:

.. code:: bash

   # On air-gapped system
   tar -xzf my-app.tar.gz
   cd my-app
   ./install.sh

Usage
-----

Preparing Packages
~~~~~~~~~~~~~~~~~~

Create deployment packages on connected systems:

.. code:: bash

   # Use manifest in current directory
   airgap-deploy prep

   # Specify manifest location
   airgap-deploy prep --manifest path/to/AirGapDeploy.toml

   # Specify target platform
   airgap-deploy prep --target linux-x86_64

   # Specify output location
   airgap-deploy prep --output dist/package.tar.gz

   # Dry run (preview without creating package)
   airgap-deploy prep --dry-run

Validating Manifests
~~~~~~~~~~~~~~~~~~~~

Validate manifest syntax before packaging:

.. code:: bash

   airgap-deploy validate
   airgap-deploy validate --manifest AirGapDeploy.toml

Creating Manifests
~~~~~~~~~~~~~~~~~~

Generate template manifests:

.. code:: bash

   # Generic template
   airgap-deploy init

   # Rust application template
   airgap-deploy init --type rust-app

   # Python application template
   airgap-deploy init --type python-app

Listing Components
~~~~~~~~~~~~~~~~~~

Show available component types:

.. code:: bash

   airgap-deploy list-components

Manifest Reference
------------------

Package Section
~~~~~~~~~~~~~~~

.. code:: toml

   [package]
   name = "app-name"           # Required: Package name
   version = "1.0.0"           # Required: Version
   description = "..."         # Required: Description

Targets Section
~~~~~~~~~~~~~~~

.. code:: toml

   [targets]
   platforms = ["linux-x86_64", "macos-aarch64", "windows-x86_64"]
   default = "linux-x86_64"

Components
~~~~~~~~~~

Rust Application
^^^^^^^^^^^^^^^^

.. code:: toml

   [[components]]
   type = "rust-app"
   source = "."                # Path to Cargo project
   vendor = true               # Vendor dependencies
   include_toolchain = true    # Include Rust installer

External Binary
^^^^^^^^^^^^^^^

.. code:: toml

   [[components]]
   type = "external-binary"
   name = "whisper.cpp"
   repo = "https://github.com/ggerganov/whisper.cpp.git"
   tag = "v1.0.0"              # Or: branch = "main", commit = "abc123"
   build_instructions = "make"

Model File
^^^^^^^^^^

.. code:: toml

   [[components]]
   type = "model-file"
   name = "base.en"
   url = "https://example.com/model.bin"
   checksum = "sha256:abc123..."
   required = true             # Default: true
   install_path = "models/model.bin"

System Package
^^^^^^^^^^^^^^

.. code:: toml

   [[components]]
   type = "system-package"
   name = "alsa"
   packages = ["libasound2-dev"]  # Debian/Ubuntu
   platforms = ["linux"]

**Note:** SystemPackageComponent deferred to v0.2

Installation Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: toml

   [install]
   method = "build-from-source"    # Or: "prebuilt-binary"
   install_to = "user"             # Or: "system"
   mode = "interactive"            # Or: "automatic"

   # Optional: Custom install steps
   [install.steps]
   step_name = [
       "command1",
       "command2"
   ]

   # Optional: Configuration template
   [install.config]
   config_file = "~/.config/app/config.toml"
   config_template = """
   app_path = "{{ install_prefix }}"
   """

Examples
--------

Example 1: Rust Application with Dependencies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: toml

   [package]
   name = "airgap-whisper"
   version = "0.1.0"
   description = "Offline audio transcription"

   [[components]]
   type = "rust-app"
   source = "."
   vendor = true
   include_toolchain = true

   [[components]]
   type = "external-binary"
   name = "whisper.cpp"
   repo = "https://github.com/ggerganov/whisper.cpp.git"
   tag = "v1.0.0"
   build_instructions = "make"

   [[components]]
   type = "model-file"
   name = "base.en"
   url = "https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-base.en.bin"
   checksum = "sha256:..."

   [install]
   method = "build-from-source"
   install_to = "user"

Example 2: Large ML Application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: toml

   [package]
   name = "ollama-deploy"
   version = "0.15.0"
   description = "Ollama runtime with models"

   [[components]]
   type = "external-binary"
   name = "ollama"
   repo = "https://github.com/ollama/ollama.git"
   tag = "v0.15.0"
   build_instructions = "make"

   [[components]]
   type = "model-file"
   name = "llama2-7b"
   url = "https://ollama.ai/download/llama2-7b.gguf"
   checksum = "sha256:..."

   [install]
   method = "build-from-source"
   install_to = "user"

Integration with airgap-transfer
--------------------------------

For large packages that exceed USB capacity, use airgap-transfer:

.. code:: bash

   # Create large package
   airgap-deploy prep --manifest AirGapDeploy.ollama.toml
   # Output: ollama-deploy-20GB.tar.gz

   # Chunk for multiple USB drives
   airgap-transfer pack ollama-deploy-20GB.tar.gz /media/usb --chunk-size 16GB

   # Transfer chunks across air-gap

   # Reconstruct on air-gapped system
   airgap-transfer unpack /media/usb ~/deployment/

   # Install as normal
   cd ~/deployment/ollama-deploy
   ./install.sh

See `airgap-transfer documentation <../airgap-transfer/README.md>`__ for details.

Platform Support
----------------

======== ======= ================================================
Platform Support Notes
======== ======= ================================================
Linux    Full    Tested on Ubuntu 20.04+, Fedora 35+, Debian 11+
macOS    Full    Tested on macOS 10.15+ (Intel and Apple Silicon)
Windows  Full    Tested on Windows 10/11
======== ======= ================================================

**Generated install scripts:** - Linux/macOS: Bash 4.0+ - Windows: PowerShell 5.1+

Building
--------

Requires Rust toolchain and platform-specific build tools.

See `Development Plan <development-plan.md>`__ for complete build instructions.

Documentation
-------------

This README covers installation and usage. For development and technical specifications, see the documents below.

Start Here
~~~~~~~~~~

+---------------------------------------------+-------------------------------------+
| Document                                    | Purpose                             |
+=============================================+=====================================+
| `principles.md <../principles.md>`__        | Core design principles (read first) |
+---------------------------------------------+-------------------------------------+
| `project-roadmap.md <project-roadmap.md>`__ | Project status and direction        |
+---------------------------------------------+-------------------------------------+

Technical Documentation
~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------+--------------------------------------------+
| Document                                     | Purpose                                    |
+==============================================+============================================+
| `Requirements (SRS) <requirements/srs.md>`__ | Detailed functional requirements (57 FR)   |
+----------------------------------------------+--------------------------------------------+
| `Design (SDD) <design/sdd.md>`__             | Architecture, component design, algorithms |
+----------------------------------------------+--------------------------------------------+
| `Test Plan <testing/plan.md>`__              | Test cases and procedures                  |
+----------------------------------------------+--------------------------------------------+

Project Planning
~~~~~~~~~~~~~~~~

+--------------------------------------------+---------------------------------+
| Document                                   | Purpose                         |
+============================================+=================================+
| `Development Plan <development-plan.md>`__ | 7-phase implementation plan     |
+--------------------------------------------+---------------------------------+
| `Use Case Analysis <use-case-analysis/>`__ | Workflow documentation          |
+--------------------------------------------+---------------------------------+

Meta-Architecture
~~~~~~~~~~~~~~~~~

+-------------------------------------------------+----------------------------------------------------+
| Document                                        | Purpose                                            |
+=================================================+====================================================+
| `Meta-Architecture <../meta-architecture.md>`__ | How airgap-deploy relates to other AirGap projects |
+-------------------------------------------------+----------------------------------------------------+
| `Traceability Matrix <../meta/traceability-matrix.rst>`__ | Requirements traceability and coverage   |
+-------------------------------------------------+----------------------------------------------------+

Use Cases
---------

airgap-deploy is designed for:

- **Release engineers** packaging applications for air-gapped deployment
- **DevOps teams** deploying to isolated environments
- **Security-conscious organizations** requiring offline installation
- **Developers** creating reproducible deployment packages

**Primary use case:** Package AirGap Whisper and similar applications for air-gapped systems.

Privacy
-------

airgap-deploy operates in two distinct phases:

- **Preparation phase (connected):** Downloads components, creates package
- **Installation phase (air-gapped):** No network access required or attempted

Generated installation scripts are completely offline.

License
-------

Dual-licensed under MIT OR Apache-2.0 (your choice).

Contributing
------------

See `Development Plan <development-plan.md>`__ for architecture and implementation details.

Roadmap
-------

See `project-roadmap.md <project-roadmap.md>`__ for current status and future plans.
