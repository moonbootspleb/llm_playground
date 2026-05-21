# Portfolio showcase

This folder documents how the [LLM Playground](../README.md) lab is presented on **moonboots.tech** (COMPANYSITE). The lab notebook ([`llm_playground.ipynb`](../llm_playground.ipynb)) is where you learn; the blog series is where you **show** that learning with visuals, short copy, and interactive demos.

## Lab vs portfolio

| | Lab (`llm_playground.ipynb`) | moonboots.tech blog |
|---|------------------------------|---------------------|
| **Audience** | You, while learning | Recruiters, peers, visitors |
| **Depth** | Full exercises, code, inspection | Curated highlights |
| **Format** | Jupyter cells | Blog posts + HF Space embed |
| **Goal** | Mental model + implementation | Clear story in minutes |

## Blog series (tier bundles)

| Part | Slug | Demos | Space tab |
|------|------|-------|-----------|
| 1 | [`how-tokenization-works`](/blog/how-tokenization-works) | Tokenizer explorer | **Tokens** |
| 2 | [`how-llms-predict-and-generate`](/blog/how-llms-predict-and-generate) | Next-token microscope, greedy vs top-p, GPT-2 vs Qwen (static) | **NextToken**, **Decoding** |
| 3 | [`inside-gpt2-architecture-and-scale`](/blog/inside-gpt2-architecture-and-scale) | Ladder, param calculator, transformer diagram (React); decoding playground | **Playground** |
| 4 | [`llm-pipeline-from-text-to-output`](/blog/llm-pipeline-from-text-to-output) | Pipeline scroll, failure gallery, video placeholder | — (links to Parts 1–3) |

Legacy: `/work/llm-playground` → Part 1 `#live-demo`; `/work/llm-playground/predict` → Part 2 `#live-demo-next-token`.

## Demo index

| Demo | Tier | Type | Spec | Status |
|------|------|------|------|--------|
| Tokenizer explorer | 1 | Interactive | [tokenizer-explorer.md](demos/tokenizer-explorer.md) | done |
| Next-token microscope | 1 | Interactive | [next-token-microscope.md](demos/next-token-microscope.md) | done (Space + Part 2) |
| Greedy vs top-p | 1 | Interactive | [greedy-vs-top-p.md](demos/greedy-vs-top-p.md) | done (Space + Part 2) |
| GPT-2 vs Qwen | 1 | Write-up | [gpt2-vs-qwen.md](demos/gpt2-vs-qwen.md) | done (static Part 2; Colab for live) |
| Tokenization ladder | 2 | React | [tokenization-ladder.md](demos/tokenization-ladder.md) | done (Part 3) |
| Parameter scale calculator | 2 | React | [parameter-scale-calculator.md](demos/parameter-scale-calculator.md) | done (Part 3) |
| Transformer block diagram | 2 | Static SVG | [transformer-block-diagram.md](demos/transformer-block-diagram.md) | done (Part 3) |
| Decoding playground | 2 | Interactive | [decoding-playground.md](demos/decoding-playground.md) | done (Space + Part 3) |
| Pipeline story | 3 | Static scroll | [pipeline-story.md](demos/pipeline-story.md) | done (Part 4) |
| Failure modes gallery | 3 | Static gallery | [failure-modes-gallery.md](demos/failure-modes-gallery.md) | done (Part 4) |
| Demo walkthrough video | 3 | Video | [demo-walkthrough-video.md](demos/demo-walkthrough-video.md) | placeholder (Part 4) |

## Implementation roadmap

### Phase 1 — Tier 1 (blog Part 2)

- [x] Gradio tabs: NextToken, Decoding on shared Space
- [x] COMPANYSITE Part 2 post + single Space embed
- [x] GPT-2 vs Qwen static comparison + Colab CTA env

### Phase 2 — Tier 2 (blog Part 3)

- [x] React ladder, parameter calculator, transformer diagram
- [x] Playground tab on Space + Part 3 post

### Phase 3 — Tier 3 (blog Part 4)

- [x] Pipeline story + failure gallery components
- [ ] Record walkthrough video; replace placeholder embed

## Deployment links

| Resource | URL |
|----------|-----|
| Blog index | `https://moonboots.tech/blog` |
| HF Space (Gradio) | https://huggingface.co/spaces/moonbootspleb/moonboots |
| Space developer guide | [space/DEVELOPER.md](../space/DEVELOPER.md) |
| COMPANYSITE repo | `MOONBOOTS/COMPANYSITE` |
| Google Colab | Set `VITE_COLAB_NOTEBOOK_URL` on Vercel |
| GitHub | https://github.com/moonbootspleb/llm_playground — set `VITE_LLM_PLAYGROUND_GITHUB_URL` on Vercel |
