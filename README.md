# AI & Growth Scenario Tracker

A living, single-page tracker that maps the **measured AI automation rate** onto the growth-scenario spectrum of Jones & Tonetti (2026), *Past Automation and Future A.I.: How Weak Links Tame the Growth Explosion*.

**What it does.** The macroeconomics of AI, in the JT task-based model, collapses to one statistic — the automation rate `x₀` (the share of total labor cost accounted for by tasks newly handed to capital each year). `x₀` pins down the degree of dynamic increasing returns `Φ`, and `Φ` decides whether growth stays balanced (`Φ < 1`), sits on the knife-edge (`Φ = 1`), or explodes (`Φ > 1`). JT could not observe `x₀`, so they elicited it from frontier LLMs. The [Anthropic Economic Index](https://www.anthropic.com/economic-index) measures it from real usage. This tool turns that measurement into the scenario picture.

**The engine.** Jones & Tonetti's published approximation:

```
Φ ≈ ( ψ̇_ℓ + x₀ / (1 − σ) ) / g_Y0
```

with their calibration `ψ̇_ℓ = 0.5%/yr`, `g_Y0 = 3%/yr`, `n = 1%/yr`, `σ = 0.2`. Drag `x₀` and `σ` to see the regime change; the two reference ticks are JT's elicited anchors (private business `x₀ = 2.0%` → `Φ ≈ 1.00`; computers / "Moore's Law everywhere" `x₀ = 5.2%` → `Φ ≈ 2.33`).

## Status

- **Live now:** the interactive `Φ` engine and JT's two reference scenarios.
- **Pending:** the AEI-measured `x₀` for software/computing (the "level-1" estimate — AEI automation shares × OEWS labor-cost weights, flows-only assumption). Lands in `data/estimate.json` and the reference table when computed. See the accompanying research proposal for the identification caveats (penetration scaling, short sample, occupation selection).

## Run locally

It's a static page with no dependencies:

```bash
# either just open the file
open index.html
# or serve it (needed if you switch to fetching data/estimate.json)
python3 -m http.server 8000   # then visit http://localhost:8000
```

## Deploy on GitHub Pages

```bash
git init && git add . && git commit -m "AI & growth scenario tracker"
gh repo create ai-growth-tracker --public --source=. --push   # GitHub CLI
# (or create the repo on github.com and: git remote add origin <url> && git push -u origin main)
```

Then enable Pages: repo **Settings → Pages → Source: deploy from branch → `main` / root**. The site publishes at:

```
https://vcormun.github.io/ai-growth-tracker/
```

## Sources

- Jones, C. I. & Tonetti, C. (2026). *Past Automation and Future A.I.: How Weak Links Tame the Growth Explosion.*
- Aghion, P., Jones, B. F. & Jones, C. I. (2019). *Artificial Intelligence and Economic Growth.* NBER w23928.
- Anthropic Economic Index — data: https://huggingface.co/datasets/Anthropic/EconomicIndex

## License

MIT (see `LICENSE`). Illustrative tool, not investment or forecasting advice.
