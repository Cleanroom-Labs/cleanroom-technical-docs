v1.1 Planning
=============

The following features are under consideration for v1.1. The v1.1 theme is **software supply chain security** — a natural extension of the air-gap deployment workflow. When deploying software to air-gapped environments, verifying the integrity and provenance of every component is critical. SBOM generation, cryptographic bill-of-materials tracking, and offline vulnerability scanning address this need directly.

AirGap Deploy v1.1
-------------------

- **SBOM generation:** Generate CycloneDX SBOM during ``prep`` phase from Cargo.lock dependency graph, component metadata, and license information
- **CBOM generation:** Scan dependencies for known cryptographic crates and document crypto usage as CycloneDX CBOM entries
- **Vulnerability scanning:** ``airgap-deploy scan`` subcommand that checks SBOMs against an offline vulnerability database (Grype or Trivy)

AirGap Transfer v1.1
---------------------

- **SBOM-aware manifests:** Reference CycloneDX SBOM files in transfer manifests for chain-of-custody documentation

Cleanroom Whisper v1.1
----------------------

No v1.1 features are currently planned for Cleanroom Whisper. Whisper's v1.0.0 scope is self-contained, and post-v1.0.0 priorities will depend on user feedback and adoption patterns. Possible future directions include additional output format support and export options, but no commitments are made at this stage.

Timeline
--------

The v1.1 scope will be finalized after v1.0.0 release and initial user feedback. No target date has been set. Per the :doc:`release philosophy <release-philosophy>`, AirGap Deploy and Transfer minor releases are coordinated while Cleanroom Whisper releases independently.

See individual project SRS documents for detailed requirements (tagged ``v1.1``).

Proposed Artifacts
------------------

The following tables list all proposed sphinx-needs artifacts for v1.1. These items are not yet approved and may change based on v1.0.0 feedback.

AirGap Deploy
~~~~~~~~~~~~~

.. needtable::
   :columns: id, title, type, priority, status
   :filter: status=='proposed' and 'deploy' in tags
   :style: table
   :sort: id

AirGap Transfer
~~~~~~~~~~~~~~~

.. needtable::
   :columns: id, title, type, priority, status
   :filter: status=='proposed' and 'transfer' in tags
   :style: table
   :sort: id
