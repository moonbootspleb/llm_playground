# Tokenization ladder

**Tier:** 2 | **Type:** React (COMPANYSITE) | **Status:** done

**Blog:** Part 3 · `#tokenization-ladder`

## Overview

One sentence, three tokenization strategies—**word**, **character**, and **subword (BPE)**—stacked so visitors see tradeoffs at a glance.

## What visitors learn

There is no perfect tokenizer. Word-level is simple but suffers OOV; character-level covers everything but creates long sequences; subword (BPE) balances vocabulary size and sequence length—why modern LLMs use it.

## Connection to the lab

- [`llm_playground.ipynb`](../../llm_playground.ipynb) — **§1.1** Word-level (`encode` / `decode` you implement)
- **§1.2** Character-level
- **§1.3** BPE via GPT-2 `AutoTokenizer`

## Demo behavior

1. Fixed default sentence (e.g. from lab corpus or visitor-editable): `"tokens are tiny pieces of text"`.
2. **Row 1 — Word-level:** split on whitespace; map through lab-style `word2id` (or inline logic); show UNK for unknown words if using corpus vocab only.
3. **Row 2 — Character-level:** one chip per character (a–z, A–Z, punctuation per lab rules).
4. **Row 3 — BPE:** GPT-2 tokenizer `convert_ids_to_tokens`.
5. Under each row: token count + one-line callout (e.g. “OOV: deploy”, “48 tokens vs 6 words”, “subword merges common pieces”).

## Visual design

- Three horizontal **token strips** (same chip style as [tokenizer explorer](../assets/tokenizer-explorer/tokens-tab-emoji.png)).
- Left label column: Word | Char | BPE.
- Optional “try OOV sentence” preset: `"Please deploy on Saturday"` with word-level showing `<UNK>` or missing IDs.

## Copy suggestions

> I built word and character tokenizers in the lab, then compared them to production BPE. The ladder shows why scaling to internet-sized data pushed the field toward subwords.

> Watch token count explode on the character row—that is real compute cost, not just a visualization trick.

## Technical notes

- **Word/char:** port minimal `encode`/`decode` from notebook §1.1–1.2 (small corpus vocab or char set).
- **BPE:** `AutoTokenizer.from_pretrained("gpt2")` only—no LM weights.
- Can be **static** on portfolio (screenshot + one interactive sentence) or Gradio with live update.
- **Hosting:** static HTML + image is enough for Phase 2; optional JS for chips.

## Build checklist

- [ ] Extract or reimplement word/char encode from notebook
- [ ] Wire BPE row to HF tokenizer
- [ ] Three presets: in-vocab sentence, OOV sentence, long sentence
- [ ] Export static screenshot for portfolio if not interactive
- [ ] Link to notebook §1.1–1.3

## Status

`done` — `TokenizationLadder.tsx` on COMPANYSITE Part 3.
