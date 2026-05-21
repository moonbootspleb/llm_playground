# GPT-2 vs Qwen

**Tier:** 1 | **Type:** Write-up + comparison | **Status:** done

**Blog:** Part 2 · `#gpt2-vs-qwen` · live comparison via Colab (`VITE_COLAB_NOTEBOOK_URL`)

## Overview

The same question sent to a **2019 completion model** (GPT-2) and a **2025 instruction-tuned model** (Qwen3-0.6B)—showing why chat templates and training objectives matter.

## What visitors learn

GPT-2 continues text; it does not “answer questions.” Modern instruction models expect structured messages (`apply_chat_template`) and behave like assistants. Format and training matter as much as parameter count.

## Connection to the lab

- [`llm_playground.ipynb`](../../llm_playground.ipynb) — **§4.1** Chat templates
- **§4.2** GPT-2 vs Qwen3-0.6B generation comparison

## Demo behavior

### On the portfolio site (recommended split)

1. **Write-up section** (static markdown on portfolio):
   - Explain completion vs instruction tuning
   - Show example chat template string for Qwen (code block from notebook)
2. **Comparison block:**
   - Fixed prompt: `"What is 2+2?"`
   - **Screenshot or cached output** for GPT-2 (raw prompt) vs Qwen (templated)
   - Labels: “GPT-2: continues the web” vs “Qwen: answers the question”
3. **CTA:** “Run live comparison” → Google Colab notebook §4 (GPU recommended for Qwen)

### Optional live embed

- Full dual-model live demo is heavy for free CPU Spaces; prefer Colab for Qwen.
- If Space has GPU: two generate buttons with clear loading states.

## Visual design

- Side-by-side cards with model name, year, parameter count, input format.
- GPT-2 card: show raw prompt string.
- Qwen card: show formatted chat (collapsed “view template” expander).
- Output in monospace or prose blocks; highlight Qwen `thinking` block if present (styled differently from final answer).

## Copy suggestions

> I asked both models “What is 2+2?” GPT-2 treated it as the start of a document. Qwen treated it as a user message and responded directly—after optional internal reasoning.

> Instruction tuning and chat templates are why “the same weights idea” feels completely different in practice.

## Technical notes

- **GPT-2:** `gpt2`, raw `tokenizer(prompt)` + `generate` with top-p.
- **Qwen:** `Qwen/Qwen3-0.6B`, messages list + `tokenizer.apply_chat_template(..., add_generation_prompt=True)`.
- **Portfolio:** static screenshots + Colab link is the pragmatic default.
- **Colab:** enable GPU runtime; models cache after first pull.

## Build checklist

- [ ] Run notebook §4.2 locally; save representative outputs as PNG
- [ ] Write portfolio markdown (use copy suggestions above)
- [ ] Add Colab badge linking to notebook §4
- [ ] Optional: short table comparing GPT-2 vs Qwen (params, behavior, input format)
- [ ] Do not block portfolio launch on live Qwen embed

## Status

`done` — static cards on COMPANYSITE; Qwen on Colab only.
