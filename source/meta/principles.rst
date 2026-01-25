Design Principles
=================

These principles guide every decision in Cleanroom Whisper. When in doubt, refer here.

--------------

Privacy Through Data Locality
--------------------------------

**All data stays on the user’s machine. No exceptions.**

Your voice recordings and transcriptions are private by design — they never leave your computer. This isn’t a policy; it’s enforced by architecture.

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
- **Self-contained binary:** Single executable plus whisper.cpp and model
- **No phone-home:** No license checks, update checks, or telemetry

Build once with internet, deploy anywhere without. No npm, no frontend build step.

Build dependencies
~~~~~~~~~~~~~~~~~~

**For air-gapped builds:** Platform-specific build tools, Rust toolchain, and C++ compiler must be pre-installed on the target system.

--------------

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

Before adding a dependency
~~~~~~~~~~~~~~~~~~~~~~~~~~

Ask:

Can I do this with stdlib?
Can I do this with code I write myself (<100 lines)?
Does this crate have network capabilities?
How many transitive dependencies does it add?
Is it actively maintained?

If the answer to #1 or #2 is yes, don’t add the dependency.

--------------

Simple Architecture
----------------------

**Write obvious code. Avoid abstraction until forced.**

File structure
~~~~~~~~~~~~~~

**Flat structure:** No nested modules.

Code rules
~~~~~~~~~~

============================== ===================================
Do                             Don’t
============================== ===================================
Write functions                Create traits you’ll implement once
Use concrete types             Use generics for “flexibility”
Copy small code                Create abstractions for DRY
Handle errors where they occur Create error hierarchies
Use ``String``                 Create newtype wrappers
============================== ===================================

The YAGNI test
~~~~~~~~~~~~~~

Before adding any feature or abstraction:

Do I need this right now to make the app work?
Have I needed this exact thing twice already?

If both answers aren’t “yes”, don’t add it.

Examples
~~~~~~~~

- **Avoid:** Trait abstractions for single implementations
- **Prefer:** Simple functions
- **Avoid:** Multiple format support (WAV, FLAC, MP3, M4A)
- **Prefer:** Single format (WAV only)

--------------

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

--------------

Quality Bar
--------------

For MVP
~~~~~~~

- **Works:** Core flow functions without crashing
- **Usable:** You can use it daily without frustration
- **Stable:** No data loss

Not required for MVP
~~~~~~~~~~~~~~~~~~~~

- Tests (add when stabilizing)
- Documentation (code is small enough to read)
- Error recovery (show error, user retries)
- Accessibility (add after core works)
- Performance optimization (make it work first)
