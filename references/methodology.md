# Solving Method

Use this reference for every nontrivial challenge.

## Start From the Verifier

Find the deployment and success checks before broad code review. Record the success condition as an observable predicate, for example:

```text
target state:
observer/verifier:
initial state:
attacker capabilities:
forbidden shortcuts:
```

Inventory source, bytecode, manifests, lockfiles, tests, containers, service wrappers, addresses, funded keys, snapshots, and compiler/framework versions. Run the original build or test command before changing files when the environment permits.

## Model the System

Use compact tables rather than a long narrative.

| Actor/component | Authority or trust | Attacker control | Relevant state/assets |
|---|---|---|---|
| Fill from artifacts | State the exact check | Yes/partial/no | Name concrete fields or objects |

| Transition | Preconditions | Writes / asset movement | External interaction | Relation to solve predicate |
|---|---|---|---|---|
| Function, instruction, or message | Exact guards | Concrete state | Callback/CPI/relayer | Direct or indirect |

Separate observed facts from inferences. Treat comments, names, UI text, and writeups as hints until code or execution confirms them.

## Rank Hypotheses

Maintain a small ledger:

| Hypothesis | Enabling evidence | Controlled input | Predicted result | Cheapest falsification | Status |
|---|---|---|---|---|---|
| Concrete mechanism | Code/state location | Exact parameter/account/order | Observable delta | Call/test/query | Open/refuted/confirmed |

Prioritize a hypothesis when its path is reachable from attacker capabilities, its predicted effect advances the verifier, and it is cheap to test. Deprioritize pattern matches that cannot influence the solve predicate.

## Boundaries and Blockers

Use local deployments, supplied RPC endpoints, or challenge infrastructure within the user's authorized scope. Before any transaction that changes a remote chain, confirm the target and mutation are authorized.

When blocked, name the exact missing item and its consequence. Examples include an absent genesis snapshot, unavailable compiler version, unknown program binary, missing RPC access, or a verifier that depends on mutable remote state. Include the strongest conclusion supported without that item.
