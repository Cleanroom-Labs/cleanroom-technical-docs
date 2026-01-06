Software Requirements Specification
===================================

AirGap Deploy
-------------

**Version:** 1.0.0 **Date:** 2026-01-04 **Status:** Draft **Standard:** IEEE 830-1998

--------------

1. Introduction
---------------

1.1 Purpose
~~~~~~~~~~~

This Software Requirements Specification (SRS) describes the functional and non-functional requirements for **airgap-deploy**, a command-line tool for packaging applications and their dependencies for deployment on air-gapped systems.

This document is intended for:

- Developers implementing airgap-deploy
- Release engineers using airgap-deploy to package applications
- Technical reviewers evaluating the tool's capabilities

1.2 Scope
~~~~~~~~~

**Product Name:** airgap-deploy

**Product Purpose:** Simplify the packaging and installation of software on air-gapped systems

**Benefits:**

- Declarative manifest-based packaging (no custom scripts)
- Cross-platform support (Linux, macOS, Windows)
- Automated dependency collection and vendoring
- Generated installation scripts for air-gapped deployment

**Goals:**

- Enable developers to package any application for air-gap deployment with a single TOML manifest
- Reduce manual effort in preparing air-gap packages from days to minutes
- Ensure reproducible, verifiable deployments

**Out of Scope (v1.0):**

- GUI interface (CLI only)
- Network-based distribution mechanisms
- Digital signature/verification (future enhancement)
- Automatic updates (contradicts air-gap philosophy)
- Plugin system (deferred to future version)

1.3 Definitions, Acronyms, and Abbreviations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------+--------------------------------------------------------------------+
| Term                  | Definition                                                         |
+=======================+====================================================================+
| **Air-gap**           | Physical isolation from networks, especially the internet          |
+-----------------------+--------------------------------------------------------------------+
| **Component**         | A deployable unit (application, binary, model, package)            |
+-----------------------+--------------------------------------------------------------------+
| **Manifest**          | TOML file defining deployment requirements (``AirGapDeploy.toml``) |
+-----------------------+--------------------------------------------------------------------+
| **Package**           | Final output archive (.tar.gz or .zip) ready for air-gap transfer  |
+-----------------------+--------------------------------------------------------------------+
| **Vendor**            | Process of including all dependencies within a package             |
+-----------------------+--------------------------------------------------------------------+
| **Prep**              | Preparation phase on connected machine                             |
+-----------------------+--------------------------------------------------------------------+
| **Install**           | Installation phase on air-gapped machine                           |
+-----------------------+--------------------------------------------------------------------+
| **TOML**              | Tom’s Obvious Minimal Language (configuration format)              |
+-----------------------+--------------------------------------------------------------------+
| **SHA-256**           | Cryptographic hash function for checksums                          |
+-----------------------+--------------------------------------------------------------------+

1.4 References
~~~~~~~~~~~~~~

- IEEE Std 830-1998: IEEE Recommended Practice for Software Requirements Specifications
- :doc:`Roadmap <../roadmap>` - Implementation roadmap
- :doc:`Use Case Analysis <../use-cases/overview>` - Detailed workflows
- :doc:`Meta-Architecture </meta/meta-architecture>` - Project relationships

1.5 Overview
~~~~~~~~~~~~

This SRS is organized as follows:

- **Section 2:** Overall description of the product
- **Section 3:** Functional requirements
- **Section 4:** Non-functional requirements
- **Section 5:** External interface requirements

--------------

2. Overall Description
----------------------

2.1 Product Perspective
~~~~~~~~~~~~~~~~~~~~~~~

airgap-deploy is a **standalone developer tool** that integrates into existing software development workflows. It operates in two distinct phases:

**Phase 1 - Preparation (Connected System):**

- Developer creates ``AirGapDeploy.toml`` manifest
- airgap-deploy collects application source, dependencies, models, binaries
- Generates deployment package (.tar.gz or .zip)
- Generates installation scripts (install.sh, install.ps1)

**Phase 2 - Installation (Air-Gapped System):**

- User transfers package via USB or other physical media
- User executes generated installation script
- Script builds/installs application from vendored dependencies
- No network access required

**Relationship to Other Systems:**

- **airgap-transfer:** Optional integration for large packages (see :doc:`meta-architecture </meta/meta-architecture>`)
- **AirGap Whisper:** Reference implementation and primary use case
- **CI/CD pipelines:** Integrates with GitHub Actions, GitLab CI for automated package generation

2.2 Product Functions
~~~~~~~~~~~~~~~~~~~~~

airgap-deploy provides the following major functions:

1. **Manifest Parsing** - Parse and validate ``AirGapDeploy.toml`` files
2. **Component Collection** - Download and collect required components:

   - Rust applications with vendored dependencies
   - External binaries from Git repositories
   - Model files from URLs with checksum verification
   - System packages (Linux distributions)

3. **Packaging** - Create compressed archives with all components
4. **Install Script Generation** - Generate platform-specific installation scripts
5. **CLI Interface** - User-friendly command-line tool with progress reporting

2.3 User Characteristics
~~~~~~~~~~~~~~~~~~~~~~~~

**Primary Users: Application Developers / Release Engineers**

- **Technical expertise:** High (familiar with command-line tools, build systems)
- **Domain knowledge:** Understands air-gap deployment constraints
- **Frequency of use:** Occasional (during release cycles)
- **Environment:** Development machine with internet access

**Secondary Users: End Users / IT Staff**

- **Technical expertise:** Medium (can run installation scripts)
- **Domain knowledge:** Works with air-gapped systems
- **Frequency of use:** Rare (only during installations/updates)
- **Environment:** Air-gapped production system

2.4 Constraints
~~~~~~~~~~~~~~~

**Regulatory Constraints:**

- Must comply with open-source licensing (MIT OR Apache-2.0)
- No export-controlled cryptography beyond SHA-256

**Technical Constraints:**

- Requires Rust toolchain for building airgap-deploy itself
- Preparation phase requires internet access (by design)
- Installation phase must work completely offline
- Package size limited by available storage media

**Design Constraints:**

- Command-line interface only (no GUI)
- Declarative manifest format (TOML)
- Cross-platform compatibility (Linux, macOS, Windows)

2.5 Assumptions and Dependencies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Assumptions:**

- Developer has internet access during package preparation
- Target air-gapped system has basic build tools (C compiler, make)
- Users can physically transfer files via USB or similar media

**Dependencies:**

- External: Git, cargo, platform-specific package managers
- Rust crates: See :doc:`Roadmap <../roadmap>` (Dependencies Summary) for complete list

--------------

3. Functional Requirements
--------------------------

3.1 Manifest Parsing and Validation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. req:: Parse TOML Manifest Files
   :id: FR-DEPLOY-001
   :status: approved
   :tags: deploy, manifest, parsing
   :priority: must

   The system SHALL parse AirGapDeploy.toml files using TOML syntax.

.. req:: Validate Manifest Structure
   :id: FR-DEPLOY-002
   :status: approved
   :tags: deploy, manifest, validation
   :priority: must

   The system SHALL validate manifest structure and required fields before processing.

.. req:: Support Manifest Sections
   :id: FR-DEPLOY-003
   :status: approved
   :tags: deploy, manifest, structure
   :priority: must

   The system SHALL support the following manifest sections: ``[package]``, ``[targets]``, ``[install]``, ``[[components]]``

.. req:: Clear Manifest Error Messages
   :id: FR-DEPLOY-004
   :status: approved
   :tags: deploy, manifest, validation, error-handling
   :priority: must

   The system SHALL provide clear error messages for invalid manifests, including line numbers and expected values.

.. req:: Manifest Schema Versioning
   :id: FR-DEPLOY-005
   :status: approved
   :tags: deploy, manifest, versioning
   :priority: should

   The system SHALL support schema versioning to enable future manifest evolution.

--------------

3.2 Component Collection
~~~~~~~~~~~~~~~~~~~~~~~~

3.2.1 Rust Application Component
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. req:: Collect Rust Application Source
   :id: FR-DEPLOY-006
   :status: approved
   :tags: deploy, rust, component
   :priority: must

   The system SHALL collect Rust application source code from local directories.

.. req:: Vendor Cargo Dependencies
   :id: FR-DEPLOY-007
   :status: approved
   :tags: deploy, rust, vendor, dependencies
   :priority: must

   The system SHALL execute cargo vendor to download and vendor all Cargo dependencies.

.. req:: Include Rust Toolchain Installer
   :id: FR-DEPLOY-008
   :status: approved
   :tags: deploy, rust, toolchain
   :priority: should

   The system SHALL optionally include Rust toolchain installer for offline builds.

.. req:: Generate Cargo Config
   :id: FR-DEPLOY-009
   :status: approved
   :tags: deploy, rust, configuration
   :priority: must

   The system SHALL generate .cargo/config.toml to configure vendored dependency usage.

.. req:: Rust Component Configuration Options
   :id: FR-DEPLOY-010
   :status: approved
   :tags: deploy, rust, configuration
   :priority: must

   The system SHALL support configuration options: source, vendor, include_toolchain, prebuild

3.2.2 External Binary Component
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. req:: Clone Git Repositories
   :id: FR-DEPLOY-011
   :status: approved
   :tags: deploy, git, external-binary
   :priority: must

   The system SHALL clone Git repositories for external binaries.

.. req:: Specify Git Version
   :id: FR-DEPLOY-012
   :status: approved
   :tags: deploy, git, versioning
   :priority: must

   The system SHALL support specifying Git branch, tag, or commit.

.. req:: Include Build Instructions
   :id: FR-DEPLOY-013
   :status: approved
   :tags: deploy, installation, build
   :priority: must

   The system SHALL include build instructions in installation scripts.

.. req:: External Binary Configuration Options
   :id: FR-DEPLOY-014
   :status: approved
   :tags: deploy, external-binary, configuration
   :priority: must

   The system SHALL support configuration options: name, repo, branch/tag/commit, build_instructions

3.2.3 Model File Component
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. req:: Download Model Files
   :id: FR-DEPLOY-015
   :status: approved
   :tags: deploy, model, download
   :priority: must

   The system SHALL download model files from HTTP/HTTPS URLs.

.. req:: Verify File Checksums
   :id: FR-DEPLOY-016
   :status: approved
   :tags: deploy, model, verification, security
   :priority: must

   The system SHALL verify downloaded files using SHA-256 checksums.

.. req:: Display Download Progress
   :id: FR-DEPLOY-017
   :status: approved
   :tags: deploy, model, download, ui
   :priority: must

   The system SHALL display download progress with progress bars.

.. req:: Resume Interrupted Downloads
   :id: FR-DEPLOY-018
   :status: approved
   :tags: deploy, model, download, reliability
   :priority: should

   The system SHALL support resume capability for interrupted downloads.

.. req:: Model File Configuration Options
   :id: FR-DEPLOY-019
   :status: approved
   :tags: deploy, model, configuration
   :priority: must

   The system SHALL support configuration options: name, url, checksum, required, install_path

3.2.4 System Package Component
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. req:: Detect Linux Distribution
   :id: FR-DEPLOY-020
   :status: approved
   :tags: deploy, system-package, linux
   :priority: could

   The system SHALL detect Linux distribution (Debian, Fedora, Arch).

.. req:: Download System Packages
   :id: FR-DEPLOY-021
   :status: approved
   :tags: deploy, system-package, dependencies
   :priority: could

   The system SHALL download system packages (.deb, .rpm, etc.) with dependencies.

.. req:: Include System Packages in Archive
   :id: FR-DEPLOY-022
   :status: approved
   :tags: deploy, system-package, packaging
   :priority: could

   The system SHALL include system packages in deployment archive.

.. req:: Configure System Package Installation
   :id: FR-DEPLOY-023
   :status: approved
   :tags: deploy, system-package, installation
   :priority: could

   The system SHALL configure installation scripts to install system packages.

**Note:** SystemPackageComponent is marked as **optional for MVP** and may be deferred to v0.2.

--------------

3.3 Packaging
~~~~~~~~~~~~~

.. req:: Create Tar.gz Archives
   :id: FR-DEPLOY-024
   :status: approved
   :tags: deploy, packaging, archive
   :priority: must

   The system SHALL create tar.gz archives for Linux and macOS deployments.

.. req:: Create Zip Archives
   :id: FR-DEPLOY-025
   :status: approved
   :tags: deploy, packaging, archive, windows
   :priority: must

   The system SHALL create zip archives for Windows deployments.

.. req:: Organize Package Directory Structure
   :id: FR-DEPLOY-026
   :status: approved
   :tags: deploy, packaging, structure
   :priority: must

   The system SHALL organize package contents with standardized directory structure.

.. req:: Generate Package Metadata
   :id: FR-DEPLOY-027
   :status: approved
   :tags: deploy, packaging, metadata
   :priority: must

   The system SHALL generate airgap-deploy-metadata.json with package information.

.. req:: Generate Package Checksum
   :id: FR-DEPLOY-028
   :status: approved
   :tags: deploy, packaging, verification, security
   :priority: must

   The system SHALL generate SHA-256 checksum for the entire package.

.. req:: Configurable Compression Levels
   :id: FR-DEPLOY-029
   :status: approved
   :tags: deploy, packaging, compression
   :priority: should

   The system SHALL support configurable compression levels.

--------------

3.4 Installation Script Generation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. req:: Generate Bash Installation Scripts
   :id: FR-DEPLOY-030
   :status: approved
   :tags: deploy, installation, bash, linux, macos
   :priority: must

   The system SHALL generate Bash installation scripts (install.sh) for Linux/macOS.

.. req:: Generate PowerShell Installation Scripts
   :id: FR-DEPLOY-031
   :status: approved
   :tags: deploy, installation, powershell, windows
   :priority: must

   The system SHALL generate PowerShell installation scripts (install.ps1) for Windows.

.. req:: Installation Script Steps
   :id: FR-DEPLOY-032
   :status: approved
   :tags: deploy, installation, workflow
   :priority: must

   Installation scripts SHALL perform dependency checks, display plan, prompt for location, execute builds, configure files, set permissions, and log actions.

.. req:: Installation Script Modes
   :id: FR-DEPLOY-033
   :status: approved
   :tags: deploy, installation, modes
   :priority: must

   Installation scripts SHALL support interactive mode and automatic (unattended) mode.

.. req:: Detect Existing Installations
   :id: FR-DEPLOY-034
   :status: approved
   :tags: deploy, installation, upgrade
   :priority: should

   Installation scripts SHALL detect existing installations and offer upgrade path.

.. req:: Verify Disk Space
   :id: FR-DEPLOY-035
   :status: approved
   :tags: deploy, installation, validation
   :priority: must

   Installation scripts SHALL verify sufficient disk space before proceeding.

.. req:: Installation Error Messages
   :id: FR-DEPLOY-036
   :status: approved
   :tags: deploy, installation, error-handling
   :priority: must

   Installation scripts SHALL provide clear error messages and recovery instructions.

--------------

3.5 Command-Line Interface
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. req:: CLI Commands
   :id: FR-DEPLOY-037
   :status: approved
   :tags: deploy, cli, commands
   :priority: must

   The system SHALL provide commands: prep, validate, init, list-components with appropriate arguments.

.. req:: Colored CLI Output
   :id: FR-DEPLOY-038
   :status: approved
   :tags: deploy, cli, ui
   :priority: should

   The system SHALL display colored output for improved readability.

.. req:: Progress Bars
   :id: FR-DEPLOY-039
   :status: approved
   :tags: deploy, cli, ui, progress
   :priority: must

   The system SHALL display progress bars for long-running operations (downloads, compression).

.. req:: Verbose Logging Flag
   :id: FR-DEPLOY-040
   :status: approved
   :tags: deploy, cli, logging
   :priority: must

   The system SHALL support --verbose flag for detailed logging.

.. req:: Help Flag
   :id: FR-DEPLOY-041
   :status: approved
   :tags: deploy, cli, help
   :priority: must

   The system SHALL support --help flag for all commands.

--------------

3.6 Configuration Management
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. req:: Global Configuration File
   :id: FR-DEPLOY-042
   :status: approved
   :tags: deploy, configuration
   :priority: should

   The system SHALL support global configuration file at ~/.airgap-deploy/config.toml.

.. req:: Global Configuration Options
   :id: FR-DEPLOY-043
   :status: approved
   :tags: deploy, configuration
   :priority: should

   The system SHALL support global configuration options: default_target, cache_dir, proxy.

.. req:: CLI Overrides Configuration
   :id: FR-DEPLOY-044
   :status: approved
   :tags: deploy, configuration, cli
   :priority: must

   Command-line arguments SHALL override global configuration.

--------------

3.7 Error Handling and Recovery
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. req:: Clear Error Messages
   :id: FR-DEPLOY-045
   :status: approved
   :tags: deploy, error-handling
   :priority: must

   The system SHALL provide clear, actionable error messages for all failure modes.

.. req:: Suggest Error Recovery Steps
   :id: FR-DEPLOY-046
   :status: approved
   :tags: deploy, error-handling, recovery
   :priority: should

   The system SHALL suggest recovery steps for common errors: missing dependencies, network failures, disk space issues, invalid manifests.

.. req:: Non-Zero Exit Codes
   :id: FR-DEPLOY-047
   :status: approved
   :tags: deploy, error-handling, cli
   :priority: must

   The system SHALL exit with non-zero status codes on errors.

.. req:: Operation Logging
   :id: FR-DEPLOY-048
   :status: approved
   :tags: deploy, logging, debugging
   :priority: must

   The system SHALL log all operations to enable debugging.

--------------

4. Non-Functional Requirements
------------------------------

4.1 Performance
~~~~~~~~~~~~~~~

**NFR-1.1:** Package preparation SHALL complete in less than 5 minutes for typical applications (<1GB components).

.. nfreq:: Package Preparation Performance
   :id: NFR-DEPLOY-001
   :status: approved
   :tags: deploy, performance
   :priority: should

   Package preparation SHALL complete in less than 5 minutes for typical applications (<1GB components).

**NFR-1.2:** Large model downloads (1-10GB) SHALL display progress and support resume.

.. nfreq:: Large Download Handling
   :id: NFR-DEPLOY-002
   :status: approved
   :tags: deploy, performance, download
   :priority: must

   Large model downloads (1-10GB) SHALL display progress and support resume.

**NFR-1.3:** Parallel component collection SHALL be used where possible to reduce preparation time.

.. nfreq:: Parallel Component Collection
   :id: NFR-DEPLOY-003
   :status: approved
   :tags: deploy, performance, parallelism
   :priority: should

   Parallel component collection SHALL be used where possible to reduce preparation time.

**NFR-1.4:** Installation scripts SHALL complete in less than 20 minutes for typical applications (including build time).

.. nfreq:: Installation Performance
   :id: NFR-DEPLOY-004
   :status: approved
   :tags: deploy, performance, installation
   :priority: should

   Installation scripts SHALL complete in less than 20 minutes for typical applications (including build time).

4.2 Reliability
~~~~~~~~~~~~~~~

**NFR-2.1:** The system SHALL verify all downloaded files using SHA-256 checksums.

.. nfreq:: Checksum Verification
   :id: NFR-DEPLOY-005
   :status: approved
   :tags: deploy, reliability, security, verification
   :priority: must

   The system SHALL verify all downloaded files using SHA-256 checksums.

**NFR-2.2:** The system SHALL retry failed network operations up to 3 times with exponential backoff.

.. nfreq:: Network Operation Retry
   :id: NFR-DEPLOY-006
   :status: approved
   :tags: deploy, reliability, network
   :priority: must

   The system SHALL retry failed network operations up to 3 times with exponential backoff.

**NFR-2.3:** Installation scripts SHALL be idempotent (safe to run multiple times).

.. nfreq:: Idempotent Installation
   :id: NFR-DEPLOY-007
   :status: approved
   :tags: deploy, reliability, installation
   :priority: must

   Installation scripts SHALL be idempotent (safe to run multiple times).

**NFR-2.4:** The system SHALL handle interruptions gracefully (Ctrl+C, system shutdown).

.. nfreq:: Graceful Interruption Handling
   :id: NFR-DEPLOY-008
   :status: approved
   :tags: deploy, reliability, error-handling
   :priority: must

   The system SHALL handle interruptions gracefully (Ctrl+C, system shutdown).

4.3 Usability
~~~~~~~~~~~~~

**NFR-3.1:** First-time users SHALL be able to create a deployment package within 10 minutes using provided examples.

.. nfreq:: First-Time User Experience
   :id: NFR-DEPLOY-009
   :status: approved
   :tags: deploy, usability
   :priority: should

   First-time users SHALL be able to create a deployment package within 10 minutes using provided examples.

**NFR-3.2:** Error messages SHALL include specific details about the failure and suggested fixes.

.. nfreq:: Detailed Error Messages
   :id: NFR-DEPLOY-010
   :status: approved
   :tags: deploy, usability, error-handling
   :priority: must

   Error messages SHALL include specific details about the failure and suggested fixes.

**NFR-3.3:** The CLI SHALL provide help text accessible via ``--help`` for all commands.

.. nfreq:: Command Help Text
   :id: NFR-DEPLOY-011
   :status: approved
   :tags: deploy, usability, cli, help
   :priority: must

   The CLI SHALL provide help text accessible via --help for all commands.

**NFR-3.4:** Progress indicators SHALL be shown for all operations taking longer than 2 seconds.

.. nfreq:: Progress Indicators
   :id: NFR-DEPLOY-012
   :status: approved
   :tags: deploy, usability, ui
   :priority: must

   Progress indicators SHALL be shown for all operations taking longer than 2 seconds.

4.4 Maintainability
~~~~~~~~~~~~~~~~~~~

**NFR-4.1:** The codebase SHALL achieve at least 80% test coverage.

.. nfreq:: Test Coverage
   :id: NFR-DEPLOY-013
   :status: approved
   :tags: deploy, maintainability, testing
   :priority: must

   The codebase SHALL achieve at least 80% test coverage.

**NFR-4.2:** All public APIs SHALL have rustdoc documentation.

.. nfreq:: API Documentation
   :id: NFR-DEPLOY-014
   :status: approved
   :tags: deploy, maintainability, documentation
   :priority: must

   All public APIs SHALL have rustdoc documentation.

**NFR-4.3:** The code SHALL pass ``cargo clippy`` with zero warnings.

.. nfreq:: Clippy Compliance
   :id: NFR-DEPLOY-015
   :status: approved
   :tags: deploy, maintainability, code-quality
   :priority: must

   The code SHALL pass cargo clippy with zero warnings.

**NFR-4.4:** The code SHALL be formatted with ``rustfmt``.

.. nfreq:: Code Formatting
   :id: NFR-DEPLOY-016
   :status: approved
   :tags: deploy, maintainability, code-quality
   :priority: must

   The code SHALL be formatted with rustfmt.

4.5 Portability
~~~~~~~~~~~~~~~

**NFR-5.1:** The system SHALL run on Linux (Ubuntu 20.04+, Fedora 35+, Debian 11+).

.. nfreq:: Linux Platform Support
   :id: NFR-DEPLOY-017
   :status: approved
   :tags: deploy, portability, linux
   :priority: must

   The system SHALL run on Linux (Ubuntu 20.04+, Fedora 35+, Debian 11+).

**NFR-5.2:** The system SHALL run on macOS (10.15+, both Intel and Apple Silicon).

.. nfreq:: macOS Platform Support
   :id: NFR-DEPLOY-018
   :status: approved
   :tags: deploy, portability, macos
   :priority: must

   The system SHALL run on macOS (10.15+, both Intel and Apple Silicon).

**NFR-5.3:** The system SHALL run on Windows (Windows 10/11).

.. nfreq:: Windows Platform Support
   :id: NFR-DEPLOY-019
   :status: approved
   :tags: deploy, portability, windows
   :priority: must

   The system SHALL run on Windows (Windows 10/11).

**NFR-5.4:** Generated installation scripts SHALL be compatible with Bash 4.0+ (Linux/macOS) and PowerShell 5.1+ (Windows).

.. nfreq:: Installation Script Compatibility
   :id: NFR-DEPLOY-020
   :status: approved
   :tags: deploy, portability, installation
   :priority: must

   Generated installation scripts SHALL be compatible with Bash 4.0+ (Linux/macOS) and PowerShell 5.1+ (Windows).

4.6 Security
~~~~~~~~~~~~

**NFR-6.1:** The system SHALL verify checksums for all downloaded files.

.. nfreq:: Verify All Checksums
   :id: NFR-DEPLOY-021
   :status: approved
   :tags: deploy, security, verification
   :priority: must

   The system SHALL verify checksums for all downloaded files.

**NFR-6.2:** The system SHALL NOT execute arbitrary code from manifests.

.. nfreq:: No Arbitrary Code Execution
   :id: NFR-DEPLOY-022
   :status: approved
   :tags: deploy, security
   :priority: must

   The system SHALL NOT execute arbitrary code from manifests.

**NFR-6.3:** Installation scripts SHALL require explicit confirmation before destructive operations.

.. nfreq:: Confirm Destructive Operations
   :id: NFR-DEPLOY-023
   :status: approved
   :tags: deploy, security, installation
   :priority: must

   Installation scripts SHALL require explicit confirmation before destructive operations.

**NFR-6.4:** The system SHALL use HTTPS for all network operations.

.. nfreq:: HTTPS for Network Operations
   :id: NFR-DEPLOY-024
   :status: approved
   :tags: deploy, security, network
   :priority: must

   The system SHALL use HTTPS for all network operations.

**NFR-6.5:** Temporary files SHALL be created with restrictive permissions (user-only).

.. nfreq:: Restrictive File Permissions
   :id: NFR-DEPLOY-025
   :status: approved
   :tags: deploy, security, filesystem
   :priority: must

   Temporary files SHALL be created with restrictive permissions (user-only).

4.7 Scalability
~~~~~~~~~~~~~~~

**NFR-7.1:** The system SHALL handle packages up to 50GB in size.

.. nfreq:: Large Package Support
   :id: NFR-DEPLOY-026
   :status: approved
   :tags: deploy, scalability
   :priority: should

   The system SHALL handle packages up to 50GB in size.

**NFR-7.2:** The system SHALL support manifests with up to 100 components.

.. nfreq:: Multi-Component Manifests
   :id: NFR-DEPLOY-027
   :status: approved
   :tags: deploy, scalability
   :priority: should

   The system SHALL support manifests with up to 100 components.

**NFR-7.3:** Parallel collection SHALL scale with available CPU cores.

.. nfreq:: CPU-Scalable Parallelism
   :id: NFR-DEPLOY-028
   :status: approved
   :tags: deploy, scalability, performance
   :priority: should

   Parallel collection SHALL scale with available CPU cores.

--------------

5. External Interface Requirements
----------------------------------

5.1 User Interfaces
~~~~~~~~~~~~~~~~~~~

**UI-1:** Command-line interface with ANSI color support

**UI-2:** Progress bars for long-running operations (using indicatif crate)

**UI-3:** Interactive prompts in generated installation scripts

5.2 Hardware Interfaces
~~~~~~~~~~~~~~~~~~~~~~~

**HW-1:** Standard filesystem I/O (no special hardware requirements)

**HW-2:** Network interface for downloading components during prep phase

**HW-3:** Removable media support (USB drives) for package transfer (OS-provided)

5.3 Software Interfaces
~~~~~~~~~~~~~~~~~~~~~~~

**SW-1:** Integration with ``cargo`` for Rust dependency vendoring

**SW-2:** Integration with ``git`` for cloning external repositories

**SW-3:** HTTP/HTTPS clients for downloading models and packages

**SW-4:** Integration with system package managers (apt, dnf, pacman) for SystemPackageComponent

**SW-5:** Integration with airgap-transfer for large package chunking (workflow level, not code level)

5.4 Communications Interfaces
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**COM-1:** HTTP/HTTPS for downloading components (preparation phase only)

**COM-2:** No network communication during installation phase (enforced by air-gap)

--------------

6. Requirements Traceability
----------------------------

6.1 Use Case Coverage
~~~~~~~~~~~~~~~~~~~~~

+------------------------------+--------------------------------------------------------------------------------------------+
| Use Case                     | Requirements                                                                               |
+==============================+============================================================================================+
| AirGap Whisper Deployment    | FR-2.1 to FR-2.5, FR-2.6 to FR-2.9, FR-2.10 to FR-2.14, FR-3.1 to FR-3.6, FR-4.1 to FR-4.7 |
+------------------------------+--------------------------------------------------------------------------------------------+
| Ollama Deployment            | FR-2.10 to FR-2.14 (large models), FR-3.1 to FR-3.6, Integration with airgap-transfer      |
+------------------------------+--------------------------------------------------------------------------------------------+
| Custom Application Packaging | All FR sections                                                                            |
+------------------------------+--------------------------------------------------------------------------------------------+

6.2 Design Principles Alignment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All requirements align with :doc:`Principles </meta/principles>`:

+---------------------------+--------------------------------------------------+
| Principle                 | Relevant Requirements                            |
+===========================+==================================================+
| **Privacy/Data Locality** | COM-2: No network during installation            |
+---------------------------+--------------------------------------------------+
| **Minimal Dependencies**  | NFR-4.1 to NFR-4.4: Clean, maintainable code     |
+---------------------------+--------------------------------------------------+
| **Simple Architecture**   | FR-1.1 to FR-1.5: Declarative manifests          |
+---------------------------+--------------------------------------------------+
| **Air-gap Ready**         | ALL requirements designed for air-gap deployment |
+---------------------------+--------------------------------------------------+

--------------

7. Appendices
-------------

7.1 Example Manifest
~~~~~~~~~~~~~~~~~~~~

.. code:: toml

   [package]
   name = "example-app"
   version = "1.0.0"
   description = "Example application for air-gap deployment"

   [targets]
   platforms = ["linux-x86_64", "macos-aarch64"]
   default = "linux-x86_64"

   [[components]]
   type = "rust-app"
   source = "."
   vendor = true
   include_toolchain = true

   [[components]]
   type = "external-binary"
   name = "dependency"
   repo = "https://github.com/example/dependency.git"
   tag = "v1.0.0"
   build_instructions = "make"

   [[components]]
   type = "model-file"
   name = "model"
   url = "https://example.com/model.bin"
   checksum = "sha256:abc123..."
   required = true

   [install]
   method = "build-from-source"
   install_to = "user"
   mode = "interactive"

7.2 Glossary
~~~~~~~~~~~~

See Section 1.3 for definitions.

--------------

**End of Software Requirements Specification**
