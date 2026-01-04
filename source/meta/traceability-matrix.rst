Traceability Matrix
===================

This document demonstrates bidirectional traceability between use cases, requirements, test cases, and implementations using sphinx-needs.

Phase 1 Demo: AirGap Whisper
-----------------------------

This initial traceability matrix shows a subset of AirGap Whisper requirements and their associated test cases as a proof-of-concept.

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

All Other Projects
------------------

.. note::

   Traceability for **airgap-deploy** and **airgap-transfer** will be added in Phase 2 and Phase 3 of the Sphinx migration.

Statistics
----------

Current traceability coverage:

- **Requirements documented:** 10 (FR-WHISPER-001 through FR-WHISPER-012)
- **Test cases documented:** 10 (TC-REC-001 through TC-TRS-005)
- **Traceability links:** 10 (each test linked to requirement)
- **Coverage:** 100% of documented requirements have tests

.. note::

   This is a Phase 1 proof-of-concept. Full traceability will include all 156 requirements across 3 projects.
