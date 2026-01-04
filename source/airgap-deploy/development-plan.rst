AirGap Deploy Implementation Plan
=================================

Executive Summary
-----------------

**Project:** ``AirGap Deploy`` - A universal Rust tool for air-gap deployment **Purpose:** Simplify preparation and installation of software on air-gapped systems **License:** MIT OR Apache-2.0 **Repository:** Separate crate, publishable to crates.io

Project Goals
-------------

Primary Goals
~~~~~~~~~~~~~

1. **Declarative manifests** - Define AirGap Deploy requirements in ``AirGapDeploy.toml``
2. **Cross-platform** - Works on Linux, macOS, Windows (prep and install)
3. **Extensible** - Plugin system for custom component types
4. **Type-safe** - Leverage Rust’s type system for validation
5. **User-friendly** - Clear CLI, good error messages, progress indicators

Non-Goals (v1.0)
~~~~~~~~~~~~~~~~

- GUI interface (CLI only)
- Network-based distribution (local packaging only)
- Digital signatures/verification (future enhancement)
- Automatic updates (contradicts air-gap philosophy)

Architecture Overview
---------------------

::

   ┌──────────────────────────────────────────────────────────┐
   │                     AirGap Deploy CLI                    │
   ├──────────────────────────────────────────────────────────┤
   │                                                           │
   │  Manifest Parser ──▶ Component Registry ──▶ Collector    │
   │                              │                            │
   │                              ▼                            │
   │                       Built-in Components:                │
   │                       • RustAppComponent                  │
   │                       • ExternalBinaryComponent           │
   │                       • ModelFileComponent                │
   │                       • SystemPackageComponent            │
   │                              │                            │
   │                              ▼                            │
   │                         Packager ──▶ Output               │
   │                              │         (tar.gz/zip)       │
   │                              ▼                            │
   │                    Install Generator                      │
   │                    (install.sh/ps1)                       │
   │                                                           │
   └──────────────────────────────────────────────────────────┘

Implementation Phases
---------------------

Phase 1: Core Infrastructure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Goal:** Establish project structure and core abstractions

Tasks
^^^^^

1. **Project Setup**

   - ☐ Create new cargo workspace with two crates:

     - ``airgap-deploy/`` - Main framework library + CLI
     - ``airgap-deploy-test-app/`` - Test application for integration tests

   - ☐ Set up CI/CD (GitHub Actions)
   - ☐ Configure cargo-deny for license compliance
   - ☐ Add basic README, CONTRIBUTING.md, CODE_OF_CONDUCT.md

2. **Core Types** (``src/core/``)

   - ☐ ``Platform`` - OS/architecture abstraction
   - ☐ ``Target`` - Deployment target specification
   - ☐ ``Component`` - Trait definition for all component types
   - ☐ ``Manifest`` - AirGapDeploy.toml structure (using serde)
   - ☐ ``Error`` - Unified error type (using thiserror)

3. **Manifest Parser** (``src/manifest.rs``)

   - ☐ Define ``AirGapDeploy.toml`` schema
   - ☐ Implement TOML parsing (using toml crate)
   - ☐ Validation logic
   - ☐ Schema versioning support

4. **Component Registry** (``src/registry.rs``)

   - ☐ Component registration system
   - ☐ Built-in component auto-registration
   - ☐ Plugin discovery mechanism (optional for Phase 1)

**Deliverables:** - Working manifest parser with validation - Type-safe component registration - 80%+ test coverage for core types

**Dependencies:**

.. code:: toml

   [dependencies]
   serde = { version = "1", features = ["derive"] }
   toml = "0.8"
   thiserror = "1"
   anyhow = "1"

--------------

Phase 2: Built-in Components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Goal:** Implement the four essential component types

.. _tasks-1:

Tasks
^^^^^

1. **RustAppComponent** (``src/components/rust_app.rs``)

   - ☐ Source code collection
   - ☐ ``cargo vendor`` integration
   - ☐ Rust toolchain downloader (from static.rust-lang.org)
   - ☐ Optional cross-compilation support (using ``cross``)
   - ☐ Generate ``.cargo/config.toml`` for vendored deps

2. **ExternalBinaryComponent** (``src/components/external_binary.rs``)

   - ☐ Git repository cloning
   - ☐ Tarball download support
   - ☐ Build instruction templating
   - ☐ Multi-platform binary support

3. **ModelFileComponent** (``src/components/model_file.rs``)

   - ☐ HTTP download with progress bar (using reqwest + indicatif)
   - ☐ Checksum verification (SHA256)
   - ☐ Resume support for large files
   - ☐ Multiple file sources (URL, local path)

4. **SystemPackageComponent** (``src/components/system_package.rs``)

   - ☐ Linux distro detection (Debian, Fedora, Arch)
   - ☐ Package download (apt, dnf, pacman)
   - ☐ Dependency resolution (basic)
   - ☐ Package metadata extraction

**Deliverables:** - Four working component types - Integration tests for each component - Example manifests in ``examples/``

**Dependencies:**

.. code:: toml

   [dependencies]
   reqwest = { version = "0.11", features = ["blocking", "rustls-tls"] }
   indicatif = "0.17"
   sha2 = "0.10"
   flate2 = "1"
   tar = "0.4"
   zip = "0.6"

--------------

Phase 3: Collection & Packaging
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Goal:** Orchestrate components and create deployment packages

.. _tasks-2:

Tasks
^^^^^

1. **Collector Engine** (``src/collector.rs``)

   - ☐ Component execution orchestration
   - ☐ Parallel collection (using rayon)
   - ☐ Progress reporting
   - ☐ Error handling and rollback
   - ☐ Temporary directory management

2. **Packager** (``src/packager.rs``)

   - ☐ Create tar.gz archives (Linux/macOS)
   - ☐ Create zip archives (Windows)
   - ☐ Package structure layout
   - ☐ Metadata file generation (``airgap-deploy-metadata.json``)
   - ☐ Compression level configuration

3. **Package Verification**

   - ☐ Checksum generation for package
   - ☐ Content manifest (list of all files)
   - ☐ Size validation

**Deliverables:** - End-to-end package creation - Package format documentation - Benchmarks for collection/packaging performance

**Dependencies:**

.. code:: toml

   [dependencies]
   rayon = "1"
   tempfile = "3"
   walkdir = "2"

--------------

Phase 4: Installation Script Generation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Goal:** Generate platform-specific installation scripts

.. _tasks-3:

Tasks
^^^^^

1. **Template System** (``src/templates/``)

   - ☐ Tera template engine integration
   - ☐ ``install.sh.tera`` - Bash script template
   - ☐ ``install.ps1.tera`` - PowerShell script template
   - ☐ ``README.txt.tera`` - Package documentation

2. **Install Step Compiler** (``src/installer.rs``)

   - ☐ Convert ``InstallStep`` to shell commands
   - ☐ Platform-specific command mapping
   - ☐ Error handling in generated scripts
   - ☐ Idempotency checks (detect existing installations)

3. **Script Features**

   - ☐ Dependency checking (Rust, git, make, etc.)
   - ☐ Interactive prompts (install location)
   - ☐ Progress output
   - ☐ Logging to install.log
   - ☐ Dry-run mode

**Deliverables:** - Working install script generation - Scripts tested on all target platforms - Script documentation

**Dependencies:**

.. code:: toml

   [dependencies]
   tera = "1"

--------------

Phase 5: CLI Interface
~~~~~~~~~~~~~~~~~~~~~~

**Goal:** User-friendly command-line interface

.. _tasks-4:

Tasks
^^^^^

1. **CLI Structure** (``src/cli.rs``, ``src/main.rs``)

   - ☐ Command parsing (using clap)
   - ☐ ``airgap-deploy prep`` - Prepare deployment package
   - ☐ ``airgap-deploy install`` - Install from package (optional, can use generated script)
   - ☐ ``airgap-deploy validate`` - Validate manifest
   - ☐ ``airgap-deploy list-components`` - Show available components
   - ☐ ``airgap-deploy init`` - Create template AirGapDeploy.toml

2. **User Experience**

   - ☐ Colored output (using colored crate)
   - ☐ Progress bars (using indicatif)
   - ☐ Spinner for long operations
   - ☐ Clear error messages with suggestions
   - ☐ ``--verbose`` flag for debugging

3. **Configuration**

   - ☐ Global config file (``~/.airgap-deploy/config.toml``)
   - ☐ Default target platform
   - ☐ Cache directory for downloads
   - ☐ Proxy settings

**Deliverables:** - Polished CLI experience - Help documentation (``--help``) - Man page generation

**Dependencies:**

.. code:: toml

   [dependencies]
   clap = { version = "4", features = ["derive"] }
   colored = "2"
   env_logger = "0.11"
   log = "0.4"

--------------

Phase 6: Testing & Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Goal:** Comprehensive testing and documentation

.. _tasks-5:

Tasks
^^^^^

1. **Unit Tests**

   - ☐ Core types (platform, target, component trait)
   - ☐ Manifest parsing (valid/invalid cases)
   - ☐ Component logic (each built-in component)
   - ☐ Template rendering

2. **Integration Tests**

   - ☐ End-to-end: manifest → package → install
   - ☐ Multi-platform testing (Linux, macOS, Windows via CI)
   - ☐ Error scenarios (missing dependencies, network failures)
   - ☐ Large package handling (multi-GB models)

3. **Documentation**

   - ☐ API documentation (rustdoc)
   - ☐ User guide (docs/guide.md)

     - Getting started
     - Manifest reference
     - Component types
     - Best practices

   - ☐ Developer guide (docs/developers.md)

     - Architecture overview
     - Creating custom components
     - Contributing guidelines

   - ☐ Examples

     - Rust application (AirGap Whisper)
     - Python application
     - ML application with models
     - Multi-binary application

4. **CI/CD**

   - ☐ Run tests on Linux, macOS, Windows
   - ☐ Clippy lints (deny warnings)
   - ☐ rustfmt checks
   - ☐ cargo-deny license checks
   - ☐ Release automation (GitHub releases)

**Deliverables:** - 80%+ code coverage - Complete documentation - Working examples - CI/CD pipeline

**Dependencies:**

.. code:: toml

   [dev-dependencies]
   criterion = "0.5"      # Benchmarks
   tempfile = "3"         # Test fixtures
   assert_cmd = "2"       # CLI testing
   predicates = "3"       # Test assertions

--------------

Phase 7: Plugin System (Optional)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Goal:** Support custom component plugins

.. _tasks-6:

Tasks
^^^^^

1. **Plugin Discovery**

   - ☐ Load plugins from ``airgap-components/`` directory
   - ☐ Dynamic library loading (using libloading)
   - ☐ Plugin API versioning
   - ☐ Plugin safety checks

2. **Plugin Development Kit**

   - ☐ ``airgap-plugin`` crate with Component trait
   - ☐ Plugin template generator (``airgap plugin new``)
   - ☐ Plugin testing utilities
   - ☐ Plugin packaging (cdylib)

3. **Examples**

   - ☐ TensorFlow model plugin
   - ☐ Docker container plugin
   - ☐ Database dump plugin

**Deliverables:** - Working plugin system - Plugin development guide - Example plugins

**Dependencies:**

.. code:: toml

   [dependencies]
   libloading = "0.8"    # Dynamic library loading

--------------

Testing Strategy
----------------

Unit Tests
~~~~~~~~~~

- Test each module in isolation
- Mock external dependencies (network, filesystem)
- Property-based testing where appropriate (using proptest)

Integration Tests
~~~~~~~~~~~~~~~~~

- Full workflow tests (manifest → package → install)
- Test with real external resources (whisper.cpp repo, models)
- Platform-specific tests (conditional compilation)

Manual Testing
~~~~~~~~~~~~~~

- Test on actual air-gapped systems (VMs with no network)
- Test with large files (multi-GB models)
- Test error recovery (interrupted downloads, disk full)

CI/CD Matrix
~~~~~~~~~~~~

.. code:: yaml

   matrix:
     os: [ubuntu-latest, macos-latest, windows-latest]
     rust: [stable, beta]

--------------

Documentation Structure
-----------------------

::

   airgap-deploy/
   ├── README.md                   # Project overview, quick start
   ├── CHANGELOG.md                # Version history
   ├── CONTRIBUTING.md             # How to contribute
   ├── CODE_OF_CONDUCT.md          # Community guidelines
   ├── docs/
   │   ├── guide/
   │   │   ├── getting-started.md
   │   │   ├── manifest-reference.md
   │   │   ├── component-types.md
   │   │   ├── best-practices.md
   │   │   └── troubleshooting.md
   │   ├── developers/
   │   │   ├── architecture.md
   │   │   ├── custom-components.md
   │   │   ├── plugin-development.md
   │   │   └── contributing.md
   │   └── examples/
   │       ├── rust-app.md
   │       ├── python-app.md
   │       └── ml-app.md
   └── examples/
       ├── airgap-whisper/
       │   └── AirGapDeploy.toml
       ├── python-app/
       │   └── AirGapDeploy.toml
       └── ml-app/
           └── AirGapDeploy.toml

--------------

Dependencies Summary
--------------------

Core Dependencies
~~~~~~~~~~~~~~~~~

.. code:: toml

   [dependencies]
   # CLI
   clap = { version = "4", features = ["derive"] }
   colored = "2"
   indicatif = "0.17"
   env_logger = "0.11"
   log = "0.4"

   # Parsing
   serde = { version = "1", features = ["derive"] }
   toml = "0.8"

   # Errors
   thiserror = "1"
   anyhow = "1"

   # HTTP
   reqwest = { version = "0.11", features = ["blocking", "rustls-tls"] }

   # Compression
   flate2 = "1"
   tar = "0.4"
   zip = "0.6"

   # Crypto
   sha2 = "0.10"

   # Concurrency
   rayon = "1"

   # Templates
   tera = "1"

   # Utilities
   tempfile = "3"
   walkdir = "2"

**Total direct dependencies:** ~20 crates **Philosophy:** Minimal but practical. Every dependency must justify its inclusion.

--------------

Minimum Viable Product (MVP)
----------------------------

For initial release (v0.1.0), include: - ✅ Phase 1: Core infrastructure - ✅ Phase 2: Built-in components (RustApp, ExternalBinary, ModelFile only) - ✅ Phase 3: Packaging - ✅ Phase 4: Install scripts - ✅ Phase 5: Basic CLI - ❌ Phase 6: Partial (basic tests, minimal docs) - ❌ Phase 7: Skip (add in v0.2.0)

--------------

Success Metrics
---------------

Technical Metrics
~~~~~~~~~~~~~~~~~

- ☐ Successfully packages AirGap Whisper for all platforms
- ☐ Generated install scripts work on air-gapped VMs
- ☐ Package creation completes efficiently for typical applications
- ☐ 80%+ code coverage
- ☐ Zero clippy warnings
- ☐ All licenses compatible with MIT/Apache-2.0

User Metrics
~~~~~~~~~~~~

- ☐ First-time user can create package quickly and easily
- ☐ Clear error messages for all failure modes
- ☐ Documentation covers all use cases
- ☐ Examples work out-of-the-box

--------------

Risk Assessment
---------------

+----------------------------------+---------------------+-------------------------------------------------+
| Risk                             | Impact              | Mitigation                                      |
+==================================+=====================+=================================================+
| Cross-compilation complexity     | High                | Start with source-only (no prebuild), add later |
+----------------------------------+---------------------+-------------------------------------------------+
| Network download failures        | Medium              | Retry logic, resume support, checksums          |
+----------------------------------+---------------------+-------------------------------------------------+
| Platform-specific bugs           | Medium              | Comprehensive CI matrix, VM testing             |
+----------------------------------+---------------------+-------------------------------------------------+
| Manifest schema evolution        | Medium              | Schema versioning from day 1                    |
+----------------------------------+---------------------+-------------------------------------------------+
| Large file handling (GB+ models) | Low                 | Streaming downloads, progress bars              |
+----------------------------------+---------------------+-------------------------------------------------+
| Plugin system security           | High                | Phase 7 optional, careful API design            |
+----------------------------------+---------------------+-------------------------------------------------+

--------------

Future Enhancements (Post v1.0)
-------------------------------

1. **v1.1: Enhanced Components**

   - PythonAppComponent (pip, virtualenv)
   - NodeAppComponent (npm, package-lock.json)
   - GoAppComponent (go mod vendor)

2. **v1.2: Advanced Features**

   - Delta updates (only changed files)
   - Multi-platform single package
   - Binary patching for updates

3. **v1.3: Enterprise Features**

   - Digital signatures (GPG, Sigstore)
   - SBOM generation (Software Bill of Materials)
   - Compliance reporting
   - License scanning

4. **v2.0: Major Evolution**

   - Full plugin system
   - GUI (Tauri-based)
   - Package repository format
   - Incremental syncing

--------------

Repository Structure
--------------------

::

   airgap-deploy/
   ├── Cargo.toml                  # Workspace
   ├── README.md
   ├── CHANGELOG.md
   ├── LICENSE-MIT
   ├── LICENSE-APACHE
   ├── .github/
   │   ├── workflows/
   │   │   ├── ci.yml
   │   │   ├── release.yml
   │   │   └── docs.yml
   │   └── ISSUE_TEMPLATE/
   ├── airgap-deploy/                     # Main crate
   │   ├── Cargo.toml
   │   ├── src/
   │   │   ├── main.rs
   │   │   ├── lib.rs
   │   │   ├── cli.rs
   │   │   ├── core/
   │   │   │   ├── mod.rs
   │   │   │   ├── platform.rs
   │   │   │   ├── target.rs
   │   │   │   ├── component.rs
   │   │   │   └── manifest.rs
   │   │   ├── components/
   │   │   │   ├── mod.rs
   │   │   │   ├── rust_app.rs
   │   │   │   ├── external_binary.rs
   │   │   │   ├── model_file.rs
   │   │   │   └── system_package.rs
   │   │   ├── registry.rs
   │   │   ├── collector.rs
   │   │   ├── packager.rs
   │   │   ├── installer.rs
   │   │   └── templates/
   │   │       ├── install.sh.tera
   │   │       ├── install.ps1.tera
   │   │       └── README.txt.tera
   │   ├── tests/
   │   └── benches/
   ├── airgap-deploy-test-app/     # Integration test app
   │   ├── Cargo.toml
   │   ├── src/
   │   └── AirGapDeploy.toml
   ├── docs/
   │   ├── guide/
   │   └── developers/
   └── examples/
       ├── airgap-whisper/
       ├── python-app/
       └── ml-app/

--------------

Integration with whisper-lite
-----------------------------

Once ``AirGap Deploy`` v0.1.0 is released:

1. **Add dependency:**

   .. code:: toml

      [dev-dependencies]
      airgap-deploy = "0.1"

2. **Create ``AirGapDeploy.toml``:**

   .. code:: toml

      [package]
      name = "airgap-whisper"
      version = "0.1.0"

      [[components]]
      type = "rust-app"
      source = "."
      vendor = true
      include_toolchain = true

      [[components]]
      type = "external-binary"
      name = "whisper.cpp"
      repo = "https://github.com/ggerganov/whisper.cpp.git"
      build_instructions = "make"

      [[components]]
      type = "model-file"
      name = "base.en"
      url = "https://huggingface.co/..."
      checksum = "sha256:..."

3. **Generate packages:**

   .. code:: bash

      airgap-deploy prep --target linux-x86_64 --output dist/whisper-lite-linux.tar.gz
      airgap-deploy prep --target macos-aarch64 --output dist/whisper-lite-macos.tar.gz

4. **Update README.md:**

   - Remove detailed instructions
   - Replace with: “See generated ``install.sh`` in package”

--------------

Next Steps
----------

1. **Get approval** on this implementation plan
2. **Create repository:** ``github.com/yourusername/airgap-deploy``
3. **Set up project structure** (Phase 1)
4. **Begin implementation** following phase plan

Questions for Discussion
------------------------

1. **Scope:** Should we include SystemPackageComponent in MVP, or defer to v0.2?
2. **Cross-compilation:** Include in v0.1 or defer to v0.2?
3. **Platform priority:** Which platform should we test most thoroughly? (Suggest: Linux)
4. **Plugin system:** Include in v1.0 or defer to v1.1?
