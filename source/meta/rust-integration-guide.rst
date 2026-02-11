Rust API Documentation Integration Guide
=========================================

This guide explains how to integrate auto-generated Rust API documentation with the Sphinx documentation system for complete traceability from requirements → design → code → tests.

Overview
--------

The Cleanroom Labs technical documentation uses a multi-layered documentation approach:

- **Requirements** (sphinx-needs ``:req:`` directives)
- **Design** (Software Design Documents)
- **API Reference** (auto-generated from Rust doc comments)
- **Tests** (sphinx-needs ``:test:`` directives)

This creates bidirectional traceability at every level.

.. note::

   This guide describes the integration infrastructure that is configured and ready in the Sphinx build system. The ``:impl:`` directives and Rust API cross-references will be populated as implementation progresses. The patterns documented here are the target workflow for development.

Prerequisites
-------------

Before integrating Rust API docs, ensure:

- Rust code exists with doc comments
- sphinxcontrib-rust installed (already in requirements.txt)
- Rust toolchain available for building docs
- Code repository location known relative to sphinx-docs

Writing Traceable Rust Doc Comments
------------------------------------

Standard Doc Comment Structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Follow this pattern for all public items:

.. code-block:: rust

   /// [One-line summary]
   ///
   /// [Detailed description explaining what this does, how it works,
   /// and any important caveats or usage notes.]
   ///
   /// # Implements
   ///
   /// - [`REQ-ID-001`]: Brief description of requirement
   /// - [`REQ-ID-002`]: Brief description of requirement
   ///
   /// # Errors
   ///
   /// Returns `Err` if [describe error conditions]
   ///
   /// # Example
   ///
   /// ```no_run
   /// # use crate_name::ModuleName;
   /// let instance = ModuleName::new();
   /// instance.do_something()?;
   /// ```
   pub struct ModuleName {
       // ...
   }

Requirement References
~~~~~~~~~~~~~~~~~~~~~~

Always include ``# Implements`` sections that reference requirement IDs:

.. code-block:: rust

   /// Parses AirGapDeploy.toml manifest files.
   ///
   /// # Implements
   ///
   /// - [`FR-DEPLOY-001`]: Parse AirGapDeploy.toml
   /// - [`FR-DEPLOY-002`]: Validate manifest structure
   ///
   pub fn parse_manifest(path: &Path) -> Result<Manifest> {
       // ...
   }

This creates a documentation trail: Requirement → Code → API Doc

Module-Level Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Document modules with file-level comments:

.. code-block:: rust

   //! Audio recording module for Cleanroom Whisper.
   //!
   //! This module provides cross-platform audio capture capabilities
   //! using ALSA (Linux), CoreAudio (macOS), and WASAPI (Windows).
   //!
   //! # Implements
   //!
   //! - [`FR-WHISPER-001`]: Global hotkey toggles recording
   //! - [`FR-WHISPER-002`]: Audio captured at 16kHz mono
   //! - [`FR-WHISPER-003`]: Audio buffered during recording
   //!
   //! # Architecture
   //!
   //! ```text
   //! ┌─────────────────┐
   //! │  HotkeyManager  │
   //! └────────┬────────┘
   //!          │ triggers
   //!          ▼
   //! ┌─────────────────┐
   //! │ AudioRecorder   │
   //! └────────┬────────┘
   //!          │ writes
   //!          ▼
   //! ┌─────────────────┐
   //! │  AudioBuffer    │
   //! └─────────────────┘
   //! ```

   pub mod recorder;
   pub mod buffer;
   pub mod device;

Configuring sphinxcontrib-rust
-------------------------------

Step 1: Update conf.py
~~~~~~~~~~~~~~~~~~~~~~~

The sphinxcontrib-rust extension is already enabled. Configure crate paths:

.. code-block:: python

   # In source/conf.py

   # sphinxcontrib-rust configuration
   rust_crates = {
       # Relative paths from sphinx-docs to Rust project roots
       'cleanroom-whisper': '../../cleanroom-whisper',
       'airgap-deploy': '../../airgap-deploy',
       'airgap-transfer': '../../airgap-transfer',
   }

   # Optional: Configure doc build command
   rust_doc_cmd = 'cargo doc --no-deps --document-private-items'

Step 2: Generate Rust Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Generate Rust docs for each project:

.. code-block:: bash

   # From each Rust project directory
   cd /path/to/cleanroom-whisper
   cargo doc --no-deps --document-private-items

   cd /path/to/airgap-deploy
   cargo doc --no-deps --document-private-items

   cd /path/to/airgap-transfer
   cargo doc --no-deps --document-private-items

This creates HTML documentation in ``target/doc/`` for each crate.

Step 3: Reference Rust Items in RST
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use Rust-specific roles in RST files:

.. code-block:: rst

   The :rust:struct:`Chunker` splits files into fixed-size chunks.

   See :rust:fn:`parse_manifest` for manifest parsing.

   The :rust:trait:`ComponentHandler` defines component behavior.

   Configure settings with :rust:enum:`RecordingMode`.

Available roles:

- ``:rust:struct:`` - Structs
- ``:rust:fn:`` - Functions
- ``:rust:trait:`` - Traits
- ``:rust:enum:`` - Enums
- ``:rust:mod:`` - Modules
- ``:rust:type:`` - Type aliases
- ``:rust:const:`` - Constants
- ``:rust:macro:`` - Macros

Linking Code to Requirements
-----------------------------

Implementation Directives
~~~~~~~~~~~~~~~~~~~~~~~~~

Use ``.. impl::`` directives to link code files to requirements:

.. code-block:: rst

   .. impl:: Audio Recording Implementation
      :id: IMPL-WHISPER-001
      :implements: FR-WHISPER-001, FR-WHISPER-002, FR-WHISPER-003
      :status: implemented
      :location: src/audio/recorder.rs
      :tests: TC-REC-001, TC-REC-002, TC-REC-003

      Implements audio recording using platform-specific APIs.
      See :rust:struct:`AudioRecorder` for API documentation.

This creates the full traceability chain:

::

     Requirement  →  Implementation  →   API Docs    →   Tests
         ↓                  ↓                ↓             ↓
   FR-WHISPER-001 → IMPL-WHISPER-001 → AudioRecorder → TC-REC-001

Updating Traceability Matrix
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once implementations exist, update the traceability matrix to include them:

.. code-block:: rst

   Requirements to Implementation to Tests
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. needtable::
      :types: req, impl, test
      :columns: id, title, outgoing
      :filter: "whisper" in tags

   .. needflow::
      :types: req, impl, test
      :tags: whisper
      :show_link_names:

Building Documentation
-----------------------

Local Build with Rust Docs
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # 1. Generate Rust docs for all projects
   for project in cleanroom-whisper airgap-deploy airgap-transfer; do
       cd /path/to/$project
       cargo doc --no-deps --document-private-items
   done

   # 2. Build Sphinx documentation
   cd /path/to/sphinx-docs
   make html

   # 3. View documentation
   open build/html/index.html

GitHub Actions Integration
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The existing GitHub Actions workflow can be extended to build Rust docs:

.. code-block:: yaml

   - name: Install Rust
     uses: dtolnay/rust-toolchain@stable

   - name: Generate Rust documentation
     run: |
       cd ../cleanroom-whisper && cargo doc --no-deps
       cd ../airgap-deploy && cargo doc --no-deps
       cd ../airgap-transfer && cargo doc --no-deps

   - name: Build Sphinx documentation
     run: make html

Best Practices
--------------

Documentation Quality
~~~~~~~~~~~~~~~~~~~~~

- **Write for users, not compilers:** Explain the "why" not just the "what"
- **Include examples:** Show common usage patterns
- **Document errors:** Explain when and why functions can fail
- **Link to requirements:** Always use ``# Implements`` sections
- **Keep it updated:** Update docs when code changes

Traceability Maintenance
~~~~~~~~~~~~~~~~~~~~~~~~

- **One requirement per implementation:** Don't mix unrelated requirements in one impl directive
- **Update all layers:** When requirements change, update design, code, and tests
- **Verify links:** Use needflow diagrams to visualize traceability
- **Check coverage:** Ensure all requirements have implementations and tests

Code Organization
~~~~~~~~~~~~~~~~~

- **Module per feature:** Organize code by functional area
- **Public API surface:** Only expose what's necessary
- **Internal documentation:** Use ``--document-private-items`` for internal docs
- **Consistent naming:** Match module names to design document sections

Troubleshooting
---------------

Rust Docs Not Appearing
~~~~~~~~~~~~~~~~~~~~~~~~

**Issue:** Rust documentation not showing in Sphinx output

**Solutions:**

- Verify ``rust_crates`` paths in ``conf.py`` are correct
- Ensure ``cargo doc`` completed successfully
- Check that ``target/doc/`` directories exist
- Rebuild with ``make clean && make html``

Broken Cross-References
~~~~~~~~~~~~~~~~~~~~~~~~

**Issue:** ``:rust:struct:`` references show as broken links

**Solutions:**

- Verify the struct name is spelled correctly
- Ensure the struct is ``pub`` (sphinxcontrib-rust only documents public items)
- Check that the crate name matches ``rust_crates`` configuration
- Rebuild Rust docs with ``cargo doc --no-deps``

Missing Requirement Links
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Issue:** ``# Implements`` sections not creating traceability links

**Solutions:**

- Use exact requirement IDs (e.g., ``FR-WHISPER-001`` not ``FR-001``)
- Add ``.. impl::`` directives in RST files to formalize the link
- Update traceability matrix with implementation nodes
- Verify sphinx-needs is processing the impl directives

Examples
--------

Complete Example: Cleanroom Whisper Audio Module
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Rust Code (src/audio/recorder.rs):**

.. code-block:: rust

   //! Audio recording implementation.

   /// Records audio from system microphone.
   ///
   /// Supports start/stop recording via hotkeys with automatic
   /// buffering at 16kHz mono format.
   ///
   /// # Implements
   ///
   /// - [`FR-WHISPER-001`]: Global hotkey toggles recording
   /// - [`FR-WHISPER-002`]: Audio captured at 16kHz mono
   /// - [`FR-WHISPER-003`]: Audio buffered during recording
   ///
   /// # Example
   ///
   /// ```no_run
   /// use cleanroom_whisper::audio::AudioRecorder;
   ///
   /// let recorder = AudioRecorder::new()?;
   /// recorder.start_recording()?;
   /// // ... record audio ...
   /// let buffer = recorder.stop_recording()?;
   /// ```
   pub struct AudioRecorder {
       device: AudioDevice,
       buffer: AudioBuffer,
   }

**RST Documentation (source/cleanroom-whisper/api/audio.rst):**

.. code-block:: rst

   Audio Module
   ============

   .. impl:: Audio Recording Implementation
      :id: IMPL-WHISPER-001
      :implements: FR-WHISPER-001, FR-WHISPER-002, FR-WHISPER-003
      :status: implemented
      :location: src/audio/recorder.rs
      :tests: TC-REC-001, TC-REC-002, TC-REC-003

      Platform-specific audio recording implementation.

   API Reference
   -------------

   .. rust:struct:: AudioRecorder

      Main audio recording interface. See implementation for details.

This creates complete traceability:

- Requirements define what to build
- Design explains how to build it
- Implementation (``IMPL-WHISPER-001``) links code to requirements
- API docs explain how to use it
- Tests validate it works

Summary
-------

The Rust API integration provides:

- ✅ **Bidirectional traceability** from requirements to code
- ✅ **Auto-generated API docs** from Rust doc comments
- ✅ **Searchable cross-references** between Sphinx and Rust docs
- ✅ **Complete documentation** in a single unified system

When implementation begins, this infrastructure is ready to automatically
generate professional API documentation with full requirement traceability.

See Also
--------

- :doc:`cleanroom-whisper:api/index` - Cleanroom Whisper API placeholder
- :doc:`airgap-deploy:api/index` - AirGap Deploy API placeholder
- :doc:`airgap-transfer:api/index` - AirGap Transfer API placeholder
- :doc:`/meta/specification-overview` - Artifact types and traceability overview
- `sphinxcontrib-rust documentation <https://sphinx-contrib-rust.readthedocs.io/>`_
