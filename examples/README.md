# Examples

Sample agent code used for testing the skill against real-world patterns.
These files are NOT distributed as part of the skill — they exist for skill
development and validation only.

- `sample_langgraph_agent.py` — minimal LangGraph agent demonstrating common
  patterns (state, tools, conditional edges). Used to validate Command 1
  (test generation) and Command 3 (gap audit) output quality.
- `sample_mcp_server.py` — minimal MCP server with two tool handlers. Used
  to validate Command 1 output for MCP-specific test patterns.

Both files will be populated with real reference code during Weekend 2's
validation phase. Currently placeholders.
