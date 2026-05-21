# Parameter scale calculator

**Tier:** 2 | **Type:** React (COMPANYSITE) | **Status:** done

**Blog:** Part 3 · `#parameter-scale`

## Overview

Pick a model scale (or enter parameter count) and see **how many weights** the model has and a **rough memory footprint** if stored in FP16.

## What visitors learn

“124 million parameters” is abstract until you connect it to bytes in RAM and compare scales (GPT-2 Small vs 7B vs 70B). Counting parameters in the lab (`model.parameters()`) grounds those headline numbers.

## Connection to the lab

- [`llm_playground.ipynb`](../../llm_playground.ipynb) — **§2.2** Counting parameters (GPT-2 Small ≈ 124M)
- Markdown “think about scale” prompt (FP16 bytes, 70B model)

## Demo behavior

1. **Presets** (dropdown or buttons):
   - GPT-2 Small — 124M
   - GPT-2 XL — 1.5B (optional)
   - Llama-class 7B — 7B
   - Llama-class 70B — 70B
   - Custom — numeric input for parameter count
2. Display:
   - Parameter count (formatted: `124,000,000`)
   - FP16 storage: `params × 2 bytes` → MB / GB
   - Optional: FP32 (`× 4 bytes`) toggle for comparison
3. Optional: “I counted GPT-2 in PyTorch” callout with snippet from §2.2.

## Visual design

- Large number typography for parameter count.
- Bar or log-scale comparison chart across presets (not linear—use log axis).
- Infographic footnote: “Training needs far more memory than weights alone (optimizer states, activations).”

## Copy suggestions

> Every weight and bias in every layer is a parameter. GPT-2 Small has about 124 million—roughly 248 MB in half precision, weights only.

> Scaling to 70B parameters is not 500× “a bit slower”; it changes infrastructure, serving, and who can run the model at all.

## Technical notes

- **No model download required** for preset calculator—pure math UI.
- Optional “verify with GPT-2” button loads `gpt2` once and runs `sum(p.numel() for p in model.parameters())` (heavier; link to notebook instead for portfolio).
- **Hosting:** static JavaScript or lightweight Gradio; ideal for instant load on portfolio page.

## Build checklist

- [ ] Preset table with documented parameter sources
- [ ] Custom input + validation (positive integers)
- [ ] FP16 / FP32 byte calculator
- [ ] Log-scale chart component
- [ ] Cite notebook §2.2 in portfolio copy
- [ ] Optional: screenshot of actual `numel()` sum from lab

## Status

`done` — `ParameterScaleCalculator.tsx` on COMPANYSITE Part 3.
