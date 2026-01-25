Requirements Overview
=====================

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

Project Statistics
------------------

This section provides an aggregate overview of all sphinx-needs directives across the AirGap Project Suite. Statistics are automatically maintained using sphinx-needs' need_count directive.

.. note::

   For detailed per-project traceability tables showing which tests validate each requirement, see each project's Test Plan:

   - :doc:`cleanroom-whisper:testing/plan` (Cleanroom Whisper Traceability)
   - :doc:`airgap-deploy:testing/plan` (AirGap Deploy Traceability)
   - :doc:`airgap-transfer:testing/plan` (AirGap Transfer Traceability)

Cleanroom Whisper
~~~~~~~~~~~~~~~~~

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

AirGap Deploy
~~~~~~~~~~~~~

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

AirGap Transfer
~~~~~~~~~~~~~~~

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

