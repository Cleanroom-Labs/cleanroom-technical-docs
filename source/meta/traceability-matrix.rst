Traceability Matrix
===================

This document demonstrates bidirectional traceability between use cases, requirements, test cases, and implementations using sphinx-needs.

AirGap Whisper Complete Traceability
-------------------------------------

This section demonstrates complete bidirectional traceability for AirGap Whisper with all requirements, use cases, and test cases linked.

AirGap Deploy Complete Traceability
------------------------------------

This section demonstrates complete bidirectional traceability for AirGap Deploy with all requirements, workflows, and test cases linked.

Requirements to Tests Table
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following table shows all requirements and test cases for AirGap Whisper, along with their traceability links:

.. needtable::
   :types: req, test
   :columns: id, title, status, tags, outgoing
   :filter: "whisper" in tags
   :style: table

Requirements Only
~~~~~~~~~~~~~~~~~

.. needtable::
   :types: req
   :columns: id, title, priority, status
   :filter: "whisper" in tags
   :style: table

Test Cases Only
~~~~~~~~~~~~~~~

.. needtable::
   :types: test
   :columns: id, title, priority, status, outgoing
   :filter: "whisper" in tags
   :style: table

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

AirGap Deploy Requirements to Tests Table
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following table shows all requirements and test cases for AirGap Deploy:

.. needtable::
   :types: req, nfreq, test
   :columns: id, title, status, tags, outgoing
   :filter: "deploy" in tags
   :style: table

AirGap Deploy Requirements Only
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. needtable::
   :types: req, nfreq
   :columns: id, title, priority, status
   :filter: "deploy" in tags
   :style: table

AirGap Deploy Test Cases Only
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. needtable::
   :types: test
   :columns: id, title, priority, status, outgoing
   :filter: "deploy" in tags
   :style: table

AirGap Deploy Traceability Flow Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This diagram visualizes the relationships between workflows, requirements and test cases:

.. needflow::
   :types: usecase, req, nfreq, test
   :tags: deploy
   :show_link_names:

AirGap Transfer Requirements to Tests Table
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following table shows all requirements and test cases for AirGap Transfer:

.. needtable::
   :types: req, nfreq, test
   :columns: id, title, status, tags, outgoing
   :filter: "transfer" in tags
   :style: table

AirGap Transfer Requirements Only
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. needtable::
   :types: req, nfreq
   :columns: id, title, priority, status
   :filter: "transfer" in tags
   :style: table

AirGap Transfer Test Cases Only
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. needtable::
   :types: test
   :columns: id, title, priority, status, outgoing
   :filter: "transfer" in tags
   :style: table

AirGap Transfer Traceability Flow Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This diagram visualizes the relationships between workflows, requirements and test cases:

.. needflow::
   :types: usecase, req, nfreq, test
   :tags: transfer
   :show_link_names:

Future Traceability
-------------------

When implementation begins, this matrix will expand to include:

- **Use Cases** (:usecase:) → Requirements
- **Requirements** (:req:, :nfreq:) → Test Cases
- **Requirements** → Implementation (:impl:)
- **Design Specifications** (:spec:) → Implementation

Complete Traceability Chain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The full traceability chain will look like:

::

   Use Case → Requirement → Design Spec → Implementation → Test Case
      ↓           ↓             ↓              ↓              ↓
   UC-XXX  →  FR-XXX    →   DS-XXX   →    IMPL-XXX   →   TC-XXX

Statistics
----------

The following tables are **automatically generated** from sphinx-needs directives and update dynamically as requirements, tests, and use cases are added or modified.

AirGap Whisper Statistics
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. needtable::
   :types: usecase, req, nfreq, test
   :columns: type
   :filter: "whisper" in tags
   :style: table
   :sort: type

**Total AirGap Whisper Needs:** The table above shows all sphinx-needs directive types for AirGap Whisper (automatically counted).

AirGap Deploy Statistics
~~~~~~~~~~~~~~~~~~~~~~~~~

.. needtable::
   :types: usecase, req, nfreq, test
   :columns: type
   :filter: "deploy" in tags
   :style: table
   :sort: type

**Total AirGap Deploy Needs:** The table above shows all sphinx-needs directive types for AirGap Deploy (automatically counted).

AirGap Transfer Statistics
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. needtable::
   :types: usecase, req, nfreq, test
   :columns: type
   :filter: "transfer" in tags
   :style: table
   :sort: type

**Total AirGap Transfer Needs:** The table above shows all sphinx-needs directive types for AirGap Transfer (automatically counted).

Summary Statistics
~~~~~~~~~~~~~~~~~~

The following tables provide automatic counts by project:

**AirGap Whisper:**

.. needtable::
   :types: usecase
   :columns: id, title
   :filter: "whisper" in tags
   :style: datatables

Use Cases: Shows count in table header

.. needtable::
   :types: req, nfreq
   :columns: id, title
   :filter: "whisper" in tags
   :style: datatables

Requirements (Functional + Non-Functional): Shows count in table header

.. needtable::
   :types: test
   :columns: id, title
   :filter: "whisper" in tags
   :style: datatables

Test Cases: Shows count in table header

**AirGap Deploy:**

.. needtable::
   :types: usecase
   :columns: id, title
   :filter: "deploy" in tags
   :style: datatables

Use Cases/Workflows: Shows count in table header

.. needtable::
   :types: req, nfreq
   :columns: id, title
   :filter: "deploy" in tags
   :style: datatables

Requirements (Functional + Non-Functional): Shows count in table header

.. needtable::
   :types: test
   :columns: id, title
   :filter: "deploy" in tags
   :style: datatables

Test Cases: Shows count in table header

**AirGap Transfer:**

.. needtable::
   :types: usecase
   :columns: id, title
   :filter: "transfer" in tags
   :style: datatables

Use Cases/Workflows: Shows count in table header

.. needtable::
   :types: req, nfreq
   :columns: id, title
   :filter: "transfer" in tags
   :style: datatables

Requirements (Functional + Non-Functional): Shows count in table header

.. needtable::
   :types: test
   :columns: id, title
   :filter: "transfer" in tags
   :style: datatables

Test Cases: Shows count in table header

