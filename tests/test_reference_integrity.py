import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / "skills" / "agent-test-kit"
SKILL_MD = SKILL_DIR / "SKILL.md"
REFERENCES_DIR = SKILL_DIR / "references"
EXPECTED_REFERENCE_FILES = {
    "test_generation_rubric.md",
    "flaky_root_causes.md",
    "gap_report_rubric.md",
}


def is_placeholder_skill_md(text: str) -> bool:
    return text.lstrip().startswith("<!-- ")


def test_references_dir_exists():
    assert REFERENCES_DIR.exists() and REFERENCES_DIR.is_dir()


def test_expected_reference_files_exist():
    for filename in EXPECTED_REFERENCE_FILES:
        path = REFERENCES_DIR / filename
        assert path.exists(), f"Missing reference file: {filename}"


def test_examples_dir_exists():
    examples_dir = ROOT / "examples"
    assert examples_dir.exists() and examples_dir.is_dir()


@pytest.mark.skipif(
    is_placeholder_skill_md(SKILL_MD.read_text(encoding="utf-8")),
    reason="SKILL.md is still placeholder content — reference integrity checks deferred",
)
def test_skill_md_reference_links_resolve():
    content = SKILL_MD.read_text(encoding="utf-8")
    references = set(re.findall(r"references/[A-Za-z0-9_\-]+\.md", content))
    assert references, "No reference links found in SKILL.md"

    for reference in references:
        path = SKILL_DIR / reference
        assert path.exists(), f"Referenced file does not exist: {reference}"
