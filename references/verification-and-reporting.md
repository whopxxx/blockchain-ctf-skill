# Exploit Verification and Reporting

## Iterate From Runtime Evidence

1. Add the smallest attacker code or transaction sequence compatible with the existing harness.
2. Compile before reasoning about runtime behavior.
3. Execute against the original setup and verifier.
4. Capture the first informative failure: compiler error, revert bytes, trace divergence, wrong account/object, or unexpected state delta.
5. Update one hypothesis or exploit assumption at a time and rerun.

Preserve useful logs and keep refuted hypotheses out of the active plan unless new evidence changes a premise.

## Success Standard

A successful process exit is insufficient. Observe the same predicate used by the challenge, or an equivalent state transition when the original verifier is unavailable. Capture relevant before/after balances, storage, account/object data, ownership, events, return values, or service output.

Do not use test-only state mutation, verifier edits, private keys unavailable to a player, or direct storage/account overrides unless the case explicitly permits them. Setup helpers may create the declared initial state but must not perform the exploit.

## Final Deliverable

Provide:

```text
Environment and assumptions
Win predicate
Root cause
Exploit sequence
Files added or changed
Exact build/run command
Observed success evidence
Remaining uncertainty or blocker
```

Separate evidence types clearly:

- code evidence identifies the enabling logic;
- runtime evidence shows the actual state transition;
- assumptions identify unverified environment or chain facts.

When blocked, give the exact missing prerequisite, the command or step that failed, and the strongest result already established.
