# Greedy vs top-p

**Tier:** 1 | **Type:** Interactive | **Status:** done

**Blog:** Part 2 · `#live-demo-decoding` · Space **Decoding** tab

## Overview

Same prompt, two decoding strategies: **greedy** (always highest probability) vs **top-p nucleus sampling**—side by side.

## What visitors learn

Text generation is a loop plus a **policy** for choosing the next token. Greedy is deterministic but often repetitive; top-p adds controlled randomness and usually sounds more natural.

## Connection to the lab

- [`llm_playground.ipynb`](../../llm_playground.ipynb) — **§3.1** Greedy decoding
- **§3.2** Top-p (nucleus) sampling

## Demo behavior

1. Visitor enters a prompt or selects a preset.
2. **Left panel:** `model.generate(..., do_sample=False)` (greedy).
3. **Right panel:** `model.generate(..., do_sample=True, top_p=p)` with slider for `p` (default 0.9).
4. Shared settings: `max_new_tokens` (e.g. 32–80), same GPT-2 model.
5. **Presets:** `"Once upon a time"`, `"What is 2+2?"`, `"Suggest a party theme."`
6. **Regenerate** button for top-p only (new random sample) to show variance.

## Visual design

- Two-column layout: **Greedy** | **Top-p (p=0.9)**.
- Slider under right column for `top_p` (0.5–1.0).
- Optional diff-style background when outputs diverge strongly.
- Caption under greedy panel when repetition appears (e.g. “the the the…”).

## Copy suggestions

> Decoding is not part of training—it is a choice at inference time. Greedy decoding always picks the most likely token, which can trap the model in loops. Top-p samples from a smaller “nucleus” of plausible tokens.

> Run the same preset twice with top-p: outputs change. Greedy stays the same every time.

## Technical notes

- **Model:** `gpt2` via `AutoModelForCausalLM`.
- **API:** Hugging Face `generate()` — `do_sample=False` vs `do_sample=True, top_p=...`.
- **Hosting:** CPU Space; generation may take 5–20s for longer `max_new_tokens`.
- **Seed:** optional `torch.manual_seed` for reproducible top-p demos in screenshots.

## Build checklist

- [ ] Dual `generate` calls with shared tokenized input
- [ ] `top_p` slider + regenerate for sampling side only
- [ ] Three preset buttons from notebook `tests` list
- [ ] Truncate/display full decoded string (strip prompt echo if desired)
- [ ] Note first-run model download in UI
- [ ] Combine into Gradio tab with tokenizer explorer / next-token (Phase 1 Space)

## Status

`done` — Space Decoding tab + COMPANYSITE Part 2.
