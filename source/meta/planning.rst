v1.1 Planning
=============

The following features are under consideration for v1.1, to be scoped after v1.0.0 release and user feedback.

**AirGap Deploy v1.1:**

- **SBOM generation:** Generate CycloneDX SBOM during ``prep`` phase from Cargo.lock dependency graph, component metadata, and license information
- **CBOM generation:** Scan dependencies for known cryptographic crates and document crypto usage as CycloneDX CBOM entries
- **Vulnerability scanning:** ``airgap-deploy scan`` subcommand that checks SBOMs against an offline vulnerability database (Grype or Trivy)

**AirGap Transfer v1.1:**

- **SBOM-aware manifests:** Reference CycloneDX SBOM files in transfer manifests for chain-of-custody documentation

**Target:** Post-v1.0.0, scope finalized based on v1.0.0 feedback and adoption patterns.

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
