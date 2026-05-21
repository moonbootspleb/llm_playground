# Tokenizer explorer

**Tier:** 1 | **Type:** Interactive | **Status:** done

**Portfolio connection:** COMPANYSITE Part 1 [`/blog/how-tokenization-works`](/blog/how-tokenization-works) (section `#live-demo`) — **Tokens** tab on the shared Hugging Face Space iframe. Legacy `/work/llm-playground` → Part 1; `/work/llm-playground/predict` → Part 2.

**Live Space:** [moonbootspleb/moonboots](https://huggingface.co/spaces/moonbootspleb/moonboots) — open the **Tokens** tab.

---

## Overview

Type any text and see how it is split into tokens—instantly comparing GPT-2 BPE (Hugging Face) with OpenAI `tiktoken` encodings (`gpt2` and `cl100k_base`).

## What visitors learn

Models do not read words or characters directly; they read **token IDs**. Different tokenizers split the same sentence differently (especially emojis, code, and non-English text). Token count affects cost, context limits, and speed.

## Copy for moonboots.tech (when the page is live)

> Before an LLM sees your prompt, a tokenizer turns it into a list of integer IDs. This demo shows that process live—and why the same sentence can have different lengths under different encodings.

> Try the emoji or code presets: you will often see more tokens than you expect. That matters for API pricing and context windows.

> In the embed below, select the **Tokens** tab. No full model download is required for this view—only tokenizer vocabularies load.

---

## Before you start

| Prerequisite | Where |
|--------------|--------|
| §1.3–1.4 concepts (or reference cells below) | [`llm_playground.ipynb`](../../llm_playground.ipynb) |
| `tiktoken` + `transformers` | [`requirements.txt`](../../requirements.txt) |
| HF Space clone (optional) | [`demos-1/moonboots`](../../../demos-1/moonboots) |

**Time estimate:** ~2–3 hours (notebook cells → HTML chips in Gradio → push Space → COMPANYSITE section).

**Do not** create a separate Space per demo. Use the existing four-tab app in `demos-1/moonboots`.

---

## Build path (follow in order)

```text
Step 1  Notebook — HF BPE + tiktoken compare (§1.3–1.4)
Step 2  Core helpers — analyze_text() + render_token_explorer()
Step 3  Gradio — Tokens tab in demos-1/moonboots/app.py
Step 4  Hugging Face Space — git push moonbootspleb/moonboots
Step 5  COMPANYSITE — #interactive-demos + env vars
```

---

## Step 1 — Notebook reference (§1.3–1.4) (30 min)

Complete or run the reference cells in the lab notebook.

### §1.3 — Hugging Face GPT-2 BPE

```python
from transformers import AutoTokenizer

bpe_tok = AutoTokenizer.from_pretrained("gpt2")
sentence = "The 🌟 star-programmer implemented AGI overnight."

ids = bpe_tok.encode(sentence)
tokens = bpe_tok.convert_ids_to_tokens(ids)
print(f"HF GPT-2 BPE: {len(tokens)} tokens")
print(tokens)
print(bpe_tok.decode(ids))
```

### §1.4 — tiktoken compare

```python
import tiktoken

enc_gpt2 = tiktoken.get_encoding("gpt2")
enc_cl100k = tiktoken.get_encoding("cl100k_base")
sentence = "The 🌟 star-programmer implemented AGI overnight."

for name, enc in [("tiktoken gpt2", enc_gpt2), ("tiktoken cl100k_base", enc_cl100k)]:
    ids = enc.encode(sentence)
    pieces = [enc.decode([i]) for i in ids]
    print(f"\n{name}: {len(ids)} tokens")
    print(pieces)
```

**Check it works:**

- [ ] HF prints subword pieces (may include `Ġ` for leading spaces)
- [ ] tiktoken `gpt2` count is usually close to HF for English
- [ ] `cl100k_base` often differs on emoji and punctuation

**Advanced:** For strict parity experiments, try `bpe_tok.encode(sentence, add_special_tokens=False)` and compare byte-for-byte with tiktoken.

---

## Step 2 — Core helpers (45 min)

Implement in [`demos-1/moonboots/app.py`](../../../demos-1/moonboots/app.py) (single source of truth for the Space).

```python
import html
from dataclasses import dataclass

@dataclass
class TokenColumn:
    label: str
    tokens: list[str]
    ids: list[int]

def analyze_text(text: str) -> list[TokenColumn]:
    hf_ids = _hf_tok.encode(text)
    hf_tokens = _hf_tok.convert_ids_to_tokens(hf_ids)
    tik_ids = _tik_gpt2.encode(text)
    tik_tokens = [_tik_gpt2.decode([i]) for i in tik_ids]
    cl_ids = _tik_cl100k.encode(text)
    cl_tokens = [_tik_cl100k.decode([i]) for i in cl_ids]
    return [
        TokenColumn("HF GPT-2 BPE", hf_tokens, hf_ids),
        TokenColumn("tiktoken gpt2", tik_tokens, tik_ids),
        TokenColumn("tiktoken cl100k_base", cl_tokens, cl_ids),
    ]

CHIP_HUES = [
    "hsl(210 55% 28%)",
    "hsl(160 45% 26%)",
    "hsl(280 40% 30%)",
    "hsl(35 50% 28%)",
]

def render_token_explorer(columns: list[TokenColumn]) -> str:
    # HTML chips + <details> for IDs + count summary when encodings diverge
    ...
```

**Count summary:** When `max(count) - min(count) >= 2`, show a one-line note (e.g. “cl100k_base uses 3 fewer tokens than HF GPT-2 BPE”).

- [ ] `analyze_text` returns three columns with tokens and ids
- [ ] `render_token_explorer` escapes user text in chips (`html.escape`)
- [ ] Input capped at 2000 chars (`_clip`)

---

## Step 3 — Gradio Tokens tab (1 hour)

Repo: **`BYTEBTYEGO/demos-1/moonboots`** (not `project_1/space/`).

### `requirements.txt`

```text
torch>=2.10.0
transformers>=5.1.0
tiktoken>=0.12.0
gradio>=5.0.0
```

### Tab wiring

```python
def tokenize_compare(text: str) -> str:
    text = _clip(text)
    if not text.strip():
        return "<p>Enter some text.</p>"
    return render_token_explorer(analyze_text(text))

with gr.Tab("Tokens"):
    tok_inp = gr.Textbox(label="Text", lines=3, value=EMOJI_PRESET)
    tok_out = gr.HTML()
    tok_btn = gr.Button("Tokenize", variant="primary")
    tok_btn.click(tokenize_compare, inputs=tok_inp, outputs=tok_out)
    tok_inp.change(tokenize_compare, inputs=tok_inp, outputs=tok_out)
    gr.Examples(examples=TOKEN_EXAMPLES, inputs=tok_inp)
```

`gr.Examples` rows act as **preset buttons** (emoji, code, multilingual, long paragraph).

### Presets (standardize everywhere)

| Preset | Purpose |
|--------|---------|
| `The 🌟 star-programmer implemented AGI overnight.` | Emoji + punctuation (§1.4) |
| `def hello():\n    print("world")` | Code / whitespace |
| `「こんにちは」 — and café` | Non-English + accents |
| Long English paragraph (~200 words) | Context-window / API cost intuition |

**Local test:**

```bash
cd BYTEBTYEGO/demos-1/moonboots
pip install -r requirements.txt
python app.py
```

- [ ] Three columns render with color chips
- [ ] Token IDs hidden under collapsible **Token IDs** per column
- [ ] Live update on text change
- [ ] Fourth preset loads without lag (clipped at 2k chars)

---

## Step 4 — Deploy to Hugging Face Space (30 min)

```bash
cd BYTEBTYEGO/demos-1/moonboots
git add app.py requirements.txt
git commit -m "Tokens tab: HTML chips, three encoders, four presets"
git push
```

Space: **https://huggingface.co/spaces/moonbootspleb/moonboots**

- [ ] Build is green (Logs tab)
- [ ] Tokens tab works on public URL (no GPT-2 weights until another tab is opened)
- [ ] Record URL in [portfolio/README.md](../README.md) deployment table

---

## Step 5 — Wire to moonboots.tech (COMPANYSITE) (30 min)

Repo: `MOONBOOTS/COMPANYSITE`

### 5a. Environment

`.env.example`:

```bash
VITE_LLM_PLAYGROUND_SPACE_URL=https://huggingface.co/spaces/moonbootspleb/moonboots
VITE_COLAB_NOTEBOOK_URL=https://colab.research.google.com/github/<user>/<repo>/blob/main/llm_playground.ipynb
VITE_LLM_PLAYGROUND_GITHUB_URL=https://github.com/<user>/<repo>
```

### 5b. Page section

Route: `/work/llm-playground` — section `#interactive-demos`:

```tsx
<section id="interactive-demos" className="scroll-mt-24 space-y-4">
  <p className="text-xs font-mono uppercase tracking-[0.18em] text-white/38">
    Tokenizer explorer
  </p>
  <h2 className="font-display text-2xl font-semibold text-white">
    Text to token IDs
  </h2>
  <p className="text-white/55 max-w-2xl">{/* paste copy from above */}</p>
  <SpaceEmbed />
  <p className="text-sm text-white/40">
    In the embed, select the <strong className="text-white/55">Tokens</strong> tab.
  </p>
</section>
```

One iframe for all Tier 1 demos—visitors switch tabs inside Gradio.

- [ ] `/work/llm-playground#interactive-demos` scrolls to section
- [ ] iframe loads public Space
- [ ] “Open in new tab” fallback on `SpaceEmbed`

---

## UI checklist (Gradio Tokens tab)

| Control | Behavior |
|---------|----------|
| Textbox | User input; live `.change()` |
| Tokenize button | Same handler as live update |
| Examples | Four presets |
| Output `gr.HTML` | Three columns, chips, counts, optional ID details |
| Max input | 2000 characters |

---

## Screenshot asset (pipeline / ladder)

Capture the emoji preset on the Tokens tab and save as:

`portfolio/assets/tokenizer-explorer/tokens-tab-emoji.png`

Use in [pipeline-story.md](pipeline-story.md) step 2 and [tokenization-ladder.md](tokenization-ladder.md) chip style reference.

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| HF tokens show `Ġ` prefix | Normal BPE marker for leading space; mention in copy |
| tiktoken vs HF count mismatch | Expected; compare `cl100k_base` on emoji/code |
| Space build fails | Pin versions in `requirements.txt`; check Logs |
| Slow first load on other tabs | GPT-2 weights download only when NextToken/Decoding/Playground used |
| iframe blank / X-Frame-Options deny | iframe must use `https://<user>-<space>.hf.space`, not `huggingface.co/spaces/...?embed=true` (COMPANYSITE converts automatically) |
| HTML shows raw tags | Ensure `html.escape` on token strings |
| UI lag on long paste | `_clip` at 2000 chars |

---

## Definition of done

- [x] [`tokenizer-explorer.md`](tokenizer-explorer.md) matches decoding-playground depth
- [x] Spec references `demos-1/moonboots` (not `project_1/space/`)
- [x] Tokens tab: 3 encoders, HTML chips, ID details, 4 presets, live update
- [x] HF Space URL in [portfolio/README.md](../README.md)
- [x] COMPANYSITE `#interactive-demos` + `SpaceEmbed` + `.env.example`
- [x] Notebook §1.3–1.4 reference solutions
- [ ] Screenshot saved to `portfolio/assets/tokenizer-explorer/` (manual capture)

---

## Reference links

- Lab notebook: [llm_playground.ipynb](../../llm_playground.ipynb) §1.3–1.4
- Space developer guide: [demos-1/moonboots/DEVELOPER.md](../../../demos-1/moonboots/DEVELOPER.md) — Milestone 1
- [tiktoken](https://github.com/openai/tiktoken)
- [GPT-2 tokenizer (HF)](https://huggingface.co/docs/transformers/en/model_doc/gpt2)
- Related: [tokenization-ladder.md](tokenization-ladder.md) (shared chip style)
- Related: [next-token-microscope.md](next-token-microscope.md) (next tab in Space)

## Status

`done` — screenshot asset optional manual step.
