# agent-test-kit

**QA-grade testing for agentic AI.** A free, open-source Claude skill that
helps you test LangGraph agents and MCP servers the way a senior QA engineer
would — generate test cases, diagnose flaky behavior, and audit your test
coverage.

Built by a QA automation engineer turned agentic AI builder. Most agent
builders skip rigorous testing. This skill brings the QA mindset to the
failure modes that classical tools (pytest, mock, vcr) don't cover:
non-deterministic tool outputs, stateful loops, retry hazards, prompt
injection on tool inputs, and context overflow.

## What it does

Three commands, recognized by what you ask:

| Ask | What you get |
|-----|--------------|
| "test my agent" / "generate test cases" | 8–12 pytest skeletons across happy path, error paths, edge cases, and adversarial inputs |
| "why is my agent flaky?" | A ranked diagnosis of the 6 most likely root causes, with detection signals and fixes |
| "audit my tests" / "test gap report" | A coverage report (tested well / superficially / not at all) plus the 3 highest-risk gaps to fix next |

## Install

This repo is itself a Claude Code marketplace. From Claude Code:

```
/plugin marketplace add rahul-bhave/agent-test-kit
/plugin install agent-test-kit@agent-test-kit
```

Then just ask Claude Code to "test my LangGraph agent" with your code open.

## Example

Point it at an agent and ask for tests:

> **You:** test my agent (with sample_langgraph_agent.py open)
>
> **Claude:** [generates pytest cases covering the search-node error path the
> sample ignores, the missing termination guard, and an adversarial test for
> prompt injection in search results]

See `examples/` for sample agents to try it against.

## What it is NOT

- Not a test runner — it generates and analyzes tests; you run pytest yourself
- Not a CI tool — no orchestration or retry logic (planned for later)
- Not an eval framework — it tests correctness and robustness, not answer quality
- Not for general Python testing — use pytest/hypothesis/schemathesis for that

## Pairs well with

- **LangGraph Agent Builder** — build the agent, then test it here
- **pytest-test** — general Python test generation; agent-test-kit adds the
  agent-specific layer on top
- **LangSmith** — runtime tracing; agent-test-kit is the before-you-deploy layer

## Roadmap

v0.1 (this release): test generation, flaky diagnosis, gap audit — all free.
Later: CI integration, auto-execution, multi-agent test orchestration.

## License

MIT. Contributions and issues welcome.

## Author

Built by Rahul Bhave. Feedback and feature requests via GitHub issues.
