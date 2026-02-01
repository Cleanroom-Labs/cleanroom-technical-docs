Scope & Limitations
===================

Scope of the AirGap Suite
--------------------------

The AirGap suite provides tools for operating in air-gapped environments — systems with no network connectivity. The three projects address complementary needs:

- **AirGap Deploy** packages applications and their dependencies for offline installation
- **AirGap Transfer** moves large files across air-gaps using removable media
- **Cleanroom Whisper** provides private, offline audio transcription

For detailed architecture and project relationships, see :doc:`meta-architecture`.

Limits of Applicability
-----------------------

AirGap Transfer
~~~~~~~~~~~~~~~

- Not a backup solution — provides no versioning, retention policies, or scheduled operations
- Not a replacement for network file transfer where network connectivity exists
- Not suitable for real-time synchronization or incremental updates
- Designed for batch transfer of large files via removable media

AirGap Deploy
~~~~~~~~~~~~~

- MVP is limited to the Rust ecosystem and select external binaries — not a general-purpose package manager
- Not a container runtime or orchestration tool
- Does not manage running applications after installation
- Does not replace system package managers (apt, dnf, brew); it complements them for offline scenarios

Cleanroom Whisper
~~~~~~~~~~~~~~~~~

- Transcription accuracy depends on the underlying whisper.cpp engine and selected model
- Not a replacement for professional transcription services where certified accuracy is required
- No real-time or streaming transcription — operates in batch mode on recorded audio
- Model quality and language support are determined by upstream Whisper model releases

--------------

Disclaimer of Warranty
----------------------

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NONINFRINGEMENT. THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE SOFTWARE IS WITH YOU. SHOULD THE SOFTWARE PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING, REPAIR, OR CORRECTION.

.. raw:: html

   <div style="margin-top: 1.5em;"></div>

See the AGPL-3.0 license (Section 15) for the complete warranty disclaimer.

Limitation of Liability
-----------------------

IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR CONVEYS THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE OR INABILITY TO USE THE PROGRAM, EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

.. raw:: html

   <div style="margin-top: 1.5em;"></div>

See the AGPL-3.0 license (Section 16) for the complete limitation of liability.

--------------

Security Considerations
-----------------------

Use of AirGap tools does **not** guarantee that an air-gapped system cannot be compromised. These tools are part of a defense-in-depth approach and must be combined with:

- **Operational security practices** — verified procedures for transferring media between environments
- **Physical security** — controlled access to air-gapped systems and removable media
- **Supply chain verification** — validating the integrity of software and dependencies before transfer
- **Endpoint hardening** — OS-level security configurations on both source and destination systems

The AirGap suite helps enforce data locality and offline operation at the application level. It does not protect against threats at the hardware, firmware, or operating system level.

.. raw:: html

   <div style="margin-top: 1.5em;"></div>

