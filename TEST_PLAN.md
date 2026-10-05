# Test Plan

## Purpose

Test whether the skill changes an agent's blockchain CTF behavior in useful, observable ways. Wording and heading matches are not success criteria. A good result derives the correct solve predicate, selects relevant chain semantics, proposes a reachable exploit, and validates the claimed state change.

The user's separate agent/tool-call harness instructions take precedence for invocation mechanics. This plan defines cases, artifacts, oracles, and scoring so it remains portable across harnesses.

## Test Layers

### 1. Package checks

Run on every change:

```powershell
python scripts/validate_structure.py
python -m unittest discover -s tests -v
python "$env:CODEX_HOME\skills\.system\skill-creator\scripts\quick_validate.py" .
```

These checks validate metadata, required files, relative links, routing coverage, and unfinished scaffold markers. They do not measure solving ability.

### 2. Behavioral cases

Each case must provide:

- an isolated challenge directory or immutable repository revision;
- the user prompt and allowed actions;
- toolchain prerequisites and setup command;
- observable solve predicate;
- essential facts the agent must discover;
- forbidden shortcuts, such as editing the verifier or directly mutating state with test-only cheat codes;
- expected deliverables and evidence;
- a timeout or bounded attempt budget;
- cleanup steps.

Score outcomes from artifacts and execution results. Do not require exact prose.

### 3. Native execution

Where a platform toolchain is available, compile and run the PoC against the actual synthetic challenge. Mark a case as one of `passed`, `failed`, `blocked-prerequisite`, or `not-run`. A missing toolchain is not a pass.

For remote or forked cases, pin the RPC network, block/ledger checkpoint, contract/program identifiers, and source/bytecode provenance. Do not depend on mutable public state for the default offline suite.

## Required Case Matrix

| ID | Platform | Core semantic trap | Required success evidence |
|---|---|---|---|
| EVM-01 | EVM proxy | delegatecall storage-layout mismatch or unsafe initialization | Native test reaches verifier through an attacker transaction sequence |
| EVM-02 | EVM composition | accounting/rounding or transient-state confusion across callbacks | Trace plus before/after balances or storage proves the invariant break |
| MOVE-01 | Sui Move | shared object or PTB composition violates a resource/time invariant | Transaction effects show the solve object/state was produced |
| SOL-01 | Solana | missing owner/signer/PDA/CPI validation | Program test confirms unauthorized state or token movement |
| XCHAIN-01 | Cross-chain | unauthenticated field, replay domain, or amount/accounting mismatch | End-to-end message lifecycle reaches destination solve predicate |
| VM-01 | Custom VM | revert journaling/rollback or opcode semantic divergence | Differential/minimal program demonstrates divergence and wins challenge |
| ALT-01 | TON, Stellar, or WASM | native message, authorization, storage, or host behavior | Native emulator/test output proves the platform-specific transition |
| ZK-01 | ZK integration | missing constraint, unbound public input, encoding, or verifier misuse | Proof/verifier execution accepts an invalid statement that reaches the predicate |
| FORENSIC-01 | EVM or other chain | source-free transaction/state reconstruction | Reproducible query set identifies root cause and fund/state flow |
| NEG-01 | Any | suspicious code with no reachable exploit under setup | Agent reports bounded uncertainty and does not claim an unexecuted solve |

At least one EVM case must run in the baseline CI environment. Other native cases may be separate jobs or documented local profiles when their SDKs are too large for baseline CI.

## Behavioral Oracle

For each positive case, score these dimensions independently:

| Dimension | Pass condition |
|---|---|
| Solve predicate | Expressed in terms that the harness can observe |
| System model | Relevant actors, authority, assets, trust boundary, and state transitions are correct |
| Platform semantics | Exploit depends on the actual platform behavior rather than a generic bug label |
| Hypothesis quality | Preconditions and a falsification method are stated |
| PoC validity | Compiles/runs in the declared native environment without verifier edits or forbidden shortcuts |
| Evidence | Output contains the state, balance, trace, event, or object change that proves success |
| Explanation | Root cause and exploit sequence agree with the executed PoC |

A positive case passes only when `PoC validity` and `Evidence` pass. Analysis without execution may be recorded as partial, never successful.

For `NEG-01`, pass when the agent tests the strongest reachable hypotheses, states what the evidence rules out, and avoids inventing a vulnerability or fabricated run output.

## Public Benchmark Tiers

Use `benchmarks/manifest.yaml` as metadata, not as trusted truth. Verify official source and pin a commit or release before enabling a benchmark.

| Tier | Purpose | Contents | Normal cadence |
|---|---|---|---|
| Synthetic smoke | Deterministic workflow regressions | The cases above, with small redistributable fixtures | Every change |
| Priority public | Modern multi-component reasoning | The nine high-information candidates identified in `reference.txt` | Before a release or major instruction change |
| Coverage public | Breadth and difficulty curve | All verified candidates from the 30-challenge historical list | Periodic evaluation |

Fetch public repositories into isolated temporary workspaces. Give the solving agent challenge artifacts and player-visible instructions only. Keep the expected exploit, writeup, and scoring oracle outside its context. Record immutable upstream revision, tool versions, model/harness settings, attempt budget, and runtime evidence.

## Regression Policy

- Preserve failing transcripts and runtime logs as test artifacts.
- Classify failures as skill routing, domain reasoning, exploit implementation, environment, fixture, or harness defects.
- Change the skill only when the failure demonstrates a reusable decision error.
- Add narrow regression cases for observed failures; avoid adding universal rules based on a single challenge.
- Re-run the affected case and at least one unrelated case after instruction changes.

## Acceptance Record

The execution agent must record:

- repository commit and skill revision;
- harness/model configuration supplied by the user;
- case status and elapsed attempts;
- exact commands run;
- native tool versions;
- success evidence or blocker;
- any instruction change prompted by the case.

The final report must separate package validation, behavioral results, and native execution results.
