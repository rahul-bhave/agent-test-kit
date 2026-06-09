"""Minimal MCP-style server for validating agent-test-kit.

Two tool handlers: one read-only, one side-effecting. The side-effecting
handler is intentionally non-idempotent and the read-only handler does no
input validation, so the skill has real gaps to find.
"""

_NOTES: dict[str, str] = {}


def get_note(note_id: str) -> dict:
    """Read-only tool. No input validation — intentional gap."""
    return {"id": note_id, "content": _NOTES[note_id]}


def append_note(note_id: str, text: str) -> dict:
    """Side-effecting tool. Non-idempotent — calling twice double-appends.

    Intentional gap: a retry would corrupt data.
    """
    _NOTES[note_id] = _NOTES.get(note_id, "") + text
    return {"id": note_id, "length": len(_NOTES[note_id])}
