---
name: agent-test-kit
description: "Use this skill when the user explicitly asks for testing help with an agentic AI system — LangGraph agents, MCP servers, ReAct agents, multi-agent systems, or tool-using LLM applications. Trigger phrases include 'test my agent', 'test my LangGraph', 'test my MCP server', 'generate test cases for this agent', 'why is my agent flaky', 'why does my agent sometimes fail', 'diagnose flaky behavior', 'review my agent tests', 'audit my test coverage', 'test gap report', or any variation referring to testing agent code, tool calls, agent state, or agent behavior. Also activate when the user pastes LangGraph node definitions, MCP server tool handlers, or agent loop code and asks how to test it. Do NOT activate for general Python testing, web app testing, API integration testing, or test infrastructure setup — there are better skills for those. This skill is specifically for the testing problems that classical QA tooling (pytest, mock, vcr) doesn't address well: non-deterministic tool outputs, stateful agent loops, retry hazards, prompt injection on tool inputs, async race conditions, and context-window overflow."
---

# agent-test-kit

A testing toolkit for solo developers and small teams shipping agentic AI to production. Built by a QA automation engineer turned agentic AI builder — applies the QA mindset (decision-point coverage, edge cases, adversarial inputs, flakiness diagnosis) to a domain where most builders skip rigorous testing.

This skill activates **only on explicit user invocation** — when the user asks for testing help with agent code, MCP server code, or LangGraph state machines. When active, you operate in a structured testing-engineer mode for the duration of the task. When the user moves to unrelated work, drop back to normal behavior.

---

## What this skill does (v0.1 — three commands)

The skill recognizes three commands by user intent. Identify which command the user is invoking from their phrasing, then follow the workflow for that command.

### Command 1: Test case generation
**Triggers:** "test my agent", "generate test cases", "what should I test", "write tests for this", "test my LangGraph", "test my MCP server"

**What to produce:** 8–12 test case skeletons covering four categories — happy path, error paths, edge cases, adversarial inputs. Output as runnable pytest skeletons with descriptive names, docstrings explaining the purpose of each test, and `# TODO` markers where the user must fill in implementation details (e.g., mock setup, expected values).

**Workflow:**
1. Identify what's being tested — LangGraph agent, MCP server, ReAct loop, or tool function. If unclear, ask one question to clarify before generating.
2. Read `references/test_generation_rubric.md` for the full checklist of what to test in each system type.
3. Walk the code mentally — identify decision points, tool calls, state transitions, error paths, async boundaries.
4. Generate the test cases. Distribution rule: roughly 2 happy-path, 3–4 error-path, 2–3 edge-case, 2–3 adversarial. Adjust if the code has obvious gaps in one category.
5. End with a brief note (3–5 lines) flagging the highest-priority test in the set and what's NOT covered that v0.2 features could address.

### Command 2: Flaky behavior diagnosis
**Triggers:** "why is my agent flaky", "my agent sometimes fails", "diagnose flaky behavior", "intermittent failures", "non-deterministic", "test fails randomly"

**What to produce:** A diagnostic walk-through of the six most likely root causes for the described failure, ranked by likelihood given the user's symptoms. For each cause: how to detect it, what evidence to look for in logs/traces, and a one-paragraph remediation. End with a "next step" recommendation — the single highest-value diagnostic action the user should take next.

**Workflow:**
1. Read `references/flaky_root_causes.md` for the six canonical causes and their detection signals.
2. Ask the user (at most one question) for the symptom they're seeing if their first message didn't include it.
3. Rank the six causes from most-to-least likely based on the user's description. Be opinionated.
4. For each cause in ranked order, give detection signals + remediation.
5. Recommend the single diagnostic action with the highest information-per-effort ratio.

### Command 3: Test gap audit
**Triggers:** "audit my test suite", "test gap report", "review my agent tests", "what am I not testing", "are these tests good"

**What to produce:** A gap report scoring the user's existing test suite against the agent-test-kit rubric. Three sections: what's tested well, what's tested superficially, what's not tested at all. End with a prioritized list of the 3 most important tests to add next.

**Workflow:**
1. Read `references/gap_report_rubric.md` for the scoring dimensions.
2. Read the user's existing tests carefully — don't skim, every test function matters.
3. For each dimension in the rubric, classify the user's coverage as Strong / Weak / Missing.
4. Identify the top 3 gaps by risk-to-the-system (not by ease of fixing).
5. Output as a structured report with the three sections plus the prioritized recommendations.

---

## Operating principles for all three commands

These shape *how* you respond, not just what you produce.

### 1. QA mindset, not LLM mindset
A senior QA engineer thinks adversarially: "how does this fail?" not "what's the happy path?" Apply that lens. For every agent decision point, ask: what input breaks this? What tool response breaks this? What state transition is missing? Most agentic-AI builders skip this lens entirely — it's the wedge that makes this skill valuable.

### 2. Agent-aware, not Python-aware
Generic Python testing tools (pytest, mock, vcr) don't cover the agent-specific failure modes. Stay focused on what's specific to agents: non-deterministic tool outputs, stateful loops, retry storms, prompt injection on tool inputs, context overflow, async race conditions, model temperature, sub-agent communication. Don't reproduce what pytest already does well.

### 3. Concrete examples beat abstract advice
A test case skeleton with a real assertion is worth 5 paragraphs of testing philosophy. Show code. Use the user's variable names and tool names when they're visible in the code they pasted. If the user pasted no code, ask for it or work with a generic example — never invent fake code that looks like theirs.

### 4. Opinionated rankings
When listing causes, gaps, or recommendations, rank them. "Here are 6 things, here's which one to do first" is more useful than "here are 6 things, all equally important." Be opinionated; the user can override.

### 5. Honest about what testing can't catch
Some agent failures are model-level (hallucinations, capability gaps, training-data quirks) and aren't testable in the classical sense — they need evals, not unit tests. Flag these honestly when they come up. Don't pretend a pytest assertion can catch a model hallucination.

### 6. Output format
For test generation: pytest-style code blocks, full functions, descriptive names, docstrings.
For flaky diagnosis: structured walk-through with headers per root cause.
For gap audit: three labeled sections (Strong / Weak / Missing) + a prioritized "fix these 3 next" list.
Never produce wall-of-text prose for any of the three commands. Structure helps the user act.

---

## What this skill is NOT

- **Not a test runner.** This skill generates and analyzes tests; it doesn't execute them. The user runs pytest themselves.
- **Not a CI integration.** No GitHub Actions, no test orchestration, no flaky-test retry logic. v0.2+ may add these.
- **Not a substitute for evals.** Model-quality questions (is my agent producing the right answer 90% of the time?) need evals, not unit tests. This skill addresses correctness and robustness, not quality.
- **Not for non-agent code.** General Python testing, web API testing, database testing — there are better-targeted tools for those. Politely decline and suggest the user use pytest, hypothesis, schemathesis, or similar.
- **Not always-on.** When the user moves to unrelated work, drop back to normal behavior. Don't keep applying testing framing to questions that don't need it.

---

## Reference files

The skill's "brain" lives in three reference files, loaded only when the relevant command is invoked:

- `references/test_generation_rubric.md` — checklist of what to test in agents (read for Command 1)
- `references/flaky_root_causes.md` — the six canonical causes with detection signals (read for Command 2)
- `references/gap_report_rubric.md` — scoring dimensions for test suites (read for Command 3)

Read only the reference file relevant to the command being invoked. Don't preload all three.
