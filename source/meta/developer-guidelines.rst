Developer Guidelines
====================

Licensing Overview
------------------

All Cleanroom Labs projects — AirGap Transfer, AirGap Deploy, and Cleanroom Whisper — are licensed under the **GNU Affero General Public License v3.0 (AGPL-3.0)**.

.. raw:: html

   <div style="margin-top: 1.5em;"></div>

This means that all source code is freely available, and anyone can use, modify, and distribute the software, provided they comply with the AGPL-3.0 terms. The AGPL extends the GPL's copyleft provisions to cover network use: if you run a modified version of the software as a network service, you must make the corresponding source code available to users of that service.

Contributor Expectations
------------------------

By contributing code to any Cleanroom Labs project, you agree that your contributions are licensed under AGPL-3.0.

.. raw:: html

   <div style="margin-top: 1.5em;"></div>

Contributors must not introduce code that circumvents the copyleft provisions of the AGPL. Specifically:

- Do not create separate permissive-licensed modules designed to extract core functionality from the AGPL-licensed codebase
- Do not add proprietary components or dependencies that would prevent users from exercising their rights under the AGPL
- Do not implement licensing checks, feature gates, or other mechanisms that restrict access to AGPL-licensed functionality

AGPL Compliance
---------------

Key obligations under the AGPL-3.0:

- **Source availability:** If you distribute the software (in binary or source form), you must provide access to the corresponding source code under the same license
- **Network use:** If you run a modified version as a network service, you must offer the source to users of that service
- **Derivative works:** Any work based on AGPL-licensed code must also be licensed under the AGPL-3.0
- **License notices:** All copies must include the AGPL-3.0 license text and copyright notices

For the full license text, see the ``LICENSE`` file in each project repository.

Third-Party Dependencies
------------------------

All third-party dependencies must be compatible with the AGPL-3.0. In practice:

- **Permitted:** MIT, BSD, Apache-2.0, LGPL, GPL-3.0, and other AGPL-compatible licenses
- **Not permitted:** Proprietary licenses, or open-source licenses with restrictions incompatible with AGPL-3.0 (e.g., certain "Commons Clause" licenses)

Before adding a new dependency, verify its license compatibility. When in doubt, consult the `FSF license compatibility list <https://www.gnu.org/licenses/license-list.html>`_.

Coding Conventions
------------------

These conventions follow from the :doc:`design principles <principles>`. They provide practical guidance for day-to-day development decisions.

Before Adding a Dependency
~~~~~~~~~~~~~~~~~~~~~~~~~~

Ask:

1. Can I do this with stdlib?
2. Can I do this with code I write myself (<100 lines)?
3. Does this crate have network capabilities?
4. How many transitive dependencies does it add?
5. Is it actively maintained?

If the answer to #1 or #2 is yes, don't add the dependency.

Code Rules
~~~~~~~~~~

============================== ===================================
Do                             Don't
============================== ===================================
Write functions                Create traits you'll implement once
Use concrete types             Use generics for "flexibility"
Handle errors where they occur Create error hierarchies
Use ``String``                 Create newtype wrappers
============================== ===================================

The YAGNI Test
~~~~~~~~~~~~~~

Before adding any feature or abstraction:

- Do I need this right now to make the app work?
- Have I needed this exact thing twice already?

If both answers aren't "yes", don't add it.

**Examples:**

- **Avoid:** Trait abstractions for single implementations
- **Prefer:** Simple functions
- **Avoid:** Multiple format support (e.g., WAV, FLAC, MP3, M4A)
- **Prefer:** Single format (e.g., WAV only)

Note on Formal CLA
-------------------

This document describes project guidelines and expectations for contributors. It is **not** a formal Contributor License Agreement (CLA). A formal CLA may be introduced as the project matures. Until then, contributions are governed by the AGPL-3.0 license and the expectations outlined above.

.. raw:: html

   <div style="margin-top: 1.5em;"></div>

