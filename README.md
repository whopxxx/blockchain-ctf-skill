# blockchain-ctf-skill

A Codex skill scaffold for solving authorized blockchain CTF challenges with a verifier-first, chain-aware, execution-backed workflow.

The implementation contract is in [AGENT.md](AGENT.md). Test scope and behavioral cases are defined in [TEST_PLAN.md](TEST_PLAN.md). Public evaluation candidates are tracked in [benchmarks/manifest.yaml](benchmarks/manifest.yaml). The curated research brief in [reference.txt](reference.txt) records design rationale and unverified source candidates for the execution agent; it is not loaded by the runtime skill.

Run the scaffold checks with:

```powershell
python scripts/validate_structure.py
python -m unittest discover -s tests -v
```

The repository is currently a foundation for the execution agent. Passing structure checks does not establish challenge-solving quality; the behavioral and native-toolchain cases in the implementation brief are the acceptance evidence.
