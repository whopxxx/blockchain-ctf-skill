# Custom VMs and On-Chain Forensics

## Custom or Forked VM

Identify the upstream implementation and fork delta. Compare small programs across both implementations when possible.

Focus on state journals and rollback across nested calls, create/self-destruct behavior, exception classes, gas and refunds, memory expansion, returndata, opcode edge cases, precompiles/syscalls, host serialization, and persistent caches. Reduce a divergence to the smallest instruction/call sequence, then connect it to the challenge predicate.

Record both expected and observed state after success, revert, out-of-gas, panic, or host error. Process termination is not proof of a useful state transition.

## Forensics

Record chain, network, block/ledger checkpoint, RPC or explorer source, address/program ID, and query commands so results are reproducible.

Resolve proxies and implementations, match runtime bytecode or program data to source when possible, and distinguish verified metadata from inferred source. Reconstruct transactions with calls/instructions, logs/events, state/storage changes, token/native balance deltas, and ordering. Track fund flow across wrappers, routers, bridges, and internal calls without assuming event logs are complete.

When historical state or traces are unavailable, state the resulting uncertainty and use independent evidence such as bytecode, receipts, archived events, or balance snapshots.
