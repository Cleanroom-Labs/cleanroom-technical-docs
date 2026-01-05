sphinx-needs Usage Guide
========================

This guide explains how to use sphinx-needs for requirements engineering and traceability in the AirGap Project Suite documentation.

What is sphinx-needs?
---------------------

sphinx-needs is a Sphinx extension that provides directives for requirements engineering. It allows you to:

- Define requirements, tests, specifications, and other needs
- Link needs bidirectionally
- Generate traceability matrices automatically
- Create visual flow diagrams
- Filter and search needs
- Validate completeness and coverage

Why Use sphinx-needs?
---------------------

**Benefits:**

✅ **Bidirectional Traceability:** Automatically track relationships between requirements, designs, implementations, and tests
✅ **Automated Validation:** Sphinx validates all links at build time
✅ **Visual Diagrams:** Auto-generate flowcharts showing relationships
✅ **Searchable:** Full-text search across all requirements
✅ **Maintainable:** Changes propagate automatically
✅ **Standards-Compliant:** Supports IEEE requirements engineering practices

Available Directive Types
--------------------------

The AirGap Project Suite uses 6 sphinx-needs directive types:

.. list-table::
   :header-rows: 1
   :widths: 20 15 15 50

   * - Directive
     - Prefix
     - Color
     - Purpose
   * - ``.. usecase::``
     - UC-
     - Blue
     - User stories and workflow descriptions
   * - ``.. req::``
     - FR-
     - Orange
     - Functional requirements
   * - ``.. nfreq::``
     - NFR-
     - Dark Orange
     - Non-functional requirements (performance, security, etc.)
   * - ``.. spec::``
     - DS-
     - Yellow
     - Design specifications
   * - ``.. impl::``
     - IMPL-
     - Purple
     - Code implementations (future)
   * - ``.. test::``
     - TC-
     - Green
     - Test cases

Creating Needs
--------------

Basic Syntax
~~~~~~~~~~~~

All sphinx-needs directives follow this pattern:

.. code-block:: rst

   .. directive-type:: Title
      :id: UNIQUE-ID
      :status: approved|pending|rejected
      :tags: tag1, tag2, tag3
      :priority: must|should|could|wont  (or high|medium|low|critical)
      :links-to-other-needs: OTHER-ID-1, OTHER-ID-2

      Description of the need goes here.
      Can be multiple paragraphs.

Use Case Example
~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. usecase:: Large File Transfer
      :id: UC-TRANSFER-001
      :status: approved
      :tags: transfer, workflow, large-file, chunking

      Transfer a single large file (50GB VM image) across air-gap using
      multiple 16GB USB drives with automatic chunking.

      **Pack:** Split file into chunks sized for USB capacity.

      **Transfer:** Physically move USB drives across air-gap.

      **Unpack:** Verify checksums, reconstruct original file.

      **Success Criteria:** File reconstructed matches original, all
      checksums verified, no data loss.

Functional Requirement Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. req:: Split Files into Chunks
      :id: FR-TRANSFER-001
      :status: approved
      :tags: transfer, pack, chunking
      :priority: must
      :satisfies: UC-TRANSFER-001

      The system SHALL split source files/directories into fixed-size
      chunks suitable for transfer across air-gap boundaries.

Non-Functional Requirement Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. nfreq:: Offline Functionality
      :id: NFR-TRANSFER-004
      :status: approved
      :tags: transfer, offline
      :priority: must

      The system SHALL be 100% functional without network connectivity.
      All operations must work in air-gapped environments.

Test Case Example
~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. test:: Pack Single File into Chunks
      :id: TC-PCK-001
      :status: approved
      :tags: transfer, pack, chunking
      :tests: FR-TRANSFER-001
      :priority: high

      **Objective:** Verify pack operation splits single file into chunks.

      **Setup:** Create 50GB test file, connect 16GB USB drive.

      **Steps:**
      1. Run: airgap-transfer pack vm-image.qcow2 /media/usb-drive
      2. Verify 4 chunks created (3x 16GB + 1x 2GB)
      3. Verify checksums generated for each chunk
      4. Verify manifest file created

      **Expected:** All chunks created successfully with valid checksums.

Implementation Example (Future)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. impl:: Chunker Implementation
      :id: IMPL-TRANSFER-001
      :implements: FR-TRANSFER-001, FR-TRANSFER-002, FR-TRANSFER-005
      :status: implemented
      :location: src/chunker/mod.rs
      :tests: TC-PCK-001, TC-PCK-002, TC-PCK-003

      Streaming file chunker that splits files into fixed-size chunks
      without creating temporary files. Uses memory-mapped I/O for
      efficient processing.

      See :rust:struct:`Chunker` for API documentation.

Linking Needs
-------------

Link Types
~~~~~~~~~~

sphinx-needs supports multiple link types:

.. list-table::
   :header-rows: 1
   :widths: 20 30 50

   * - Option
     - Meaning
     - Use When
   * - ``:tests:``
     - "Tests the requirement(s)"
     - Link test cases to requirements
   * - ``:implements:``
     - "Implements the requirement(s)"
     - Link code to requirements
   * - ``:satisfies:``
     - "Satisfies the use case(s)"
     - Link requirements to use cases
   * - ``:derives:``
     - "Derives from the need(s)"
     - Link derived requirements

Link Syntax
~~~~~~~~~~~

Add link options to the directive header:

.. code-block:: rst

   .. test:: Checksum Verification Test
      :id: TC-INT-001
      :tests: FR-TRANSFER-020, FR-TRANSFER-021, FR-TRANSFER-022
      :priority: critical

      Verifies that SHA-256 checksums are generated correctly.

**Multiple links:** Separate with commas

**Validation:** Sphinx will error if linked IDs don't exist

Viewing Links
~~~~~~~~~~~~~

**In the documentation:**

- Each need displays its links in a metadata section
- Click any linked ID to navigate to that need
- "Incoming links" show what links TO this need
- "Outgoing links" show what this need links TO

**Example rendered output:**

::

   Test Case TC-INT-001: Checksum Verification Test

   Status: approved | Priority: critical

   Tests: FR-TRANSFER-020, FR-TRANSFER-021, FR-TRANSFER-022

   Description: Verifies that SHA-256 checksums...

   Tested by: (automatically populated by sphinx-needs)

Generating Traceability Matrices
---------------------------------

needtable Directive
~~~~~~~~~~~~~~~~~~~

Generate tables of needs with filtering:

.. code-block:: rst

   Requirements Table
   ^^^^^^^^^^^^^^^^^^

   .. needtable::
      :types: req, nfreq
      :columns: id, title, priority, status, outgoing
      :filter: "transfer" in tags
      :style: table

**Parameters:**

- ``:types:`` - Which directive types to include
- ``:columns:`` - Which fields to display
- ``:filter:`` - Filter expression (Python syntax)
- ``:style:`` - Display style (table, datatables)

Common Filters
~~~~~~~~~~~~~~

**By project:**

.. code-block:: rst

   :filter: "whisper" in tags

**By status:**

.. code-block:: rst

   :filter: status == "approved"

**By priority:**

.. code-block:: rst

   :filter: priority == "must" or priority == "critical"

**Untested requirements:**

.. code-block:: rst

   :filter: len(is_tested_by) == 0

**Multiple conditions:**

.. code-block:: rst

   :filter: "transfer" in tags and status == "approved" and priority == "must"

Column Options
~~~~~~~~~~~~~~

Available columns:

- ``id`` - Unique identifier
- ``title`` - Need title
- ``status`` - Status (approved, pending, rejected)
- ``tags`` - Tags list
- ``priority`` - Priority level
- ``outgoing`` - Links TO other needs
- ``incoming`` - Links FROM other needs

Requirements to Tests Table
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Requirements Coverage
   ^^^^^^^^^^^^^^^^^^^^^

   .. needtable::
      :types: req, test
      :columns: id, title, status, outgoing
      :filter: "whisper" in tags
      :style: table

This shows all requirements and tests, with the ``outgoing`` column showing which tests validate each requirement.

Creating Flow Diagrams
----------------------

needflow Directive
~~~~~~~~~~~~~~~~~~

Generate visual diagrams of need relationships:

.. code-block:: rst

   Traceability Flow
   ^^^^^^^^^^^^^^^^^

   .. needflow::
      :types: usecase, req, test
      :tags: transfer
      :show_link_names:

**Parameters:**

- ``:types:`` - Which directive types to include in diagram
- ``:tags:`` - Filter by tags
- ``:show_link_names:`` - Display link type labels on arrows
- ``:filter:`` - Advanced filtering (same as needtable)

Full Traceability Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Complete Traceability
   ^^^^^^^^^^^^^^^^^^^^^

   .. needflow::
      :types: usecase, req, nfreq, impl, test
      :tags: whisper
      :show_link_names:

This creates a Graphviz diagram showing:

- Use cases at the top
- Requirements in the middle
- Implementations and tests at the bottom
- Arrows showing relationships
- Color-coded by directive type

Focused Diagrams
~~~~~~~~~~~~~~~~

**Just requirements and tests:**

.. code-block:: rst

   .. needflow::
      :types: req, test
      :tags: recording
      :show_link_names:

**Specific requirement and its links:**

.. code-block:: rst

   .. needflow::
      :filter: id == "FR-WHISPER-001" or "FR-WHISPER-001" in links

Best Practices
--------------

ID Naming Conventions
~~~~~~~~~~~~~~~~~~~~~

**Format:** ``PREFIX-PROJECT-###``

**Examples:**

- ``FR-WHISPER-001`` - AirGap Whisper functional requirement #1
- ``NFR-DEPLOY-005`` - AirGap Deploy non-functional requirement #5
- ``TC-TRANSFER-CLI-003`` - AirGap Transfer CLI test #3
- ``UC-WHISPER-001`` - AirGap Whisper use case #1

**Rules:**

- Use project name in ID for clarity
- Sequential numbering within each type
- Add subcategory for tests (TC-CLI, TC-ERR, etc.)
- Never reuse IDs

Status Values
~~~~~~~~~~~~~

Use consistent status values:

- ``approved`` - Requirement is approved and ready for implementation
- ``pending`` - Under review, not yet approved
- ``rejected`` - Explicitly rejected, not to be implemented

Priority Values
~~~~~~~~~~~~~~~

**For requirements (MoSCoW):**

- ``must`` - Must have, critical
- ``should`` - Should have, important
- ``could`` - Could have, nice to have
- ``wont`` - Won't have this release

**For tests:**

- ``critical`` - Critical test, must pass
- ``high`` - High priority
- ``medium`` - Medium priority
- ``low`` - Low priority

Tags
~~~~

**Use hierarchical tags:**

- Project: ``whisper``, ``deploy``, ``transfer``
- Feature: ``recording``, ``transcription``, ``packaging``, ``chunking``
- Type: ``security``, ``performance``, ``usability``
- Platform: ``linux``, ``macos``, ``windows``

**Example:**

.. code-block:: rst

   :tags: whisper, recording, security, linux

Writing Good Descriptions
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Requirements:**

- Start with SHALL/SHOULD/MAY
- Be specific and measurable
- One requirement per directive
- Include acceptance criteria

**Tests:**

- Include objective, setup, steps, expected result
- Link to ALL requirements tested
- Be reproducible
- Include pass/fail criteria

**Use Cases:**

- Describe user's goal
- Include actors, preconditions, success criteria
- Link to requirements that satisfy it

Validation
----------

Build-Time Checks
~~~~~~~~~~~~~~~~~

Sphinx validates:

✅ All need IDs are unique
✅ All linked IDs exist
✅ Required options are present
✅ Status values are valid

**Error example:**

::

   WARNING: Need could not be created: A need with ID 'TC-001' already exists.
   ERROR: Unknown status 'complete' for need 'FR-WHISPER-001'

Coverage Checking
~~~~~~~~~~~~~~~~~

Use filters to find gaps:

**Untested requirements:**

.. code-block:: rst

   .. needtable::
      :types: req
      :columns: id, title
      :filter: len(is_tested_by) == 0

**Requirements without use cases:**

.. code-block:: rst

   .. needtable::
      :types: req
      :columns: id, title
      :filter: len(satisfies) == 0

Common Tasks
------------

Adding a New Requirement
~~~~~~~~~~~~~~~~~~~~~~~~

1. **Choose ID:** Next sequential number (e.g., FR-WHISPER-037)
2. **Add directive to SRS:**

   .. code-block:: rst

      .. req:: Brief Title
         :id: FR-WHISPER-037
         :status: pending
         :tags: whisper, feature-name
         :priority: should
         :satisfies: UC-WHISPER-001

         The system SHALL [specific requirement].

3. **Build docs:** ``make html``
4. **Verify:** Check traceability matrix shows new requirement

Adding a New Test Case
~~~~~~~~~~~~~~~~~~~~~~

1. **Choose ID:** Sequential in category (e.g., TC-REC-010)
2. **Add directive to testing plan:**

   .. code-block:: rst

      .. test:: Brief Title
         :id: TC-REC-010
         :status: approved
         :tags: whisper, recording
         :tests: FR-WHISPER-037
         :priority: high

         **Objective:** Verify [what]

         **Steps:**
         1. [Step 1]
         2. [Step 2]

         **Expected:** [Expected result]

3. **Build docs:** ``make html``
4. **Verify:** Requirement now shows "tested by TC-REC-010"

Updating Traceability
~~~~~~~~~~~~~~~~~~~~~

When requirements change:

1. Update the requirement directive
2. Update linked test cases
3. Update :satisfies: links if use cases changed
4. Run ``make html`` to regenerate matrices
5. Check needflow diagrams for accuracy

Troubleshooting
---------------

Duplicate ID Error
~~~~~~~~~~~~~~~~~~

**Error:**

::

   WARNING: Need could not be created: A need with ID 'TC-CLI-001' already exists.

**Solution:**

Use project prefix: ``TC-TRANSFER-CLI-001`` instead of ``TC-CLI-001``

Broken Link Error
~~~~~~~~~~~~~~~~~

**Error:**

::

   WARNING: Linked need 'FR-WHISPER-999' not found for need 'TC-REC-001'

**Solution:**

Check that:

1. The linked ID exists
2. The ID is spelled correctly
3. The linked need is in a file that's included in the build

Missing in Traceability Matrix
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Problem:** Need doesn't appear in needtable

**Solutions:**

1. Check ``:filter:`` expression matches need's tags
2. Check ``:types:`` includes need's directive type
3. Rebuild with ``make clean && make html``

Summary
-------

**Key Points:**

✅ Use directive types consistently (usecase, req, nfreq, test, impl, spec)
✅ Follow ID naming conventions (PREFIX-PROJECT-###)
✅ Link needs bidirectionally (:tests:, :implements:, :satisfies:)
✅ Use tags for filtering and organization
✅ Generate matrices with needtable
✅ Visualize with needflow
✅ Validate at build time

**Workflow:**

1. Write use cases (.. usecase::)
2. Write requirements that satisfy use cases (:satisfies:)
3. Write design specs that implement requirements (:implements:)
4. Write code with doc comments referencing requirements
5. Write tests that validate requirements (:tests:)
6. Generate matrices to verify coverage
7. Build docs to validate all links

**Result:**

Complete, validated, bidirectional traceability from use cases through requirements, design, implementation, and tests.

See Also
--------

- :doc:`/meta/traceability-matrix` - See sphinx-needs in action
- :doc:`/meta/rust-integration-guide` - Link code to requirements
- `sphinx-needs Documentation <https://sphinx-needs.readthedocs.io/>`_
- `IEEE 830-1998 <https://standards.ieee.org/standard/830-1998.html>`_ - Requirements specification standard
