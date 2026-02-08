Writing Good Specifications
===========================

This guide helps contributors write clear, testable, and well-scoped specification artifacts. It complements the artifact type definitions in :doc:`specification-overview` and the directive syntax in the :doc:`sphinx-needs-guide`.

Writing Requirements
--------------------

A good requirement is **testable**, **unambiguous**, and states a **single obligation**.

.. raw:: html

   <div style="margin-top: 1.5em;"></div>

**Use IEEE 830 language conventions:**

- **SHALL** for mandatory behavior
- **SHOULD** for recommended behavior
- **MAY** for optional behavior

.. raw:: html

   <div style="margin-top: 1.5em;"></div>

**Make requirements measurable.** A requirement that cannot be verified by a test is not a requirement — it is a wish.

- Bad: "The system shall be fast"
- Good: "The system SHALL complete pack operations at a rate of at least 100 MB/s for files 1 GB or larger"

.. raw:: html

   <div style="margin-top: 1.5em;"></div>

- Bad: "The system shall handle errors gracefully"
- Good: "The system SHALL display a human-readable error message and exit with non-zero status when the source file does not exist"

.. raw:: html

   <div style="margin-top: 1.5em;"></div>

**One obligation per requirement.** If a requirement contains "and" joining two distinct behaviors, split it into two requirements. "The system shall pack and verify files" should become two separate requirements — one for packing, one for verification.

.. raw:: html

   <div style="margin-top: 1.5em;"></div>

**Functional vs. non-functional:** If a requirement describes *what the system does*, it is functional (``:req:``). If it describes *how well* the system performs — covering performance, security, usability, or portability — it is non-functional (``:nfreq:``).

Writing Use Cases
-----------------

A use case describes a **user's goal**, not a system behavior.

.. raw:: html

   <div style="margin-top: 1.5em;"></div>

**Include:**

- **Actor:** Who is performing the action (e.g., "IT administrator", "privacy-conscious user")
- **Preconditions:** What must be true before the use case begins
- **Main flow:** The steps the user takes to accomplish their goal
- **Success criteria:** How the user knows they succeeded

.. raw:: html

   <div style="margin-top: 1.5em;"></div>

**Granularity:** One use case per distinct user goal. "Transfer a large file across an air gap" is a use case. "Click the pack button" is not — that is a UI interaction within a use case.

.. raw:: html

   <div style="margin-top: 1.5em;"></div>

Use cases are the starting point of the traceability chain. Requirements derive from use cases (linked via ``:satisfies:``). Avoid implementation details in use cases — those belong in design specifications.

Writing Test Cases
------------------

A test case verifies that a **requirement** is satisfied. It does not restate the requirement — it describes how to prove the requirement is met.

.. raw:: html

   <div style="margin-top: 1.5em;"></div>

**Structure each test case with:**

- **Objective:** What this test verifies (reference the requirement)
- **Setup/Preconditions:** What must be in place before the test runs
- **Steps:** The specific actions to perform, in order
- **Expected result:** The observable outcome that constitutes a pass
- **Pass/fail criteria:** How to distinguish success from failure

.. raw:: html

   <div style="margin-top: 1.5em;"></div>

Each test should be **reproducible** by someone who did not write it. Avoid "verify it works correctly" — state the specific expected output.

.. raw:: html

   <div style="margin-top: 1.5em;"></div>

One test can cover multiple requirements (``:tests: FR-XXX, FR-YYY``), but every requirement should have at least one test. Use the :doc:`traceability matrices <specification-overview>` to identify untested requirements.

Writing Design Specifications
-----------------------------

Design specifications bridge requirements and implementation. They describe **how** the system fulfills its requirements and **why** a particular approach was chosen.

.. raw:: html

   <div style="margin-top: 1.5em;"></div>

**Include:**

- Architecture decisions and their rationale
- Data structures and formats
- Algorithm choices and trade-offs
- Component interfaces and boundaries

.. raw:: html

   <div style="margin-top: 1.5em;"></div>

A design spec should not restate the requirement. Where the requirement says "the system shall verify file integrity," the design spec says "use SHA-256 checksums stored in a JSON manifest file." Link to the requirements being addressed using the ``:implements:`` option.

Common Mistakes
---------------

- **Requirements that are really design specs:** "The system shall use SHA-256 for checksums" specifies *how*, not *what*. The requirement is "the system shall verify file integrity"; the algorithm choice belongs in the design spec.
- **Test cases that restate requirements:** "Verify that the system splits files into chunks" is a requirement restated as a test. A proper test specifies: create a 50GB file, run pack, verify 4 chunks of expected size are created with valid checksums.
- **Use cases that are too granular:** System-level actions ("parse the manifest file") are not use cases. Use cases describe user goals ("deploy an application to an air-gapped system").
- **Missing traceability links:** Orphaned requirements with no tests, or tests that don't link back to requirements, break the traceability chain. Run a docs build and check the untested requirements table in :doc:`specification-overview` to catch these.

See Also
--------

- :doc:`specification-overview` - Artifact type definitions and the traceability chain
- :doc:`standards-framework` - IEEE standards alignment and the artifact type schema
- :doc:`sphinx-needs-guide` - Directive syntax, linking, and best practices
