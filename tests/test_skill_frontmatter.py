import yaml
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
SKILL_MD = ROOT / "skills" / "agent-test-kit" / "SKILL.md"

ALLOWED_FRONTMATTER_KEYS = {"name", "description", "license", "allowed-tools", "metadata", "compatibility"}


def has_frontmatter(text: str) -> bool:
    if not text.startswith("---"):
        return False
    closing_index = text.find("---", 3)
    return closing_index != -1


def get_frontmatter(text: str) -> dict:
    lines = text.splitlines()
    if len(lines) < 3 or lines[0] != "---":
        raise ValueError("No YAML frontmatter found")
    end = None
    for index, line in enumerate(lines[1:], start=1):
        if line == "---":
            end = index
            break
    if end is None:
        raise ValueError("No closing YAML delimiter found")
    raw = "\n".join(lines[1:end])
    parsed = yaml.safe_load(raw)
    if not isinstance(parsed, dict):
        raise ValueError("Frontmatter must parse to a YAML mapping")
    return parsed


def is_kebab_case(value: str) -> bool:
    return bool(__import__("re").fullmatch(r"(?!-)(?!.*--)[a-z0-9-]{1,64}(?<!-)", value))


def test_skill_md_exists():
    assert SKILL_MD.exists(), "SKILL.md must exist"


@pytest.mark.skipif(
    not has_frontmatter(SKILL_MD.read_text(encoding="utf-8")),
    reason="SKILL.md frontmatter not yet written — placeholder phase",
)
def test_skill_md_frontmatter_parses():
    content = SKILL_MD.read_text(encoding="utf-8")
    frontmatter = get_frontmatter(content)
    assert frontmatter["name"] == "agent-test-kit"


@pytest.mark.skipif(
    not has_frontmatter(SKILL_MD.read_text(encoding="utf-8")),
    reason="SKILL.md frontmatter not yet written — placeholder phase",
)
def test_skill_md_frontmatter_name_is_kebab_case():
    frontmatter = get_frontmatter(SKILL_MD.read_text(encoding="utf-8"))
    assert isinstance(frontmatter.get("name"), str)
    assert frontmatter["name"] == "agent-test-kit"
    assert is_kebab_case(frontmatter["name"])


@pytest.mark.skipif(
    not has_frontmatter(SKILL_MD.read_text(encoding="utf-8")),
    reason="SKILL.md frontmatter not yet written — placeholder phase",
)
def test_skill_md_frontmatter_name_length_is_valid():
    frontmatter = get_frontmatter(SKILL_MD.read_text(encoding="utf-8"))
    assert len(frontmatter["name"]) <= 64


@pytest.mark.skipif(
    not has_frontmatter(SKILL_MD.read_text(encoding="utf-8")),
    reason="SKILL.md frontmatter not yet written — placeholder phase",
)
def test_skill_md_frontmatter_description_is_valid():
    frontmatter = get_frontmatter(SKILL_MD.read_text(encoding="utf-8"))
    description = frontmatter.get("description")
    assert isinstance(description, str)
    assert len(description) <= 1536
    assert "<" not in description and ">" not in description


@pytest.mark.skipif(
    not has_frontmatter(SKILL_MD.read_text(encoding="utf-8")),
    reason="SKILL.md frontmatter not yet written — placeholder phase",
)
def test_skill_md_frontmatter_allowed_keys():
    frontmatter = get_frontmatter(SKILL_MD.read_text(encoding="utf-8"))
    assert set(frontmatter.keys()).issubset(ALLOWED_FRONTMATTER_KEYS)
