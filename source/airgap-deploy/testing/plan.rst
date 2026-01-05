Test Plan
=========

AirGap Deploy
-------------

**Version:** 1.0.0 **Date:** 2026-01-04 **Standard:** IEEE 829-2008

--------------

1. Introduction
---------------

1.1 Purpose
~~~~~~~~~~~

This Test Plan describes the testing strategy, approach, and test cases for **airgap-deploy**, ensuring the tool reliably packages applications for air-gapped deployment.

1.2 Scope
~~~~~~~~~

**In Scope:** - Unit tests for all modules - Integration tests for end-to-end workflows - Platform-specific tests (Linux, macOS, Windows) - Performance tests for large packages - Error handling and recovery tests

**Out of Scope:** - GUI testing (no GUI in this application) - Load testing (not a server application) - Security penetration testing (manual review only)

1.3 References
~~~~~~~~~~~~~~

- `Requirements (SRS) <../requirements/srs.md>`__
- `Design (SDD) <../design/sdd.md>`__
- `Development Plan <../development-plan.md>`__
- IEEE 829-2008: IEEE Standard for Software Test Documentation

--------------

2. Test Strategy
----------------

2.1 Test Levels
~~~~~~~~~~~~~~~

**Unit Testing:** - Test individual functions and modules in isolation - Mock external dependencies (filesystem, network) - Target: 80%+ code coverage

**Integration Testing:** - Test component interactions - Test full workflows (manifest → package → install) - Test on real external resources (Git repos, model files)

**System Testing:** - Test on actual air-gapped VMs - Test multi-platform deployments - Test error recovery scenarios

**Acceptance Testing:** - Verify requirements satisfaction - User workflow testing - Reference implementation (AirGap Whisper deployment)

2.2 Test Types
~~~~~~~~~~~~~~

=============== ======================== ================
Test Type       Purpose                  Coverage
=============== ======================== ================
**Functional**  Verify requirements      All FR from SRS
**Performance** Verify speed/scalability NFR-1.x from SRS
**Reliability** Verify error handling    NFR-2.x from SRS
**Usability**   Verify UX                NFR-3.x from SRS
**Portability** Verify platforms         NFR-5.x from SRS
**Security**    Verify checksums         NFR-6.x from SRS
=============== ======================== ================

2.3 Test Environment
~~~~~~~~~~~~~~~~~~~~

**Development Environment:** - Local development machines (Linux, macOS, Windows) - Unit tests run on developer machines - Fast feedback loop

**CI Environment:** - GitHub Actions with matrix builds - Ubuntu 20.04, 22.04 - macOS 12, 14 - Windows 10, 11 - Rust stable, beta

**Air-Gapped Environment:** - VirtualBox/VMware VMs with no network - Test actual air-gap deployment - Ubuntu 22.04 VM (primary test target)

--------------

3. Test Cases
-------------

3.1 Manifest Parsing (FR-1.x)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**TC-001: Valid Manifest Parsing** - **Input:** Valid AirGapDeploy.toml with all required fields - **Expected:** Manifest parses successfully, returns Manifest struct - **Type:** Unit test

.. test:: Valid Manifest Parsing
   :id: TC-MAN-001
   :status: approved
   :tags: deploy, manifest, parsing
   :tests: FR-DEPLOY-001
   :priority: high

   Verify valid AirGapDeploy.toml parses successfully

**TC-002: Invalid Manifest - Missing Required Field** - **Input:** TOML missing ``package.name`` - **Expected:** Parse error with clear message indicating missing field - **Type:** Unit test

.. test:: Invalid Manifest - Missing Required Field
   :id: TC-MAN-002
   :status: approved
   :tags: deploy, manifest, validation, error-handling
   :tests: FR-DEPLOY-002, FR-DEPLOY-004
   :priority: high

   Verify parse error when required field missing

**TC-003: Invalid Manifest - Wrong Type** - **Input:** ``package.version`` is integer, not string - **Expected:** Parse error with type mismatch message - **Type:** Unit test

.. test:: Invalid Manifest - Wrong Type
   :id: TC-MAN-003
   :status: approved
   :tags: deploy, manifest, validation, error-handling
   :tests: FR-DEPLOY-002, FR-DEPLOY-004
   :priority: high

   Verify parse error on type mismatch

**TC-004: Unsupported Component Type** - **Input:** Component with ``type = "unknown-type"`` - **Expected:** Validation error listing supported types - **Type:** Unit test

.. test:: Unsupported Component Type
   :id: TC-MAN-004
   :status: approved
   :tags: deploy, manifest, validation, component
   :tests: FR-DEPLOY-002, FR-DEPLOY-004
   :priority: medium

   Verify validation error for unknown component type

**TC-005: Schema Versioning** - **Input:** Manifest with future schema version - **Expected:** Warning about version mismatch, attempt to parse - **Type:** Unit test

.. test:: Schema Versioning
   :id: TC-MAN-005
   :status: approved
   :tags: deploy, manifest, versioning
   :tests: FR-DEPLOY-005
   :priority: low

   Verify warning for future schema version

--------------

3.2 RustAppComponent (FR-2.1 to FR-2.5)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**TC-010: Rust App with Vendoring** - **Input:** Rust project with dependencies - **Expected:** ``cargo vendor`` executed, .cargo/config.toml generated - **Type:** Integration test

.. test:: Rust App with Vendoring
   :id: TC-RUST-001
   :status: approved
   :tags: deploy, rust, vendor
   :tests: FR-DEPLOY-007, FR-DEPLOY-009
   :priority: high

   Verify cargo vendor and config generation

**TC-011: Rust Toolchain Inclusion** - **Input:** RustApp with ``include_toolchain = true`` - **Expected:** Rust installer downloaded and included in package - **Type:** Integration test

.. test:: Rust Toolchain Inclusion
   :id: TC-RUST-002
   :status: approved
   :tags: deploy, rust, toolchain
   :tests: FR-DEPLOY-008
   :priority: medium

   Verify Rust installer download and inclusion

**TC-012: Missing Cargo.toml** - **Input:** Directory without Cargo.toml - **Expected:** Error indicating Cargo.toml not found - **Type:** Unit test

.. test:: Missing Cargo.toml
   :id: TC-RUST-003
   :status: approved
   :tags: deploy, rust, error-handling
   :tests: FR-DEPLOY-006, FR-DEPLOY-045
   :priority: medium

   Verify error when Cargo.toml not found

**TC-013: Cargo Vendor Failure** - **Input:** Rust project with invalid dependencies - **Expected:** Error with cargo vendor output - **Type:** Integration test

.. test:: Cargo Vendor Failure
   :id: TC-RUST-004
   :status: approved
   :tags: deploy, rust, vendor, error-handling
   :tests: FR-DEPLOY-007, FR-DEPLOY-045
   :priority: medium

   Verify error handling for cargo vendor failures

--------------

3.3 ExternalBinaryComponent (FR-2.6 to FR-2.9)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**TC-020: Git Repository Cloning** - **Input:** Valid GitHub repository URL with tag - **Expected:** Repository cloned, tag checked out - **Type:** Integration test

.. test:: Git Repository Cloning
   :id: TC-GIT-001
   :status: approved
   :tags: deploy, git, clone
   :tests: FR-DEPLOY-011, FR-DEPLOY-012
   :priority: high

   Verify Git repository cloning with tag checkout

**TC-021: Git Branch Checkout** - **Input:** Repository with ``branch = "main"`` - **Expected:** Main branch checked out - **Type:** Integration test

.. test:: Git Branch Checkout
   :id: TC-GIT-002
   :status: approved
   :tags: deploy, git, branch
   :tests: FR-DEPLOY-012
   :priority: high

   Verify Git branch checkout

**TC-022: Invalid Repository URL** - **Input:** Non-existent Git repository - **Expected:** Error indicating repository not found - **Type:** Integration test

.. test:: Invalid Repository URL
   :id: TC-GIT-003
   :status: approved
   :tags: deploy, git, error-handling
   :tests: FR-DEPLOY-011, FR-DEPLOY-045
   :priority: medium

   Verify error for invalid repository URL

**TC-023: Network Failure During Clone** - **Input:** Git clone with simulated network failure - **Expected:** Retry up to 3 times, clear error message - **Type:** Integration test

.. test:: Network Failure During Clone
   :id: TC-GIT-004
   :status: approved
   :tags: deploy, git, network, reliability
   :tests: NFR-DEPLOY-006, FR-DEPLOY-045
   :priority: high

   Verify retry logic for network failures

--------------

3.4 ModelFileComponent (FR-2.10 to FR-2.14)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**TC-030: Model File Download** - **Input:** URL to downloadable file with checksum - **Expected:** File downloaded, checksum verified - **Type:** Integration test

.. test:: Model File Download
   :id: TC-MODEL-001
   :status: approved
   :tags: deploy, model, download
   :tests: FR-DEPLOY-015, FR-DEPLOY-016
   :priority: high

   Verify model file download with checksum verification

**TC-031: Checksum Verification Success** - **Input:** Downloaded file with matching checksum - **Expected:** Verification passes - **Type:** Unit test

.. test:: Checksum Verification Success
   :id: TC-MODEL-002
   :status: approved
   :tags: deploy, model, verification, security
   :tests: FR-DEPLOY-016, NFR-DEPLOY-005
   :priority: high

   Verify checksum verification passes for matching checksum

**TC-032: Checksum Verification Failure** - **Input:** Downloaded file with mismatched checksum - **Expected:** Error with expected/actual checksums, file deleted - **Type:** Unit test

.. test:: Checksum Verification Failure
   :id: TC-MODEL-003
   :status: approved
   :tags: deploy, model, verification, security, error-handling
   :tests: FR-DEPLOY-016, NFR-DEPLOY-005, FR-DEPLOY-045
   :priority: high

   Verify error and file deletion on checksum mismatch

**TC-033: Download Resume** - **Input:** Partially downloaded file, resume download - **Expected:** Download continues from partial point - **Type:** Integration test

.. test:: Download Resume
   :id: TC-MODEL-004
   :status: approved
   :tags: deploy, model, download, reliability
   :tests: FR-DEPLOY-018
   :priority: medium

   Verify download resume capability

**TC-034: Large File Download (1GB+)** - **Input:** Large model file - **Expected:** Progress bar displayed, streaming to disk, low memory usage - **Type:** Performance test

.. test:: Large File Download
   :id: TC-MODEL-005
   :status: approved
   :tags: deploy, model, download, performance
   :tests: FR-DEPLOY-017, NFR-DEPLOY-002
   :priority: high

   Verify large file download with progress display

**TC-035: Download Cache Hit** - **Input:** File already in cache with matching checksum - **Expected:** Skip download, use cached file - **Type:** Integration test

.. test:: Download Cache Hit
   :id: TC-MODEL-006
   :status: approved
   :tags: deploy, model, cache, performance
   :tests: FR-DEPLOY-016
   :priority: medium

   Verify cached file reuse

--------------

3.5 Packaging (FR-3.1 to FR-3.6)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**TC-040: Create tar.gz Package (Linux/macOS)** - **Input:** Collected components, target platform = linux-x86_64 - **Expected:** tar.gz archive created with correct structure - **Type:** Integration test

.. test:: Create tar.gz Package
   :id: TC-PKG-001
   :status: approved
   :tags: deploy, packaging, archive, linux, macos
   :tests: FR-DEPLOY-024, FR-DEPLOY-026
   :priority: high

   Verify tar.gz archive creation with correct structure

**TC-041: Create zip Package (Windows)** - **Input:** Collected components, target platform = windows-x86_64 - **Expected:** zip archive created with correct structure - **Type:** Integration test

.. test:: Create zip Package
   :id: TC-PKG-002
   :status: approved
   :tags: deploy, packaging, archive, windows
   :tests: FR-DEPLOY-025, FR-DEPLOY-026
   :priority: high

   Verify zip archive creation for Windows

**TC-042: Package Metadata Generation** - **Input:** Package with multiple components - **Expected:** airgap-deploy-metadata.json with all components listed - **Type:** Unit test

.. test:: Package Metadata Generation
   :id: TC-PKG-003
   :status: approved
   :tags: deploy, packaging, metadata
   :tests: FR-DEPLOY-027
   :priority: high

   Verify metadata file generation

**TC-043: Package Checksum Generation** - **Input:** Created package - **Expected:** SHA-256 checksum file created - **Type:** Unit test

.. test:: Package Checksum Generation
   :id: TC-PKG-004
   :status: approved
   :tags: deploy, packaging, checksum, security
   :tests: FR-DEPLOY-028, NFR-DEPLOY-005
   :priority: high

   Verify package checksum generation

**TC-044: Large Package (10GB+)** - **Input:** Multiple large model files - **Expected:** Package created successfully, memory usage stable - **Type:** Performance test

.. test:: Large Package Creation
   :id: TC-PKG-005
   :status: approved
   :tags: deploy, packaging, performance, scalability
   :tests: NFR-DEPLOY-026
   :priority: medium

   Verify large package creation with stable memory usage

--------------

3.6 Install Script Generation (FR-4.1 to FR-4.7)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**TC-050: Bash Script Generation** - **Input:** Components with install steps - **Expected:** install.sh with dependency checks, build commands - **Type:** Unit test

.. test:: Bash Script Generation
   :id: TC-INSTALL-001
   :status: approved
   :tags: deploy, installation, bash, linux, macos
   :tests: FR-DEPLOY-030, FR-DEPLOY-032
   :priority: high

   Verify Bash installation script generation

**TC-051: PowerShell Script Generation** - **Input:** Components with install steps - **Expected:** install.ps1 with equivalent logic - **Type:** Unit test

.. test:: PowerShell Script Generation
   :id: TC-INSTALL-002
   :status: approved
   :tags: deploy, installation, powershell, windows
   :tests: FR-DEPLOY-031, FR-DEPLOY-032
   :priority: high

   Verify PowerShell installation script generation

**TC-052: Interactive Mode Prompts** - **Input:** Install script with ``mode = "interactive"`` - **Expected:** Script prompts for installation location - **Type:** Integration test

.. test:: Interactive Mode Prompts
   :id: TC-INSTALL-003
   :status: approved
   :tags: deploy, installation, interactive
   :tests: FR-DEPLOY-033
   :priority: high

   Verify interactive mode prompts user

**TC-053: Automatic Mode** - **Input:** Install script run with ``MODE=automatic`` - **Expected:** No prompts, uses environment variables - **Type:** Integration test

.. test:: Automatic Mode
   :id: TC-INSTALL-004
   :status: approved
   :tags: deploy, installation, automatic
   :tests: FR-DEPLOY-033
   :priority: high

   Verify automatic unattended installation

**TC-054: Dependency Check Success** - **Input:** System with all required dependencies - **Expected:** Script proceeds to installation - **Type:** System test

.. test:: Dependency Check Success
   :id: TC-INSTALL-005
   :status: approved
   :tags: deploy, installation, dependencies
   :tests: FR-DEPLOY-032
   :priority: high

   Verify dependency check passes when all present

**TC-055: Dependency Check Failure** - **Input:** System missing C compiler - **Expected:** Clear error message with installation instructions - **Type:** System test

.. test:: Dependency Check Failure
   :id: TC-INSTALL-006
   :status: approved
   :tags: deploy, installation, dependencies, error-handling
   :tests: FR-DEPLOY-032, FR-DEPLOY-036
   :priority: high

   Verify clear error message for missing dependencies

--------------

3.7 CLI Interface (FR-5.1 to FR-5.5)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**TC-060: Prep Command - Default Manifest** - **Input:** ``airgap-deploy prep`` with AirGapDeploy.toml in current dir - **Expected:** Package created successfully - **Type:** Integration test

.. test:: Prep Command - Default Manifest
   :id: TC-CLI-001
   :status: approved
   :tags: deploy, cli, prep
   :tests: FR-DEPLOY-037
   :priority: high

   Verify prep command with default manifest

**TC-061: Prep Command - Custom Manifest** - **Input:** ``airgap-deploy prep --manifest custom.toml`` - **Expected:** Uses custom.toml - **Type:** Integration test

.. test:: Prep Command - Custom Manifest
   :id: TC-CLI-002
   :status: approved
   :tags: deploy, cli, prep
   :tests: FR-DEPLOY-037
   :priority: high

   Verify prep command with custom manifest path

**TC-062: Prep Command - Dry Run** - **Input:** ``airgap-deploy prep --dry-run`` - **Expected:** Shows what would be done, no files created - **Type:** Integration test

.. test:: Prep Command - Dry Run
   :id: TC-CLI-003
   :status: approved
   :tags: deploy, cli, prep, dry-run
   :tests: FR-DEPLOY-037
   :priority: medium

   Verify dry run mode shows plan without executing

**TC-063: Validate Command** - **Input:** ``airgap-deploy validate`` with valid manifest - **Expected:** "Manifest is valid" message - **Type:** Integration test

.. test:: Validate Command
   :id: TC-CLI-004
   :status: approved
   :tags: deploy, cli, validate
   :tests: FR-DEPLOY-037
   :priority: high

   Verify validate command checks manifest

**TC-064: Init Command** - **Input:** ``airgap-deploy init --type rust-app`` - **Expected:** AirGapDeploy.toml template created - **Type:** Integration test

.. test:: Init Command
   :id: TC-CLI-005
   :status: approved
   :tags: deploy, cli, init
   :tests: FR-DEPLOY-037
   :priority: medium

   Verify init command creates template

**TC-065: List Components Command** - **Input:** ``airgap-deploy list-components`` - **Expected:** Lists rust-app, external-binary, model-file - **Type:** Integration test

.. test:: List Components Command
   :id: TC-CLI-006
   :status: approved
   :tags: deploy, cli, list
   :tests: FR-DEPLOY-037
   :priority: low

   Verify list-components command displays available types

**TC-066: Help Flag** - **Input:** ``airgap-deploy --help`` - **Expected:** Usage information displayed - **Type:** Integration test

.. test:: Help Flag
   :id: TC-CLI-007
   :status: approved
   :tags: deploy, cli, help
   :tests: FR-DEPLOY-041
   :priority: high

   Verify --help flag displays usage information

--------------

3.8 Error Handling (FR-7.1 to FR-7.4)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**TC-070: Network Error with Retry** - **Input:** Download with intermittent network failure - **Expected:** Retry up to 3 times, eventual success or clear error - **Type:** Integration test

.. test:: Network Error with Retry
   :id: TC-ERR-001
   :status: approved
   :tags: deploy, error-handling, network, reliability
   :tests: NFR-DEPLOY-006, FR-DEPLOY-046
   :priority: high

   Verify retry logic for network errors

**TC-071: Disk Space Error** - **Input:** Insufficient disk space for package - **Expected:** Clear error message with space required/available - **Type:** System test

.. test:: Disk Space Error
   :id: TC-ERR-002
   :status: approved
   :tags: deploy, error-handling, disk-space
   :tests: FR-DEPLOY-035, FR-DEPLOY-045
   :priority: high

   Verify clear error for insufficient disk space

**TC-072: Permission Error** - **Input:** Write to directory without permissions - **Expected:** Clear error message about permissions - **Type:** System test

.. test:: Permission Error
   :id: TC-ERR-003
   :status: approved
   :tags: deploy, error-handling, permissions
   :tests: FR-DEPLOY-045
   :priority: medium

   Verify clear error for permission issues

**TC-073: Invalid Platform** - **Input:** ``--target unknown-platform`` - **Expected:** Error listing valid platforms - **Type:** Unit test

.. test:: Invalid Platform
   :id: TC-ERR-004
   :status: approved
   :tags: deploy, error-handling, platform
   :tests: FR-DEPLOY-045
   :priority: medium

   Verify error for invalid platform target

--------------

3.9 End-to-End Workflows
~~~~~~~~~~~~~~~~~~~~~~~~

**TC-100: AirGap Whisper Deployment (Reference Implementation)** - **Input:** AirGap Whisper AirGapDeploy.toml - **Expected:** 1. Package created successfully 2. Transfer to air-gapped VM 3. Install script runs successfully 4. AirGap Whisper binary functional - **Type:** System test - **Environment:** Ubuntu 22.04 air-gapped VM

.. test:: AirGap Whisper End-to-End Deployment
   :id: TC-E2E-001
   :status: approved
   :tags: deploy, e2e, airgap-whisper, system
   :tests: UC-DEPLOY-001
   :priority: critical

   Verify complete AirGap Whisper deployment workflow from package creation to functional installation on air-gapped system

**TC-101: Ollama Deployment with Large Models** - **Input:** Ollama manifest with 3 models (20GB total) - **Expected:** 1. Package created (may take 30+ min) 2. Package > 16GB (test large package handling) 3. Install script generated correctly - **Type:** System test - **Environment:** Development machine with fast internet

.. test:: Ollama Large Model Deployment
   :id: TC-E2E-002
   :status: approved
   :tags: deploy, e2e, ollama, large-package, system
   :tests: UC-DEPLOY-002, NFR-DEPLOY-026
   :priority: high

   Verify Ollama deployment with multiple large models (20GB+ total)

**TC-102: Multi-Platform Build** - **Input:** Same manifest, build for linux, macos, windows - **Expected:** Three platform-specific packages created - **Type:** Integration test - **Environment:** CI matrix (Linux runner creates Linux package, etc.)

.. test:: Multi-Platform Build
   :id: TC-E2E-003
   :status: approved
   :tags: deploy, e2e, multi-platform, portability
   :tests: NFR-DEPLOY-017, NFR-DEPLOY-018, NFR-DEPLOY-019
   :priority: high

   Verify same manifest builds packages for all platforms

--------------

3.10 Performance Tests
~~~~~~~~~~~~~~~~~~~~~~

**TC-110: Package Preparation Time** - **Input:** Typical application (<1GB components) - **Expected:** Package created in < 5 minutes - **Type:** Performance test - **Metric:** NFR-1.1

.. test:: Package Preparation Time
   :id: TC-PERF-001
   :status: approved
   :tags: deploy, performance, packaging
   :tests: NFR-DEPLOY-001
   :priority: medium

   Verify package preparation completes within 5 minutes for typical applications

**TC-111: Large Model Download** - **Input:** 5GB model file - **Expected:** Download with progress, memory usage < 100MB - **Type:** Performance test - **Metric:** NFR-1.2

.. test:: Large Model Download Performance
   :id: TC-PERF-002
   :status: approved
   :tags: deploy, performance, download, memory
   :tests: NFR-DEPLOY-002
   :priority: high

   Verify large model download with progress display and low memory usage

**TC-112: Parallel Component Collection** - **Input:** Manifest with 4 independent components - **Expected:** Collection time < sequential time (50-70% faster) - **Type:** Performance test - **Metric:** NFR-1.3

.. test:: Parallel Component Collection
   :id: TC-PERF-003
   :status: approved
   :tags: deploy, performance, parallelism
   :tests: NFR-DEPLOY-003
   :priority: medium

   Verify parallel collection improves performance

**TC-113: Installation Script Execution** - **Input:** Generated install script for typical app - **Expected:** Installation completes in < 20 minutes - **Type:** Performance test - **Metric:** NFR-1.4

.. test:: Installation Script Performance
   :id: TC-PERF-004
   :status: approved
   :tags: deploy, performance, installation
   :tests: NFR-DEPLOY-004
   :priority: medium

   Verify installation completes within 20 minutes

--------------

3.11 Security Tests
~~~~~~~~~~~~~~~~~~~

**TC-120: Checksum Verification Prevents Corruption** - **Input:** Downloaded file with corrupted bytes - **Expected:** Checksum verification fails, error reported - **Type:** Security test - **Metric:** NFR-6.1

.. test:: Checksum Verification Prevents Corruption
   :id: TC-DEPLOY-SEC-001
   :status: approved
   :tags: deploy, security, checksum, verification
   :tests: NFR-DEPLOY-021
   :priority: critical

   Verify checksum verification detects corrupted files

**TC-121: No Arbitrary Code Execution** - **Input:** Manifest with malicious build command attempt - **Expected:** Command is templated string, not executed during prep - **Type:** Security test - **Metric:** NFR-6.2

.. test:: No Arbitrary Code Execution
   :id: TC-DEPLOY-SEC-002
   :status: approved
   :tags: deploy, security, code-execution
   :tests: NFR-DEPLOY-022
   :priority: critical

   Verify manifest cannot execute arbitrary code during prep phase

**TC-122: HTTPS for Downloads** - **Input:** Model file URL with HTTP (not HTTPS) - **Expected:** Error or automatic upgrade to HTTPS - **Type:** Security test - **Metric:** NFR-6.4

.. test:: HTTPS for Downloads
   :id: TC-DEPLOY-SEC-003
   :status: approved
   :tags: deploy, security, network, https
   :tests: NFR-DEPLOY-024
   :priority: high

   Verify all downloads use HTTPS

**TC-123: Temporary File Permissions** - **Input:** Create temporary file during collection - **Expected:** File has user-only permissions (0600 on Unix) - **Type:** Security test - **Metric:** NFR-6.5

.. test:: Temporary File Permissions
   :id: TC-DEPLOY-SEC-004
   :status: approved
   :tags: deploy, security, permissions, filesystem
   :tests: NFR-DEPLOY-025
   :priority: high

   Verify temporary files have restrictive permissions

--------------

4. Test Execution
-----------------

4.1 Unit Tests
~~~~~~~~~~~~~~

.. code:: bash

   # Run all unit tests
   cargo test --lib

   # Run with coverage
   cargo tarpaulin --out Html

   # Target: 80%+ coverage

4.2 Integration Tests
~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

   # Run integration tests
   cargo test --test '*'

   # Run specific integration test
   cargo test --test e2e_whisper_deployment

4.3 CI/CD Testing
~~~~~~~~~~~~~~~~~

.. code:: yaml

   # .github/workflows/test.yml
   name: Tests

   on: [push, pull_request]

   jobs:
     test:
       strategy:
         matrix:
           os: [ubuntu-latest, macos-latest, windows-latest]
           rust: [stable, beta]
       runs-on: ${{ matrix.os }}
       steps:
         - uses: actions/checkout@v4
         - uses: dtolnay/rust-toolchain@${{ matrix.rust }}
         - run: cargo test --all-features
         - run: cargo clippy -- -D warnings
         - run: cargo fmt --check

4.4 Air-Gapped VM Testing
~~~~~~~~~~~~~~~~~~~~~~~~~

**Setup:**

.. code:: bash

   # Create Ubuntu 22.04 VM in VirtualBox
   # Disable network adapter
   # Install basic build tools (gcc, make)

   # Transfer package via shared folder
   # Run install script
   # Verify installation

--------------

5. Test Metrics
---------------

5.1 Coverage Metrics
~~~~~~~~~~~~~~~~~~~~

===================== ====== ===============
Metric                Target Measurement
===================== ====== ===============
**Line coverage**     80%+   cargo tarpaulin
**Branch coverage**   75%+   cargo tarpaulin
**Function coverage** 90%+   cargo tarpaulin
===================== ====== ===============

5.2 Quality Metrics
~~~~~~~~~~~~~~~~~~~

========================== ================ ================
Metric                     Target           Measurement
========================== ================ ================
**Clippy warnings**        0                cargo clippy
**Formatting issues**      0                cargo fmt –check
**Documentation coverage** 100% public APIs cargo doc
========================== ================ ================

5.3 Performance Metrics
~~~~~~~~~~~~~~~~~~~~~~~

========================= ======== =========
Metric                    Target   Test Case
========================= ======== =========
**Package prep time**     < 5 min  TC-110
**Large download memory** < 100 MB TC-111
**Install time**          < 20 min TC-113
========================= ======== =========

--------------

6. Test Schedule
----------------

Phase 1: Core Infrastructure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- TC-001 to TC-005 (Manifest parsing)
- Unit tests for core types

Phase 2: Built-in Components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- TC-010 to TC-013 (RustApp)
- TC-020 to TC-023 (ExternalBinary)
- TC-030 to TC-035 (ModelFile)

Phase 3: Packaging
~~~~~~~~~~~~~~~~~~

- TC-040 to TC-044 (Packaging)

Phase 4: Install Scripts
~~~~~~~~~~~~~~~~~~~~~~~~

- TC-050 to TC-055 (Install scripts)

Phase 5: CLI
~~~~~~~~~~~~

- TC-060 to TC-066 (CLI interface)

Phase 6: Integration & System
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- TC-070 to TC-073 (Error handling)
- TC-100 to TC-102 (End-to-end workflows)
- TC-110 to TC-113 (Performance)
- TC-120 to TC-123 (Security)

--------------

7. Defect Management
--------------------

7.1 Severity Levels
~~~~~~~~~~~~~~~~~~~

+---------------------+-------------------------------+-----------------------------+
| Severity            | Description                   | Example                     |
+=====================+===============================+=============================+
| **Critical**        | Blocks development/deployment | Package creation fails      |
+---------------------+-------------------------------+-----------------------------+
| **High**            | Major functionality broken    | Checksum verification fails |
+---------------------+-------------------------------+-----------------------------+
| **Medium**          | Feature impaired              | Progress bar doesn’t show   |
+---------------------+-------------------------------+-----------------------------+
| **Low**             | Minor issue                   | Typo in help text           |
+---------------------+-------------------------------+-----------------------------+

7.2 Defect Tracking
~~~~~~~~~~~~~~~~~~~

- Use GitHub Issues
- Label with severity (critical, high, medium, low)
- Tag with affected component
- Link to failing test case

--------------

8. Test Deliverables
--------------------

8.1 Test Code
~~~~~~~~~~~~~

- ``tests/`` directory with all test files
- ``tests/fixtures/`` with test manifests and data
- ``benches/`` with performance benchmarks

8.2 Test Reports
~~~~~~~~~~~~~~~~

- CI test results (GitHub Actions)
- Coverage reports (HTML from tarpaulin)
- Performance benchmark results

8.3 Test Documentation
~~~~~~~~~~~~~~~~~~~~~~

- This test plan
- Test case documentation (inline in test code)
- Testing guide for contributors

--------------

9. Risks and Mitigation
-----------------------

+-------------------------------+---------------------+---------------------------------------------+
| Risk                          | Impact              | Mitigation                                  |
+===============================+=====================+=============================================+
| Network-dependent tests flaky | High                | Mock network calls, use test fixtures       |
+-------------------------------+---------------------+---------------------------------------------+
| Platform-specific bugs        | Medium              | CI matrix with all platforms                |
+-------------------------------+---------------------+---------------------------------------------+
| Large file tests slow         | Medium              | Use smaller test files, separate slow tests |
+-------------------------------+---------------------+---------------------------------------------+
| Air-gapped VM setup complex   | Low                 | Document setup, provide VM image            |
+-------------------------------+---------------------+---------------------------------------------+

--------------

10. Approval
------------

Test plan will be approved when:

- ✅ All test cases defined
- ✅ CI/CD pipeline configured
- ✅ Test environment documented
- ✅ Coverage targets set
- ✅ Ready to begin testing during implementation

**Status:** ✅ Test Plan Complete - Ready for implementation

--------------

Requirements Traceability
-------------------------

This section demonstrates bidirectional traceability between requirements and test cases for AirGap Deploy.

Requirements to Tests Matrix
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following table shows all requirements and their associated test cases.

.. needtable::
   :types: req, nfreq, test
   :columns: id, title, status, type
   :filter: "deploy" in tags
   :style: table

Requirements Coverage
~~~~~~~~~~~~~~~~~~~~~

This table shows only requirements for AirGap Deploy.

.. needtable::
   :types: req, nfreq
   :columns: id, title, priority, status
   :filter: "deploy" in tags
   :style: table

.. note::

   To see which tests validate each requirement, refer to the Requirements to Tests Matrix above, or check the individual test case definitions throughout this document.

Test Cases
~~~~~~~~~~

This table lists all test cases with their validation links.

.. needtable::
   :types: test
   :columns: id, title, priority, status, tests
   :filter: "deploy" in tags
   :style: table

The "Tests" column shows which requirements each test case validates (via the :tests: link).

--------------

**End of Test Plan**
