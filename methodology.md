# Methodology — the level-1 illustrative AEI estimate of x₀

This documents exactly how the "AEI-measured, economy-wide (illustrative)" number on the tracker is produced. It is a **level-1 proof-of-concept**, not the final identified estimate. Everything here is reproducible with `compute_x0.py`.

## What we are estimating

Jones & Tonetti (2026) define the **automation rate** `x₀` as the share of total labor cost accounted for by tasks that are *newly* handed from labor to capital each year. Their forward simulation maps `x₀` to the degree of dynamic increasing returns:

```
Φ ≈ ( ψ̇_ℓ + x₀ / (1 − σ) ) / g_Y0
```

with the JT calibration `ψ̇_ℓ = 0.5%/yr`, `g_Y0 = 3%/yr`, `σ = 0.2`, `n = 1%/yr`.

## Step 1 — the measured input: automation share `a`

From the Anthropic Economic Index, `release_2025_02_10/automation_vs_augmentation.csv` (Claude usage classified into six collaboration modes):

| mode | % | bucket |
|---|---|---|
| directive | 22.56 | automation |
| feedback loop | 12.04 | automation |
| task iteration | 25.48 | augmentation |
| learning | 18.92 | augmentation |
| validation | 2.31 | augmentation |
| none | 2.90 | — |

Following AEI's taxonomy, **automation = directive + feedback loop** and **augmentation = task iteration + learning + validation**. The automation share among classified collaborative conversations is

```
a = (22.56 + 12.04) / (22.56 + 12.04 + 25.48 + 18.92 + 2.31) = 0.43
```

This is the empirical anchor. Computing/software use skews more automating than the economy-wide average (first-party API traffic is ~77% automation in later releases), so `a = 0.43` is conservative for this sector; the high case uses `a = 0.77`.

This automation/augmentation split is also the conceptual hook of the proposal: AEI's **automation** modes are the empirical counterpart of JT's `β̇` (tasks moving to capital), while **augmentation** modes correspond to `ψ̇_ℓ` (labor getting more productive on retained tasks).

## Step 2 — from automation share to the automation rate `x₀`

`x₀` is a *flow* — newly automated labor cost per year — so it depends on the **change** in AI's reach, not its level. Writing the automated fraction of a task as `β = π · a` (AI penetration of the task × within-AI automation share) and using JT's `x = −Δln(1 − β)/Δt` with a common sector penetration, the level-1 estimate is

```
x₀ = −ln( 1 − a · Δπ )        (per year, Δt = 1)
```

where `Δπ` is the **annual increase in AI penetration** of the sector's task volume.

## Step 3 — the one assumption that matters: `Δπ`

`Δπ` is **not measured here** — it is the central unknown (and exactly the gap flagged in §4.3 of the proposal). AEI gives within-Claude shares, not economy-wide task penetration. We therefore report a range:

| case | a | Δπ (pp/yr) | x₀ (%/yr) | Φ (σ=0.2) | regime |
|---|---|---|---|---|---|
| low | 0.43 | 5 | 2.2 | 1.07 | explosive (~460 yr horizon) |
| **base** | **0.45** | **8** | **3.7** | **1.69** | **explosive (~48 yr horizon)** |
| high | 0.77 | 15 | 12.3 | 5.28 | explosive (~8 yr horizon) |

For context, JT's elicited anchors are private business `x₀ = 2.0%` (Φ = 1.00) and computers / "Moore's Law everywhere" `x₀ = 5.2%` (Φ = 2.33). The base AEI case sits **between** them.

`Δπ` is anchored loosely to adoption evidence (Census BTOS firm AI adoption ≈ 18% end-2025, rising; software is the most penetrated sector). Replacing this assumption with a measured penetration series — e.g., from successive AEI releases or BTOS by sector — is the level-2 research task.

## Honest status

- **Measured:** the automation share `a` (from AEI).
- **Assumed:** the penetration-growth `Δπ`, and the JT structural parameters (`σ`, `ψ̇_ℓ`, `g_Y0`, taken from the paper).
- **Not yet done:** task-level construction with O\*NET task statements as the partition and OEWS×O\*NET labor-cost weights (`ω̃ʲ`); proper penetration scaling; the augmentation→`ψ̇_ℓ` channel. These are the proposal's deliverables.

The headline takeaway is deliberately framed around the boundary the data can speak to: **given the measured automation share, the growth regime is governed by how fast AI penetration rises** — a quantity AEI is positioned to measure over time, and the reason this tracker is built to update with each release.

## Reproduce

```bash
python3 compute_x0.py
```
