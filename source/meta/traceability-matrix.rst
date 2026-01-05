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

The following charts and tables are **automatically generated** from sphinx-needs directives and update dynamically as requirements, tests, and use cases are added or modified.

AirGap Whisper Statistics
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. needpie:: AirGap Whisper Need Distribution
   :tags: whisper
   :legend:
   :shadow:

The pie chart above automatically counts and visualizes all sphinx-needs directives tagged with "whisper".

AirGap Deploy Statistics
~~~~~~~~~~~~~~~~~~~~~~~~~

.. needpie:: AirGap Deploy Need Distribution
   :tags: deploy
   :legend:
   :shadow:

The pie chart above automatically counts and visualizes all sphinx-needs directives tagged with "deploy".

AirGap Transfer Statistics
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. needpie:: AirGap Transfer Need Distribution
   :tags: transfer
   :legend:
   :shadow:

The pie chart above automatically counts and visualizes all sphinx-needs directives tagged with "transfer".

Combined Project Statistics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. needpie:: All Projects Need Distribution by Type
   :legend:
   :shadow:

The pie chart above shows the distribution of all sphinx-needs directives across all three projects, automatically counting use cases, requirements (functional and non-functional), and test cases.

