Software Requirements Specification
===================================

airgap-deploy
-------------

**Version:** 1.0.0 **Date:** 2026-01-04 **Status:** Draft **Standard:** IEEE 830-1998

--------------

1. Introduction
---------------

1.1 Purpose
~~~~~~~~~~~

This Software Requirements Specification (SRS) describes the functional and non-functional requirements for **airgap-deploy**, a command-line tool for packaging applications and their dependencies for deployment on air-gapped systems.

This document is intended for: - Developers implementing airgap-deploy - Release engineers using airgap-deploy to package applications - Technical reviewers evaluating the tool’s capabilities

1.2 Scope
~~~~~~~~~

**Product Name:** airgap-deploy **Product Purpose:** Simplify the packaging and installation of software on air-gapped systems

**Benefits:** - Declarative manifest-based packaging (no custom scripts) - Cross-platform support (Linux, macOS, Windows) - Automated dependency collection and vendoring - Generated installation scripts for air-gapped deployment

**Goals:** - Enable developers to package any application for air-gap deployment with a single TOML manifest - Reduce manual effort in preparing air-gap packages from days to minutes - Ensure reproducible, verifiable deployments

**Out of Scope (v1.0):** - GUI interface (CLI only) - Network-based distribution mechanisms - Digital signature/verification (future enhancement) - Automatic updates (contradicts air-gap philosophy) - Plugin system (deferred to future version)

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
- `Development Plan <../development-plan.md>`__ - Implementation roadmap
- `Use Case Analysis <../use-case-analysis/overview.md>`__ - Detailed workflows
- `Meta-Architecture <../../meta-architecture.md>`__ - Project relationships

1.5 Overview
~~~~~~~~~~~~

This SRS is organized as follows: - **Section 2:** Overall description of the product - **Section 3:** Functional requirements - **Section 4:** Non-functional requirements - **Section 5:** External interface requirements

--------------

2. Overall Description
----------------------

2.1 Product Perspective
~~~~~~~~~~~~~~~~~~~~~~~

airgap-deploy is a **standalone developer tool** that integrates into existing software development workflows. It operates in two distinct phases:

**Phase 1 - Preparation (Connected System):** - Developer creates ``AirGapDeploy.toml`` manifest - airgap-deploy collects application source, dependencies, models, binaries - Generates deployment package (.tar.gz or .zip) - Generates installation scripts (install.sh, install.ps1)

**Phase 2 - Installation (Air-Gapped System):** - User transfers package via USB or other physical media - User executes generated installation script - Script builds/installs application from vendored dependencies - No network access required

**Relationship to Other Systems:** - **airgap-transfer:** Optional integration for large packages (see `meta-architecture <../../meta-architecture.md>`__) - **AirGap Whisper:** Reference implementation and primary use case - **CI/CD pipelines:** Integrates with GitHub Actions, GitLab CI for automated package generation

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

**Regulatory Constraints:** - Must comply with open-source licensing (MIT OR Apache-2.0) - No export-controlled cryptography beyond SHA-256

**Technical Constraints:** - Requires Rust toolchain for building airgap-deploy itself - Preparation phase requires internet access (by design) - Installation phase must work completely offline - Package size limited by available storage media

**Design Constraints:** - Command-line interface only (no GUI) - Declarative manifest format (TOML) - Cross-platform compatibility (Linux, macOS, Windows)

2.5 Assumptions and Dependencies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Assumptions:** - Developer has internet access during package preparation - Target air-gapped system has basic build tools (C compiler, make) - Users can physically transfer files via USB or similar media

**Dependencies:** - External: Git, cargo, platform-specific package managers - Rust crates: See `Development Plan <../development-plan.md#dependencies-summary>`__ for complete list

--------------

3. Functional Requirements
--------------------------

3.1 Manifest Parsing and Validation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**FR-1.1:** The system SHALL parse ``AirGapDeploy.toml`` files using TOML syntax.

**FR-1.2:** The system SHALL validate manifest structure and required fields before processing.

**FR-1.3:** The system SHALL support the following manifest sections: - ``[package]`` - Package metadata (name, version, description) - ``[targets]`` - Target platforms (linux-x86_64, macos-aarch64, windows-x86_64) - ``[install]`` - Installation configuration (method, prefix, mode) - ``[[components]]`` - List of components to include

**FR-1.4:** The system SHALL provide clear error messages for invalid manifests, including line numbers and expected values.

**FR-1.5:** The system SHALL support schema versioning to enable future manifest evolution.

--------------

3.2 Component Collection
~~~~~~~~~~~~~~~~~~~~~~~~

3.2.1 Rust Application Component
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**FR-2.1:** The system SHALL collect Rust application source code from local directories.

**FR-2.2:** The system SHALL execute ``cargo vendor`` to download and vendor all Cargo dependencies.

**FR-2.3:** The system SHALL optionally include Rust toolchain installer for offline builds.

**FR-2.4:** The system SHALL generate ``.cargo/config.toml`` to configure vendored dependency usage.

**FR-2.5:** The system SHALL support the following configuration options: - ``source`` - Path to Rust project - ``vendor`` - Boolean flag to enable vendoring (default: true) - ``include_toolchain`` - Boolean flag to include Rust installer (default: false) - ``prebuild`` - Boolean flag to prebuild binary (default: false, deferred to v0.2)

3.2.2 External Binary Component
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**FR-2.6:** The system SHALL clone Git repositories for external binaries.

**FR-2.7:** The system SHALL support specifying Git branch, tag, or commit.

**FR-2.8:** The system SHALL include build instructions in installation scripts.

**FR-2.9:** The system SHALL support the following configuration options: - ``name`` - Component name - ``repo`` - Git repository URL - ``branch`` / ``tag`` / ``commit`` - Version specification - ``build_instructions`` - Build command (e.g., “make”)

3.2.3 Model File Component
^^^^^^^^^^^^^^^^^^^^^^^^^^

**FR-2.10:** The system SHALL download model files from HTTP/HTTPS URLs.

**FR-2.11:** The system SHALL verify downloaded files using SHA-256 checksums.

**FR-2.12:** The system SHALL display download progress with progress bars.

**FR-2.13:** The system SHALL support resume capability for interrupted downloads.

**FR-2.14:** The system SHALL support the following configuration options: - ``name`` - Model name - ``url`` - Download URL - ``checksum`` - SHA-256 checksum - ``required`` - Boolean flag (default: true) - ``install_path`` - Installation destination

3.2.4 System Package Component
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**FR-2.15:** The system SHALL detect Linux distribution (Debian, Fedora, Arch).

**FR-2.16:** The system SHALL download system packages (.deb, .rpm, etc.) with dependencies.

**FR-2.17:** The system SHALL include system packages in deployment archive.

**FR-2.18:** The system SHALL configure installation scripts to install system packages.

**Note:** SystemPackageComponent is marked as **optional for MVP** and may be deferred to v0.2.

--------------

3.3 Packaging
~~~~~~~~~~~~~

**FR-3.1:** The system SHALL create tar.gz archives for Linux and macOS deployments.

**FR-3.2:** The system SHALL create zip archives for Windows deployments.

**FR-3.3:** The system SHALL organize package contents with the following structure:

::

   package-name-version/
   ├── install.sh / install.ps1    # Installation script
   ├── README.txt                  # Package documentation
   ├── airgap-deploy-metadata.json # Package metadata
   ├── app-source/                 # Application source code
   ├── vendor/                     # Vendored dependencies
   ├── external-binaries/          # External binary sources
   ├── models/                     # Model files
   └── packages/                   # System packages (if any)

**FR-3.4:** The system SHALL generate ``airgap-deploy-metadata.json`` with package information: - Package name, version, description - Target platform - Component inventory - Build date - airgap-deploy version

**FR-3.5:** The system SHALL generate SHA-256 checksum for the entire package.

**FR-3.6:** The system SHALL support configurable compression levels.

--------------

3.4 Installation Script Generation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**FR-4.1:** The system SHALL generate Bash installation scripts (``install.sh``) for Linux/macOS.

**FR-4.2:** The system SHALL generate PowerShell installation scripts (``install.ps1``) for Windows.

**FR-4.3:** Installation scripts SHALL perform the following steps: 1. Check for required dependencies (compilers, build tools) 2. Display installation plan (dry-run mode) 3. Prompt for installation location (interactive mode) 4. Execute component-specific build/install steps 5. Generate application configuration files 6. Set file permissions and ownership 7. Log all actions to install.log

**FR-4.4:** Installation scripts SHALL support the following modes: - **Interactive mode:** Prompt user for installation location and options - **Automatic mode:** Use environment variables for unattended installation

**FR-4.5:** Installation scripts SHALL detect existing installations and offer upgrade path.

**FR-4.6:** Installation scripts SHALL verify sufficient disk space before proceeding.

**FR-4.7:** Installation scripts SHALL provide clear error messages and recovery instructions.

--------------

3.5 Command-Line Interface
~~~~~~~~~~~~~~~~~~~~~~~~~~

**FR-5.1:** The system SHALL provide the following commands:

**``airgap-deploy prep``** - **Purpose:** Prepare deployment package - **Required arguments:** None (reads ``AirGapDeploy.toml`` in current directory) - **Optional arguments:** - ``--manifest <PATH>`` - Path to manifest file - ``--target <PLATFORM>`` - Target platform (linux-x86_64, macos-aarch64, windows-x86_64) - ``--output <PATH>`` - Output file path - ``--include <COMPONENT>`` - Include optional component - ``--dry-run`` - Preview operations without executing - ``--verbose`` - Enable verbose logging

**``airgap-deploy validate``** - **Purpose:** Validate manifest without preparing package - **Required arguments:** None (reads ``AirGapDeploy.toml`` in current directory) - **Optional arguments:** - ``--manifest <PATH>`` - Path to manifest file

**``airgap-deploy init``** - **Purpose:** Create template ``AirGapDeploy.toml`` file - **Optional arguments:** - ``--type <TYPE>`` - Template type (rust-app, python-app, generic)

**``airgap-deploy list-components``** - **Purpose:** Show available built-in component types - **No arguments**

**FR-5.2:** The system SHALL display colored output for improved readability.

**FR-5.3:** The system SHALL display progress bars for long-running operations (downloads, compression).

**FR-5.4:** The system SHALL support ``--verbose`` flag for detailed logging.

**FR-5.5:** The system SHALL support ``--help`` flag for all commands.

--------------

3.6 Configuration Management
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**FR-6.1:** The system SHALL support global configuration file at ``~/.airgap-deploy/config.toml``.

**FR-6.2:** The system SHALL support the following global configuration options: - ``default_target`` - Default target platform - ``cache_dir`` - Directory for cached downloads - ``proxy`` - HTTP proxy settings (for downloads)

**FR-6.3:** Command-line arguments SHALL override global configuration.

--------------

3.7 Error Handling and Recovery
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**FR-7.1:** The system SHALL provide clear, actionable error messages for all failure modes.

**FR-7.2:** The system SHALL suggest recovery steps for common errors: - Missing dependencies - Network failures - Disk space issues - Invalid manifests

**FR-7.3:** The system SHALL exit with non-zero status codes on errors.

**FR-7.4:** The system SHALL log all operations to enable debugging.

--------------

4. Non-Functional Requirements
------------------------------

4.1 Performance
~~~~~~~~~~~~~~~

**NFR-1.1:** Package preparation SHALL complete in less than 5 minutes for typical applications (<1GB components).

**NFR-1.2:** Large model downloads (1-10GB) SHALL display progress and support resume.

**NFR-1.3:** Parallel component collection SHALL be used where possible to reduce preparation time.

**NFR-1.4:** Installation scripts SHALL complete in less than 20 minutes for typical applications (including build time).

4.2 Reliability
~~~~~~~~~~~~~~~

**NFR-2.1:** The system SHALL verify all downloaded files using SHA-256 checksums.

**NFR-2.2:** The system SHALL retry failed network operations up to 3 times with exponential backoff.

**NFR-2.3:** Installation scripts SHALL be idempotent (safe to run multiple times).

**NFR-2.4:** The system SHALL handle interruptions gracefully (Ctrl+C, system shutdown).

4.3 Usability
~~~~~~~~~~~~~

**NFR-3.1:** First-time users SHALL be able to create a deployment package within 10 minutes using provided examples.

**NFR-3.2:** Error messages SHALL include specific details about the failure and suggested fixes.

**NFR-3.3:** The CLI SHALL provide help text accessible via ``--help`` for all commands.

**NFR-3.4:** Progress indicators SHALL be shown for all operations taking longer than 2 seconds.

4.4 Maintainability
~~~~~~~~~~~~~~~~~~~

**NFR-4.1:** The codebase SHALL achieve at least 80% test coverage.

**NFR-4.2:** All public APIs SHALL have rustdoc documentation.

**NFR-4.3:** The code SHALL pass ``cargo clippy`` with zero warnings.

**NFR-4.4:** The code SHALL be formatted with ``rustfmt``.

4.5 Portability
~~~~~~~~~~~~~~~

**NFR-5.1:** The system SHALL run on Linux (Ubuntu 20.04+, Fedora 35+, Debian 11+).

**NFR-5.2:** The system SHALL run on macOS (10.15+, both Intel and Apple Silicon).

**NFR-5.3:** The system SHALL run on Windows (Windows 10/11).

**NFR-5.4:** Generated installation scripts SHALL be compatible with Bash 4.0+ (Linux/macOS) and PowerShell 5.1+ (Windows).

4.6 Security
~~~~~~~~~~~~

**NFR-6.1:** The system SHALL verify checksums for all downloaded files.

**NFR-6.2:** The system SHALL NOT execute arbitrary code from manifests.

**NFR-6.3:** Installation scripts SHALL require explicit confirmation before destructive operations.

**NFR-6.4:** The system SHALL use HTTPS for all network operations.

**NFR-6.5:** Temporary files SHALL be created with restrictive permissions (user-only).

4.7 Scalability
~~~~~~~~~~~~~~~

**NFR-7.1:** The system SHALL handle packages up to 50GB in size.

**NFR-7.2:** The system SHALL support manifests with up to 100 components.

**NFR-7.3:** Parallel collection SHALL scale with available CPU cores.

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

All requirements align with `principles.md <../../principles.md>`__:

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
