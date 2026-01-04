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

   Traceability for **AirGap Deploy** and **AirGap Transfer** will be added in Phase 2 and Phase 3 of the Sphinx migration.

Statistics
----------

AirGap Whisper Traceability Coverage:

- **Use Cases:** 4 (UC-WHISPER-001 through UC-WHISPER-004)
- **Functional Requirements:** 36 (FR-WHISPER-001 through FR-WHISPER-036)
- **Non-Functional Requirements:** 6 (NFR-WHISPER-001 through NFR-WHISPER-006)
- **Test Cases:** 43 (TC-REC-001 through TC-NFR-004)
- **Total Needs:** 89 sphinx-needs directives
- **Traceability Links:** 43 requirement-to-test links
- **Coverage:** 100% of requirements have associated test cases

AirGap Deploy Traceability Coverage:

- **Use Cases/Workflows:** 2 (UC-DEPLOY-001 through UC-DEPLOY-002)
- **Functional Requirements:** 48 (FR-DEPLOY-001 through FR-DEPLOY-048)
- **Non-Functional Requirements:** 28 (NFR-DEPLOY-001 through NFR-DEPLOY-028)
- **Test Cases:** 52 (TC-MAN-001 through TC-DEPLOY-SEC-004)
- **Total Needs:** 130 sphinx-needs directives
- **Traceability Links:** 52+ requirement-to-test links
- **Coverage:** 100% of requirements have associated test cases

Project Status:

- **AirGap Whisper:** ✅ Complete (42 requirements, 4 use cases, 43 tests) = 89 directives
- **AirGap Deploy:** ✅ Complete (76 requirements, 2 workflows, 52 tests) = 130 directives
- **AirGap Transfer:** ⏳ Pending (51 requirements, 3 workflows, ~100 tests)

.. note::

   Phase 3 in progress. AirGap Whisper and AirGap Deploy demonstrate complete bidirectional traceability.
   AirGap Transfer will be completed next.
