# Test Gap Audit Rubric

The scoring framework for auditing an existing test suite (Command 3). Classify
the user's coverage on each dimension as Strong / Weak / Missing, then surface
the top 3 gaps by risk to the system.

## Scoring dimensions

For each dimension, classify: **Strong** (well covered), **Weak** (some coverage
but shallow or incomplete), **Missing** (no meaningful coverage).

1. **Decision-point coverage** — Is every branch/conditional edge in the agent
   tested for each outcome? Weak if only the happy branch is tested.

2. **Tool I/O coverage** — Is each tool tested for both valid calls and invalid
   calls? Weak if only success cases exist.

3. **Error-path coverage** — Are failure modes tested (tool exceptions, parse
   failures, timeouts)? This is the most commonly Missing dimension.

4. **State-transition coverage** — For stateful agents, are state changes
   asserted? Is unwanted mutation tested for? Usually Weak or Missing.

5. **Termination / loop-guard coverage** — Is it tested that the agent always
   terminates (max iterations, recursion limits)? Almost always Missing in
   solo-built agents — high risk.

6. **Adversarial / security coverage** — Prompt injection, malicious tool
   args, loop-trigger inputs. Almost always Missing. The QA-mindset wedge.

7. **Determinism handling** — Are non-deterministic dependencies mocked or
   handled with structural assertions? Weak if tests assert exact LLM/tool
   output (these tests will be flaky themselves).

8. **Async coverage** (if applicable) — Are concurrent invocations tested?
   Usually Missing.

## Output format

Three labeled sections:

### Tested well
List dimensions classified Strong, with a one-line note on each.

### Tested superficially
List dimensions classified Weak, with what's missing to make each Strong.

### Not tested
List dimensions classified Missing, ordered by risk.

### Fix these 3 next
The three highest-risk gaps, ranked. For each: what to add, why it matters,
and a one-line starter (e.g., "Add a test asserting the graph terminates when
the tool always fails — prevents the infinite-loop cost bomb"). Rank by
risk-to-the-system, NOT by ease of fixing.

## Risk-ranking guidance

When choosing the top 3, weight by blast radius:
- Termination/loop gaps → can cause runaway cost; usually rank high
- Error-path gaps → cause production crashes; rank high
- Adversarial gaps → security/safety risk; rank high for anything user-facing
- Determinism gaps → cause flaky CI but rarely prod outages; rank medium
- Happy-path-only tool coverage → rank by how critical the tool is

Be honest if the suite is actually good — don't manufacture gaps. "Your suite
is solid; the only meaningful gap is X" is a valid and valuable report.
