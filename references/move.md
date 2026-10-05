# Move Analysis

First identify the concrete Move platform, framework revision, package manifest, transaction model, and verifier. Generic Move resource rules do not imply identical Sui, Aptos, or other platform behavior.

## Generic Questions

- Which values are resources, which abilities do they have, and where can they be created, moved, copied, dropped, or stored?
- Which capabilities authorize state changes, how are they obtained, and can they be wrapped, transferred, or reused?
- Which functions are entry points versus publicly composable functions?
- Does an invariant assume calls occur in isolation even though a transaction can compose them?
- Can receipts, positions, clocks, counters, or claims be split, merged, reordered, or replayed?

## Sui-Specific Path

Map owned, shared, immutable, and dynamic-field objects. Track object identity, version, ownership transitions, shared-object access, and the exact effects of a programmable transaction block.

For each relevant public function, consider its use before and after other calls in the same PTB. Check whether randomness, clock/epoch values, capabilities, transfer rules, or receipt aggregation are assumed to provide separation that composition defeats.

Validate with the package's native build/test tooling and transaction effects. Success evidence should identify created, mutated, transferred, wrapped, or destroyed objects and show how those effects satisfy the verifier.
