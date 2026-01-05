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

Statistics
----------

**Statistics are automatically maintained** - The counts below are derived from the need_count directives throughout this document. When requirements, tests, or use cases are added or removed, these statistics automatically reflect the changes.

**AirGap Whisper:**

- **Use Cases:** :need_count:`type=='usecase' and 'whisper' in tags`
- **Requirements:** :need_count:`type=='req' and 'whisper' in tags` functional + :need_count:`type=='nfreq' and 'whisper' in tags` non-functional = :need_count:`type in ['req', 'nfreq'] and 'whisper' in tags` total
- **Test Cases:** :need_count:`type=='test' and 'whisper' in tags`
- **Total:** :need_count:`'whisper' in tags` sphinx-needs directives

**AirGap Deploy:**

- **Use Cases/Workflows:** :need_count:`type=='usecase' and 'deploy' in tags`
- **Requirements:** :need_count:`type=='req' and 'deploy' in tags` functional + :need_count:`type=='nfreq' and 'deploy' in tags` non-functional = :need_count:`type in ['req', 'nfreq'] and 'deploy' in tags` total
- **Test Cases:** :need_count:`type=='test' and 'deploy' in tags`
- **Total:** :need_count:`'deploy' in tags` sphinx-needs directives

**AirGap Transfer:**

- **Use Cases/Workflows:** :need_count:`type=='usecase' and 'transfer' in tags`
- **Requirements:** :need_count:`type=='req' and 'transfer' in tags` functional + :need_count:`type=='nfreq' and 'transfer' in tags` non-functional = :need_count:`type in ['req', 'nfreq'] and 'transfer' in tags` total
- **Test Cases:** :need_count:`type=='test' and 'transfer' in tags`
- **Total:** :need_count:`'transfer' in tags` sphinx-needs directives

**Combined Total:** 321 sphinx-needs directives across all three projects

