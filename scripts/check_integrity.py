#!/usr/bin/env python3
"""
check_integrity.py — deterministic, dependency-free integrity guard for the
Shopify-Development skill. Validates the *navigation contract* the skill sells:
every index -> reference target must resolve, every internal link must point at a
real file/anchor, and the filter-count semantics must be made explicit.

Run from the repo root:  python3 scripts/check_integrity.py
Exit code: 0 if no hard failures, 1 if broken file links or missing nav targets.
It is a REPORT, not an opinion: it prints what it checked and what it skipped.
No network. No external links validated (those rot independently; see NOTE).
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILL = os.path.join(ROOT, "shopify-development")
REF = os.path.join(SKILL, "reference")
IDX = os.path.join(SKILL, "indexes")

fails = []          # hard failures (broken file link / missing nav target)
warns = []          # soft (anchor not found via slug heuristic)


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def lines(path):
    return read(path).splitlines()


# ---------------------------------------------------------------- GitHub slugger
def slugify(heading_text):
    """Replicate github-slugger: lower, drop non [\\w\\s-], then replace EACH space
    with '-' (github-slugger does NOT collapse runs — '— ' -> '--'). \\w=[a-z0-9_]."""
    s = heading_text.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s, flags=re.ASCII)   # ASCII \w = [a-zA-Z0-9_]
    s = s.replace("\t", " ").replace(" ", "-")       # per-space, no collapsing
    return s


def heading_slugs(path):
    slugs = {}
    for ln in lines(path):
        m = re.match(r"^(#{1,6})\s+(.*?)\s*$", ln)
        if m:
            base = slugify(m.group(2))
            # github-slugger disambiguates repeats with -1, -2 ...
            n = slugs.get(base, 0)
            slugs[base] = n + 1
    out = set()
    for base, count in slugs.items():
        out.add(base)
        for i in range(1, count):
            out.add(f"{base}-{i}")
    return out


# --------------------------------------------------- self-test of the slugifier
def slug_selftest():
    known = {
        "⚡ Install": "-install",
        "📦 What's inside": "-whats-inside",
        "🔍 How it works": "-how-it-works",
        "💡 Example": "-example",
        "❓ FAQ": "-faq",
        "Reference chapter map": "reference-chapter-map",
    }
    bad = [(h, slugify(h), exp) for h, exp in known.items() if slugify(h) != exp]
    return bad


# -------------------------------------------------------- (a) internal md links
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def all_md_files():
    for dp, dns, fns in os.walk(ROOT):
        if ".git" in dp.split(os.sep):
            continue
        for fn in fns:
            if fn.endswith(".md"):
                yield os.path.join(dp, fn)


CONTENT_ROOTS = ("docs/", "api/", "apps/", "themes/", "storefronts/")


def is_repo_relative(path_part):
    """A link is an intra-repo navigation link only if it is explicitly relative
    (./ ../) or a bare *.md/*.svg sibling. Everything else that doesn't resolve is
    a verbatim shopify.dev content href, not a navigation target."""
    return (path_part.startswith(("./", "../"))
            or path_part.endswith((".md", ".svg")))


def check_links():
    ext = internal_file = internal_anchor = content = 0
    for md in all_md_files():
        base = os.path.dirname(md)
        for raw in LINK_RE.findall(read(md)):
            target = raw.split()[0].strip()          # drop optional "title"
            if target.startswith(("http://", "https://", "mailto:")):
                ext += 1
                continue
            path_part, _, anchor = target.partition("#")
            rel = os.path.relpath(md, ROOT)
            if path_part == "":                      # same-file anchor
                internal_anchor += 1
                if anchor and slugify(anchor) not in heading_slugs(md):
                    warns.append(f"[anchor] {rel}: #{anchor} not found in same file")
                continue
            dest = os.path.normpath(os.path.join(base, path_part))
            if os.path.exists(dest):                 # real repo file
                internal_file += 1
                if anchor and dest.endswith(".md"):
                    internal_anchor += 1
                    if slugify(anchor) not in heading_slugs(dest):
                        warns.append(f"[anchor] {rel}: {path_part}#{anchor} not found")
                continue
            # does not exist on disk -> repo-nav link (FAIL) or content href (note)?
            if (path_part.startswith("/") or path_part.startswith(CONTENT_ROOTS)
                    or not is_repo_relative(path_part)):
                content += 1                         # verbatim shopify.dev href
            else:
                fails.append(f"[link] {rel}: -> {path_part} (broken repo nav link)")
    return ext, internal_file, internal_anchor, content


# ----------------------------------------- (b) index -> reference nav targets
def first_backtick_cell(line):
    """first-column backtick token of a markdown table row, else None."""
    if not line.startswith("|"):
        return None
    cell = line.split("|", 2)[1] if line.count("|") >= 2 else ""
    m = re.search(r"`([^`]+)`", cell)
    return m.group(1) if m else None


def heading_lines(path, prefix):
    return {ln.strip() for ln in lines(path) if ln.startswith(prefix)}


def check_objects():
    ref = os.path.join(REF, "07-liquid-objects.md")
    present = {ln[4:].strip() for ln in lines(ref) if ln.startswith("### ")}
    names, missing = [], []
    for ln in lines(os.path.join(IDX, "liquid-objects.md")):
        n = first_backtick_cell(ln)
        if n and n not in ("name",):
            names.append(n)
            if n not in present:
                missing.append(n)
    for n in missing:
        fails.append(f"[nav object] index lists `{n}` but `### {n}` absent in ref/07")
    return len(names), len(missing)


def check_tags():
    ref = os.path.join(REF, "08-liquid-tags.md")
    present = {ln[3:].strip() for ln in lines(ref) if ln.startswith("## ")}
    names, missing = [], []
    for ln in lines(os.path.join(IDX, "liquid-tags.md")):
        n = first_backtick_cell(ln)
        if n:
            names.append(n)
            if n not in present:
                missing.append(n)
    for n in missing:
        fails.append(f"[nav tag] index lists `{n}` but `## {n}` absent in ref/08")
    return len(names), len(missing)


def filter_headings():
    """unique filter NAMES from '## <cat> — <name>' headings across ref/09+10."""
    listings = []
    for fn in ("09-liquid-filters-part1.md", "10-liquid-filters-part2.md"):
        for ln in lines(os.path.join(REF, fn)):
            if ln.startswith("## ") and "—" in ln:      # em-dash
                listings.append(ln.split("—", 1)[1].strip())
    return listings


def index_filter_names():
    names = []
    for ln in lines(os.path.join(IDX, "liquid-filters.md")):
        n = first_backtick_cell(ln)
        if n and n not in ("name",):
            names.append(n)
    return names


def check_filters_and_counts():
    listings = filter_headings()
    uniq_ref = sorted(set(listings))
    dupes = sorted({x for x in listings if listings.count(x) > 1})
    idx_names = index_filter_names()
    idx_uniq = sorted(set(idx_names))

    in_idx_not_ref = sorted(set(idx_uniq) - set(uniq_ref))
    in_ref_not_idx = sorted(set(uniq_ref) - set(idx_uniq))

    for n in in_idx_not_ref:
        fails.append(f"[nav filter] index lists `{n}` but no `## … — {n}` heading in ref/09-10 (dead nav target)")
    for n in in_ref_not_idx:
        warns.append(f"[nav filter] ref has filter `{n}` but it's NOT in the index (unnavigable)")

    return {
        "listings": len(listings),
        "uniq_ref": len(uniq_ref),
        "idx_rows": len(idx_names),
        "idx_uniq": len(idx_uniq),
        "dupes": dupes,
        "in_idx_not_ref": in_idx_not_ref,
        "in_ref_not_idx": in_ref_not_idx,
    }


def check_schemas_index():
    ref = os.path.join(REF, "02-key-concepts.md")
    body = read(ref)
    checked = skipped = miss = 0
    for ln in lines(os.path.join(IDX, "schemas.md")):
        if not ln.startswith("|"):          # grep targets live in the table only,
            continue                        # not in the prose preamble (e.g. `##### attr`)
        for tok in re.findall(r"`(#{1,6} [^`]+)`", ln):
            # skip placeholders & descriptive (non-literal) tokens
            if ("<" in tok or "…" in tok or "..." in tok
                    or tok.endswith(("2.x", "2.x.y"))):
                skipped += 1
                continue
            checked += 1
            # index targets are grep PREFIXES ("grep for the ## 2.4 heading"),
            # not full lines -> prefix match, allowing trailing heading text.
            if not re.search(r"^" + re.escape(tok) + r"(\s|$)", body, re.M):
                miss += 1
                fails.append(f"[nav schema] target `{tok}` not found as a heading in ref/02")
    return checked, skipped, miss


def check_taskrouting_sections():
    ref = os.path.join(REF, "02-key-concepts.md")
    present = {ln.strip() for ln in lines(ref) if re.match(r"^## 2\.\d+", ln)}
    present_prefix = {re.match(r"^(## 2\.\d+)", ln.strip()).group(1) for ln in present}
    checked = miss = 0
    for sec in sorted(set(re.findall(r"§(2\.\d+)", read(os.path.join(IDX, "task-routing.md"))))):
        checked += 1
        if f"## {sec}" not in present_prefix:
            miss += 1
            fails.append(f"[nav §] task-routing references §{sec} but no '## {sec}' heading in ref/02")
    return checked, miss


# ------------------------------------------- (c2) enforce filter-count claims
def check_filter_claims(canonical):
    """Every doc stating a filter count must state the canonical UNIQUE count.
    Catches the 148/155/166 drift recurring. Listing/row counts use other nouns
    ('listing', 'righe') so they are not matched."""
    targets = {
        "README.md": os.path.join(ROOT, "README.md"),
        "shopify-development/SKILL.md": os.path.join(SKILL, "SKILL.md"),
        "reference/00-INDICE.md": os.path.join(REF, "00-INDICE.md"),
        "indexes/liquid-filters.md": os.path.join(IDX, "liquid-filters.md"),
    }
    claims = {}
    for name, path in targets.items():
        if not os.path.exists(path):
            continue
        # only TOTAL claims matter (all >= 100); small descriptive counts
        # like "7 filtri in 2 categorie" or "3 array filters" are not totals.
        nums = [int(n) for n in re.findall(
            r"(\d+)\s+(?:Liquid\s+)?(?:filters?|filtri)\b", read(path), re.I)
            if int(n) >= 100]
        claims[name] = nums
        for n in nums:
            if n != canonical:
                fails.append(f"[filter-count] {name} states {n} filters as a total; canonical unique = {canonical}")
    return claims


# --------------------------------------------------- (eval) validate gold set
def check_eval_gold():
    gold = os.path.join(ROOT, "eval", "retrieval_gold.tsv")
    if not os.path.exists(gold):
        return None
    total = ok = 0
    for ln in lines(gold):
        if not ln.strip() or ln.startswith("#"):
            continue
        parts = ln.split("\t")
        if len(parts) < 4:
            continue
        _, _, ref_file, target = parts[0], parts[1], parts[2], parts[3]
        total += 1
        path = os.path.join(SKILL, ref_file)
        if os.path.exists(path) and re.search(r"^" + re.escape(target.strip()),
                                              read(path), re.M):
            ok += 1
        else:
            fails.append(f"[eval gold] task '{parts[0][:48]}' -> {ref_file} :: '{target}' NOT FOUND")
    return total, ok


# ----------------------------------------------------------------------- main
def main():
    print("=" * 72)
    print("SHOPIFY-DEV SKILL — INTEGRITY REPORT (deterministic, offline)")
    print("=" * 72)

    st = slug_selftest()
    print(f"\n[slugifier self-test] {'PASS' if not st else 'FAIL: ' + str(st)}")

    ext, ifile, ianch, content = check_links()
    print(f"\n(a) LINKS  internal-file={ifile}  internal-anchor={ianch}  "
          f"external-skipped={ext}  verbatim-content-hrefs={content}")

    on, om = check_objects()
    tn, tm = check_tags()
    print(f"(b) NAV    objects: {on} indexed, {om} missing | tags: {tn} indexed, {tm} missing")

    sc, ss, sm = check_schemas_index()
    print(f"           schemas index: {sc} literal targets checked, {ss} placeholders skipped, {sm} missing")
    trc, trm = check_taskrouting_sections()
    print(f"           task-routing §: {trc} section refs checked, {trm} missing")

    fc = check_filters_and_counts()
    canonical = fc["uniq_ref"]
    print("\n(c) FILTER COUNT — canonical = unique filter names:")
    print(f"      canonical (unique filters) ............... {canonical}")
    print(f"      index rows (liquid-filters.md) ........... {fc['idx_rows']}  ({fc['idx_uniq']} unique; {fc['idx_rows'] - fc['idx_uniq']} multi-category rows)")
    print(f"      total listings (filter × category) ....... {fc['listings']}  (= {canonical} unique + {len(fc['dupes'])} cross-category dupes)")
    claims = check_filter_claims(canonical)
    flat = sorted({n for ns in claims.values() for n in ns})
    consistent = flat == [canonical] or flat == []
    print(f"      doc claims found ......................... {flat}  -> {'CONSISTENT' if consistent else 'MISMATCH'}")
    if fc["in_idx_not_ref"]:
        print(f"    in INDEX, no ref heading ({len(fc['in_idx_not_ref'])}): {', '.join(fc['in_idx_not_ref'])}")
    if fc["in_ref_not_idx"]:
        print(f"    in REF, not in index ({len(fc['in_ref_not_idx'])}): {', '.join(fc['in_ref_not_idx'])}")

    ev = check_eval_gold()
    if ev is not None:
        print(f"\n(eval) GOLD SET: {ev[1]}/{ev[0]} gold targets resolve to a real heading")

    print("\n" + "-" * 72)
    print(f"WARNINGS (soft): {len(warns)}")
    for w in warns:
        print("  ! " + w)
    print(f"\nHARD FAILURES: {len(fails)}")
    for f in fails:
        print("  ✗ " + f)
    print("-" * 72)
    if not fails:
        print("RESULT: PASS — navigation contract holds, no broken internal links.")
    else:
        print(f"RESULT: FAIL — {len(fails)} hard failure(s).")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
