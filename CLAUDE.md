# Project: agent-test-kit

A Claude Code skill that helps solo developers and indie builders test their LangGraph agents and MCP servers like a QA engineer would.

## Author context
Built by a QA automation engineer who transitioned into agentic AI engineering. The unfair advantage of this skill is the QA mindset applied to a domain (agentic AI) where most builders skip rigorous testing.

## Target buyer
A solo developer or 2–5 person team building a LangGraph agent or MCP server who knows their tests are weak (or nonexistent) and would pay $29–$49 to get a senior QA engineer's review of their code via Claude Code.

## v0.1 scope (the only scope that matters right now)
The skill triggers on three explicit invocations:

1. **"test my agent" / "generate test cases"** — reads agent code, generates 8–12 pytest skeletons covering happy path, error paths, edge cases, adversarial inputs (prompt injection on tool inputs).
2. **"diagnose flaky behavior"** — given a failure description, walks through 6 most likely root causes (state mutation, retry storms, tool non-determinism, model temperature, async race conditions, context overflow).
3. **"audit my test suite" / "test gap report"** — reads existing tests, produces a gap report (what's untested, what's tested superficially, what tests are testing the wrong thing).

## What is NOT in v0.1
- No auto-execution of generated tests
- No CI integration
- No visualization or dashboards
- No multi-agent test orchestration

These are v0.2+ features, deliberately held back to keep v0.1 shippable in a weekend.

## Distribution plan
- Free version (test generation only) → Anthropic's official plugin marketplace
- Paid version (all three commands, $29) → Agent37
- Source of truth → this GitHub repo, also installable as a Claude Code marketplace directly

## Working principles for AI coding assistance
- Keep SKILL.md under 200 lines. The frontmatter description is the highest-leverage paragraph in the project — it determines whether Claude triggers the skill.
- Reference files in `skills/agent-test-kit/references/` are the brain. SKILL.md tells Claude *what* to do; references tell it *how*.
- Don't add features outside v0.1 scope. If something feels useful, note it in `IDEAS.md` for v0.2 and move on.
- Prefer concrete examples over abstract instructions in the references. Real LangGraph code snippets beat generic descriptions.
