# Cross-Chain Analysis

Treat the bridge or protocol as a distributed state machine. Model each component separately before searching for a single-contract bug.

| Stage | Input | Authentication | Replay/order state | Accounting/output |
|---|---|---|---|---|
| Source action | User/contract data | Source-chain checks | Source nonce/event | Locked/burned/recorded value |
| Observation | Event/state | Finality assumption | Checkpoint | Relayer representation |
| Attestation | Message fields | Signers/quorum/proof | Domain and nonce | Signed payload |
| Destination | Submitted message | Verification logic | Consumed state | Mint/release/call |

Verify which fields are actually authenticated, not merely present. Check source and destination chain/domain binding, contract/program identity, sender and recipient, token/mint, amount and decimals, call data, nonce uniqueness, expiry, quorum, and version.

Analyze retries, reordering, duplicate delivery, partial failure, reorg/finality assumptions, relayer races, and accounting across locked, burned, minted, released, refunded, or failed states. Track units at every conversion.

An exploit PoC should reproduce the full message lifecycle or isolate a cryptographically and semantically equivalent verifier path. State any mocked trust component and show why the mock preserves the vulnerable boundary.
