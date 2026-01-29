Specification Overview
======================

This document provides an aggregate overview of requirements, test cases, and traceability across the Cleanroom Labs technical documentation using sphinx-needs. When implementation begins, this overview will expand to include:

- **Use Cases** (``:usecase:``) → Requirements
- **Requirements** (``:req:``, ``:nfreq:``) → Test Cases
- **Requirements** → Implementation (``:impl:``)
- **Design Specifications** (``:spec:``) → Implementation

The full traceability chain will look like:

::

   Use Case → Requirement → Design Spec → Implementation → Test Case
      ↓           ↓             ↓              ↓              ↓
   UC-XXX   →   FR-XXX    →   DS-XXX    →   IMPL-XXX     →  TC-XXX

.. Import needs from subprojects for aggregation (built first by Makefile)

.. needimport:: ../../cleanroom-whisper-docs/build/html/needs.json
   :hide:

.. needimport:: ../../airgap-deploy-docs/build/html/needs.json
   :hide:

.. needimport:: ../../airgap-transfer-docs/build/html/needs.json
   :hide:

Project Statistics
------------------

This section provides an aggregate overview of all sphinx-needs directives across Cleanroom Lab's project suite. Statistics are automatically maintained using sphinx-needs' need_count directive.

AirGap Transfer
~~~~~~~~~~~~~~~

**Project docs:** :doc:`Use Cases <airgap-transfer:use-cases/index>` · :doc:`Requirements (SRS) <airgap-transfer:requirements/srs>` · :doc:`Design (SDD) <airgap-transfer:design/sdd>` · :doc:`Test Plan <airgap-transfer:testing/plan>`

================= ======================================================================================
Category          Count
================= ======================================================================================
Use Cases         :need_count:`type=='usecase' and 'transfer' in tags`
Requirements      :need_count:`type in ['req', 'nfreq'] and 'transfer' in tags`
  Functional      :need_count:`type=='req' and 'transfer' in tags`
  Non-Functional  :need_count:`type=='nfreq' and 'transfer' in tags`
Test Cases        :need_count:`type=='test' and 'transfer' in tags`
**Total**         :need_count:`'transfer' in tags`
================= ======================================================================================

AirGap Deploy
~~~~~~~~~~~~~

**Project docs:** :doc:`Use Cases <airgap-deploy:use-cases/index>` · :doc:`Requirements (SRS) <airgap-deploy:requirements/srs>` · :doc:`Design (SDD) <airgap-deploy:design/sdd>` · :doc:`Test Plan <airgap-deploy:testing/plan>`

================= ======================================================================================
Category          Count
================= ======================================================================================
Use Cases         :need_count:`type=='usecase' and 'deploy' in tags`
Requirements      :need_count:`type in ['req', 'nfreq'] and 'deploy' in tags`
  Functional      :need_count:`type=='req' and 'deploy' in tags`
  Non-Functional  :need_count:`type=='nfreq' and 'deploy' in tags`
Test Cases        :need_count:`type=='test' and 'deploy' in tags`
**Total**         :need_count:`'deploy' in tags`
================= ======================================================================================

Cleanroom Whisper
~~~~~~~~~~~~~~~~~

**Project docs:** :doc:`Use Cases <cleanroom-whisper:use-cases/index>` · :doc:`Requirements (SRS) <cleanroom-whisper:requirements/srs>` · :doc:`Design (SDD) <cleanroom-whisper:design/sdd>` · :doc:`Test Plan <cleanroom-whisper:testing/plan>`

================= ======================================================================================
Category          Count
================= ======================================================================================
Use Cases         :need_count:`type=='usecase' and 'whisper' in tags`
Requirements      :need_count:`type in ['req', 'nfreq'] and 'whisper' in tags`
  Functional      :need_count:`type=='req' and 'whisper' in tags`
  Non-Functional  :need_count:`type=='nfreq' and 'whisper' in tags`
Test Cases        :need_count:`type=='test' and 'whisper' in tags`
**Total**         :need_count:`'whisper' in tags`
================= ======================================================================================

Suite-Wide Summary
~~~~~~~~~~~~~~~~~~

=================== ======================================================================================
Category            Count
=================== ======================================================================================
Total Use Cases     :need_count:`type=='usecase'`
Total Requirements  :need_count:`type in ['req', 'nfreq']`
Total Test Cases    :need_count:`type=='test'`
**Grand Total**     :need_count:`True`
=================== ======================================================================================

