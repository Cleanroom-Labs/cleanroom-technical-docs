MVP Development Plan
====================

**Goal:** A working transcription app you use daily.

**Guiding document:** `principles.md <../../principles.md>`__

--------------

MVP Scope
---------

============ =================================================
Feature      Implementation
============ =================================================
Record audio Microphone → WAV file
Transcribe   Shell to whisper.cpp
View result  Tray menu + notification
Copy text    Hotkey + menu click
History      SQLite, shown in tray menu
Settings     Native dialog (whisper path, model path, hotkeys)
Tray         Background operation, status indicator
============ =================================================

For out-of-scope features, file structure, and dependencies, see `principles.md <../../principles.md>`__.

--------------

Milestones
----------

Milestone 1: Skeleton
~~~~~~~~~~~~~~~~~~~~~

**Goal:** Tray icon appears.

- ☐ Create Cargo project with dependencies
- ☐ Create module files per SDD architecture
- ☐ Initialize system tray with placeholder icon
- ☐ Verify app runs and shows tray icon

**Done when:** Tray icon visible, right-click shows “Quit”.

--------------

Milestone 2: Recording
~~~~~~~~~~~~~~~~~~~~~~

**Goal:** Record voice to WAV file.

- ☐ List audio input devices
- ☐ Capture from default device
- ☐ Write samples to WAV (16kHz mono)
- ☐ Left-click tray toggles recording
- ☐ Tray icon changes when recording (red)

**Done when:** Can record, find WAV file, play in system player.

--------------

Milestone 3: Transcription
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Goal:** Get text from whisper.cpp.

- ☐ Settings stored in SQLite
- ☐ Settings dialog for whisper binary path
- ☐ Settings dialog for model path
- ☐ Validate both paths exist
- ☐ Invoke whisper.cpp with configured paths
- ☐ Capture and parse stdout for transcription text
- ☐ Show notification with result preview

**Done when:** Record → notification shows text.

--------------

Milestone 4: Persistence
~~~~~~~~~~~~~~~~~~~~~~~~

**Goal:** Save transcriptions, survive restart.

- ☐ Initialize SQLite in app data directory
- ☐ Create tables on first run (see SDD schema)
- ☐ Save transcription after whisper completes
- ☐ Load recent transcriptions into tray menu
- ☐ Click menu item copies text to clipboard
- ☐ “View History” opens native dialog with full list

**Done when:** Close app, reopen, history still there.

--------------

Milestone 5: Hotkeys
~~~~~~~~~~~~~~~~~~~~

**Goal:** Control without touching mouse.

- ☐ Register ``Ctrl+Alt+R`` for toggle recording
- ☐ Register ``Ctrl+Alt+C`` for copy last transcription
- ☐ Settings dialog to change hotkeys
- ☐ Handle registration failures gracefully

**Done when:** Can record and copy without touching mouse.

--------------

Milestone 6: Polish
~~~~~~~~~~~~~~~~~~~

**Goal:** Comfortable daily use.

- ☐ First-run: prompt for whisper paths if not set
- ☐ Error notification when whisper not found
- ☐ Error notification when recording fails
- ☐ Show timestamp and preview on menu items
- ☐ Tray icon shows busy state during transcription
- ☐ Settings persist between runs

**Done when:** Use it for a week without frustration.

--------------

Definition of Done
------------------

MVP is complete when:

1. ☐ Press hotkey → recording starts (tray icon changes)
2. ☐ Press hotkey → notification shows transcription
3. ☐ Press hotkey → last text copied to clipboard
4. ☐ Recent transcriptions visible in tray menu
5. ☐ Click menu item → text copied to clipboard
6. ☐ Quit and reopen → history preserved
7. ☐ Use daily for one week without major issues

--------------

What’s NOT in MVP
-----------------

Defer all of this until after shipping:

- Tests
- CI/CD
- Documentation
- Error recovery beyond “show notification”
- Accessibility
- Dark mode toggle (follow system is fine)
- Performance optimization
- Code signing (needed for distribution, not development)

Build it. Use it. Then improve it.
