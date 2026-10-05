# TON, Stellar, WASM, and ZK

Use a semantics-first workflow for platforms that do not match the EVM, Move, or Solana models. Before proposing an exploit, identify the execution unit, caller/authority representation, persistent state, atomicity and failure behavior, address derivation, serialization, fee/resource model, and local emulator or test runner.

## TON

Model accounts/contracts and inbound/outbound messages rather than synchronous EVM calls. Check internal versus external messages, sender/authentication rules, bounce behavior, message modes/fees/value, logical time and ordering, state initialization/address derivation, serialization cells, and partial effects across asynchronous message chains. For shared or multi-instance economies, track value and state across every contract instance and queued message.

## Stellar and Soroban

Distinguish Stellar classic operations from Soroban contract execution. For classic transactions, inspect source accounts, sequence numbers, signers/thresholds, assets, trustlines, claimable balances, operation ordering, memo/time bounds, and transaction versus operation failure. For Soroban, inspect authorization trees, address credentials/nonces, contract instances, persistent/temporary/instance storage, ledger TTL, token interfaces, host serialization, and ledger footprint/resource limits.

## WASM Contract Runtimes

Identify the host ABI and chain-specific message model. Check canonical address and integer conversion, serialization/schema mismatches, submessage/reply behavior, rollback boundaries, storage namespaces, funds attachment, migration/admin paths, query versus execute assumptions, and host imports. For CosmWasm, include reply IDs, reply-on behavior, `instantiate2` address derivation, and cross-contract messages where relevant.

## Zero-Knowledge Challenges

Separate the statement the protocol intends to prove from the constraints and public inputs the verifier actually checks. Trace witness generation, unconstrained or underconstrained signals, range/field assumptions, public-input ordering and binding, hash/domain separation, proof and point encoding, subgroup/on-curve checks, verifier-key or trusted-setup selection, transcript construction, replay, and application state updated after verification.

Validate the strongest available boundary: generate a proof for an invalid intended statement that the real verifier accepts, or construct a minimal verifier-integration test that shows the missing binding. A malformed proof rejected before reaching the vulnerable path is not success.

## Unknown Platforms

Read the manifest, framework version, runtime documentation, generated interfaces, deployment scripts, and verifier. Build a one-operation experiment for uncertain semantics before designing a long exploit chain. Record which observations come from documentation, source, emulator execution, or live-chain state.
