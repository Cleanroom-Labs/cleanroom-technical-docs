Test Plan
=========

airgap-deploy
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

**TC-002: Invalid Manifest - Missing Required Field** - **Input:** TOML missing ``package.name`` - **Expected:** Parse error with clear message indicating missing field - **Type:** Unit test

**TC-003: Invalid Manifest - Wrong Type** - **Input:** ``package.version`` is integer, not string - **Expected:** Parse error with type mismatch message - **Type:** Unit test

**TC-004: Unsupported Component Type** - **Input:** Component with ``type = "unknown-type"`` - **Expected:** Validation error listing supported types - **Type:** Unit test

**TC-005: Schema Versioning** - **Input:** Manifest with future schema version - **Expected:** Warning about version mismatch, attempt to parse - **Type:** Unit test

--------------

3.2 RustAppComponent (FR-2.1 to FR-2.5)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**TC-010: Rust App with Vendoring** - **Input:** Rust project with dependencies - **Expected:** ``cargo vendor`` executed, .cargo/config.toml generated - **Type:** Integration test

**TC-011: Rust Toolchain Inclusion** - **Input:** RustApp with ``include_toolchain = true`` - **Expected:** Rust installer downloaded and included in package - **Type:** Integration test

**TC-012: Missing Cargo.toml** - **Input:** Directory without Cargo.toml - **Expected:** Error indicating Cargo.toml not found - **Type:** Unit test

**TC-013: Cargo Vendor Failure** - **Input:** Rust project with invalid dependencies - **Expected:** Error with cargo vendor output - **Type:** Integration test

--------------

3.3 ExternalBinaryComponent (FR-2.6 to FR-2.9)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**TC-020: Git Repository Cloning** - **Input:** Valid GitHub repository URL with tag - **Expected:** Repository cloned, tag checked out - **Type:** Integration test

**TC-021: Git Branch Checkout** - **Input:** Repository with ``branch = "main"`` - **Expected:** Main branch checked out - **Type:** Integration test

**TC-022: Invalid Repository URL** - **Input:** Non-existent Git repository - **Expected:** Error indicating repository not found - **Type:** Integration test

**TC-023: Network Failure During Clone** - **Input:** Git clone with simulated network failure - **Expected:** Retry up to 3 times, clear error message - **Type:** Integration test

--------------

3.4 ModelFileComponent (FR-2.10 to FR-2.14)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**TC-030: Model File Download** - **Input:** URL to downloadable file with checksum - **Expected:** File downloaded, checksum verified - **Type:** Integration test

**TC-031: Checksum Verification Success** - **Input:** Downloaded file with matching checksum - **Expected:** Verification passes - **Type:** Unit test

**TC-032: Checksum Verification Failure** - **Input:** Downloaded file with mismatched checksum - **Expected:** Error with expected/actual checksums, file deleted - **Type:** Unit test

**TC-033: Download Resume** - **Input:** Partially downloaded file, resume download - **Expected:** Download continues from partial point - **Type:** Integration test

**TC-034: Large File Download (1GB+)** - **Input:** Large model file - **Expected:** Progress bar displayed, streaming to disk, low memory usage - **Type:** Performance test

**TC-035: Download Cache Hit** - **Input:** File already in cache with matching checksum - **Expected:** Skip download, use cached file - **Type:** Integration test

--------------

3.5 Packaging (FR-3.1 to FR-3.6)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**TC-040: Create tar.gz Package (Linux/macOS)** - **Input:** Collected components, target platform = linux-x86_64 - **Expected:** tar.gz archive created with correct structure - **Type:** Integration test

**TC-041: Create zip Package (Windows)** - **Input:** Collected components, target platform = windows-x86_64 - **Expected:** zip archive created with correct structure - **Type:** Integration test

**TC-042: Package Metadata Generation** - **Input:** Package with multiple components - **Expected:** airgap-deploy-metadata.json with all components listed - **Type:** Unit test

**TC-043: Package Checksum Generation** - **Input:** Created package - **Expected:** SHA-256 checksum file created - **Type:** Unit test

**TC-044: Large Package (10GB+)** - **Input:** Multiple large model files - **Expected:** Package created successfully, memory usage stable - **Type:** Performance test

--------------

3.6 Install Script Generation (FR-4.1 to FR-4.7)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**TC-050: Bash Script Generation** - **Input:** Components with install steps - **Expected:** install.sh with dependency checks, build commands - **Type:** Unit test

**TC-051: PowerShell Script Generation** - **Input:** Components with install steps - **Expected:** install.ps1 with equivalent logic - **Type:** Unit test

**TC-052: Interactive Mode Prompts** - **Input:** Install script with ``mode = "interactive"`` - **Expected:** Script prompts for installation location - **Type:** Integration test

**TC-053: Automatic Mode** - **Input:** Install script run with ``MODE=automatic`` - **Expected:** No prompts, uses environment variables - **Type:** Integration test

**TC-054: Dependency Check Success** - **Input:** System with all required dependencies - **Expected:** Script proceeds to installation - **Type:** System test

**TC-055: Dependency Check Failure** - **Input:** System missing C compiler - **Expected:** Clear error message with installation instructions - **Type:** System test

--------------

3.7 CLI Interface (FR-5.1 to FR-5.5)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**TC-060: Prep Command - Default Manifest** - **Input:** ``airgap-deploy prep`` with AirGapDeploy.toml in current dir - **Expected:** Package created successfully - **Type:** Integration test

**TC-061: Prep Command - Custom Manifest** - **Input:** ``airgap-deploy prep --manifest custom.toml`` - **Expected:** Uses custom.toml - **Type:** Integration test

**TC-062: Prep Command - Dry Run** - **Input:** ``airgap-deploy prep --dry-run`` - **Expected:** Shows what would be done, no files created - **Type:** Integration test

**TC-063: Validate Command** - **Input:** ``airgap-deploy validate`` with valid manifest - **Expected:** “Manifest is valid” message - **Type:** Integration test

**TC-064: Init Command** - **Input:** ``airgap-deploy init --type rust-app`` - **Expected:** AirGapDeploy.toml template created - **Type:** Integration test

**TC-065: List Components Command** - **Input:** ``airgap-deploy list-components`` - **Expected:** Lists rust-app, external-binary, model-file - **Type:** Integration test

**TC-066: Help Flag** - **Input:** ``airgap-deploy --help`` - **Expected:** Usage information displayed - **Type:** Integration test

--------------

3.8 Error Handling (FR-7.1 to FR-7.4)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**TC-070: Network Error with Retry** - **Input:** Download with intermittent network failure - **Expected:** Retry up to 3 times, eventual success or clear error - **Type:** Integration test

**TC-071: Disk Space Error** - **Input:** Insufficient disk space for package - **Expected:** Clear error message with space required/available - **Type:** System test

**TC-072: Permission Error** - **Input:** Write to directory without permissions - **Expected:** Clear error message about permissions - **Type:** System test

**TC-073: Invalid Platform** - **Input:** ``--target unknown-platform`` - **Expected:** Error listing valid platforms - **Type:** Unit test

--------------

3.9 End-to-End Workflows
~~~~~~~~~~~~~~~~~~~~~~~~

**TC-100: AirGap Whisper Deployment (Reference Implementation)** - **Input:** AirGap Whisper AirGapDeploy.toml - **Expected:** 1. Package created successfully 2. Transfer to air-gapped VM 3. Install script runs successfully 4. AirGap Whisper binary functional - **Type:** System test - **Environment:** Ubuntu 22.04 air-gapped VM

**TC-101: Ollama Deployment with Large Models** - **Input:** Ollama manifest with 3 models (20GB total) - **Expected:** 1. Package created (may take 30+ min) 2. Package > 16GB (test large package handling) 3. Install script generated correctly - **Type:** System test - **Environment:** Development machine with fast internet

**TC-102: Multi-Platform Build** - **Input:** Same manifest, build for linux, macos, windows - **Expected:** Three platform-specific packages created - **Type:** Integration test - **Environment:** CI matrix (Linux runner creates Linux package, etc.)

--------------

3.10 Performance Tests
~~~~~~~~~~~~~~~~~~~~~~

**TC-110: Package Preparation Time** - **Input:** Typical application (<1GB components) - **Expected:** Package created in < 5 minutes - **Type:** Performance test - **Metric:** NFR-1.1

**TC-111: Large Model Download** - **Input:** 5GB model file - **Expected:** Download with progress, memory usage < 100MB - **Type:** Performance test - **Metric:** NFR-1.2

**TC-112: Parallel Component Collection** - **Input:** Manifest with 4 independent components - **Expected:** Collection time < sequential time (50-70% faster) - **Type:** Performance test - **Metric:** NFR-1.3

**TC-113: Installation Script Execution** - **Input:** Generated install script for typical app - **Expected:** Installation completes in < 20 minutes - **Type:** Performance test - **Metric:** NFR-1.4

--------------

3.11 Security Tests
~~~~~~~~~~~~~~~~~~~

**TC-120: Checksum Verification Prevents Corruption** - **Input:** Downloaded file with corrupted bytes - **Expected:** Checksum verification fails, error reported - **Type:** Security test - **Metric:** NFR-6.1

**TC-121: No Arbitrary Code Execution** - **Input:** Manifest with malicious build command attempt - **Expected:** Command is templated string, not executed during prep - **Type:** Security test - **Metric:** NFR-6.2

**TC-122: HTTPS for Downloads** - **Input:** Model file URL with HTTP (not HTTPS) - **Expected:** Error or automatic upgrade to HTTPS - **Type:** Security test - **Metric:** NFR-6.4

**TC-123: Temporary File Permissions** - **Input:** Create temporary file during collection - **Expected:** File has user-only permissions (0600 on Unix) - **Type:** Security test - **Metric:** NFR-6.5

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

**End of Test Plan**
