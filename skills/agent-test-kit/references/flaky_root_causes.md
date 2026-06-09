# Flaky Behavior Root Causes

The six canonical causes of intermittent agent failures (Command 2). For each:
symptoms, how to detect, and remediation. Rank these by likelihood against the
user's specific symptom before presenting — be opinionated.

## 1. Shared mutable state across invocations
**Symptom:** Agent works the first time, misbehaves on subsequent runs in the
same process. Tests pass alone but fail when run together.
**Detect:** Look for module-level mutable defaults, class attributes holding
state, caches or memory objects reused across calls, default arguments that
are lists/dicts. Run the failing test in isolation vs in the suite — if
isolation fixes it, this is your cause.
**Remediate:** Make state explicit and per-invocation. Reset or rebuild state
at the start of each run. Avoid mutable default arguments. In LangGraph, ensure
the state object is fresh per graph invocation.

## 2. Unbounded or aggressive retries (retry storms)
**Symptom:** Occasional hangs, runaway costs, duplicated side effects (an email
sent twice), or "sometimes it just spins."
**Detect:** Look for retry decorators or loops without a max-attempts cap,
retries on non-retryable errors (a 400 retried like a 500), missing backoff,
no circuit breaker. Check logs for the same operation logged repeatedly.
**Remediate:** Cap retries. Exponential backoff with jitter. Only retry
genuinely transient errors. Make side-effecting operations idempotent so a
retry can't double-charge or double-send.

## 3. Tool output non-determinism
**Symptom:** Same input, different agent behavior. Tests that assert on exact
tool output fail randomly.
**Detect:** Identify tools whose output varies — web search, time/date, random,
external APIs with changing data, anything LLM-based. Check whether assertions
depend on the volatile parts.
**Remediate:** Mock non-deterministic tools in tests. Assert on structure not
exact content. For tools that must be live, use property-based assertions
(result is non-empty, has the right shape) rather than equality.

## 4. Model sampling / temperature
**Symptom:** The LLM itself produces different outputs for the same prompt,
causing downstream parsing or routing to sometimes fail.
**Detect:** Temperature > 0 anywhere in the chain. Output-parsing code that
works for one phrasing but not another. Routing logic that depends on exact
LLM wording.
**Remediate:** For tests, set temperature to 0 and/or mock the LLM. For
production robustness, make parsing tolerant (structured output / function
calling instead of free-text parsing), and make routing depend on structured
fields not prose.

## 5. Async race conditions
**Symptom:** Failures only under load or concurrency; works when stepped through
a debugger; order-dependent results.
**Detect:** Concurrent tool calls sharing a resource, `asyncio.gather` over
operations with side effects, missing awaits, shared clients not safe for
concurrent use. Failures that change with timing.
**Remediate:** Isolate per-task state. Use locks around shared resources.
Verify clients are concurrency-safe. Add tests that run the agent concurrently
and assert consistent results.

## 6. Context-window overflow / truncation
**Symptom:** Agent degrades or fails on long conversations or large inputs;
works fine on short ones. Failures correlate with input size.
**Detect:** Check whether total tokens (history + tools + input) can exceed the
model's window. Look for silent truncation. Failures that appear deep into a
conversation but never early.
**Remediate:** Measure token usage. Add summarization or windowing of history.
Test explicitly at and beyond the context limit. Fail loudly on overflow rather
than silently truncating.

## Diagnostic recommendation framework

After presenting the ranked causes, recommend the single highest-value next
action — the one diagnostic that distinguishes between the top candidates with
least effort. Usually one of:
- "Run the failing test in isolation" (distinguishes #1)
- "Add request logging and look for repeats" (distinguishes #2)
- "Set temperature to 0 and re-run 10x" (distinguishes #3 and #4)
- "Correlate failures with input size" (distinguishes #6)
