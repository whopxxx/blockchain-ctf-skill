# Solana Analysis

Determine whether the program uses Anchor or raw Solana APIs, then inspect the deployed program ID, account schemas, instruction encoding, token program variants, and test validator configuration.

## Account and Authority Model

For every instruction account, verify:

- expected owner and executable status;
- signer and writable requirements;
- PDA seeds, bump, program ID, and canonical derivation assumptions;
- discriminator, data length, initialization state, and serialization bounds;
- mint, token authority, delegate, close authority, and token-program identity;
- whether duplicate or aliased accounts change assumptions;
- how remaining accounts are parsed and validated.

Trace CPI privilege propagation and every account passed to the callee. Confirm that a validated account is the same account later read or written.

## Native-Code Path

For Rust/C or custom allocators, include integer conversion, alignment, offsets, pointer arithmetic, lifetime, overlapping buffers, and out-of-bounds behavior. Connect any memory primitive to controllable account data or state; a crash alone rarely satisfies the verifier.

Use the supplied program-test/validator harness. Prove the result with account data, lamport/token deltas, ownership changes, or verifier output after the attacker instruction sequence.
