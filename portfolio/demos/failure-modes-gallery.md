# Failure modes gallery

**Tier:** 3 | **Type:** Static gallery | **Status:** done

**Blog:** Part 4 · `#failure-modes`

## Overview

A curated **gallery of instructive mistakes**: when greedy decoding loops, when word-level tokenizers hit OOV, and when GPT-2 “answers” a question by continuing a webpage.

## What visitors learn

Understanding LLMs includes knowing how they fail. These examples motivate why decoding strategies, subword tokenization, and instruction tuning exist—not just how to get a good demo output.

## Connection to the lab

- [`llm_playground.ipynb`](../../llm_playground.ipynb) — **§1.1** OOV on word-level tokenizer
- **§3.1** Greedy repetition discussion
- **§4.2** GPT-2 vs Qwen on `"What is 2+2?"`

## Demo behavior

1. **Gallery grid** (3–6 cards), each card:
   - Title (failure mode name)
   - Input (prompt or sentence)
   - Output or token visualization
   - **Why it happened** (2–3 sentences)
   - Link to notebook section
2. Planned cards:

| Card | Input | What to show | Lesson |
|------|-------|--------------|--------|
| Greedy loop | `"Once upon a time"` + greedy, 80 tokens | Repeated phrases | Local optimum; use sampling |
| GPT-2 “Q&A” | `"What is 2+2?"` | Web-style continuation, not `4` | Completion ≠ instruction following |
| Word OOV | Sentence with word not in tiny corpus vocab | `<UNK>` or broken encode | Need subword or larger vocab |
| Char explosion | Same sentence as BPE row | Many char tokens | Sequence length cost |
| Top-p variance | Same prompt, two samples | Different but coherent outputs | Stochastic decoding |

3. No live generation required on portfolio—**cached outputs** from lab runs are enough.

## Visual design

- Card layout: muted “warning” accent border or icon (not alarmist—educational tone).
- Monospace for model outputs; truncate very long repetition with “…” and expand on click.
- Optional before/after: greedy vs top-p on same card.

## Copy suggestions

> The best demos also show where models break. These are not bugs in my code—they are structural behaviors you plan around in real systems.

> Production apps choose decoding parameters, tokenizers, and model families deliberately. These examples show why.

## Technical notes

- Generate all outputs once from completed notebook; store in `portfolio/assets/failures/` when created.
- Include run metadata in repo (prompt, `max_new_tokens`, `do_sample`, seed) in spec footnotes for reproducibility.
- Do not cherry-pick misleading failures—use examples called out in the lab text.

## Build checklist

- [ ] Reproduce greedy loop output from §3.1 tests
- [ ] Capture GPT-2 vs Qwen screenshot for §4.2 card
- [ ] Capture word-level OOV from §1.1 exercise
- [ ] Write “why it happened” captions per card
- [ ] Build static gallery component on portfolio page
- [ ] Cross-link to greedy-vs-top-p and gpt2-vs-qwen demos

## Status

`done` — `FailureModesGallery.tsx` on COMPANYSITE Part 4.
