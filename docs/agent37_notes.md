# Agent37 — Platform Reality Check

Research date: 2026-05-10. Sources: agent37.com, news.ycombinator.com,
revuo.ai/agent37, toolify.ai.

## What Agent37 is

A managed hosting + monetization platform for Claude skills and MCP servers.
Pitch: "Gumroad for Claude skills." The platform hosts the skill in a cloud
sandbox so buyers don't need to install Claude Code locally; payment, trial,
analytics, and access control are built in.

Founded late 2025 (HN launch post Dec 2025). Still early-stage product.

## What we know

**Revenue split:** Creators keep 80%. Platform takes 20%.

**Payment processor:** Stripe (integrated). One-time pricing and
subscription tiers both supported (subscription tiers confirmed via the
$3.99/mo OpenClaw managed-instance pricing reference; one-time
[VERIFY at signup]).

**Buyer experience:** Hosted workspace with terminal access, no local
install required, no Claude account required.

**Trial mechanism:** "Try before you buy" supported per the platform
description.

**Time from upload to live:** ~60 seconds claimed (MCP config to URL).

**Analytics:** Built-in usage and evaluation metrics for sellers.

## Open questions [VERIFY at signup]

These are the dealbreakers — must confirm before we list anything:

- [ ] **VERIFY: Stripe Connect availability for India.** Stripe Connect (which
  is how multi-seller platforms pay creators) has historically had complex
  India support. Some platforms route via PayPal, Wise, or direct bank
  transfer instead. Sign up, go to payout settings, confirm India is in the
  supported-country list.

- [ ] **VERIFY: One-time $29 pricing supported, not just subscriptions.**
  Most multi-seller platforms support both, but confirm in the listing
  creation flow before designing the product around one-time pricing.

- [ ] **VERIFY: Minimum payout threshold.** Stripe Connect typically requires
  ~$10-25 minimum balance before payout. Confirm Agent37's threshold; if
  high (>$50), we'll be sitting on revenue for longer than ideal.

- [ ] **VERIFY: Refund policy.** Who handles refund requests — Agent37 or us?
  What's the window? Affects how we pitch the trial.

- [ ] **VERIFY: Claude API key handling.** Agent37 hosts skills in a sandbox.
  Whose API key gets billed for buyer usage — ours or theirs? If ours, we
  need to factor inference cost into the $29 price (potentially making it
  negative-margin on heavy users). If theirs, the buyer brings their own
  key — simpler for us, slightly more friction for them.

## Risks to be aware of

**Platform dependency.** Agent37 is small, and Anthropic could launch a
native paid skill store at any time. The platform's reviews flag this
explicitly. Don't build distribution exclusively on Agent37.

**API key trust.** Sellers/buyers must trust Agent37's sandbox isolation.
Lower-stakes for us (we're not exposing user secrets), but worth knowing
when explaining the platform to LinkedIn audience.

**Early-stage product.** Feature parity with general cloud hosts not
proven yet.

## Backup platforms if Agent37 fails verification

In rough order of preference:
1. **Skills4Agents** (skills4agents.com) — claims 85% creator share, less
   information available publicly, would need its own VERIFY pass.
2. **Gumroad** — universal digital product platform, requires us to handle
   skill distribution manually (zip download), but payment/payout maturity
   is far higher. Indian payouts well-established.
3. **Lemon Squeezy** — Stripe alternative built for digital products, strong
   international payout support including India.
4. **Direct via Stripe** — set up our own checkout page, host the skill on
   GitHub releases, deliver via email. Lowest fee (~3%), most work.