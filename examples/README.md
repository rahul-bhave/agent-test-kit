# Examples

Sample agent code for trying out agent-test-kit. These files are NOT
distributed as part of the skill — they exist as a playground and as
reference fixtures for validating the skill's output.

- `sample_langgraph_agent.py` — a minimal LangGraph-style agent (typed state,
  a search tool, conditional routing). It intentionally contains gaps: no
  recursion/termination guard, and happy-path-only tool handling. The skill
  should surface these when generating tests or auditing coverage.
- `sample_mcp_server.py` — a minimal MCP-style server with two tool handlers:
  one read-only with no input validation, one side-effecting and
  non-idempotent. Both gaps are intentional.

To try the skill: open one of these files in Claude Code with agent-test-kit
installed, then ask "test my agent" or "audit my tests".
