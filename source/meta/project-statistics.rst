Project Statistics
==================

This page provides an aggregate overview of approved sphinx-needs directives across Cleanroom Lab's project suite. Statistics are automatically maintained using sphinx-needs' need_count directive. Proposed items for future releases are tracked in the :doc:`Release Roadmap <release-roadmap>`.

AirGap Transfer
---------------

**Project docs:** :doc:`Use Cases <airgap-transfer:use-cases/index>` · :doc:`Requirements (SRS) <airgap-transfer:requirements/srs>` · :doc:`Design (SDD) <airgap-transfer:design/sdd>` · :doc:`Test Plan <airgap-transfer:testing/plan>`

================= ======================================================================================
Category          Count
================= ======================================================================================
Use Cases         :need_count:`type=='usecase' and 'transfer' in tags and status=='approved'`
Requirements      :need_count:`type in ['req', 'nfreq'] and 'transfer' in tags and status=='approved'`
  Functional      :need_count:`type=='req' and 'transfer' in tags and status=='approved'`
  Non-Functional  :need_count:`type=='nfreq' and 'transfer' in tags and status=='approved'`
Test Cases        :need_count:`type=='test' and 'transfer' in tags and status=='approved'`
**Total**         :need_count:`'transfer' in tags and status=='approved'`
================= ======================================================================================

AirGap Deploy
-------------

**Project docs:** :doc:`Use Cases <airgap-deploy:use-cases/index>` · :doc:`Requirements (SRS) <airgap-deploy:requirements/srs>` · :doc:`Design (SDD) <airgap-deploy:design/sdd>` · :doc:`Test Plan <airgap-deploy:testing/plan>`

================= ======================================================================================
Category          Count
================= ======================================================================================
Use Cases         :need_count:`type=='usecase' and 'deploy' in tags and status=='approved'`
Requirements      :need_count:`type in ['req', 'nfreq'] and 'deploy' in tags and status=='approved'`
  Functional      :need_count:`type=='req' and 'deploy' in tags and status=='approved'`
  Non-Functional  :need_count:`type=='nfreq' and 'deploy' in tags and status=='approved'`
Test Cases        :need_count:`type=='test' and 'deploy' in tags and status=='approved'`
**Total**         :need_count:`'deploy' in tags and status=='approved'`
================= ======================================================================================

Cleanroom Whisper
-----------------

**Project docs:** :doc:`Use Cases <cleanroom-whisper:use-cases/index>` · :doc:`Requirements (SRS) <cleanroom-whisper:requirements/srs>` · :doc:`Design (SDD) <cleanroom-whisper:design/sdd>` · :doc:`Test Plan <cleanroom-whisper:testing/plan>`

================= ======================================================================================
Category          Count
================= ======================================================================================
Use Cases         :need_count:`type=='usecase' and 'whisper' in tags and status=='approved'`
Requirements      :need_count:`type in ['req', 'nfreq'] and 'whisper' in tags and status=='approved'`
  Functional      :need_count:`type=='req' and 'whisper' in tags and status=='approved'`
  Non-Functional  :need_count:`type=='nfreq' and 'whisper' in tags and status=='approved'`
Test Cases        :need_count:`type=='test' and 'whisper' in tags and status=='approved'`
**Total**         :need_count:`'whisper' in tags and status=='approved'`
================= ======================================================================================

Suite-Wide Summary
------------------

=================== ======================================================================================
Category            Count
=================== ======================================================================================
Total Use Cases     :need_count:`type=='usecase' and status=='approved'`
Total Requirements  :need_count:`type in ['req', 'nfreq'] and status=='approved'`
Total Test Cases    :need_count:`type=='test' and status=='approved'`
**Grand Total**     :need_count:`status=='approved'`
=================== ======================================================================================

See Also
--------

- :doc:`specification-overview` - Artifact type definitions and traceability chain
- :doc:`release-roadmap` - Release planning and milestone tracking
