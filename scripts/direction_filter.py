#!/usr/bin/env python3
"""Direction filter for checkpoint-deficiency drug repurposing.

Three questions, in order:
  1. Which way does the disease push? (set per gene from its measured checkpoint phenotype)
  2. Which way does the drug push? (from the drug's own published mechanism)
  3. Does the filter apply to this gene? (if the gene has no measured checkpoint collapse, the sign is not set)

Consistency rules: a "flag" row must push down, a "lead-path" row must push the helpful
way, and every row that pushes down and is in real-world use (column in_real_world_use)
must be a "flag" row, labelled "Avoid: wrong direction".

It reads the candidate table, sorts each row by direction, and checks that the
human verdicts in the table never contradict the direction.
Uses only the Python standard library.
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "data" / "apeliny_track2_candidates.csv"

# Therapeutic direction for BubR1/checkpoint function, per gene.
# BUB1B and TRIP13: badly impaired checkpoint in patient cells, so the goal is up.
# CEP57: no matching checkpoint collapse reported (Yost 2017, PMID 28553959), so the sign is not set.
GENE_SIGN = {"BUB1B": "up", "TRIP13": "up", "CEP57": None}


def drug_push(raw: str) -> str:
    v = raw.strip().lower()
    if v == "up":
        return "up"
    if v == "down":
        return "down"
    if v == "unknown":
        return "unknown"
    return "other"


def classify(goal: str | None, push: str) -> str:
    if goal is None:
        return "sign not set for this gene: measure the checkpoint first"
    if push == "unknown":
        return "no published direction: no basis to test"
    if push == "other":
        return "not a direct checkpoint mechanism: judged on its own evidence"
    if push == goal:
        return "passes direction: worth an evidence review and a cell test"
    return "excluded by direction: Avoid, wrong direction"


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--input", type=Path, default=DEFAULT)
    p.add_argument("--gene", default="BUB1B", choices=sorted(GENE_SIGN))
    args = p.parse_args()

    goal = GENE_SIGN[args.gene]
    rows = list(csv.DictReader(args.input.open(newline="", encoding="utf-8")))
    problems = []
    print(f"gene={args.gene} therapeutic_direction={goal or 'not set'} rows={len(rows)}\n")
    for r in rows:
        push = drug_push(r["direction_vs_BubR1"])
        print(f"{r['candidate']}\n    drug pushes: {push}  ->  {classify(goal, push)}\n    table verdict: {r['verdict']}")
        if goal is not None:
            if r["role"] == "flag" and push == goal:
                problems.append(f"{r['candidate']}: marked Avoid but pushes the helpful way")
            if r["role"] == "lead-path" and push != goal:
                problems.append(f"{r['candidate']}: lead path but does not push the helpful way")
            in_use = r.get("in_real_world_use", "").strip().lower()
            if in_use not in ("yes", "no"):
                problems.append(f"{r['candidate']}: in_real_world_use must be yes or no")
            if push == "down" and push != goal and in_use == "yes" and r["role"] != "flag":
                problems.append(f"{r['candidate']}: pushes the wrong way and is in real-world use, but is not marked Avoid")
            if r["role"] == "flag" and push != "down":
                problems.append(f"{r['candidate']}: marked Avoid without a Down direction")
        if not r["key_evidence_PMID"].strip():
            problems.append(f"{r['candidate']}: empty evidence field (use a PMID or 'none')")
    print()
    if problems:
        print("CONSISTENCY PROBLEMS:")
        for x in problems:
            print("  " + x)
        return 1
    print("consistency check: OK (no verdict contradicts its direction; every Down drug in real-world use is marked Avoid)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
