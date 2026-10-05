---
name: blockchain-ctf
description: Solve and reproduce authorized blockchain CTF and puzzle challenges by deriving the win condition, modeling chain-specific state and trust boundaries, building an exploit, and validating it in the challenge's native environment. Use for EVM, Move, Solana, TON, Stellar, WASM, ZK, cross-chain, custom-VM, and on-chain forensic challenge work; use a production security-review workflow for ordinary audits without a CTF solve condition.
---

# Blockchain CTF

Work backward from the challenge's observable success condition. A plausible vulnerability is a hypothesis; completion requires a reproducible state transition or a precise, evidenced blocker.

## Core Workflow

1. Confirm the target is a CTF, puzzle, local lab, or otherwise authorized environment. Do not broadcast transactions unless the user has authorized the specific target and mutation.
2. Inventory the repository, deployment scripts, tests, wrapper services, RPC assumptions, compiler/framework versions, funded accounts, and existing commands.
3. Read the setup and verifier path first. Write the win condition as a concrete predicate over state, balance, ownership, events, return data, or service output.
4. Map contracts/programs, actors, authority, assets, trust boundaries, and state transitions. Distinguish observed facts, inferences, and hypotheses.
5. Load only the platform reference relevant to the challenge, plus the verification reference when constructing the exploit.
6. Rank exploit hypotheses by reachability, control of inputs, impact on the win predicate, and cost to falsify. Track why each failed.
7. Build the smallest PoC compatible with the challenge's native harness. Compile and execute it; inspect revert data, traces, events, state diffs, and balance changes.
8. Revise from runtime evidence until the win predicate passes or a concrete missing input/environment condition blocks progress.
9. Deliver the exploit, exact run command, observed success evidence, root cause, assumptions, and any remaining uncertainty.

For the shared analysis method and compact working templates, read [references/methodology.md](references/methodology.md).

If the input is a repository URL, remote chain address, or unfamiliar toolchain, read [references/tooling.md](references/tooling.md) before acquiring artifacts or choosing analyzers.

## Platform Routing

- For Solidity, Vyper, EVM bytecode, proxies, assembly, DeFi math, signatures, transient storage, or transaction ordering, read [references/evm.md](references/evm.md).
- For Move packages and especially Sui objects, capabilities, shared state, or programmable transaction blocks, read [references/move.md](references/move.md).
- For Solana/Anchor programs, PDAs, CPI, token accounts, or native Rust/C account handling, read [references/solana.md](references/solana.md).
- For TON, Stellar/Soroban, CosmWasm or another WASM chain, ZK circuits/verifiers, or an unfamiliar blockchain runtime, read [references/other-platforms-and-zk.md](references/other-platforms-and-zk.md).
- For bridges, relayers, attestations, cross-domain messages, or multi-chain accounting, read [references/cross-chain.md](references/cross-chain.md). Also load each involved platform reference.
- For custom/forked VMs or source-free chain investigations, read [references/vm-and-forensics.md](references/vm-and-forensics.md).
- When implementing, debugging, and reporting the PoC, read [references/verification-and-reporting.md](references/verification-and-reporting.md).

## Working Standard

Keep a short hypothesis ledger. For every candidate, record the enabling code or behavior, attacker-controlled input, predicted state change, cheapest falsification test, and result. Do not recycle a disproved idea without new evidence.

Prefer primary evidence: challenge source, deployment state, compiler output, execution traces, state diffs, framework documentation, and specifications. Treat scanners and writeups as leads. Preserve the challenge's toolchain unless incompatibility is itself the blocker.

If execution cannot proceed, name the exact missing dependency, artifact, credential, chain state, or authorization and show what was established without it.
