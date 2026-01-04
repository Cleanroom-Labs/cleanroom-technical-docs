AirGap Deploy API Reference
============================

.. note::

   API documentation will be auto-generated from Rust source code once implementation begins.

Future Documentation
--------------------

Planned modules based on :doc:`/airgap-deploy/design/sdd`:

- ``cli`` - Command-line interface
- ``cargo`` - Cargo workspace management
- ``vendor`` - Dependency vendoring
- ``package`` - Archive creation

Integration Instructions
-------------------------

Once Rust code exists:

1. Add doc comments to all public items
2. Run ``cargo doc --no-deps``
3. Integrate with Sphinx using sphinxcontrib-rust
