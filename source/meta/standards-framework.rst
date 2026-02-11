Documentation Standards Framework
==================================

This document defines the standards and artifact types that underpin the Cleanroom Labs specification process.

IEEE Standards Alignment
------------------------

Each project's technical documents are loosely modeled on IEEE standards for structure and content guidance:

- **SRS** (Software Requirements Specification) — informed by `IEEE 830-1998 <https://standards.ieee.org/standard/830-1998.html>`_
- **SDD** (Software Design Document) — informed by `IEEE 1016-2009 <https://standards.ieee.org/standard/1016-2009.html>`_
- **Test Plan** — informed by `IEEE 829-2008 <https://standards.ieee.org/standard/829-2008.html>`_

These standards serve as structural guides, not strict compliance targets. The projects adopt the general document outline (Introduction, Scope, Definitions, etc.) while keeping content lean and MVP-focused.

.. _artifact-type-schema:

Artifact Type Schema
--------------------

The Cleanroom Labs project suite uses 6 sphinx-needs directive types to represent engineering artifacts:

.. list-table::
   :header-rows: 1
   :widths: 20 15 15 50

   * - Directive
     - Prefix
     - Color
     - Purpose
   * - ``usecase``
     - ``UC``
     - Blue
     - User stories and workflow descriptions
   * - ``req``
     - ``FR``
     - Orange
     - Functional requirements
   * - ``nfreq``
     - ``NFR``
     - Dark Orange
     - Non-functional requirements (performance, security, etc.)
   * - ``spec``
     - ``DS``
     - Yellow
     - Design specifications
   * - ``impl``
     - ``IMPL``
     - Purple
     - Code implementations (future)
   * - ``test``
     - ``TC``
     - Green
     - Test cases

For detailed descriptions of each artifact type and the traceability chain that connects them, see :doc:`specification-overview`.

How Standards Are Applied
-------------------------

Each project maintains three standards-informed documents:

- **SRS** — found at ``requirements/srs.rst`` in each project submodule
- **SDD** — found at ``design/sdd.rst`` in each project submodule
- **Test Plan** — found at ``testing/plan.rst`` in each project submodule

These documents follow the general structure of their respective IEEE standards while remaining adapted to the scale of the projects. For the technical details of authoring and linking specification artifacts, see the :doc:`sphinx-needs-guide`.

See Also
--------

- :doc:`specification-overview` - Artifact types in depth and the traceability chain
- :doc:`sphinx-needs-guide` - Technical guide for creating and linking needs directives
- `sphinx-needs Documentation <https://sphinx-needs.readthedocs.io/>`_
