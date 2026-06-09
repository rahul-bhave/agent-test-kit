"""Minimal LangGraph-style agent for validating agent-test-kit.

Intentionally imperfect: it has no explicit recursion guard and its tool
node assumes the tool always succeeds. The skill should flag these when
generating tests or auditing coverage.
"""
from typing import TypedDict, Literal


class AgentState(TypedDict):
    query: str
    search_results: list[str]
    answer: str
    steps: int


def search_tool(query: str) -> list[str]:
    """Pretend web search. Non-deterministic in reality."""
    if not query.strip():
        raise ValueError("empty query")
    return [f"result for {query}"]


def search_node(state: AgentState) -> AgentState:
    results = search_tool(state["query"])  # assumes success — no error handling
    return {**state, "search_results": results, "steps": state["steps"] + 1}


def answer_node(state: AgentState) -> AgentState:
    answer = f"Based on {len(state['search_results'])} results: ..."
    return {**state, "answer": answer}


def router(state: AgentState) -> Literal["search", "answer"]:
    if not state["search_results"]:
        return "search"
    return "answer"
