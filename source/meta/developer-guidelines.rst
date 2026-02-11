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

By contributing code to any Cleanroom Labs project, you agree that your contributions are licensed under AGPL-3.0. (Note: this is not a formal Contributor License Agreement. A formal CLA may be introduced as the project matures. Until then, contributions are governed by the AGPL-3.0 license and the expectations outlined here.)

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

Code Style
~~~~~~~~~~

- All Rust code must pass ``cargo fmt`` (default rustfmt settings)
- All code must pass ``cargo clippy`` with no warnings
- Avoid ``#[allow(...)]`` annotations to suppress clippy warnings without a comment explaining why the suppression is necessary
- Follow standard Rust naming: ``snake_case`` for functions and variables, ``CamelCase`` for types, ``SCREAMING_CASE`` for constants

Testing Expectations
~~~~~~~~~~~~~~~~~~~~

- Every functional requirement that reaches implementation should have at least one corresponding test
- Test cases in sphinx-needs (``:test:`` directives) describe *what* to verify; Rust ``#[test]`` functions implement the verification
- Focus on happy-path tests for MVP — see the :doc:`v1.0.0 quality bar <release-roadmap>` for the current bar
- Prefer integration tests over unit tests where they cover the same behavior with less coupling to internals
- No coverage targets — test the behavior, not the line count

Documentation Standards
~~~~~~~~~~~~~~~~~~~~~~~

- When changing behavior covered by existing requirements, update the corresponding sphinx-needs artifacts (SRS, test plan)
- Add Rust doc comments (``///``) on public API items: modules, structs, and public functions
- No documentation needed for obvious getters/setters or trivial utility functions
- See the :doc:`sphinx-needs-guide` for requirements authoring syntax and :doc:`specification-writing-guide` for guidance on writing good specification artifacts

Git Workflow
~~~~~~~~~~~~

- Work on feature branches; merge to ``main`` via pull request
- Commit messages: imperative mood, concise subject line, body for non-obvious changes
- One logical change per commit — split unrelated changes into separate commits
- Build docs before pushing documentation changes: ``node scripts/build-docs.mjs`` from the website root, or ``make html`` from the ``technical-docs/`` directory
- Pull requests should describe what changed and why; link to relevant requirements if applicable

