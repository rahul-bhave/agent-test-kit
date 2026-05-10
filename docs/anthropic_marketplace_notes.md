# Anthropic Plugin Marketplace — Submission Notes

Research date: 2026-05-10. Sources: code.claude.com/docs, claude.com/plugins,
github.com/anthropics/claude-plugins-official.

## What is the marketplace?

Anthropic maintains an official, curated plugin directory called
`claude-plugins-official`. It ships built into Claude Cowork (the web app at
claude.ai) and is available in Claude Code via `/plugin` commands. Plugins
listed here get distribution to every Claude user who browses the marketplace.

There is also a separate "demo plugins" repo (`claude-code-plugins`) maintained
by Anthropic with example plugins. We don't submit there — that's their
showcase, not a third-party listing.

## Submission process (what we'll do)

Two submission paths exist (use either):

- Claude Code in-app submission form: triggered from inside Claude Code
- Web form: `platform.claude.com/plugins/submit`

The submission becomes a PR-style review, but the form-based intake means we
don't need to file a GitHub PR ourselves.

## What gets reviewed (and what doesn't)

Anthropic explicitly states two review tiers:

1. **Basic automated review** for every accepted plugin (default tier)
2. **"Anthropic Verified" badge** for plugins that pass an additional manual
   quality + safety review

Anthropic also explicitly disclaims they cannot verify plugin behavior
end-to-end — they advise users to install only from publishers they trust.
This means: a clean, professional repo with a credible author bio is part of
the trust signal.

## Quality bar (inferred from existing approved plugins)

Examples of currently-listed plugins:
- frontend-design (production-grade frontend tooling)
- claude-md-management (CLAUDE.md hygiene tools)
- pr-review-toolkit (multi-agent PR review)
- hookify (custom workflow hooks)
- ralph-loop (iterative dev workflow)
- Various LSP plugins (Pyright, TypeScript LS, etc.)
- Trail of Bits security plugins (multiple)
- Atlassian, Asana, Atlan, ClickHouse, Cloud SQL connectors

Pattern: each approved plugin has a clear, single-purpose value prop, a
README that explains what it does and how to use it, and a publishable
brand or credible author behind it.

## What we need to ship

For the agent-test-kit submission:
- `.claude-plugin/plugin.json` ✅ done
- `.claude-plugin/marketplace.json` ✅ done (we are our own marketplace too)
- README that sells the skill ⏭ Weekend 3
- SKILL.md content that triggers reliably ⏭ Weekend 2
- At least one example output (recommended, not required) ⏭ Weekend 2

## Open questions [VERIFY]

These need confirmation by reading the actual submission form when we get
to Weekend 3:

- [ ] **VERIFY: Does Anthropic's submission form ask for source code, or just
  a marketplace URL?** Likely just a URL pointing to our GitHub repo, but
  confirm at the form itself.
- [ ] **VERIFY: Review timeline.** Public docs don't state SLA. Plan for 1-4
  weeks based on what other community submitters have reported, but check
  the form for any stated timeline.
- [ ] **VERIFY: Commercial restrictions.** Does Anthropic prohibit listing a
  plugin in their official marketplace if a paid version of the same plugin
  exists elsewhere (e.g., Agent37)? Critical for our free-on-Anthropic +
  paid-on-Agent37 model. Read the submission form's terms carefully.
- [ ] **VERIFY: Anthropic Verified badge eligibility.** Does our v0.1 plugin
  qualify for this, or is it reserved for Anthropic-partnered companies only?
  If achievable, worth pursuing — significant credibility boost.

## How auto-updates work

- Official marketplace plugins: auto-update enabled by default
- Third-party marketplaces (including ours, when used directly):
  auto-update disabled by default

Implication: if we want users who installed via our GitHub marketplace to get
v0.2 automatically, they need to opt in. The Anthropic-marketplace path gets
auto-updates for free.