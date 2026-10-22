#!/usr/bin/env python3
"""Re-run the Europe PMC title and abstract searches described in the report.

Writes one text file per query into results/. Needs internet. Standard library only.
Hit counts can grow over time as new papers are indexed.
"""
from __future__ import annotations

import json
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results"
API = "https://www.ebi.ac.uk/europepmc/webservices/rest/search?"

QUERIES = {
    "nad_precursors_and_metformin": (
        '(TITLE_ABS:"BubR1" OR TITLE_ABS:"BUB1B") AND (TITLE_ABS:"nicotinamide" OR TITLE_ABS:"niacin" '
        'OR TITLE_ABS:"nicotinic acid" OR TITLE_ABS:"nicotinamide riboside" OR TITLE_ABS:"NMN" OR TITLE_ABS:"metformin")'
    ),
    "other_named_drugs": (
        '(TITLE_ABS:"BubR1" OR TITLE_ABS:"BUB1B") AND (TITLE_ABS:"geldanamycin" OR TITLE_ABS:"dasatinib" '
        'OR TITLE_ABS:"quercetin" OR TITLE_ABS:"everolimus" OR TITLE_ABS:"sirolimus" OR TITLE_ABS:"aspirin" '
        'OR TITLE_ABS:"resveratrol")'
    ),
    "arimoclomol": (
        '(TITLE_ABS:"BubR1" OR TITLE_ABS:"BUB1B" OR TITLE_ABS:"spindle checkpoint" '
        'OR TITLE_ABS:"spindle assembly checkpoint") AND TITLE_ABS:"arimoclomol"'
    ),
}


def search(q: str, n: int = 100) -> dict:
    url = API + urllib.parse.urlencode({"query": q, "format": "json", "pageSize": n, "resultType": "lite"})
    with urllib.request.urlopen(url, timeout=60) as fh:
        return json.load(fh)


def main() -> None:
    OUT.mkdir(exist_ok=True)
    for name, q in QUERIES.items():
        d = search(q)
        lines = [f"query: {q}", f"hits: {d['hitCount']}", ""]
        for r in d["resultList"]["result"]:
            lines.append(f"{r.get('pmid', '-')}\t{r.get('pubYear', '')}\t{r.get('title', '')}\t{r.get('journalTitle', '')}")
        (OUT / f"{name}.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"{name}: {d['hitCount']} hits -> results/{name}.txt")


if __name__ == "__main__":
    main()
