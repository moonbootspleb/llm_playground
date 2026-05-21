# Pipeline story

**Tier:** 3 | **Type:** Static scroll | **Status:** done

**Blog:** Part 4 · `/blog/llm-pipeline-from-text-to-output#pipeline-overview`

## Overview

A vertical **scroll narrative** that walks through the full LLM pipeline: raw text → tokens → model → logits → decode → generated text—one step per viewport with visuals from the lab.

## What visitors learn

How the pieces from the notebook connect in order. Visitors who only try one interactive demo still see the whole journey and where each demo sits in the stack.

## Connection to the lab

- [`llm_playground.ipynb`](../../llm_playground.ipynb) — full arc: **§1** Tokenization → **§2** Language model → **§3** Decoding → **§4** Modern models

## Demo behavior

1. Six sections (sticky scroll or full-page sections):
   1. **Text** — user prompt as plain string
   2. **Tokens** — chip visualization (screenshot: [../assets/tokenizer-explorer/tokens-tab-emoji.png](../assets/tokenizer-explorer/tokens-tab-emoji.png))
   3. **Model** — cropped architecture diagram (from transformer-block-diagram)
   4. **Logits** — top-k bar chart screenshot (from next-token microscope)
   5. **Decode** — greedy vs top-p snippet (from greedy-vs-top-p)
   6. **Output** — final generated text + optional GPT-2 vs Qwen footnote
2. Each section: **headline + 2 sentences + image placeholder** (`assets/pipeline/step-N.png`).
3. Final CTA: “Run the full lab” → Colab / GitHub.

## Visual design

- Scroll-snap or generous section padding; progress indicator on the side (optional).
- Consistent illustration style across steps (screenshots from same theme).
- Mobile: single column; reduce image height; keep headlines short.

## Copy suggestions

> Every chat message you send to an LLM travels this path. I built each step in a Jupyter lab before wrapping the highest-signal parts in interactive demos.

> This page is the map; the demos are the magnifying glass on individual stops.

## Technical notes

- **Pure static** content on portfolio site (HTML, MDX, or Astro section).
- Capture screenshots after Tier 1 demos work so visuals match live UIs.
- Store images under `portfolio/assets/pipeline/` when created (folder not required until assets exist).

## Build checklist

- [ ] Write six section headlines and body copy
- [ ] Run notebook end-to-end; capture one screenshot per step
- [ ] Wire scroll section into portfolio project page
- [ ] Cross-link each step to relevant interactive demo or spec
- [ ] Add “full pipeline” diagram at top (optional simplified mermaid)

## Status

`done` — `PipelineStory.tsx` on COMPANYSITE Part 4.
