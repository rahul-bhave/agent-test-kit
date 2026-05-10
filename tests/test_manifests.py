import json
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
MANIFEST_DIR = ROOT / ".claude-plugin"
MARKETPLACE_JSON = MANIFEST_DIR / "marketplace.json"
PLUGIN_JSON = MANIFEST_DIR / "plugin.json"

RESERVED_MARKETPLACE_NAMES = {
    "claude-code-marketplace",
    "claude-code-plugins",
    "claude-plugins-official",
    "anthropic-marketplace",
    "anthropic-plugins",
    "agent-skills",
    "knowledge-work-plugins",
    "life-sciences",
}


def is_kebab_case(name: str) -> bool:
    if len(name) > 64:
        return False
    return bool(re.fullmatch(r"(?!-)(?!.*--)[a-z0-9-]{1,64}(?<!-)", name))


def test_marketplace_json_exists():
    assert MARKETPLACE_JSON.exists(), "marketplace.json must exist"


def test_plugin_json_exists():
    assert PLUGIN_JSON.exists(), "plugin.json must exist"


def test_marketplace_json_valid_json():
    MARKETPLACE_JSON.read_text(encoding="utf-8")
    with MARKETPLACE_JSON.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    assert isinstance(data, dict)


def test_plugin_json_valid_json():
    PLUGIN_JSON.read_text(encoding="utf-8")
    with PLUGIN_JSON.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    assert isinstance(data, dict)


def test_marketplace_top_level_keys():
    with MARKETPLACE_JSON.open("r", encoding="utf-8") as handle:
        data = json.load(handle)

    for key in ["name", "owner", "description", "plugins"]:
        assert key in data, f"'{key}' must be present in marketplace.json"


def test_marketplace_name_is_agent_test_kit():
    with MARKETPLACE_JSON.open("r", encoding="utf-8") as handle:
        data = json.load(handle)

    assert data["name"] == "agent-test-kit"


def test_marketplace_name_is_kebab_case():
    with MARKETPLACE_JSON.open("r", encoding="utf-8") as handle:
        data = json.load(handle)

    assert is_kebab_case(data["name"])


def test_marketplace_name_is_not_reserved():
    with MARKETPLACE_JSON.open("r", encoding="utf-8") as handle:
        data = json.load(handle)

    assert data["name"] not in RESERVED_MARKETPLACE_NAMES


def test_marketplace_plugins_is_non_empty_array():
    with MARKETPLACE_JSON.open("r", encoding="utf-8") as handle:
        data = json.load(handle)

    assert isinstance(data["plugins"], list)
    assert data["plugins"], "plugins array must not be empty"


def test_marketplace_plugin_entries_have_required_fields():
    with MARKETPLACE_JSON.open("r", encoding="utf-8") as handle:
        data = json.load(handle)

    for entry in data["plugins"]:
        assert isinstance(entry, dict)
        for required in ["name", "source", "description", "version"]:
            assert required in entry, f"Plugin entry must contain '{required}'"


def test_plugin_top_level_keys():
    with PLUGIN_JSON.open("r", encoding="utf-8") as handle:
        data = json.load(handle)

    for key in ["name", "version", "description", "author", "license"]:
        assert key in data, f"'{key}' must be present in plugin.json"


def test_plugin_name_matches_marketplace():
    with MARKETPLACE_JSON.open("r", encoding="utf-8") as handle:
        marketplace = json.load(handle)
    with PLUGIN_JSON.open("r", encoding="utf-8") as handle:
        plugin = json.load(handle)

    assert plugin["name"] == marketplace["name"]


def test_plugin_description_is_valid():
    with PLUGIN_JSON.open("r", encoding="utf-8") as handle:
        data = json.load(handle)

    description = data["description"]
    assert isinstance(description, str)
    assert description, "description must not be empty"
    assert len(description) < 1024
    assert "<" not in description and ">" not in description
