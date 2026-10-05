# EVM Analysis

Read deployment scripts, constructor/initializer paths, proxy slots, compiler version, and the verifier before auditing individual functions.

## Map Execution and Storage

- Resolve proxy, implementation, beacon, admin, library, clone, and factory relationships from deployed behavior.
- Derive storage layout across inheritance and delegatecall; include packed fields, mappings, dynamic arrays, unstructured slots, and transient slots.
- Distinguish constructor state from proxy state and check every initialization path.
- For assembly or bytecode, track memory, returndata, call context, selector dispatch, and storage operands explicitly.
- Treat CREATE2 addresses as a result of deployer, salt, and init-code hash. Verify runtime code and lifecycle assumptions.

## Trace Attacker-Controlled Composition

List external calls, callbacks, token hooks, fallback/receive paths, multicalls, flash liquidity, and same-transaction state reuse. Model the state visible at each callback rather than applying a generic reentrancy label.

For transient storage, identify the contract context, slot computation, lifetime within the transaction, delegatecall effects, and whether distinct assets/users/actions collide.

## Check Economic and Authentication Invariants

- Write conversion formulas with integer rounding and units. Test boundaries, repeated actions, partial fills, zero/liquidity extremes, fee timing, and decimal conversion.
- Identify the source and freshness assumptions of every price or reserve value.
- Reconstruct exactly what a signature commits to: domain, chain, verifying contract, action, recipient, amount, nonce, deadline, and encoding.
- Check nonce scope and update order, replay across contracts/chains/actions, malleability where relevant, and ERC-1271 behavior.
- Distinguish block-wide values from transaction-local state. Inspect failed calldata and ordering only when the challenge exposes them.

## Validate

Prefer the supplied Foundry or Hardhat setup. Useful evidence includes call traces, revert bytes, emitted events, storage reads, code hashes, and before/after balances. A scanner finding is a lead. A passing exploit test tied to the verifier is proof.
