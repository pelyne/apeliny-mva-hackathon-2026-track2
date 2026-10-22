# MVA Hackathon 2026: Track 2

This is my Track 2 (drug repurposing) entry for the [Rare Disease, Real Kid: MVA Hackathon](https://sagebio-rare-disease-real-kid-mva-hackathon-2026.hf.space/). My Track 1 entry, which found the variants this work starts from, is in a separate repo: [apeliny-mva-hackathon-2026-track1](https://github.com/pelyne/apeliny-mva-hackathon-2026-track1).

**No patient genome or phenotype is in this repository.** The only case details used are the two public variant coordinates from my Track 1 answer. This is not medical advice, not a diagnosis, and it gives no doses.

## What this work delivers

1. A short list of drugs and drug classes marked "Avoid: wrong direction" (checkpoint, MPS1, ATR and PARP inhibitors, mitotic poisons, nicotinamide, and metformin, whose BubR1 result was seen only at high lab concentrations), because their published mechanism weakens the spindle checkpoint or targets cells with a weak one.
2. A testable path built on the NAD+/SIRT2/BubR1 axis, with nicotinamide mononucleotide (NMN) as the lead molecule to test in the child's own cells first. The report sets out five ordered steps: phase, BubR1 protein, the checkpoint phenotype, NMN in the child's own cells, then a wider screen.
3. A reusable direction filter that any team can run on any checkpoint-deficiency gene before spending money on lab work.

Standard cancer surveillance under existing MVA guidance stays exactly as it is.

- Report: [report/apeliny_track2_report.md](report/apeliny_track2_report.md)
- Candidate table: [data/apeliny_track2_candidates.csv](data/apeliny_track2_candidates.csv)

## The case

Track 2 builds on my Track 1 finding: two *BUB1B* variants on GRCh38, `chr15:40209701 T>G` (stop-gained) and `chr15:40220612 T>G` (missense), about 11 kb apart. It was the only recessive pair left in my preregistered MVA gene panel after my filters, and my phenotype ranking pointed to the same gene. One truncating plus one missense allele is the classic genetic pattern of *BUB1B* MVA, with low BubR1 and a weak spindle checkpoint in published patient cells (Hanks 2004; Suijkerbuijk 2010). The two variants are presumed in trans, which parental testing can confirm.

## Repo layout

- `report/` holds the full write-up with references.
- `data/` holds the 14-candidate table: 1 lead, 4 marked "Avoid: wrong direction", 9 not pursued. Each row has a direction, an approval status, a real-world use flag, a PMID and a reason.
- `scripts/direction_filter.py` runs the three filter questions on the table and checks that no verdict contradicts its direction and that every Down drug in real-world use is marked Avoid.
- `scripts/literature_search.py` re-runs the three Europe PMC title and abstract searches from the report.
- `results/` holds the latest search output.

## Run it

Python 3 with the standard library is enough.

```bash
make check     # direction filter for BUB1B
python3 scripts/direction_filter.py --gene CEP57   # shows the sign is not set for CEP57
make search    # re-runs the literature searches (needs internet)
```

Search hit counts can grow as Europe PMC indexes more papers. On 21 Oct 2026 the three searches returned 4, 6 and 0 hits, and none of them reports an approved medicine that raises BubR1.

## Generative AI disclosure

I used Cursor Pro (Privacy Mode enabled), Claude Pro (training opt-out enabled, no feedback provided) and Grok Bot, as an assistant, for literature search, drafting and code. No patient data was used as training data. I checked every citation by opening its abstract or full text myself.

## License

CC BY 4.0, as the hackathon rules require. See [LICENSE](LICENSE).
