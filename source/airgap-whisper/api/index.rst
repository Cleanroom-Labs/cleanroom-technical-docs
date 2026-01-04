AirGap Whisper API Reference
==============================

.. note::

   API documentation will be auto-generated from Rust source code once implementation begins.
   This page serves as a placeholder and integration guide for future developers.

Planned Architecture
--------------------

Based on :doc:`/airgap-whisper/design/sdd`, AirGap Whisper will consist of these modules:

Audio Module (``audio``)
~~~~~~~~~~~~~~~~~~~~~~~~~

**Purpose:** Audio capture and recording

**Key Components:**

- ``AudioRecorder`` - Main recording interface
- ``AudioDevice`` - Platform-specific audio device abstraction
- ``AudioBuffer`` - Circular buffer for audio data

**Implements Requirements:** FR-WHISPER-001, FR-WHISPER-002, FR-WHISPER-003

Whisper Module (``whisper``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Purpose:** Integration with whisper.cpp for transcription

**Key Components:**

- ``WhisperEngine`` - Wrapper around whisper.cpp binary
- ``ModelManager`` - Manages available whisper models
- ``TranscriptionJob`` - Represents a transcription task

**Implements Requirements:** FR-WHISPER-004, FR-WHISPER-005, FR-WHISPER-006

Database Module (``db``)
~~~~~~~~~~~~~~~~~~~~~~~~~

**Purpose:** SQLite persistence for transcription history

**Key Components:**

- ``Database`` - SQLite connection and query interface
- ``Transcription`` - Data model for stored transcriptions
- ``HistoryManager`` - CRUD operations for transcription history

**Implements Requirements:** FR-WHISPER-007, FR-WHISPER-008

Tray Module (``tray``)
~~~~~~~~~~~~~~~~~~~~~~~

**Purpose:** System tray interface and hotkey management

**Key Components:**

- ``TrayIcon`` - System tray icon and menu
- ``HotkeyManager`` - Global hotkey registration
- ``Settings`` - User configuration management

**Implements Requirements:** FR-WHISPER-009, FR-WHISPER-010, FR-WHISPER-011

Integration with Sphinx
------------------------

Rust Doc Comment Guidelines
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Write doc comments that reference requirements for traceability:

.. code-block:: rust

   /// Global hotkey manager for recording controls.
   ///
   /// Registers system-wide hotkeys that work even when the application
   /// is not focused. Supports start/stop recording toggle.
   ///
   /// # Implements
   ///
   /// - [`FR-WHISPER-001`]: Global hotkey toggles recording
   /// - [`FR-WHISPER-011`]: Configurable hotkey binding
   ///
   /// # Example
   ///
   /// ```no_run
   /// let manager = HotkeyManager::new();
   /// manager.register("Ctrl+Alt+R", |_| {
   ///     println!("Recording toggled");
   /// });
   /// ```
   pub struct HotkeyManager {
       // ...
   }

Using sphinxcontrib-rust
~~~~~~~~~~~~~~~~~~~~~~~~

Once code exists, integrate with Sphinx:

1. **Generate Rust docs:**

   .. code-block:: bash

      cargo doc --no-deps --document-private-items

2. **Configure sphinxcontrib-rust in conf.py:**

   .. code-block:: python

      extensions = [
          # ... existing extensions
          'sphinxcontrib.rust',
      ]

      rust_crates = {
          'airgap-whisper': '../airgap-whisper',
      }

3. **Reference Rust items in RST:**

   .. code-block:: rst

      See :rust:struct:`HotkeyManager` for hotkey management.

4. **Build documentation:**

   .. code-block:: bash

      cd sphinx-docs
      make html

Traceability Linking
~~~~~~~~~~~~~~~~~~~~

Link code documentation back to requirements using custom directives:

.. code-block:: rst

   .. impl:: Audio Recording Implementation
      :id: IMPL-WHISPER-001
      :implements: FR-WHISPER-001, FR-WHISPER-002, FR-WHISPER-003
      :status: planned
      :location: src/audio/recorder.rs

      Implementation of audio recording using ALSA (Linux) / CoreAudio (macOS)

Future Enhancements
-------------------

When implementation begins:

1. Add ``.. impl::`` directives for each major component
2. Link implementations to requirements in traceability matrix
3. Auto-generate API docs with sphinxcontrib-rust
4. Add code examples to test cases for validation
5. Update needflow diagrams to include implementation nodes

See Also
--------

- :doc:`/airgap-whisper/requirements/srs` - Requirements this API implements
- :doc:`/airgap-whisper/design/sdd` - Detailed design specifications
- :doc:`/airgap-whisper/testing/plan` - Test cases validating this API
