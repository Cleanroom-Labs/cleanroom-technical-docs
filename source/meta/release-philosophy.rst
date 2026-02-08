Release Philosophy
==================

This document describes the versioning and release coordination strategy across the Cleanroom Labs project suite. All projects follow `Semantic Versioning <https://semver.org/>`_.

v1.0.0: Coordinated Launch
---------------------------

The v1.0.0 release is the only release coordinated across all three foundation projects:

- **AirGap Deploy** — deployment packaging tool
- **AirGap Transfer** — large file transfer utility
- **Cleanroom Whisper** — offline transcription application

The goal of the coordinated v1.0.0 is to demonstrate integrated workflows (e.g., Deploy → Transfer → Install) and deliver a Minimum Viable Product for each project.

Post-v1.0.0: AirGap Synchronized, Whisper Independent
-------------------------------------------------------

After v1.0.0, only **AirGap Deploy** and **AirGap Transfer** follow a synchronized release strategy. These two projects are tightly coupled — Deploy produces deployment packages that Transfer moves across the air gap — so their compatibility must be explicitly managed.

**Cleanroom Whisper** releases independently. It consumes AirGap Deploy packages but does not impose compatibility constraints on the AirGap tools.

Versioning Rules
-----------------

Patch Releases
~~~~~~~~~~~~~~

All projects may have independent patch releases (v1.0.1, v1.0.2) for bug fixes at any time. Patch releases do not require coordination.

Minor Releases
~~~~~~~~~~~~~~

Minor releases (v1.1, v1.2) for the AirGap projects are coordinated between Deploy and Transfer but do not require Whisper involvement. Minor releases add functionality in a backward-compatible manner.

Major Releases
~~~~~~~~~~~~~~

The AirGap projects share a major version number. A major version bump (e.g., v1.x → v2.0) is reserved for changes that **break mutual compatibility** between Deploy and Transfer — for example, a package format change that makes Deploy v2.0 output unreadable by Transfer v1.x.

.. raw:: html

   <div style="margin-top: 1.5em;"></div>

When the shared boundary breaks, both projects bump to the same new major version simultaneously. This keeps the version numbers permanently aligned: if Deploy and Transfer share a major version, they are guaranteed to be mutually compatible.

.. raw:: html

   <div style="margin-top: 1.5em;"></div>

Per-project backward-incompatible changes (breaking CLI flags, configuration format changes) are introduced through **deprecation cycles in minor releases**, not major bumps. This avoids forcing the companion project to bump for changes that don't affect it.

.. raw:: html

   <div style="margin-top: 1.5em;"></div>

Cleanroom Whisper manages its own major version independently.

.. raw:: html

   <div style="margin-top: 1.5em;"></div>

