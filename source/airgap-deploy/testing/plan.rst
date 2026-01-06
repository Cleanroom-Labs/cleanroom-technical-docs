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

- :doc:`Requirements (SRS) <../requirements/srs>`
- :doc:`Design (SDD) <../design/sdd>`
- :doc:`Roadmap <../roadmap>`
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

.. test:: Valid Manifest Parsing
   :id: TC-MAN-001
   :status: approved
   :tags: deploy, manifest, parsing
   :tests: FR-DEPLOY-001
   :priority: high

   Verify valid AirGapDeploy.toml parses successfully

.. test:: Invalid Manifest - Missing Required Field
   :id: TC-MAN-002
   :status: approved
   :tags: deploy, manifest, validation, error-handling
   :tests: FR-DEPLOY-002, FR-DEPLOY-004
   :priority: high

   Verify parse error when required field missing

.. test:: Invalid Manifest - Wrong Type
   :id: TC-MAN-003
   :status: approved
   :tags: deploy, manifest, validation, error-handling
   :tests: FR-DEPLOY-002, FR-DEPLOY-004
   :priority: high

   Verify parse error on type mismatch

.. test:: Unsupported Component Type
   :id: TC-MAN-004
   :status: approved
   :tags: deploy, manifest, validation, component
   :tests: FR-DEPLOY-002, FR-DEPLOY-004
   :priority: medium

   Verify validation error for unknown component type

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

.. test:: Rust App with Vendoring
   :id: TC-RUST-001
   :status: approved
   :tags: deploy, rust, vendor
   :tests: FR-DEPLOY-007, FR-DEPLOY-009
   :priority: high

   Verify cargo vendor and config generation

.. test:: Rust Toolchain Inclusion
   :id: TC-RUST-002
   :status: approved
   :tags: deploy, rust, toolchain
   :tests: FR-DEPLOY-008
   :priority: medium

   Verify Rust installer download and inclusion

.. test:: Missing Cargo.toml
   :id: TC-RUST-003
   :status: approved
   :tags: deploy, rust, error-handling
   :tests: FR-DEPLOY-006, FR-DEPLOY-045
   :priority: medium

   Verify error when Cargo.toml not found

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

.. test:: Git Repository Cloning
   :id: TC-GIT-001
   :status: approved
   :tags: deploy, git, clone
   :tests: FR-DEPLOY-011, FR-DEPLOY-012
   :priority: high

   Verify Git repository cloning with tag checkout

.. test:: Git Branch Checkout
   :id: TC-GIT-002
   :status: approved
   :tags: deploy, git, branch
   :tests: FR-DEPLOY-012
   :priority: high

   Verify Git branch checkout

.. test:: Invalid Repository URL
   :id: TC-GIT-003
   :status: approved
   :tags: deploy, git, error-handling
   :tests: FR-DEPLOY-011, FR-DEPLOY-045
   :priority: medium

   Verify error for invalid repository URL

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

.. test:: Model File Download
   :id: TC-MODEL-001
   :status: approved
   :tags: deploy, model, download
   :tests: FR-DEPLOY-015, FR-DEPLOY-016
   :priority: high

   Verify model file download with checksum verification

.. test:: Checksum Verification Success
   :id: TC-MODEL-002
   :status: approved
   :tags: deploy, model, verification, security
   :tests: FR-DEPLOY-016, NFR-DEPLOY-005
   :priority: high

   Verify checksum verification passes for matching checksum

.. test:: Checksum Verification Failure
   :id: TC-MODEL-003
   :status: approved
   :tags: deploy, model, verification, security, error-handling
   :tests: FR-DEPLOY-016, NFR-DEPLOY-005, FR-DEPLOY-045
   :priority: high

   Verify error and file deletion on checksum mismatch

.. test:: Download Resume
   :id: TC-MODEL-004
   :status: approved
   :tags: deploy, model, download, reliability
   :tests: FR-DEPLOY-018
   :priority: medium

   Verify download resume capability

.. test:: Large File Download
   :id: TC-MODEL-005
   :status: approved
   :tags: deploy, model, download, performance
   :tests: FR-DEPLOY-017, NFR-DEPLOY-002
   :priority: high

   Verify large file download with progress display

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

.. test:: Create tar.gz Package
   :id: TC-PKG-001
   :status: approved
   :tags: deploy, packaging, archive, linux, macos
   :tests: FR-DEPLOY-024, FR-DEPLOY-026
   :priority: high

   Verify tar.gz archive creation with correct structure

.. test:: Create zip Package
   :id: TC-PKG-002
   :status: approved
   :tags: deploy, packaging, archive, windows
   :tests: FR-DEPLOY-025, FR-DEPLOY-026
   :priority: high

   Verify zip archive creation for Windows

.. test:: Package Metadata Generation
   :id: TC-PKG-003
   :status: approved
   :tags: deploy, packaging, metadata
   :tests: FR-DEPLOY-027
   :priority: high

   Verify metadata file generation

.. test:: Package Checksum Generation
   :id: TC-PKG-004
   :status: approved
   :tags: deploy, packaging, checksum, security
   :tests: FR-DEPLOY-028, NFR-DEPLOY-005
   :priority: high

   Verify package checksum generation

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

.. test:: Bash Script Generation
   :id: TC-INSTALL-001
   :status: approved
   :tags: deploy, installation, bash, linux, macos
   :tests: FR-DEPLOY-030, FR-DEPLOY-032
   :priority: high

   Verify Bash installation script generation

.. test:: PowerShell Script Generation
   :id: TC-INSTALL-002
   :status: approved
   :tags: deploy, installation, powershell, windows
   :tests: FR-DEPLOY-031, FR-DEPLOY-032
   :priority: high

   Verify PowerShell installation script generation

.. test:: Interactive Mode Prompts
   :id: TC-INSTALL-003
   :status: approved
   :tags: deploy, installation, interactive
   :tests: FR-DEPLOY-033
   :priority: high

   Verify interactive mode prompts user

.. test:: Automatic Mode
   :id: TC-INSTALL-004
   :status: approved
   :tags: deploy, installation, automatic
   :tests: FR-DEPLOY-033
   :priority: high

   Verify automatic unattended installation

.. test:: Dependency Check Success
   :id: TC-INSTALL-005
   :status: approved
   :tags: deploy, installation, dependencies
   :tests: FR-DEPLOY-032
   :priority: high

   Verify dependency check passes when all present

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

.. test:: Prep Command - Default Manifest
   :id: TC-CLI-001
   :status: approved
   :tags: deploy, cli, prep
   :tests: FR-DEPLOY-037
   :priority: high

   Verify prep command with default manifest

.. test:: Prep Command - Custom Manifest
   :id: TC-CLI-002
   :status: approved
   :tags: deploy, cli, prep
   :tests: FR-DEPLOY-037
   :priority: high

   Verify prep command with custom manifest path

.. test:: Prep Command - Dry Run
   :id: TC-CLI-003
   :status: approved
   :tags: deploy, cli, prep, dry-run
   :tests: FR-DEPLOY-037
   :priority: medium

   Verify dry run mode shows plan without executing

.. test:: Validate Command
   :id: TC-CLI-004
   :status: approved
   :tags: deploy, cli, validate
   :tests: FR-DEPLOY-037
   :priority: high

   Verify validate command checks manifest

.. test:: Init Command
   :id: TC-CLI-005
   :status: approved
   :tags: deploy, cli, init
   :tests: FR-DEPLOY-037
   :priority: medium

   Verify init command creates template

.. test:: List Components Command
   :id: TC-CLI-006
   :status: approved
   :tags: deploy, cli, list
   :tests: FR-DEPLOY-037
   :priority: low

   Verify list-components command displays available types

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

.. test:: Network Error with Retry
   :id: TC-ERR-001
   :status: approved
   :tags: deploy, error-handling, network, reliability
   :tests: NFR-DEPLOY-006, FR-DEPLOY-046
   :priority: high

   Verify retry logic for network errors

.. test:: Disk Space Error
   :id: TC-ERR-002
   :status: approved
   :tags: deploy, error-handling, disk-space
   :tests: FR-DEPLOY-035, FR-DEPLOY-045
   :priority: high

   Verify clear error for insufficient disk space

.. test:: Permission Error
   :id: TC-ERR-003
   :status: approved
   :tags: deploy, error-handling, permissions
   :tests: FR-DEPLOY-045
   :priority: medium

   Verify clear error for permission issues

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

.. test:: AirGap Whisper End-to-End Deployment
   :id: TC-E2E-001
   :status: approved
   :tags: deploy, e2e, airgap-whisper, system
   :tests: UC-DEPLOY-001
   :priority: critical

   Verify complete AirGap Whisper deployment workflow from package creation to functional installation on air-gapped system

.. test:: Ollama Large Model Deployment
   :id: TC-E2E-002
   :status: approved
   :tags: deploy, e2e, ollama, large-package, system
   :tests: UC-DEPLOY-002, NFR-DEPLOY-026
   :priority: high

   Verify Ollama deployment with multiple large models (20GB+ total)

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

.. test:: Package Preparation Time
   :id: TC-PERF-001
   :status: approved
   :tags: deploy, performance, packaging
   :tests: NFR-DEPLOY-001
   :priority: medium

   Verify package preparation completes within 5 minutes for typical applications

.. test:: Large Model Download Performance
   :id: TC-PERF-002
   :status: approved
   :tags: deploy, performance, download, memory
   :tests: NFR-DEPLOY-002
   :priority: high

   Verify large model download with progress display and low memory usage

.. test:: Parallel Component Collection
   :id: TC-PERF-003
   :status: approved
   :tags: deploy, performance, parallelism
   :tests: NFR-DEPLOY-003
   :priority: medium

   Verify parallel collection improves performance

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

.. test:: Checksum Verification Prevents Corruption
   :id: TC-DEPLOY-SEC-001
   :status: approved
   :tags: deploy, security, checksum, verification
   :tests: NFR-DEPLOY-021
   :priority: critical

   Verify checksum verification detects corrupted files

.. test:: No Arbitrary Code Execution
   :id: TC-DEPLOY-SEC-002
   :status: approved
   :tags: deploy, security, code-execution
   :tests: NFR-DEPLOY-022
   :priority: critical

   Verify manifest cannot execute arbitrary code during prep phase

.. test:: HTTPS for Downloads
   :id: TC-DEPLOY-SEC-003
   :status: approved
   :tags: deploy, security, network, https
   :tests: NFR-DEPLOY-024
   :priority: high

   Verify all downloads use HTTPS

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

The following table shows all requirements and their associated test cases. The "Incoming" column shows which tests validate each requirement.

.. needtable::
   :types: req, nfreq
   :columns: id, title, status, incoming
   :filter: "deploy" in tags
   :style: table

Requirements Coverage Statistics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This table provides an overview of all AirGap Deploy requirements with their priority and status.

.. needtable::
   :types: req, nfreq
   :columns: id, title, priority, status
   :filter: "deploy" in tags
   :style: table

.. note::

   **Understanding Traceability:**

   - **Incoming links** show which test cases validate each requirement
   - **Tests column** (in test tables below) shows which requirements each test validates
   - This bidirectional linking ensures complete coverage and traceability

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
