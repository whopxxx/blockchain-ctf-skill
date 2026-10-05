# Behavioral Test Cases

`cases/manifest.yaml` is the harness-neutral case inventory. The execution agent should add isolated synthetic fixtures and immutable expected-result metadata for every listed case.

Each case must declare its setup, prompt, allowed actions, prerequisites, solve predicate, required evidence, forbidden shortcuts, timeout or attempt budget, and cleanup. Agent/tool-call invocation is supplied separately by the user.

Keep generated chain data, tool caches, compiled artifacts, transcripts, and secrets out of version control. Store only small redistributable fixtures and sanitized expected results.
