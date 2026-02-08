Principles
==========

These principles guide every design decision across all Cleanroom Labs
projects. When in doubt, refer here.

Privacy Through Data Locality
--------------------------------

**All data stays on the user’s machine. No exceptions.**

Your data is private by design — it never leaves your computer without your
explicit consent. This isn't a policy; it's enforced by architecture.

What this means
~~~~~~~~~~~~~~~

- No network code in the application
- No dependencies that make network calls
- No analytics, telemetry, or crash reporting
- No update checks (user updates manually)
- No external API calls
- No CDN resources, external fonts, or remote assets

How to verify
~~~~~~~~~~~~~

The app must work identically with:

- Network disabled at OS level
- Firewall blocking all connections
- No internet connections

Implementation rules
~~~~~~~~~~~~~~~~~~~~

- Audit dependencies for network capabilities before adding
- No network-related code (HTTP clients, WebSockets, DNS lookups, etc.)

Air-gap deployment
~~~~~~~~~~~~~~~~~~

The app must be deployable on air-gapped systems (no internet access ever). This requires:

- **Vendored dependencies:** All Cargo crates checked into repo
- **Self-contained binary:** Single executable with all required assets bundled
- **No phone-home:** No license checks, update checks, or telemetry

Build once with internet, deploy anywhere without. No npm, no frontend build step.

Build dependencies
~~~~~~~~~~~~~~~~~~

**For air-gapped builds:** Platform-specific build tools, Rust toolchain, and C++ compiler must be pre-installed on the target system.

Minimal Dependencies
-----------------------

**Fewer dependencies = less risk, less complexity, faster builds.**

Target
~~~~~~

- **Direct dependencies:** Ideally ≤10 crates
- **No system dependencies:** Everything bundled or uses OS APIs
- **No native bindings:** Pure Rust where possible

Technology constraints
~~~~~~~~~~~~~~~~~~~~~~

- Pure Rust
- Use stdlib where possible (time handling, string operations, etc.)

For the dependency evaluation checklist, see :doc:`developer-guidelines`.

Simple Architecture
----------------------

**Write obvious code. Avoid abstraction until forced.**

File structure
~~~~~~~~~~~~~~

**Flat structure:** No needless module nesting.

For coding conventions and the YAGNI test, see :doc:`developer-guidelines`.

Features We Don’t Build
--------------------------

These are explicitly out of scope, regardless of how useful they might seem:

+-------------------------------------+-------------------------------------------------+
| Feature                             | Reason                                          |
+=====================================+=================================================+
| Cloud sync                          | Violates data locality                          |
+-------------------------------------+-------------------------------------------------+
| Auto-update                         | Requires network                                |
+-------------------------------------+-------------------------------------------------+
| Crash reporting                     | Requires network                                |
+-------------------------------------+-------------------------------------------------+
| FLAC compression                    | Extra dependency, WAV is fine                   |
+-------------------------------------+-------------------------------------------------+
| MP3/M4A import                      | Extra dependencies, record in-app               |
+-------------------------------------+-------------------------------------------------+
| Multiple models                     | One model works, user can change in settings    |
+-------------------------------------+-------------------------------------------------+
| Streaming transcription             | Complexity, batch works                         |
+-------------------------------------+-------------------------------------------------+
| Word timestamps                     | Extra parsing, plain text is fine               |
+-------------------------------------+-------------------------------------------------+
| Speaker diarization                 | whisper.cpp feature, adds complexity            |
+-------------------------------------+-------------------------------------------------+
| Full-text search (FTS5)             | Simple string matching works for small datasets |
+-------------------------------------+-------------------------------------------------+
| Audio playback                      | User can play WAV in system player              |
+-------------------------------------+-------------------------------------------------+
| Batch import                        | Record one at a time                            |
+-------------------------------------+-------------------------------------------------+

If we need any of these later, we add them later. Not before.

Design Principles Alignment
----------------------------

All three projects follow the core principles above:

+---------------------------+--------------------------+-------------------------------------+-------------------------------+
| Principle                 | AirGap Transfer          | AirGap Deploy                       | Cleanroom Whisper             |
+===========================+==========================+=====================================+===============================+
| **Privacy/Data Locality** | No network code          | No network in generated packages    | No network code               |
+---------------------------+--------------------------+-------------------------------------+-------------------------------+
| **Minimal Dependencies**  | Minimal stdlib usage     | Essential packaging crates only     | ~10 crates                    |
+---------------------------+--------------------------+-------------------------------------+-------------------------------+
| **Simple Architecture**   | Single responsibility    | Clear component separation          | Flat structure, ~5 files      |
+---------------------------+--------------------------+-------------------------------------+-------------------------------+
| **Air-gap Ready**         | Designed for air-gaps    | Entire purpose                      | Vendored deps                 |
+---------------------------+--------------------------+-------------------------------------+-------------------------------+

