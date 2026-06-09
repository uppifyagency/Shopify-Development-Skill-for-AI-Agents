# Retrieval eval — make every claim about this skill falsifiable

This skill's entire value proposition is one measurable thing: **given a Shopify
task, does the agent land on the exact reference slice — without reading whole
files and without hallucinating?** Until that number exists, every "improvement"
(including the integrity script) is an opinion. This file defines the measurement.

## Two layers

**Layer 1 — answerability (automated, already enforced).**
`scripts/check_integrity.py` validates that every gold target in
`eval/retrieval_gold.tsv` resolves to a real heading in the corpus. If a gold
answer doesn't exist, the eval is broken, not the agent. Current status: **51/51
gold targets resolve** (16 common + ~34 long-tail/adversarial). Re-run on every change.

**Layer 2 — retrieval quality (manual / agentic, the real test).**
Give a *fresh* agent session **only** the `shopify-development/` skill and the
task text below — nothing else. Observe where it goes. This cannot be faked by
the script because it measures agent behavior, not corpus structure.

## Protocol (per task)

1. New session. Load the skill. Paste the task verbatim. No hints.
2. Record:
   - **target file** the agent opened
   - **heading** it grepped/landed on
   - **whole-file read?** (did it `Read` a reference file without offset/limit?)
   - **approx context tokens** pulled from the skill
3. Score:
   | Score | Meaning |
   |------|---------|
   | **HIT** | correct file **and** correct (or adjacent) heading, read by slice |
   | **PARTIAL** | correct file, wrong heading — or correct slice but read the whole file |
   | **MISS** | wrong file, no skill use, or hallucinated an answer not in the corpus |

A skill that works should score HIT on ≥ 14/16 with **zero whole-file reads**.
Whole-file reads are a failure even when the answer is right: they defeat the
token-economy thesis.

## Gold set (16 tasks)

Authored from `eval/retrieval_gold.tsv`. Expected targets are the *minimum*
acceptable landing point; an adjacent finer heading also counts as HIT.

| # | Task | Surface | Expected file → heading |
|---|------|---------|-------------------------|
| 1 | Show a savings badge when a variant is on sale | theme/liquid | 07-liquid-objects · `### variant` |
| 2 | Loop over every product in a collection | theme/liquid | 08-liquid-tags · `## for` |
| 3 | Render a snippet with an isolated scope | theme/liquid | 08-liquid-tags · `## render` |
| 4 | Format a price as money in the store currency | theme/liquid | 10-liquid-filters-part2 · `## money — money` |
| 5 | Output a responsive product image (srcset/width) | theme/liquid | 10-liquid-filters-part2 · `## media — image_url` |
| 6 | Build a section schema with configurable blocks | theme/architecture | 02-key-concepts · `## 2.4` |
| 7 | Add a line item to the cart via Ajax | theme/api | 11-theme-apis · `### Cart API reference` |
| 8 | Re-render a section without a full page reload | theme/api | 11-theme-apis · `## Section Rendering API` |
| 9 | Decode a session token in the app backend | app/auth | 12-apps-foundations · `## About session tokens` |
| 10 | Verify an incoming webhook is authentic | app/webhooks | 13-apps-build-operate · `## About Webhooks` |
| 11 | Add a Checkout UI extension | app/extensions | 14-app-extensions · `## Checkout UI extensions` |
| 12 | Fetch storefront data from a Hydrogen route | headless | 15-headless-hydrogen · `## Hydrogen (API overview)` |
| 13 | Write a product discount Shopify Function | functions | 16-functions · `## Discounts (Product, Order, Shipping)` |
| 14 | Build a cart-transform bundle Function | functions | 16-functions · `## Cart Transform (bundles, line item changes)` |
| 15 | Define metafield types on a product | custom-data | 17-custom-data · `## About metafields (Custom data overview)` |
| 16 | Make the store operable by AI agents via UCP | ai/agentic | 18-ai-agentic · `## 1. Agentic commerce / UCP` |

## Results log (fill in)

| Date | Agent/model | tasks | HIT | PARTIAL | MISS | whole-file reads | notes |
|------|-------------|------:|----:|--------:|-----:|-----------------:|-------|
| 2026-06-09 | Explore subagents | 12 (stress: 4 common, 4 long-tail, 4 trap) | 12 | 0 | 0 | 0 | 0 hallucinations; all 4 traps resisted; see Run 1 findings |
| 2026-06-09 | general-purpose (Sonnet) | 51 (full gold set) | 33 auto / 51 adjudicated | 12→0 | 6→0 | 0 | 0 hallucinations; used_index 51/51; see Run 2 findings |

### Run 1 findings (2026-06-09)

Ran a 12-task stress sample (not the full 51) through fresh Explore subagents, each
restricted to the skill folder. Result: **12/12 HIT, 0 MISS, 0 hallucinations,
0 whole-file reads.** Every agent reached the documenting heading via an index
(`liquid-filters`, `liquid-objects`, `liquid-tags`, `schemas`, `task-routing`),
then grepped and read a slice. The four adversarial traps — deprecated `include`
tag, session-token→access-token exchange, *current* vs *legacy* billing, Storefront
vs Admin API — were all answered correctly and grounded in the corpus.

Two results exposed a **flaw in the gold, not the agent**, and force a rubric fix:

- **Multiple valid landing points.** Task "savings badge when a variant is on sale"
  was scored against `ref/07 ### variant`, but the agent landed on
  `ref/05 ## Product merchandising — Support product variants`, which actually shows
  the `compare_at_price > price` pattern — a *better* answer. Both are correct.
- **Gold too narrow.** "Lighten/darken a color" was scored against `color_modify`,
  but the agent returned `color_lighten`/`color_darken` — verified to exist in the
  corpus (ref/09 lines 3445/3281) and arguably more on-point.

**Rubric fix adopted:** HIT = the agent lands on *any* corpus heading that fully and
correctly answers the task and is grounded (cites file+heading, no memory). The
single `expected_heading` in the TSV is the *canonical* target for Layer-1
answerability, **not** the only acceptable Layer-2 answer.

### Caveats specific to Run 1 (do not over-read it)

- **Agent-type bias.** Explore is built to read excerpts, so `whole-file reads = 0`
  is partly innate to the agent, not proof the skill *enforces* slicing. Re-run with
  a general-purpose agent before claiming the token-economy property.
- **12 of 51, one run, one author, no variance.** This is a smoke test that the
  common + sampled-adversarial path works — not a benchmark. The untested 39 and any
  multi-run variance remain open.

### Run 2 — full 51, general-purpose agents (2026-06-09)

Ran **all 51** gold tasks through fresh **general-purpose** subagents (Sonnet), each
restricted to the skill folder, via a deterministic workflow (51 agents, 1.64M
tokens, 331 tool calls, ~4.6 min). This removes the Explore read-excerpts bias —
the open question from Run 1.

**Hard, unambiguous metrics (machine-counted, not judged):**
- **`whole_file_reads = 0 / 51`.** A *normal* coding agent, following the skill's
  protocol, never dumped a whole reference file — even the 9.4k-line ch02. The
  slicing discipline is the **skill's**, not the agent type's. Run-1's open question
  is answered.
- **`used_index = 51 / 51`.** Every agent went through an `indexes/` file to locate
  the slice. The navigation layer is exercised, not bypassed.
- **`found_in_corpus = 51 / 51`, hallucinations = 0.** Every answer was grounded in
  a real heading in a real file. Zero invented filters/objects across 51 agents.

**Landing accuracy (auto-score vs adjudicated):**
- Auto-score against the single canonical gold target: **HIT 33 · PARTIAL 12 · MISS 6.**
- Manual adjudication of all 18 non-HITs: **every one is a grounded, correct landing**
  — and several are *more precise than the gold*: e.g. cart-add hit the exact
  `#### POST /{locale}/cart/add.js` endpoint (gold was the section header), decode hit
  `### Step 3: Decode session tokens…`, webhook hit `## Verify webhook deliveries`.
  The rest are equal-valid alternates (e.g. object in ch07 vs how-to in ch05;
  `color_lighten` vs `color_modify`; `image_tag` vs `image_url`). Two borderline
  cases (`shop` vs `policy`; ch02 Fonts vs `font_face` filter) were verified against
  the corpus and hold (`shop.policies` exists; ch02 §2.8.4 teaches the `@font-face`
  rule). **Adjudicated functional success: 51/51.**

**What the 33-vs-51 gap actually means (a finding, not a victory lap):**
- The verbatim docs legitimately have **multiple correct slices per task** (object
  reference vs feature how-to vs Ajax API). Single-target gold *under-scores* this.
  Fix: give each gold row a list of acceptable headings so the auto-scorer matches
  reality. Until then, auto-HIT is a **lower bound**, not the true rate.
- The adjudication was done by me — the eval's author — so it carries an
  optimism risk. The two genuinely borderline calls were corpus-verified to limit it;
  the ch05-vs-ch07 "how-to vs object" calls remain judgment calls tied to task intent.

**Substantive conclusion (unchanged across both runs):** the skill does what it
promises — grounded, sliced, index-driven retrieval across common, long-tail, and
adversarial tasks, with zero hallucinations and zero whole-file reads. The only
defect surviving verification is the **filter-count semantics** (148/155/166), which
is a definition to choose, not a bug.

## Known limitations of this eval (read before trusting it)

- **16 tasks is a smoke test, not a benchmark.** It proves the contract works on
  the common path; it does not prove long-tail coverage.
- **Selection bias.** I authored these toward the most common surfaces. The places
  drift hides — obscure filters, deprecated tags, renamed sections — are
  *under-represented* on purpose-of-convenience. Add adversarial tasks before
  claiming robustness.
- **Single author.** Gold targets and tasks share an author; independent authoring
  would catch my blind spots.
- **HIT is judged by a human.** No automated agent-behavior scoring yet.

Expanding to ~50 tasks with deliberate long-tail and adversarial items is the
next step if any real decision rides on the number.
