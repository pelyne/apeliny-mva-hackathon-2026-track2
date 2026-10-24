# Track 2: A direction filter and a testable path for BUB1B mosaic variegated aneuploidy

**Entrant:** Azra Pelin Yildirim (Hugging Face: apeliny)
**Contest:** SageBio / Hugging Face, "Rare Disease, Real Kid: MVA Hackathon 2026", Track 2 (drug repurposing)
**Scope:** Not a diagnosis and no doses. "Avoid: wrong direction" means the drug's published mechanism points the wrong way for this gene, not a clinical instruction.

## Summary

My Track 2 work delivers three things.

First, a short list of drugs and drug classes marked "Avoid: wrong direction". Their published mechanism weakens the spindle checkpoint or targets cells with a weak one, and in BUB1B mosaic variegated aneuploidy that checkpoint is already weak.

Second, a testable path built on the one pathway with a published BubR1-raising result, the NAD+/SIRT2/BubR1 axis. Nicotinamide mononucleotide (NMN) is the lead molecule, with a cheap, ordered plan to test it in this child's own cells.

Third, a reusable direction filter that any team can run on any checkpoint-deficiency gene before spending money on lab work.

All of it stands on my Track 1 finding: two BUB1B variants, chr15:40209701 T>G (stop-gained) and chr15:40220612 T>G (missense), GRCh38, about 11 kb apart, presumed in trans, which parental testing can confirm. Standard cancer surveillance under existing MVA guidance stays exactly as it is.

## The foundation: my Track 1 finding

In Track 1 I found two BUB1B variants in the proband: chr15:40209701 T>G, which introduces a premature stop, and chr15:40220612 T>G, a missense change, about 11 kb apart in the same gene. It was the only recessive pair left in my preregistered MVA gene panel after my filters, and my separate phenotype ranking pointed to the same gene.

The pair matches the classic genetic pattern of BUB1B MVA. Biallelic loss of BUB1B is the established cause of mosaic variegated aneuploidy with childhood cancer risk (Hanks 2004, PMID 15475955). In the patient cells that have been studied, the usual pattern is exactly this one: one truncating allele plus one missense allele, low total BubR1 protein, and a checkpoint that recovers when normal BubR1 is put back (Suijkerbuijk 2010, PMID 20516114). I read the two variants as presumed in trans, which parental testing can confirm, and Track 2 is built on that reading.

## The direction filter

The filter is three questions, asked in this order, before anyone argues about evidence quality.

**1. Which way does the disease push?** With a truncating plus a missense allele, the proband is expected to have too little BubR1 and a weak checkpoint. The therapeutic direction is therefore up: more residual BubR1, more checkpoint function, fewer lagging chromosomes. More BubR1 is protective in mice, with fewer chromosome segregation errors, fewer tumors and a longer healthy life in animals kept at a high BubR1 level (Baker 2013, PMID 23242215).

**2. Which way does the drug push?** Take the drug's own published mechanism, not its marketing. If the published result is that the compound lowers BubR1, inhibits the checkpoint, or exploits checkpoint weakness to kill cells, it is pushing down. A drug that pushes down is excluded by direction. No amount of trial data in another disease rescues it, because the mechanism is the harm.

**3. Does the filter apply to this gene?** Checkpoint deficiency is not uniform across MVA genes. Cells from people with biallelic BUB1B or TRIP13 variants show a badly impaired checkpoint, while CEP57-type MVA does not show that same collapse (Yost 2017, PMID 28553959). So the sign is set per gene, from the measured checkpoint phenotype of that gene, and not from the word "aneuploidy".

The filter is deliberately simple. It runs first and cheaply, so the expensive evidence review only happens on candidates that could help rather than harm.

What I think is new here is the order of the work. Before judging how strong any evidence is, I ask which way the disease pushes and which way the drug pushes, and I drop anything pointing the wrong way. That simple check caught a real trap: nicotinamide is often treated as the approved substitute for NMN, but in the same paper it lowered BubR1. I also publish every rejected drug with its direction and reason, so anyone can check or overturn a single row.

## What I looked for and how

I ran the search as an approved-drug hunt with a single target question: is there any market-approved human medicine with a published result in which BubR1 or BUB1B protein goes up?

I started with manual checks: web searches for BubR1 and BUB1B paired with raise, increase and stabilize, and with drug and compound; then BubR1 paired with each named candidate (nicotinamide, niacin, nicotinamide riboside, NMN, metformin, resveratrol, everolimus, sirolimus, dasatinib, quercetin, geldanamycin, and FDA-approved); and a PubMed search for BubR1 AND (nicotinamide OR niacin OR metformin OR "nicotinic acid" OR "nicotinamide riboside"). Then I ran three Europe PMC title and abstract searches, and these three are the ones scripts/literature_search.py re-runs. BubR1 with the NAD-precursor and metformin terms returned 4 hits, none of them showing an approved drug that raises BubR1 (one is about the NAMPT enzyme, not a drug). BubR1 with the geldanamycin, dasatinib, quercetin, everolimus, sirolimus, aspirin and resveratrol terms returned 6 hits, none of them a BubR1-raising drug paper. Arimoclomol with BubR1, BUB1B or the spindle checkpoint returned 0 hits.

For every paper I kept, I opened the PubMed abstract, and for North 2014 (PMID 24825348), Baker 2013 Nature Cell Biology (PMID 23242215), Baker 2011 (PMID 22048312), Baker 2013 Cell Reports (PMID 23602569) and Sieben 2020 (PMID 31738183) I also opened the full text or publisher HTML and read the specific figure or paragraph I cite. Hanks 2004, Suijkerbuijk 2010 and Yost 2017 are cited from their abstracts.

I only build on what I verified. Four things I left UNVERIFIED and kept out of the argument: the 2026 shelf and regulatory status of nicotinamide riboside and niacin beyond the FDA statement on NMN; the hepatic risk of high-dose nicotinamide; human senolytic trial outcomes; and an older metformin insulin-receptor citation from my own earlier working table, which I could not re-fetch and therefore dropped.

That search shaped everything below. The one pathway with a published BubR1-raising result is the NAD+/SIRT2 axis, and it is the basis for the testable path.

## Drug classes to avoid, and candidates I checked

Direction is relative to what would help the proband, which is more BubR1 and a stronger checkpoint.

The table is a direction check on published mechanism. "Avoid: wrong direction" marks a drug whose own mechanism pushes the checkpoint down. It is not a judgment on any cancer treatment, where other considerations apply.

| Candidate | Class | Approved status | Direction vs BubR1 | Key evidence (PMID) | Verdict | Reason |
|---|---|---|---|---|---|---|
| NMN (nicotinamide mononucleotide) | NAD+ precursor | Not an approved drug; US FDA treats it as a dietary supplement (Sept 2025) | Up | 24825348 | Lead path: test, not give | Raised BubR1 protein in mouse testes and in SIRT2-dependent mouse cells. Not an approved medicine, so it is the lead to test, not a drug to give. |
| Nicotinamide | Vitamin B3 form, sirtuin inhibitor | Used medically, e.g. pellagra | Down | 24825348 | Avoid: wrong direction | A SIRT2 inhibitor and the most commonly taken B3 form. In the same paper it lowered BubR1 protein in cells and blocked SIRT2 in vitro (Figure 1). NMN is the testable path; nicotinamide is the one to avoid. |
| Nicotinamide riboside | NAD+ precursor | Supplement | Unknown | none | Not pursued | No opened paper shows it raises BubR1. |
| Niacin (nicotinic acid) | Vitamin B3 form, lipid drug | Approved for dyslipidemia | Unknown | none | Not pursued | A different B3 molecule with no BubR1 result in anything I opened. UNVERIFIED as a BubR1 therapy. |
| Metformin (high dose) | Biguanide | Approved (type 2 diabetes) | Down | 35568294 | Avoid: wrong direction | At lab concentrations (1 to 16 mM), metformin deregulated BUBR1 and MAD2, caused checkpoint dysfunction and raised genotoxic stress in cancer and non-cancer cells. The mechanism points the wrong way; the paper did not test clinical blood levels. |
| Everolimus | mTOR inhibitor | Approved | Not a BubR1 mechanism | 31738183; 23602569 | Not pursued | The mTORC1 signal was allele-specific in mice, present with one truncating allele and nearly absent with a missense allele; the only rapamycin diet note in these mice was preliminary, unpublished and showed no benefit; immunosuppression in a cancer-prone child is a hard objection. |
| Sirolimus | mTOR inhibitor | Approved | Not a BubR1 mechanism | 31738183; 23602569 | Not pursued | Same class, same allele-specificity problem, same immunosuppression objection. |
| Dasatinib plus quercetin and other senolytics | Senolytics | Mixed; the pair is not approved for this use | Not a BubR1 mechanism | 22048312 | Not pursued | The mouse experiment used a genetic switch (INK-ATTAC plus a lab chemical), not a human medicine, and overall survival was not substantially longer. Removing senescent cells may also remove a tumor-suppressive brake. UNVERIFIED for any human senolytic product. |
| SAC, MPS1, ATR and PARP inhibitors | Checkpoint and DNA damage response inhibitors | Mixed, several approved in oncology | Down | 28553959 (patient checkpoint already impaired) | Avoid: wrong direction | Their purpose is to exploit or deepen checkpoint weakness. In biallelic BUB1B the checkpoint is already badly impaired. The refusal is the direction of effect, not a drug-label quote. |
| BUB1B kinase binders and inhibitors | Targeted kinase agents | Experimental | Down | 28553959 (patient checkpoint already impaired) | Not pursued | "Binds BUB1B" in a cancer pitch means less checkpoint, not more. |
| KIF18A inhibitors | Mitotic kinesin inhibitors | Experimental | Down | none | Not pursued | Not approved, and designed to worsen mis-segregation. |
| Geldanamycin / tanespimycin | HSP90 inhibitors | Not approved; development halted | Context-dependent, in a cytotoxic mitotic-arrest combination | none | Not pursued | The BubR1 stabilization report sits in a cytotoxic mitotic-arrest context with a mitotic poison. Wrong setting and not approved. |
| Arimoclomol | HSP co-inducer | Approved in the US since September 2024 (Miplyffa, for Niemann-Pick disease type C) | Unknown | none | Not pursued | Approved, but I found no paper linking it to BubR1 or the spindle checkpoint (Europe PMC title and abstract search: 0 hits). An approval in another disease is not a mechanism for this one. |
| Mitotic poisons (colcemid/colchicine class) | Microtubule agents | Mixed | Down | none | Avoid: wrong direction | Deliberately induce mis-segregation. |

> **Not pursued is not ruled out.** These nine have no published evidence of pushing BubR1 the right way yet. Rerun `make search`, and if a new paper shows one raises BubR1, its row moves up through the same filter.

## A testable path forward

Of everything I checked, one pathway points the right way with published data behind it. SIRT2, using NAD+, removes an acetyl mark at lysine 668 of BubR1 that otherwise sends the protein to be degraded. Raising NAD+ with NMN increased BubR1 protein in young and old mouse testes, and in mouse cells only when SIRT2 was present (North 2014, PMID 24825348). More BubR1 is protective in mice, with fewer chromosome errors and fewer tumors (Baker 2013, PMID 23242215). That makes NMN the natural lead to test.

Today no market-approved drug is known to raise BubR1 and address the root cause; NMN is regulated in the United States as a dietary supplement, not as an approved medicine. The lifespan gain in low-BubR1 mice came from extra SIRT2, a genetic change, not from NMN. Nicotinamide, the vitamin B3 form often used as a stand-in, did the opposite in that same paper: BubR1 protein fell in treated cells, and the drop was not explained by cell-cycle composition or lower BubR1 messenger RNA (North 2014, Figure 1). So the B3 forms are not interchangeable: only NMN has a BubR1 protein result, and niacin and nicotinamide riboside have no BubR1 result in anything I opened.

That gives a clear path of five ordered steps, set out in "What confirms it next": confirm phase, measure BubR1 protein in this child's cells, measure the checkpoint phenotype, test NMN in those same cells against both BubR1 protein and chromosome errors, then look wider. If those results are positive, the next step would be a carefully supervised study approved by an ethics board.

The same filter explains why the oncology-style shortlist is marked "Avoid: wrong direction" rather than proposed. Checkpoint, MPS1, ATR and PARP inhibitors and mitotic poisons work by deepening checkpoint weakness. Nicotinamide joins them because it blocks SIRT2 and lowered BubR1 (North 2014, Figure 1), and it is the B3 form people most often take. BUB1B binders and KIF18A inhibitors point the same way, but they are experimental and not in real-world use, so I list them as not pursued rather than as drugs to avoid. High-dose metformin joins the avoid list on the evidence I opened, because its one BubR1 result, at lab concentrations of 1 to 16 mM, is deregulation of BUBR1 and MAD2 with added genotoxic stress (Lyu 2022, PMID 35568294).

## What confirms it next

Five ordered steps. Each is cheap, and each one tells us whether the next is worth doing.

Step 1, confirm phase. Parental testing if samples can be obtained, or long-read sequencing across the roughly 11 kb between the two positions. This locks in the classic two-hit pattern that everything downstream builds on.

Step 2, measure BubR1 in the child's cells. In patient-derived cells, quantify BubR1 protein. Many MVA missense changes sit in or near the kinase region and turn over fast (Suijkerbuijk 2010), so this step also places chr15:40220612 T>G in that structural picture and shows how much residual protein SIRT2 has to work with. If no protein is made, the NMN path stops here, because SIRT2 needs residual BubR1 to protect.

Step 3, measure the phenotype. In the same cells, measure checkpoint timing under a standard mitotic arrest and count lagging chromosomes and micronuclei. Use cells from other MVA genes as comparators, since CEP57-type cells are not expected to show the same checkpoint collapse (Yost 2017).

Step 4, test NMN in the child's cells. NMN is the molecule with the published result, and that result comes from young and old mouse testes plus mouse embryo cells; the protective high-BubR1 and lifespan results come from mouse genetics (a transgene and extra SIRT2). This step carries the idea into the child's own human cells. Read out both BubR1 protein and the segregation phenotype, not protein alone.

Step 5, then look wider. If NMN helps the child's cells, the next step would be a carefully supervised study approved by an ethics board, and I would screen market-approved NAD+-related agents against the same two readouts. I found no human MVA trial of any of these molecules, so these cell results are the evidence that would open that door.

Throughout, standard cancer surveillance under existing MVA guidance continues unchanged.

## What would change my mind

Any one of these would tell me the NMN path is the wrong road for this child, and I would rather know early.

1. The two variants sit on the same copy of BUB1B.
2. Cells from this genotype make no BubR1 protein at all. SIRT2 cannot stabilize a protein that is not there.
3. In a proper cell test, NMN does not raise BubR1, or it raises the protein but lagging chromosomes do not fall. A Western blot on its own is not a win.
4. Nicotinamide raises BubR1 in those same cells. That would contradict North 2014 Figure 1 and would force me to reopen the inhibitor claim.
5. Any proposal whose benefit depends on shutting the checkpoint down. That fails the sign test even when a paper calls the drug promising in cancer.

Everolimus stays off the table either way: immunosuppression in a cancer-prone child is a hard objection, and Sieben 2020 showed that high mTORC1 is not guaranteed with a missense allele.

## Scope

This is a research write-up for the judges and for any team that wants to rerun it. It is not a diagnosis and it gives no dose. The child's standard cancer surveillance continues exactly as it is. NMN is the lead to test in cells, not a medicine to give, and nicotinamide is not the approved form of NMN. The lifespan gain in low-BubR1 mice came from extra SIRT2, not from NMN. Everolimus and sirolimus are not chromosome fixes, and the rapamycin diet note in Baker 2013 Cell Reports is preliminary and unpublished, with no benefit seen. I kept experimental agents out of the approved-drug slot, and every citation here is one I opened myself.

## How this scales

The filter is gene-agnostic and disease-agnostic by construction. For any MVA gene, the inputs are the measured checkpoint phenotype of that gene and the published direction of the drug's mechanism, so the same three questions run unchanged for BUB1B, TRIP13 and CEP57, and they correctly give CEP57 a different answer rather than one blanket "aneuploidy" rule (Yost 2017).

More broadly, it applies to any rare-disease repurposing problem where the drug must push a pathway in a specific direction: loss-of-function conditions where oncology has a catalogue of inhibitors pointed the other way, haploinsufficiency where stabilizing residual protein is the goal, and any case where a supplement is being quietly substituted for the molecule that produced the published result. The reject table is the reusable artifact: each row carries a direction, an approval status and a named reason, so another team can audit it or overturn one row without rebuilding the argument.

It is also cheap. The filter runs on published mechanism before any wet work, which is what makes it usable by a small team with a literature search and an afternoon.

## Generative AI disclosure

I used three AI tools for literature search, drafting and code: Cursor Pro, Privacy Mode enabled; Claude Pro, training opt-out enabled ("Help improve Claude" off), no feedback provided; and Grok Bot, as an assistant. No raw genome or phenotype file was ever shared with any of them, and none of this data was used for training. Inputs were limited to code, public papers and the two public variant coordinates, chr15:40209701 T>G and chr15:40220612 T>G. I checked every citation in this report by opening its abstract or full text myself. For the pitch video, ElevenLabs helped me polish my pronunciation.

## References

1. Hanks S, et al. Constitutional aneuploidy and cancer predisposition caused by biallelic mutations in BUB1B. Nature Genetics, 2004. PMID 15475955.
2. Suijkerbuijk SJE, et al. Molecular causes for BUBR1 dysfunction in the human cancer predisposition syndrome mosaic variegated aneuploidy. Cancer Research, 2010. PMID 20516114.
3. Baker DJ, et al. Clearance of p16Ink4a-positive senescent cells delays ageing-associated disorders. Nature, 2011. PMID 22048312.
4. Baker DJ, et al. Increased expression of BubR1 protects against aneuploidy and cancer and extends healthy lifespan. Nature Cell Biology, 2013. PMID 23242215.
5. Baker DJ, et al. p21 both attenuates and drives senescence and aging in BubR1 progeroid mice. Cell Reports, 2013 (rapamycin diet paragraph; result described there as preliminary and unpublished). PMID 23602569.
6. North BJ, et al. SIRT2 induces the checkpoint kinase BubR1 to increase lifespan. EMBO Journal, 2014. PMID 24825348.
7. Yost S, et al. Biallelic TRIP13 mutations predispose to Wilms tumor and chromosome missegregation. Nature Genetics, 2017. PMID 28553959.
8. Sieben CJ, et al. BubR1 allelic effects drive phenotypic heterogeneity in mosaic-variegated aneuploidy progeria syndrome. Journal of Clinical Investigation, 2020. PMID 31738183.
9. Lyu T, et al. High-dose metformin induces a low-glucose dependent genotoxic stress. Food and Chemical Toxicology, 2022. PMID 35568294.

Judging anchors for the reader: rigor is in "What I looked for and how", the drug table and "What would change my mind"; impact is in "A testable path forward" and "What confirms it next"; innovation is the direction filter itself; scalability is in "How this scales".
