# Artifact Acquisition and Tooling

Use this reference when the input is a repository URL, chain address, bytecode/program artifact, or a toolchain the workspace has not established.

## Acquire Reproducible Inputs

For a GitHub URL, use an available authenticated GitHub connector, `gh`, or `git`. Record the exact repository and commit before analysis. Inspect submodules, Git LFS pointers, releases, Docker files, package locks, deployment manifests, and generated/deployed artifacts. A source tree without the wrapper, verifier, genesis state, or deployed bytecode may be incomplete.

For on-chain inputs, record network, chain ID, block or ledger checkpoint, addresses/program IDs, implementation resolution, RPC/explorer provenance, and every query needed to reproduce the snapshot. Prefer read-only queries until a specific remote mutation is authorized.

## Choose Tools by Question

| Question | Useful tools when present | Evidence produced |
|---|---|---|
| Build and execute EVM PoC | Foundry, Anvil, cast, Hardhat | Bytecode execution, trace, logs, state/balance delta |
| Find EVM candidates | Slither, compiler output | Static hypotheses requiring reachability checks |
| Explore sequences/invariants | Echidna, Medusa, native fuzzers | Counterexample sequence to reproduce in the verifier |
| Explore bytecode paths | Symbolic execution or disassembly | Candidate constraints/path, followed by concrete execution |
| Build Move challenge | Platform Move CLI/test runner | Transaction effects and object/resource changes |
| Build Solana challenge | cargo, program-test, solana-test-validator, Anchor | Instruction result and account/token deltas |
| Investigate chain state | RPC, trace APIs, explorer connector | Reproducible transaction/state/fund-flow evidence |

Check availability and versions before planning around a tool. If an optional analyzer is missing, continue with source/runtime inspection when feasible and name the lost capability. Do not install a large toolchain unless the challenge path and user scope justify it.

Static analyzers, fuzzers, symbolic tools, and other agents propose hypotheses. The native challenge verifier or an equivalent observable state transition decides success.

## Bound the Feedback Loop

Compile first, then fix the earliest concrete failure. During execution, retain the shortest informative trace and before/after state. Change one exploit assumption per iteration when possible. Stop retrying a path after its necessary precondition is disproved, and record that result in the hypothesis ledger.

Do not require multi-agent orchestration. When the environment and user authorize independent agents, they may explore distinct hypotheses or perform blinded evaluation; keep the main solve state and final runtime oracle in one place.
