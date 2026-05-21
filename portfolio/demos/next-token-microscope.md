# Next-token microscope

**Tier:** 1 | **Type:** Interactive | **Status:** done

**Blog:** [Part 2 — Predict and generate](https://moonboots.tech/blog/how-llms-predict-and-generate) · section `#live-demo-next-token` · Space **NextToken** tab

## Overview

Peek inside a language model at a single step: given a prompt, see the **top-k most likely next tokens** and their probabilities.

## What visitors learn

An LLM is a **next-token predictor**. At each position it outputs a score (logit) for every vocabulary entry; softmax turns that into a probability distribution. Generation is repeating: pick a token, append, predict again.

## Connection to the lab

- [`llm_playground.ipynb`](../../llm_playground.ipynb) — **§2.3** From text to predictions (logits shape, softmax, `torch.topk`)

## Demo behavior

1. Visitor edits a prompt (default: `"Hello my name"`).
2. Tokenize with GPT-2 tokenizer; run **one forward pass** through `GPT2LMHeadModel`.
3. Take logits at the **final position**; apply `softmax`; show **top 5** (or top 10) tokens with:
   - Decoded token string
   - Probability (percentage, 2 decimal places)
4. Optional **“Step forward”**: append the greedy top-1 token to the prompt and re-run (up to 3 steps) to show autoregressive growth.
5. Optional: mark which token greedy decoding would pick vs what top-p might sample.

## Visual design

- Horizontal **bar chart** (token label vs probability) for top-k.
- Prompt displayed above with trailing cursor or highlight on “prediction position.”
- If stepping: small timeline (step 1 → 2 → 3) with growing prompt string.
- Mobile: vertical bars or table (token | prob).

## Copy suggestions

> This is the core loop of GPT-style models: one forward pass produces a distribution over the entire vocabulary. The model does not “know the answer” in one shot—it ranks what might come next.

> Notice how probable tokens cluster: grammar, common words, and context from the prompt all shape the distribution.

## Technical notes

- **Model:** `gpt2` (124M) — load once at Space startup.
- **Libraries:** `torch`, `transformers`, `torch.nn.functional.softmax`, `torch.topk`.
- **Hosting:** HF Space CPU acceptable; first load ~10–30s (show loading state).
- **Performance:** single forward pass only unless “step forward” is used (max 3 extra passes).

## Build checklist

- [ ] Load `GPT2LMHeadModel` and tokenizer at app init
- [ ] Gradio `Textbox` for prompt + `Plot` or `Dataframe` for top-k
- [ ] Implement logits → softmax → topk pipeline from §2.3
- [ ] Optional multi-step “advance” button
- [ ] Loading spinner during model download on cold start
- [ ] Link to notebook §2.3 from portfolio copy

## Status

`done` — Space NextToken tab + COMPANYSITE Part 2.
