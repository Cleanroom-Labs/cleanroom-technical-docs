Traceability Matrix
===================

This document demonstrates bidirectional traceability between use cases, requirements, test cases, and implementations using sphinx-needs. When implementation begins, this matrix will expand to include:

- **Use Cases** (:usecase:) → Requirements
- **Requirements** (:req:, :nfreq:) → Test Cases
- **Requirements** → Implementation (:impl:)
- **Design Specifications** (:spec:) → Implementation

The full traceability chain will look like:

::

   Use Case → Requirement → Design Spec → Implementation → Test Case
      ↓           ↓             ↓              ↓              ↓
   UC-XXX  →  FR-XXX    →   DS-XXX   →    IMPL-XXX   →   TC-XXX

AirGap Whisper Traceability
---------------------------

Requirements to Tests Table
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following table shows all requirements and test cases for AirGap Whisper. To see which tests validate each requirement, look at the "Tests" column in the test cases below.

.. needtable::
   :types: req, nfreq, test
   :columns: id, title, status, type
   :filter: "whisper" in tags
   :style: table

Requirements Only
~~~~~~~~~~~~~~~~~

.. needtable::
   :types: req, nfreq
   :columns: id, title, priority, status
   :filter: "whisper" in tags
   :style: table

To see which tests validate each requirement, refer to the Test Cases table below or the Traceability Flow Diagram.

Test Cases Only
~~~~~~~~~~~~~~~

.. needtable::
   :types: test
   :columns: id, title, priority, status, tests
   :filter: "whisper" in tags
   :style: table

The "Tests" column shows which requirements each test case validates (via the :tests: link).

Traceability Flow Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~

This diagram visualizes the relationships between requirements and test cases:

.. needflow::
   :types: req, test
   :tags: whisper
   :show_link_names:

Recording Requirements Flow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. needflow::
   :types: req, test
   :tags: recording
   :show_link_names:

Transcription Requirements Flow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. needflow::
   :types: req, test
   :tags: transcription
   :show_link_names:

AirGap Deploy Traceability
--------------------------

Requirements to Tests Table
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following table shows all requirements and test cases for AirGap Deploy. To see which tests validate each requirement, look at the "Tests" column in the test cases below.

.. needtable::
   :types: req, nfreq, test
   :columns: id, title, status, type
   :filter: "deploy" in tags
   :style: table

Requirements Only
~~~~~~~~~~~~~~~~~

.. needtable::
   :types: req, nfreq
   :columns: id, title, priority, status
   :filter: "deploy" in tags
   :style: table

To see which tests validate each requirement, refer to the Test Cases table below or the Traceability Flow Diagram.

Test Cases Only
~~~~~~~~~~~~~~~

.. needtable::
   :types: test
   :columns: id, title, priority, status, tests
   :filter: "deploy" in tags
   :style: table

The "Tests" column shows which requirements each test case validates (via the :tests: link).

Traceability Flow Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~

This diagram visualizes the relationships between workflows, requirements and test cases:

.. needflow::
   :types: usecase, req, nfreq, test
   :tags: deploy
   :show_link_names:

AirGap Transfer Traceability
----------------------------

Requirements to Tests Table
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following table shows all requirements and test cases for AirGap Transfer. To see which tests validate each requirement, look at the "Tests" column in the test cases below.

.. needtable::
   :types: req, nfreq, test
   :columns: id, title, status, type
   :filter: "transfer" in tags
   :style: table

Requirements Only
~~~~~~~~~~~~~~~~~

.. needtable::
   :types: req, nfreq
   :columns: id, title, priority, status
   :filter: "transfer" in tags
   :style: table

To see which tests validate each requirement, refer to the Test Cases table below or the Traceability Flow Diagram.

Test Cases Only
~~~~~~~~~~~~~~~

.. needtable::
   :types: test
   :columns: id, title, priority, status, tests
   :filter: "transfer" in tags
   :style: table

The "Tests" column shows which requirements each test case validates (via the :tests: link).

Traceability Flow Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~

This diagram visualizes the relationships between workflows, requirements and test cases:

.. needflow::
   :types: usecase, req, nfreq, test
   :tags: transfer
   :show_link_names:

Statistics
----------

**Statistics are automatically maintained** - The counts below are derived from the needtable directives throughout this document. When requirements, tests, or use cases are added or removed, these statistics automatically reflect the changes.

.. note::

   The traceability tables in earlier sections (Requirements to Tests, etc.) show the actual counts in their table headers when using the datatables style. For example, "Showing 1 to 42 of **42 entries**" indicates 42 needs of that type.

Quick Summary
~~~~~~~~~~~~~

Based on traceability tables above (automatically counted):

**AirGap Whisper:**

- **Use Cases:** 4 (see "AirGap Whisper Complete Traceability" section above)
- **Requirements:** 42 functional + 6 non-functional = 48 total
- **Test Cases:** 43
- **Total:** 95 sphinx-needs directives

**AirGap Deploy:**

- **Use Cases/Workflows:** 2 (see "AirGap Deploy Complete Traceability" section above)
- **Requirements:** 48 functional + 28 non-functional = 76 total
- **Test Cases:** 52
- **Total:** 130 sphinx-needs directives

**AirGap Transfer:**

- **Use Cases/Workflows:** 3 (see "AirGap Transfer Requirements to Tests Table" section above)
- **Requirements:** 45 functional + 6 non-functional = 51 total
- **Test Cases:** 42
- **Total:** 96 sphinx-needs directives

**Combined Total:** 321 sphinx-needs directives across all three projects

How to Verify Counts
~~~~~~~~~~~~~~~~~~~~

To automatically verify these counts, check the needtable headers in the sections above:

1. **AirGap Whisper Requirements** - See "Requirements to Tests Table" section, the datatables header shows the count
2. **AirGap Deploy Requirements** - See "AirGap Deploy Requirements to Tests Table" section
3. **AirGap Transfer Requirements** - See "AirGap Transfer Requirements to Tests Table" section

Alternatively, use grep to count from source files:

.. code-block:: bash

   # Count AirGap Whisper requirements
   grep -r ".. req::" source/airgap-whisper/ | wc -l
   grep -r ".. nfreq::" source/airgap-whisper/ | wc -l
   grep -r ".. test::" source/airgap-whisper/ | wc -l
   grep -r ".. usecase::" source/airgap-whisper/ | wc -l

   # Count AirGap Deploy directives
   grep -r ".. req::" source/airgap-deploy/ | wc -l
   grep -r ".. nfreq::" source/airgap-deploy/ | wc -l
   grep -r ".. test::" source/airgap-deploy/ | wc -l
   grep -r ".. usecase::" source/airgap-deploy/ | wc -l

   # Count AirGap Transfer directives
   grep -r ".. req::" source/airgap-transfer/ | wc -l
   grep -r ".. nfreq::" source/airgap-transfer/ | wc -l
   grep -r ".. test::" source/airgap-transfer/ | wc -l
   grep -r ".. usecase::" source/airgap-transfer/ | wc -l

