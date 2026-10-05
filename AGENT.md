# Blockchain CTF Skill - Implementation Brief

## 1. Mission

Build a Codex skill that helps an agent solve authorized blockchain CTF challenges from challenge artifacts through a reproducible exploit. The skill must improve the agent's decisions, especially for modern challenges that go beyond basic Solidity bugs.

The final skill should help an agent:

1. identify the actual solve condition;
2. reconstruct deployment, actors, trust boundaries, state, assets, and transaction ordering;
3. select a chain-specific analysis path;
4. turn observations into ranked, falsifiable exploit hypotheses;
5. implement and execute a proof of concept in the challenge's native toolchain;
6. use compiler errors, test failures, traces, and state diffs to revise the exploit;
7. report only claims supported by code or execution evidence.

This is a solving skill, not a general smart-contract audit checklist, a vulnerability encyclopedia, a challenge generator, or an autonomous system for interacting with unapproved live targets.

## 2. Inputs and Current State

- `reference.txt` is a curated research brief distilled from historical conversation. It separates design conclusions from unverified challenge and project candidates. Use it as a research backlog and rationale, not as runtime skill instructions or a trusted source. Verify every external claim against primary sources before promotion.
- The repository contains a minimal valid skill scaffold. Replace or deepen scaffold content where this brief requires it.
- The user will separately tell the execution agent how agent/tool-call tests must be invoked. Do not invent a proprietary agent harness. Keep behavioral cases harness-neutral.
- The repository itself is the skill directory. `SKILL.md` stays at the repository root.

## 3. Design Principles

### Solve backward from success

Read the setup, deployment scripts, tests, server wrapper, and verifier before conducting broad vulnerability searches. Express the solve condition as an observable predicate. Then identify which state transitions and assets can satisfy it.

### Prefer evidence over labels

Do not stop at labels such as "reentrancy" or "storage collision." Record the exact precondition, controllable input, violated invariant, call sequence, and success observation. Static findings are hypotheses until the exploit or an equivalent minimal reproduction succeeds.

### Execute in the native environment

Reuse the challenge's Foundry, Hardhat, Move, Anchor, Rust, Docker, or custom VM setup. Add the smallest compatible proof of concept. Do not replace the challenge harness merely because another framework is familiar.

### Route by semantics

The common workflow belongs in `SKILL.md`. Detailed instructions belong in references loaded only when relevant. Platform routing must cover:

- Solidity, Vyper, EVM bytecode, proxies, assembly, DeFi, signatures, CREATE/CREATE2, transient storage, and transaction ordering;
- Move object/capability models, shared objects, programmable transaction composition, time, randomness, and resource invariants, with Sui-specific details when applicable;
- Solana accounts, owner/signer/writable checks, PDA derivation, CPI, account aliasing, serialization, and native Rust/C memory hazards;
- cross-chain relayers, messages, attestations, replay domains, finality assumptions, source/destination accounting, and ordering;
- custom VM or fork implementation bugs, rollback/journaling, gas, opcode semantics, host boundaries, and differential execution;
- TON account/message semantics, Stellar/Soroban authorization and asset behavior, WASM contract/host boundaries, and ZK circuit/verifier/public-input mismatches;
- on-chain forensics using transaction traces, events, bytecode/source matching, storage, and fund flow.

Do not pretend that every Move chain or every account-based chain shares identical semantics. Tell the solver to inspect the actual framework and version.

### Keep the skill small enough to load

`SKILL.md` should be a router and core method, ideally below 250 lines. Avoid exhaustive vulnerability catalogs. Put conditional detail and compact decision aids in `references/`. Add scripts only for deterministic work that agents would otherwise reimplement often.

## 4. Required Final Tree

The execution agent may adjust names when there is a concrete reason, but must preserve the responsibilities below.

```text
.
|-- SKILL.md
|-- AGENT.md
|-- README.md
|-- TEST_PLAN.md
|-- reference.txt             Curated research and candidate catalog; not loaded at runtime
|-- agents/
|   `-- openai.yaml
|-- references/
|   |-- methodology.md
|   |-- evm.md
|   |-- move.md
|   |-- solana.md
|   |-- cross-chain.md
|   |-- other-platforms-and-zk.md
|   |-- tooling.md
|   |-- vm-and-forensics.md
|   `-- verification-and-reporting.md
|-- benchmarks/
|   |-- README.md
|   `-- manifest.yaml
|-- scripts/
|   `-- validate_structure.py
`-- tests/
    |-- README.md
    |-- test_structure.py
    `-- cases/
        `-- manifest.yaml
```

Do not add copied challenge repositories, generated build output, large corpora, solver frameworks, or dependencies without demonstrated need.

## 5. `SKILL.md` Contract

Use valid YAML frontmatter:

- `name`: `blockchain-ctf`
- `description`: clearly trigger on solving, analyzing, reproducing, or writing exploits for authorized blockchain CTF/puzzle challenges; distinguish it from ordinary production audits and contract development.

The body must direct the solver through this decision loop:

```text
artifacts and verifier
        |
observable solve predicate
        |
deployment + actors + state + assets + trust boundaries
        |
platform-specific semantics
        |
ranked exploit hypotheses
        |
minimal executable PoC
        |
compile/run/trace/state diff
        |
revise until success or evidence-backed blocker
```

Required behaviors:

- Establish scope and avoid broadcast transactions unless the user explicitly authorized the target and mutation.
- Inventory files and tool versions before editing.
- Read the verifier/setup path before chasing vulnerability patterns.
- Separate observed facts, inferences, and untested hypotheses.
- Make each hypothesis falsifiable and prioritize by reachability and impact.
- Preserve useful failures: compiler output, revert data, traces, logs, storage/state diffs, and balance changes.
- Keep a compact hypothesis ledger to avoid cycling through disproved ideas.
- Stop only on a verified solve, a precise environment/input blocker, or exhausted evidence-backed hypotheses. "Looks vulnerable" is not completion.
- Produce the exploit, run command, observed result, root cause, and assumptions.

The entrypoint must link each reference and say when to read it. It must not require all references on every invocation.

## 6. Reference Content

### `references/methodology.md`

Describe artifact triage, verifier-first analysis, system modeling, hypothesis ranking, state/asset flow, and blocker reporting. Include compact working templates for:

- solve predicate;
- actors and authority;
- asset/state transition table;
- hypothesis ledger with evidence and falsification test.

### `references/evm.md`

Focus on EVM-specific reasoning rather than a long SWC list. Cover at least:

- deployment and initialization, proxy/implementation/admin relationships;
- storage layout across inheritance and delegatecall, including transient storage;
- external call surfaces, callbacks, token hooks, fallback/receive, and same-transaction composition;
- accounting, precision, rounding direction, share/asset conversion, oracle assumptions;
- signatures, domain separation, nonces, replay, permit/meta-transaction boundaries;
- CREATE2, metamorphic assumptions, constructor/runtime code, bytecode and assembly;
- block, timestamp, calldata, failed transaction, and mempool/order semantics;
- using Foundry/Anvil/cast traces and state inspection without assuming those tools are installed.

### `references/move.md`

Distinguish generic Move concepts from Sui specifics. Cover resources, abilities, capabilities, ownership, shared objects, dynamic fields, object identity/version, entry/public exposure, programmable transaction blocks, composition, clocks, epochs, randomness, and receipt aggregation. Tell the solver to inspect `Move.toml`, framework revision, and transaction model.

### `references/solana.md`

Cover account metadata and validation, PDA seeds/bump, signer and writable privilege, CPI privilege propagation, remaining accounts, duplicate/aliased accounts, token program variants, discriminator/serialization checks, rent/lifecycle behavior, arithmetic, and native Rust/C memory concerns. Route Anchor and raw programs differently where useful.

### `references/cross-chain.md`

Model source chain, relayer/watcher, message format, attestation/signature, replay state, destination execution, and asset accounting as separate components. Check which fields are actually authenticated, domain/chain binding, nonce uniqueness, quorum, ordering, partial failure, retry semantics, finality, and amount/decimal conversion. Require an end-to-end message lifecycle diagram or table before exploit construction.

### `references/other-platforms-and-zk.md`

Provide a semantics-first path for platforms that should not be forced into an EVM model. Include focused sections for TON account/message/bounce/state behavior; Stellar classic transactions and Soroban authorization/storage/host behavior; CosmWasm or other WASM host/serialization/reply boundaries; and ZK circuits, witness constraints, public-input binding, proof encoding, verifier integration, and trusted-setup assumptions. For any unfamiliar platform, require the agent to identify its execution unit, authority model, persistent state model, atomicity/failure behavior, address derivation, serialization, and local emulator before proposing an exploit.

### `references/tooling.md`

Define artifact acquisition and tool selection. A GitHub URL should be resolved through an available authenticated connector, `gh`, or `git`, then pinned to a commit before analysis. Record submodules, LFS assets, releases, containers, and generated/deployed bytecode needed to reproduce the challenge. Describe native tools and optional analyzers by role, not as mandatory dependencies. Foundry/Anvil/cast, Slither, Echidna/Medusa, symbolic execution, Move CLIs, Solana/Anchor tooling, debuggers, and RPC/explorer connectors generate evidence or hypotheses; the challenge verifier and native state transition remain the oracle. Specify graceful fallback when a tool is unavailable.

### `references/vm-and-forensics.md`

Include custom VM differential reasoning and chain forensics. For VMs, cover state journaling/rollback, nested calls, gas/refunds, exceptions, opcode/host semantics, precompiles/syscalls, serialization, and differential tests against an upstream implementation. For forensics, cover provenance of RPC/explorer data, implementation resolution, traces, logs, storage, balance flow, and reproducible snapshots.

### `references/verification-and-reporting.md`

Define the compile-run-observe-revise loop, success evidence, trace triage, minimal exploit requirements, and the final report format. Include rules for differentiating code proof, runtime proof, and assumptions. A successful process exit alone is insufficient; validate the challenge predicate or equivalent state transition.

## 7. Scripts

Keep `scripts/validate_structure.py` dependency-free. It should validate only stable package invariants:

- required files exist;
- `SKILL.md` frontmatter has the expected name and a nonempty description;
- every local Markdown link in `SKILL.md` resolves inside the repository;
- required references are reachable from `SKILL.md`;
- scaffold markers such as `TODO`, `TBD`, and placeholder boilerplate do not remain in shipped skill/reference files.

Do not build a generic vulnerability scanner or framework detector unless real behavioral testing proves one is necessary.

## 8. Testing Requirements

`TEST_PLAN.md` is authoritative for coverage. Implement tests at three levels:

1. **Package validation:** deterministic, offline, standard-library-only checks for structure, metadata, and local links.
2. **Behavioral cases:** harness-neutral cases that judge decisions and produced evidence, not exact wording.
3. **Native PoC validation:** compile and execute small synthetic vulnerable challenges in their native toolchains when available.

The behavioral suite must include at least:

- EVM proxy/delegatecall storage-layout exploit;
- EVM accounting or transient-storage composition exploit;
- Sui Move shared-object or PTB composition exploit;
- Solana missing account validation or PDA/CPI exploit;
- cross-chain message-authentication/accounting exploit;
- custom VM rollback or opcode-semantics exploit;
- TON, Stellar/Soroban, or WASM case that requires its native message/authorization/host semantics;
- ZK case with a constraint, public-input, encoding, or verifier-integration flaw;
- forensic investigation with no provided source;
- negative control where no exploit is established, requiring calibrated uncertainty rather than a fabricated success.

Use synthetic, redistributable fixtures. Do not copy full third-party CTF challenges into the repository. Each case needs observable pass criteria, expected essential reasoning, forbidden shortcuts, required artifacts, and optional toolchain prerequisites.

The user will provide the execution agent with agent/tool-call test invocation details. The project should expose cases and expected results cleanly so that harness can consume them, while avoiding assumptions about its vendor or API.

### Public benchmark corpus

Maintain a separate `benchmarks/manifest.yaml` for public challenges. Start from the 30 candidates in `reference.txt`, but promote an entry only after verifying its official source, license/redistribution constraints, platform, challenge path, and immutable commit or release. The nine high-information candidates called out in the history should form the first external evaluation tier: PP Farming 2, Outer Stellar, Lootboxes, Staking, Transient Heist Revenge, CODEGATE DEX, Solalloc, Teragas, and Zoo.

Do not vendor whole challenge repositories by default. Store metadata and setup adapters; fetch into an isolated cache when the license and test environment allow it. Keep solution notes and expected exploit details outside the artifacts and prompt visible to the solving agent. Use synthetic cases for deterministic CI and public challenges for periodic forward evaluation.

Record benchmark results by immutable skill revision, challenge commit, model/harness configuration, native tool versions, success evidence, attempt budget, and elapsed time. A remembered challenge name or copied writeup is not a valid solve.

## 9. Source Quality

When improving references from the curated candidate links:

1. prefer official challenge repositories, protocol/framework documentation, EIPs/SIPs, and source code;
2. pin claims to a commit, tag, or version where practical;
3. use writeups to discover techniques, then verify against code or runtime behavior;
4. remove tracking query parameters from stored links;
5. do not encode unverified 2026 event details as settled facts;
6. record source URLs only where they materially help future decisions.

The final skill should teach transferable reasoning. Challenge names belong primarily in benchmark metadata, not in universal rules.

## 10. Implementation Order

1. Read all repository files and preserve user-authored material.
2. Finalize the behavioral contract and reference routing.
3. Write the common methodology and verification/reporting references.
4. Write each platform reference, checking primary sources for semantic claims.
5. Verify public benchmark metadata and pin immutable upstream revisions without importing solution text into solver inputs.
6. Refine `SKILL.md` after the references exist so links and routing are exact.
7. Implement deterministic validation and unit tests.
8. Create synthetic behavioral fixtures and manifest entries.
9. Run static/package tests.
10. Run available native fixtures and the user-specified agent/tool-call tests.
11. Run selected public benchmarks in isolated workspaces.
12. Review failures for skill defects; change instructions only when the evidence supports the change.
13. Run the official skill validator and all repository checks one final time.

## 11. Acceptance Criteria

The work is complete when:

- `SKILL.md` passes the official `quick_validate.py` validator;
- `python scripts/validate_structure.py` succeeds;
- `python -m unittest discover -s tests -v` succeeds;
- every local link from `SKILL.md` resolves;
- the entrypoint routes to all required platform references without loading them all by default;
- no unfinished scaffold markers remain in shipped instructions;
- each required behavioral category has a self-contained case and observable oracle;
- every promoted public benchmark has a verified upstream URL, immutable revision, license decision, clean solver input, and separately stored oracle;
- at least one executable EVM fixture proves the full exploit loop in CI or the documented baseline environment;
- platform fixtures either run successfully in their declared environments or are explicitly marked with concrete prerequisites, never silently treated as passing;
- the negative control penalizes unsupported vulnerability and success claims;
- agent/tool-call tests use the harness instructions supplied by the user and their results are recorded;
- README commands match commands actually run;
- generated files and build artifacts are excluded from version control.

## 12. Final Handoff

Report:

- the implemented skill behavior and routing;
- the tests run and exact outcomes;
- unavailable native toolchains and their impact;
- behavioral cases that failed and whether the skill or fixture was changed;
- remaining assumptions or known coverage gaps.

Do not claim multi-chain solving quality solely because every reference file exists. The evidence is the agent's behavior on independent cases and the native execution result.
