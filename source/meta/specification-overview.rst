Specification Overview
======================

This document provides an aggregate overview of requirements, test cases, and traceability across the Cleanroom Labs technical documentation using sphinx-needs.

Artifact Types
--------------

Each project's documentation is organized around five artifact types that serve distinct roles in the development process. The structure draws on IEEE 830 (SRS) for requirements, IEEE 1016 (SDD) for design specifications, and IEEE 829 for test documentation, adapted to the scale of these projects. For details on how these standards inform the documentation structure, see :doc:`standards-framework`.

.. raw:: html

   <div style="margin-top: 1.5em;"></div>

**Use Case** (``:usecase:``)
   Describes a goal a user wants to accomplish and the scenario in which they accomplish it. Use cases capture *who* needs *what* and *why*, without prescribing implementation details. They are the starting point for identifying what the software must do.

.. raw:: html

   <div style="margin-top: 1.5em;"></div>

**Requirement** (``:req:``, ``:nfreq:``)
   A precise, testable statement of what the system shall do (functional) or how well it shall perform (non-functional). Requirements translate the intent of use cases into concrete obligations. The boundary between a use case and a requirement can be fuzzy — the key distinction is that a requirement is specific enough to verify, while a use case describes a broader user goal.

.. raw:: html

   <div style="margin-top: 1.5em;"></div>

**Design Specification** (``:spec:``)
   Documents *how* the system fulfills its requirements — architecture, data structures, algorithms, and component interfaces. Where a requirement says "the system shall verify file integrity," a design spec says "use SHA-256 checksums stored in a manifest file." The line between a detailed requirement and a high-level design spec can blur; in practice, the requirement focuses on observable behavior while the spec focuses on internal structure.

.. raw:: html

   <div style="margin-top: 1.5em;"></div>

**Implementation** (``:impl:``)
   A reference to the actual code or artifact that realizes a design specification. Implementation records connect the documentation to the codebase, enabling traceability from user need to source code.

.. raw:: html

   <div style="margin-top: 1.5em;"></div>

**Test Case** (``:test:``)
   A procedure that verifies a requirement is satisfied. Each test case links back to the requirement(s) it validates, closing the traceability loop.

Traceability Chain
------------------

The idealized development flow follows a waterfall-style sequence:

.. raw:: html

   <div style="margin-top: 1.5em;"></div>

::

   Use Case → Requirement → Design Spec → Implementation → Test Case
      ↓           ↓             ↓              ↓              ↓
   UC-XXX   →   FR-XXX    →   DS-XXX    →   IMPL-XXX     →  TC-XXX

In practice, this sequence is not strictly followed. Requirements and design specs often evolve together, test cases may be written before implementation (TDD), and use cases may be refined after early prototyping reveals new constraints. The chain represents the logical dependency between artifacts — each artifact type answers questions raised by the one before it — rather than a rigid process order.

.. raw:: html

   <div style="margin-top: 1.5em;"></div>

.. note::

   Currently, the projects track use cases, requirements, loose descriptions of design specifications, and preliminary test plans with some identified cases. Implementation traceability will be added as the software is developed. The design specifications may be formalized as the projects mature.

Traceability Matrices
---------------------

The following tables provide a cross-project view of requirements coverage, automatically generated from sphinx-needs directives across all project submodules.

Requirements Coverage
~~~~~~~~~~~~~~~~~~~~~

All approved requirements with their linked test cases:

.. needtable::
   :types: req, nfreq
   :columns: id, title, priority, tests_back
   :filter: status=='approved'
   :style: table
   :sort: id

Untested Requirements
~~~~~~~~~~~~~~~~~~~~~

Requirements that do not yet have linked test cases:

.. needtable::
   :types: req, nfreq
   :columns: id, title, priority
   :filter: status=='approved' and len(tests_back) == 0
   :style: table
   :sort: id

.. seealso::

   For aggregate project statistics (artifact counts per project), see :doc:`project-statistics`.

