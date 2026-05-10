# Competitive Scan — Agent Testing Skills (May 2026)

Research date: 2026-05-10. The skill ecosystem is large (1,000+ public skills
across awesome lists) and growing weekly. This snapshot captures what's
relevant to agent-test-kit's specific niche: testing tooling for solo
developers building LangGraph agents and MCP servers.

## Direct competitors

### `pytest-test` — closest direct overlap
- **Found at:** mcpmarket.com/tools/skills/python-testing-with-pytest
- **What it does:** Generates pytest suites for general Python projects.
  Supports fixtures, parametrization, mocking, monkeypatching. Outputs
  structured JSON for CI integration.
- **Pricing:** Listed (price visibility [VERIFY on the listing page])
- **Differentiator vs ours:** This is for *general Python code*, not
  *agentic AI code*. It doesn't know about LangGraph state, tool calls,
  retry behavior, prompt injection on tool inputs, or context overflow.
- **Threat level: medium.** Its existence means buyers searching "pytest"
  or "python test generation" will find it first. We need to position
  agent-test-kit as the agent-specific layer that complements (not
  competes with) pytest-test.

### Anthropic's `pr-test-analyzer` (part of pr-review-toolkit)
- **Found at:** github.com/anthropics/claude-code (official plugins)
- **What it does:** PR review agent that specifically reviews tests.
- **Differentiator vs ours:** Reviews existing test PRs, doesn't generate
  tests for un-tested code. Different workflow position.
- **Threat level: low.** Different surface area.

## Adjacent — not direct competitors but nibbling at our space

### `LangSmith Fetch`
- **Found at:** awesome-claude-skills (Composio HQ list)
- **What it does:** Fetches LangGraph execution traces from LangSmith
  Studio for debugging.
- **Overlap:** Touches our flaky-behavior-diagnosis territory.
- **Differentiator vs ours:** Requires LangSmith subscription. Observability
  angle, not testing angle. Reactive (debug after) vs proactive (test before).
- **Threat level: low.** Different buyer (those already on LangSmith)
  and different timing (after failure vs before deploy).

### `LangGraph Agent Builder`
- **Found at:** mcpmarket.com/tools/skills/langgraph-agent-builder
- **What it does:** Helps architect production-grade LangGraph systems.
- **Differentiator vs ours:** Builds, doesn't test. We're the
  complement — once you've built with their skill, you'd test with ours.
- **Threat level: low.** Could potentially partner with or cross-link
  with this skill's author for mutual visibility.

### `qa-orchestra` (wshobson/agents)
- **What it does:** Multi-agent QA toolkit using Chrome MCP for browser
  validation.
- **Differentiator vs ours:** Browser/end-to-end testing focus, not
  unit/integration testing for agent code itself.
- **Threat level: low.** Different buyer (web app builders vs agent
  builders).

### `MCP Builder`
- **Found at:** awesome-claude-skills
- **What it does:** Guides creation of MCP servers.
- **Differentiator vs ours:** Build phase, not test phase.
- **Threat level: low.**

### Trail of Bits security skills
- **What they do:** Code review for crypto, smart contracts, Firebase
  configs, insecure defaults.
- **Differentiator vs ours:** Security-specific, not testing-specific.
  Could be relevant if we pivot to the MCP-security-audit alternative
  (Path A from earlier convo), but for agent-test-kit they're not
  in the way.

## Niche-density assessment

Searches performed:
- agent37.com (search functionality limited; browsed listings) [VERIFY]
- skills4agents.com (browsed) [VERIFY]
- claudemarketplaces.com — searched "test", "qa", "langgraph", "mcp"
- mcpmarket.com — same searches
- lobehub.com/skills — same searches
- skillsmp.com (claims 1,200,000+ skills) — search [VERIFY]
- Anthropic's `claude-plugins-official` repo (browsed marketplace.json)
- GitHub topic searches: claude-skill, claude-code-plugin
- VoltAgent's awesome-agent-skills (browsed)
- alirezarezvani's claude-skills (232+, browsed)

**Verdict:** The "QA-engineer-mindset testing for solo LangGraph/MCP
builders" niche is genuinely open. No skill targets this specific
intersection. The closest competitor (pytest-test) is for general
Python, not agentic AI. Agent-aware testing — knowing about state
mutation, tool I/O determinism, retry hazards, prompt injection on
tool inputs, async race conditions — is the wedge.

## Implications for positioning

**Sharpen the trigger description toward agent-specific language.**
Don't just say "testing" — say "agent testing", "LangGraph testing",
"MCP server testing", "tool-call testing". This both improves Claude's
trigger accuracy and avoids being lumped with generic Python-test skills.

**Lead with what pytest-test can't do.** The buyer who already uses
pytest-test will pay $29 for an agent-specific layer on top, but only
if we explicitly call out the gap.

**Cross-reference adjacent skills in our README.** Mentioning LangGraph
Agent Builder, LangSmith Fetch, and pytest-test by name in our README
("agent-test-kit pairs well with...") is a low-cost way to ride their
discoverability and signal that we know the ecosystem.

## Things to re-check before launch [VERIFY]

The space moves weekly. Before submitting to Anthropic's marketplace
on Weekend 3:

- [ ] **Re-run all searches.** A direct competitor could ship between now
  and then.
- [ ] **Search the Anthropic Verified plugins specifically.** If a Verified
  plugin in our exact niche has launched, repositioning may be needed.
- [ ] **Check Agent37's top sellers.** If a "test agents" skill is selling
  there, see what it does and price below it.