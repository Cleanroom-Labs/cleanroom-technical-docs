Software Design Document
========================

Introduction
---------------

This SDD describes the architecture and design of AirGap Whisper’s MVP.

**Guiding document:** :doc:`Principles </meta/principles>`

--------------

Architecture Overview
------------------------

System Context
~~~~~~~~~~~~~~

::

   ┌─────────────────────────────────────────────────────────────────┐
   │                    Pure Rust Application                        │
   ├─────────────────────────────────────────────────────────────────┤
   │                                                                 │
   │   ┌──────────────┐     ┌──────────────┐      ┌──────────────┐   │
   │   │  System Tray │     │   Hotkeys    │      │    Audio     │   │
   │   │  (tray-icon) │     │(global-hotkey│      │    (cpal)    │   │
   │   └──────┬───────┘     └──────┬───────┘      └──────┬───────┘   │
   │          │                    │                     │           │
   │          └────────────────────┼─────────────────────┘           │
   │                               ▼                                 │
   │                    ┌──────────────────┐                         │
   │                    │    Event Loop    │                         │
   │                    │    (main.rs)     │                         │
   │                    └────────┬─────────┘                         │
   │                             │                                   │
   │              ┌──────────────┼──────────────┐                    │
   │              ▼              ▼              ▼                    │
   │   ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
   │   │  whisper.rs  │  │    db.rs     │  │  Native      │          │
   │   │ (subprocess) │  │  (SQLite)    │  │  Dialogs     │          │
   │   └──────┬───────┘  └──────────────┘  └──────────────┘          │
   │          │                                                      │
   │          ▼                                                      │
   │   ┌──────────────┐                                              │
   │   │ whisper.cpp  │                                              │
   │   │(user-managed)│                                              │
   │   └──────────────┘                                              │
   └─────────────────────────────────────────────────────────────────┘

Design Rationale
~~~~~~~~~~~~~~~~

+---------------------------------+---------------------------------------------------------+
| Decision                        | Rationale                                               |
+=================================+=========================================================+
| Pure Rust (no WebView)          | Smaller binary, simpler deployment, air-gap friendly    |
+---------------------------------+---------------------------------------------------------+
| System tray UI                  | Native look, minimal footprint, keyboard-first workflow |
+---------------------------------+---------------------------------------------------------+
| tray-icon + global-hotkey       | Same crates Tauri uses, without the WebView overhead    |
+---------------------------------+---------------------------------------------------------+
| SQLite                          | ACID transactions, single file backup                   |
+---------------------------------+---------------------------------------------------------+
| Shell to whisper.cpp            | Simplicity, user controls version                       |
+---------------------------------+---------------------------------------------------------+
| No traits                       | Only one implementation exists (YAGNI)                  |
+---------------------------------+---------------------------------------------------------+

--------------

File Structure
-----------------

Per :doc:`Principles </meta/principles>`: **5 Rust files, flat structure. No frontend.**

::

   airgap-whisper/
   ├── src/
   │   ├── main.rs       # Entry point, event loop, tray setup
   │   ├── audio.rs      # Record WAV from microphone
   │   ├── whisper.rs    # Shell to whisper.cpp
   │   ├── db.rs         # SQLite CRUD
   │   └── tray.rs       # Tray menu construction and handlers
   ├── Cargo.toml
   ├── vendor/           # Vendored dependencies (for air-gap builds)
   └── .cargo/
       └── config.toml   # Points to vendor directory

--------------

Data Design
--------------

Database Schema
~~~~~~~~~~~~~~~

**2 tables. No indexes. No FTS. No migrations.**

.. code:: sql

   CREATE TABLE transcriptions (
       id TEXT PRIMARY KEY,          -- UUID v4
       created_at INTEGER NOT NULL,  -- Unix timestamp (ms)
       duration_seconds REAL,        -- Audio duration
       text TEXT NOT NULL,           -- Transcription content
       audio_path TEXT               -- NULL if audio deleted
   );

   CREATE TABLE settings (
       key TEXT PRIMARY KEY,
       value TEXT NOT NULL
   );

Settings Keys
~~~~~~~~~~~~~

========================= ======= ================
Key                       Type    Default
========================= ======= ================
``whisper_binary_path``   string  —
``model_path``            string  —
``hotkey_toggle_record``  string  ``Ctrl+Alt+R``
``hotkey_copy_last``      string  ``Ctrl+Alt+C``
``audio_input_device``    string  (system default)
``max_recording_minutes`` integer 120
========================= ======= ================

Settings Validation
~~~~~~~~~~~~~~~~~~~

+---------------------------+-----------------------------------------------------------+
| Setting                   | Validation Rules                                          |
+===========================+===========================================================+
| ``whisper_binary_path``   | File exists, is executable                                |
+---------------------------+-----------------------------------------------------------+
| ``model_path``            | File exists, has ``.bin`` extension                       |
+---------------------------+-----------------------------------------------------------+
| ``hotkey_*``              | Valid key combination, no conflict with other app hotkeys |
+---------------------------+-----------------------------------------------------------+
| ``audio_input_device``    | Device exists in system (or empty for default)            |
+---------------------------+-----------------------------------------------------------+
| ``max_recording_minutes`` | Integer 1-480 (8 hours max)                               |
+---------------------------+-----------------------------------------------------------+

**Path validation:** - Reject paths containing ``..`` (path traversal) - Expand ``~`` to home directory - Convert to absolute path before storing

**On validation failure:** Show inline error message in settings dialog, prevent save until fixed.

File Storage
~~~~~~~~~~~~

::

   {APP_DATA_DIR}/
   ├── airgap-whisper.db   # SQLite database
   ├── audio/              # Audio files
   │   └── {uuid}.wav
   └── temp/               # Recording in progress
       └── recording.wav

Schema Migration Strategy
~~~~~~~~~~~~~~~~~~~~~~~~~

**MVP approach:** No migrations. Schema is simple and stable.

**If schema changes are needed later:** - Add columns with ALTER TABLE and defaults - Store schema version in ``settings`` table - Run migrations sequentially on startup if version < current - Never delete data during migration - Always add columns with NULL or default values

Data Retention Policy
~~~~~~~~~~~~~~~~~~~~~

**Audio files:**

+-------------------------------+--------------------------------------------------------------+
| Policy                        | Behavior                                                     |
+===============================+==============================================================+
| Default                       | Keep audio indefinitely with transcription                   |
+-------------------------------+--------------------------------------------------------------+
| Manual delete                 | User deletes from history dialog; sets ``audio_path = NULL`` |
+-------------------------------+--------------------------------------------------------------+
| Temp files                    | Delete ``temp/recording.wav`` after transcription completes  |
+-------------------------------+--------------------------------------------------------------+

**Transcriptions:** - Retained indefinitely until user deletes - Deletion removes database row and associated audio file (if exists) - No automatic cleanup or archival

**Database:** - Single file, no automatic backup - User responsible for backup (copy ``airgap-whisper.db``) - No size limits enforced (SQLite handles large datasets)

**Cleanup on delete:** Delete audio file if exists, then delete database row.

--------------

Component Design
-------------------

audio.rs
~~~~~~~~

Record WAV from microphone using cpal + hound.

.. code:: rust

   pub struct AudioCapture {
       stream: Option<cpal::Stream>,
       is_recording: Arc<AtomicBool>,
       start_time: Option<Instant>,
   }

   impl AudioCapture {
       pub fn new(device_id: Option<&str>) -> Result<Self, AudioError>;
       pub fn start(&mut self, output_path: &Path) -> Result<(), AudioError>;
       pub fn stop(&mut self) -> Result<PathBuf, AudioError>;
       pub fn elapsed(&self) -> Duration;
       pub fn is_recording(&self) -> bool;
       pub fn get_level(&self) -> f32;
   }

   pub fn list_input_devices() -> Result<Vec<AudioDevice>, AudioError>;

whisper.rs
~~~~~~~~~~

Shell to whisper.cpp using simple function (no trait).

**Core function:** ``transcribe(whisper_binary, model_path, audio_path) -> Result<String>``

**Behavior:** - Invokes whisper.cpp with ``--no-timestamps`` flag for clean text output - Parses stdout for transcription text - Returns error on non-zero exit code with stderr message

db.rs
~~~~~

SQLite CRUD operations.

.. code:: rust

   pub struct Database {
       conn: Connection,
   }

   impl Database {
       pub fn open(path: &Path) -> Result<Self, DbError>;
       pub fn initialize(&self) -> Result<(), DbError>;
       pub fn save_transcription(&self, t: &Transcription) -> Result<(), DbError>;
       pub fn list_transcriptions(&self) -> Result<Vec<Transcription>, DbError>;
       pub fn get_transcription(&self, id: &str) -> Result<Option<Transcription>, DbError>;
       pub fn delete_transcription(&self, id: &str) -> Result<(), DbError>;
       pub fn get_setting(&self, key: &str) -> Result<Option<String>, DbError>;
       pub fn set_setting(&self, key: &str, value: &str) -> Result<(), DbError>;
   }

tray.rs
~~~~~~~

System tray menu and event handlers.

.. code:: rust

   pub struct TrayApp {
       tray: TrayIcon,
       state: AppState,
   }

   pub enum AppState {
       Idle,
       Recording { start: Instant },
       Transcribing,
   }

   impl TrayApp {
       pub fn new() -> Result<Self, TrayError>;
       pub fn update_icon(&mut self, state: &AppState);
       pub fn rebuild_menu(&mut self, recent: &[Transcription]);
       pub fn show_notification(&self, title: &str, body: &str);
   }

   // Menu items
   pub fn build_menu(state: &AppState, recent: &[Transcription]) -> Menu {
       // - Start/Stop Recording
       // - separator
       // - Recent transcriptions (click to copy)
       // - separator
       // - View History...
       // - Settings...
       // - Quit
   }

Tray Menu Structure
~~~~~~~~~~~~~~~~~~~

::

   ┌───────────────────────────────────────┐
   │ ● Start Recording                     │  ← or "■ Stop Recording" when active
   ├───────────────────────────────────────┤
   │   12:34 PM - "Meeting notes about..." │  ← Click to copy, shows preview
   │   11:15 AM - "Remember to call..."    │
   │   Yesterday - "The quarterly..."      │
   ├───────────────────────────────────────┤
   │ View History...                       │  ← Opens native dialog
   │ Settings...                           │  ← Opens native dialog
   ├───────────────────────────────────────┤
   │ Quit                                  │
   └───────────────────────────────────────┘

**Recent items:** Show up to 5 most recent transcriptions. Each shows: - Relative timestamp (time if today, “Yesterday”, or date) - Text preview (first ~30 characters, ellipsized)

**Click behavior:** - Left-click tray icon: Toggle recording - Right-click tray icon: Show menu - Click menu item: Copy full transcription to clipboard

Tray Icon States
~~~~~~~~~~~~~~~~

============ ========== =============
State        Icon       Color
============ ========== =============
Idle         Microphone Default/gray
Recording    Microphone Red
Transcribing Microphone Yellow/orange
============ ========== =============

Icons should be simple, monochrome-friendly for macOS menu bar.

--------------

Interaction Flows
--------------------

Record and Transcribe
~~~~~~~~~~~~~~~~~~~~~

::

   User                    App                     whisper.cpp
     │                      │                           │
     │  Press hotkey        │                           │
     │─────────────────────►│                           │
     │                      │ Start cpal stream         │
     │                      │ Update tray icon (red)    │
     │  Tray shows red icon │                           │
     │◄─────────────────────│                           │
     │                      │                           │
     │  Press hotkey        │                           │
     │─────────────────────►│                           │
     │                      │ Stop stream, save WAV     │
     │                      │ Update tray icon (busy)   │
     │                      │ Spawn whisper.cpp         │
     │                      │──────────────────────────►│
     │                      │ stdout text               │
     │                      │◄──────────────────────────│
     │                      │ Save to SQLite            │
     │                      │ Update tray menu          │
     │                      │ Show notification         │
     │  Notification shown  │                           │
     │◄─────────────────────│                           │

Settings Dialog
~~~~~~~~~~~~~~~

Native dialog with the following layout:

::

   ┌─────────────────────────────────────────────────────┐
   │ Settings                                        [X] │
   ├─────────────────────────────────────────────────────┤
   │                                                     │
   │ Whisper Binary                                      │
   │ ┌─────────────────────────────────────────┐ [Browse]│
   │ │ /usr/local/bin/whisper                  │         │
   │ └─────────────────────────────────────────┘         │
   │ ✓ Valid executable                                  │
   │                                                     │
   │ Model File                                          │
   │ ┌─────────────────────────────────────────┐ [Browse]│
   │ │ ~/models/ggml-base.en.bin               │         │
   │ └─────────────────────────────────────────┘         │
   │ ✓ Valid model file                                  │
   │                                                     │
   │ ─────────────────────────────────────────────────── │
   │                                                     │
   │ Hotkeys                                             │
   │   Toggle Recording  [ Ctrl+Alt+R    ] [Set]         │
   │   Copy Last         [ Ctrl+Alt+C    ] [Set]         │
   │                                                     │
   │ Audio Input                                         │
   │   Device  [ System Default          ▼]              │
   │                                                     │
   │ ─────────────────────────────────────────────────── │
   │                                                     │
   │                              [Cancel]  [Save]       │
   └─────────────────────────────────────────────────────┘

**Validation feedback:**

- Green checkmark: Valid path/setting
- Red X with message: Invalid (e.g., “File not found”, “Not executable”)
- Save button disabled until all required fields valid

**Hotkey capture:**

- Click [Set] button, dialog shows “Press hotkey…”
- User presses key combination
- If conflicts with other app hotkey: “Conflicts with Toggle Recording”
- If conflicts with system: “May conflict with system shortcut” (warning, not error)

First-Run Flow
~~~~~~~~~~~~~~

::

   ┌───────────────────────────────────────────────────────┐
   │                   Welcome to AirGap Whisper           │
   ├───────────────────────────────────────────────────────┤
   │                                                       │
   │  To get started, configure your whisper.cpp paths:    │
   │                                                       │
   │  1. Whisper Binary                                    │
   │     ┌─────────────────────────────────┐ [Browse]      │
   │     │                                 │               │
   │     └─────────────────────────────────┘               │
   │     ⚠ Required                                        │
   │                                                       │
   │  2. Model File                                        │
   │     ┌─────────────────────────────────┐ [Browse]      │
   │     │                                 │               │
   │     └─────────────────────────────────┘               │
   │     ⚠ Required                                        │
   │                                                       │
   │  Need whisper.cpp?                                    │
   │  https://github.com/ggerganov/whisper.cpp             │
   │                                                       │
   │                                        [Continue]     │
   └───────────────────────────────────────────────────────┘

**First-run detection:**

- Check if ``whisper_binary_path`` setting exists and is valid
- If not, show first-run dialog before tray menu is active
- [Continue] disabled until both paths valid
- After setup, show “Ready! Press Ctrl+Alt+R to record.”

History Dialog
~~~~~~~~~~~~~~

::

   ┌─────────────────────────────────────────────────────┐
   │ Transcription History                           [X] │
   ├─────────────────────────────────────────────────────┤
   │ ┌─────────────────────────────────────────────────┐ │
   │ │ ● Today, 2:34 PM (1m 23s)                       │ │
   │ │   Meeting notes about the quarterly review...   │ │
   │ ├─────────────────────────────────────────────────┤ │
   │ │ ○ Today, 11:15 AM (45s)                         │ │
   │ │   Remember to call the dentist tomorrow...      │ │
   │ ├─────────────────────────────────────────────────┤ │
   │ │ ○ Yesterday, 4:30 PM (2m 10s)                   │ │
   │ │   The project deadline has been moved to...     │ │
   │ └─────────────────────────────────────────────────┘ │
   │                                                     │
   │ ─────────────────────────────────────────────────── │
   │ Selected: Today, 2:34 PM                            │
   │ ┌─────────────────────────────────────────────────┐ │
   │ │ Meeting notes about the quarterly review.       │ │
   │ │ Sales are up 15% compared to last quarter.      │ │
   │ │ Action items: update forecast, schedule...      │ │
   │ └─────────────────────────────────────────────────┘ │
   │                                                     │
   │ [Copy Text]  [Export .txt]  [Delete]        [Close] │
   └─────────────────────────────────────────────────────┘

**Behavior:**

- List shows all transcriptions, newest first
- Click to select and show full text in preview pane
- [Copy Text]: Copy to clipboard, show confirmation
- [Export .txt]: Save dialog, default filename from timestamp
- [Delete]: Confirm dialog, then remove transcription and audio file

--------------

Dependencies
---------------

**8 crates.** Pure Rust, no WebView, no npm, no frontend build.

See :doc:`Principles </meta/principles>` (Current Minimal Set section) for the authoritative dependency list with versions.

--------------

Security & Privacy
---------------------

**Privacy by architecture:** No network code exists in the application. Voice recordings and transcriptions never leave the user’s machine.

================= ======================================
Threat            Mitigation
================= ======================================
Data exfiltration No network crates in dependency tree
Path traversal    Reject paths containing ``..``
Command injection No shell execution, explicit args only
SQL injection     Parameterized queries
================= ======================================

--------------

Deployment
-------------

Air-Gap Support
~~~~~~~~~~~~~~~

The application supports deployment on air-gapped systems (no internet access).

**Architecture requirements:**

- Pure Rust, no npm, no frontend build step
- Vendored dependencies via ``cargo vendor``
- Offline build: ``cargo build --release --offline``

See `README.md Air-Gapped Installation <../../README.md#air-gapped-installation>`__ for complete deployment procedures including whisper.cpp, Rust toolchain, and platform-specific packages.

Deployment Package
~~~~~~~~~~~~~~~~~~

**Typical deployment structure:**

- Application binary (~10-15 MB)
- whisper.cpp binary (user-provided or bundled)
- Whisper model file (user-provided or bundled)
- Setup instructions

See `README.md <../../README.md#air-gapped-installation>`__ for detailed package creation.

Platform Packages
~~~~~~~~~~~~~~~~~

======== =================== =====================================
Platform Format              Notes
======== =================== =====================================
macOS    .app bundle         Code-signed and notarized
Windows  .exe / .msi         Code-signed
Linux    .deb, .rpm, Flatpak GNOME requires AppIndicator extension
======== =================== =====================================

Release Process
~~~~~~~~~~~~~~~

**Version numbering:** Semantic versioning (MAJOR.MINOR.PATCH)

- MAJOR: Breaking changes
- MINOR: New features, backward compatible
- PATCH: Bug fixes

**Release checklist:**

.. code-block:: none

   [ ] Update version in Cargo.toml
   [ ] Update CHANGELOG.md
   [ ] Run all tests: cargo test
   [ ] Build release: cargo build --release
   [ ] Test on each platform (macOS, Windows, Linux)
   [ ] Code sign (see platform-specific steps below)
   [ ] Create GitHub release with binaries
   [ ] Update download links on website

Code Signing
~~~~~~~~~~~~

+----------------------+-------------------------------------------------+---------------------------------------------+
| Platform             | Requirements                                    | Notes                                       |
+======================+=================================================+=============================================+
| macOS                | Apple Developer account, codesign, notarization | Required for distribution outside App Store |
+----------------------+-------------------------------------------------+---------------------------------------------+
| Windows              | Code signing certificate, signtool              | Required to avoid security warnings         |
+----------------------+-------------------------------------------------+---------------------------------------------+
| Linux                | Optional GPG signing                            | For package repositories only               |
+----------------------+-------------------------------------------------+---------------------------------------------+

Distribution Channels
~~~~~~~~~~~~~~~~~~~~~

=============== ========== ==========================================
Channel         Platform   Notes
=============== ========== ==========================================
GitHub Releases All        Primary distribution, free
Gumroad/Paddle  All        For paid distribution
Homebrew        macOS      ``brew install airgap-whisper`` (future)
AUR             Arch Linux Community maintained (future)
=============== ========== ==========================================

**GitHub Release structure:**

::

   airgap-whisper-v1.0.0/
   ├── airgap-whisper-v1.0.0-macos-arm64.dmg
   ├── airgap-whisper-v1.0.0-macos-x64.dmg
   ├── airgap-whisper-v1.0.0-windows-x64.msi
   ├── airgap-whisper-v1.0.0-linux-x64.tar.gz
   ├── airgap-whisper-v1.0.0-linux-x64.deb
   ├── CHANGELOG.md
   └── SHA256SUMS.txt

--------------

Platform Considerations
---------------------------

Build Requirements
~~~~~~~~~~~~~~~~~~

======== ========================= =================================
Platform Toolchain                 System Libraries
======== ========================= =================================
macOS    Xcode Command Line Tools  None (uses CoreAudio)
Windows  Visual Studio Build Tools None (uses WASAPI)
Linux    ``build-essential``       ``libasound2-dev`` (ALSA headers)
======== ========================= =================================

All platforms require the Rust toolchain (rustc, cargo).

Audio Backends
~~~~~~~~~~~~~~

======== ========= ============================================
Platform Backend   Notes
======== ========= ============================================
macOS    CoreAudio System framework, no extra dependencies
Windows  WASAPI    System API, no extra dependencies
Linux    ALSA      Requires development headers at compile time
======== ========= ============================================

The ``cpal`` crate abstracts these differences. Audio code is platform-agnostic.

System Tray Behavior
~~~~~~~~~~~~~~~~~~~~

+-------------------------+-------------------------+----------------------------------------------------+
| Platform                | Behavior                | Notes                                              |
+=========================+=========================+====================================================+
| macOS                   | Menu bar icon           | Native support                                     |
+-------------------------+-------------------------+----------------------------------------------------+
| Windows                 | System tray icon        | Native support                                     |
+-------------------------+-------------------------+----------------------------------------------------+
| Linux (KDE, XFCE, etc.) | System tray icon        | Native support via StatusNotifierItem              |
+-------------------------+-------------------------+----------------------------------------------------+
| Linux (GNOME)           | Requires extension      | Install AppIndicator/KStatusNotifierItem extension |
+-------------------------+-------------------------+----------------------------------------------------+

The ``tray-icon`` crate handles platform differences. Left-click and right-click behavior is consistent.

Global Hotkeys
~~~~~~~~~~~~~~

=============== ======= ==========================
Platform        Support Notes
=============== ======= ==========================
macOS           Full    Native support
Windows         Full    Native support
Linux (X11)     Full    Native support
Linux (Wayland) Limited Requires XWayland fallback
=============== ======= ==========================

**Wayland limitation:** Pure Wayland does not support global hotkey capture by design (security model). Most distributions run XWayland for compatibility, which enables hotkey support.

whisper.cpp
~~~~~~~~~~~

whisper.cpp must be compiled or obtained separately for each target platform:

======== ============= ==============================
Platform Build Command Notes
======== ============= ==============================
macOS    ``make``      Uses Accelerate framework
Windows  CMake + MSVC  Or use pre-built releases
Linux    ``make``      Optional CUDA/OpenBLAS support
======== ============= ==============================

For air-gapped deployment, include pre-compiled whisper.cpp binaries for each target platform.

--------------

Localization Strategy
-------------------------

MVP Approach
~~~~~~~~~~~~

**MVP is English-only.** Localization is deferred until post-MVP based on user demand.

This aligns with :doc:`Principles </meta/principles>`: ship working software first, add features based on actual need.

Localization-Ready Architecture
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**String externalization:** Use a strings module instead of hardcoded strings throughout codebase.

**UI text inventory:** ~60 total strings across tray menu, settings, dialogs, notifications, and error messages. Small enough for manual translation.

Future Localization Approaches
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Three options when localization is needed:**

1. **Compile-time:** Separate binary per language (recommended for air-gap simplicity)
2. **Runtime embedded:** All languages in binary, select at runtime (single binary, larger size)
3. **External files:** Locale files in app data (flexible, but not air-gap friendly)

Localization Priority
~~~~~~~~~~~~~~~~~~~~~

Based on whisper.cpp model availability and likely user base:

======== ==================== ===== =================================
Priority Language             Code  Notes
======== ==================== ===== =================================
1        English              en    Default, MVP
2        German               de    Strong Rust/privacy community
3        Japanese             ja    Whisper has good Japanese support
4        Spanish              es    Large user base
5        French               fr    Large user base
6        Chinese (Simplified) zh-CN Large user base
======== ==================== ===== =================================

**Note:** Transcription language (whisper.cpp) is independent of UI language. Users can transcribe any language whisper.cpp supports regardless of UI locale.

What NOT to Localize
~~~~~~~~~~~~~~~~~~~~

Log messages, settings keys, file paths, error codes (localize descriptions only), and technical documentation.

