# Test Generation Rubric

The checklist Claude consults when generating test cases (Command 1). Covers
what to test across the four categories and the system-specific patterns for
LangGraph agents, MCP servers, and ReAct loops.

## The four categories (always cover all four)

### Happy path (target: ~2 tests)
The agent does what it's supposed to when everything works. One end-to-end
success test, plus one test of the primary tool-use path resolving correctly.

### Error paths (target: ~3-4 tests)
What happens when things go wrong, specifically:
- A tool call raises an exception
- A tool returns a malformed or unexpected response
- The LLM returns output that fails to parse (bad JSON, missing fields)
- An external dependency times out or is unavailable
- The agent hits a terminal error state — verify it exits cleanly, not in a loop

### Edge cases (target: ~2-3 tests)
The boundaries where agents commonly break:
- Empty input / null input / whitespace-only input
- Maximum-length input approaching context limits
- A tool returning an empty result set (not an error, just nothing)
- State at its initial value (first turn) vs deep into a conversation
- Concurrent or rapid repeated invocations if the agent is async

### Adversarial inputs (target: ~2-3 tests)
The QA-mindset differentiator. Inputs designed to break or subvert:
- Prompt injection embedded in a tool's *output* (e.g., a web-search tool
  returns text containing "ignore previous instructions")
- Prompt injection in user input that tries to skip tool authorization
- Input designed to trigger infinite loops (a request the agent can never
  satisfy, testing whether loop guards fire)
- Malicious tool arguments (path traversal, SQL-ish strings, oversized payloads)
- A tool response that claims success but returns garbage

## System-specific patterns

### LangGraph agents
- Test each node in isolation with a constructed state object
- Test conditional edges: assert the router sends state to the correct next
  node for each branch condition
- Test for unreachable nodes (a node no edge leads to) — flag as a design bug
- Test state mutations: assert each node returns the expected state delta and
  does NOT mutate fields it shouldn't touch
- Test the recursion/iteration limit: assert the graph terminates and doesn't
  exceed its configured max steps
- Test checkpointing/persistence if used: state survives a save/load cycle

### MCP servers
- Test each tool handler with valid arguments → correct result
- Test each tool handler with invalid/missing arguments → proper error, not crash
- Test the tool schema itself: assert advertised input schema matches what the
  handler actually validates
- Test read-only vs side-effecting tools differently: side-effecting tools need
  idempotency and rollback tests
- Test authentication/authorization if the server has any
- Test that error responses follow MCP's error format, not raw exceptions

### ReAct / tool-using loops
- Test the reasoning-action-observation cycle terminates
- Test tool selection: given a prompt, assert the agent picks the right tool
- Test the agent handles a tool it decided to call but that then fails
- Test max-iteration guards fire before runaway cost

## Output format for generated tests

- Runnable pytest functions, not pseudocode
- Descriptive names: `test_router_sends_to_error_node_on_tool_failure`
- A docstring on each test stating what it verifies and why it matters
- `# TODO:` markers where the user must supply mocks, fixtures, or expected values
- Group tests by category with a comment header
- Use the user's actual class/function/tool names when visible in their code
- If mocking LLM calls, show the mock setup; don't assume a framework

## Honesty notes to include when relevant

- Some properties (does the agent give a *good* answer?) are eval territory,
  not unit-test territory. Say so; don't generate a test that asserts
  subjective quality.
- Non-deterministic outputs need either seeding, mocking, or property-based
  assertions (assert structure, not exact text). Flag which approach fits.
