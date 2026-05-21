# Decoding playground

**Tier:** 2 | **Type:** Interactive | **Status:** done

**Portfolio connection:** COMPANYSITE Part 3 · `/blog/inside-gpt2-architecture-and-scale#live-demo-playground` — **Playground** tab on the shared Hugging Face Space iframe.

---

## Overview

A compact **playground UI**: prompt in, decoding options, generated text out. Same idea as notebook **§5** (optional `ipywidgets`), built on **§3.1–3.2** `model.generate()`.

## What visitors learn

Inference is configurable: token count, greedy vs sampling, and `top_p`. Same API as the lab—packaged like a minimal chat box without hiding how it works.

## Copy for moonboots.tech (when the page is live)

> This playground wraps the same `generate()` call from the lab: pick a prompt, choose greedy or top-p, and see GPT-2 complete the text.

> For Qwen, chat templates, and side-by-side model comparison, open the full notebook in Colab—this public demo stays on GPT-2 so it runs on free CPU hosting.

---

## Before you start

| Prerequisite | Where |
|--------------|--------|
| §3.1 and §3.2 done in notebook | `generate()` with greedy and top-p works locally |
| `llm_playground` env active | `conda activate llm_playground` or `source env.sh` |
| Optional §5 started | Not required—you can skip straight to Gradio |

**Time estimate:** ~2–4 hours (notebook helper → Gradio tab → one test on Space → COMPANYSITE section).

**Do not** load Qwen on the public Space (slow on CPU). Link to Colab for that.

---

## Build path (follow in order)

```text
Step 1  Notebook — one generate() helper (copy-paste below)
Step 2  Notebook — optional ipywidgets (quick win in Jupyter)
Step 3  Gradio — Playground tab in project_1/space/
Step 4  Hugging Face Space — deploy and copy URL
Step 5  COMPANYSITE — #playground section + env var
```

---

## Step 1 — Core helper in the notebook (30 min)

Finish **§3.2** first if you have not already. Then add or refine this function in a new cell (or in the §5 cell). It is the **single function** Gradio will call later.

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)
model.eval()

def decode_text(
    prompt: str,
    strategy: str = "top_p",  # "greedy" | "top_p"
    max_new_tokens: int = 48,
    top_p: float = 0.9,
    temperature: float = 1.0,
) -> str:
    if not prompt.strip():
        return "Enter a prompt."

    inputs = tokenizer(prompt, return_tensors="pt")
    input_len = inputs["input_ids"].shape[1]

    gen_kwargs = dict(
        max_new_tokens=max_new_tokens,
        pad_token_id=tokenizer.eos_token_id,
    )

    if strategy == "greedy":
        gen_kwargs["do_sample"] = False
    else:
        gen_kwargs["do_sample"] = True
        gen_kwargs["top_p"] = top_p
        gen_kwargs["temperature"] = temperature

    with torch.no_grad():
        out = model.generate(**inputs, **gen_kwargs)

    new_ids = out[0, input_len:]
    return tokenizer.decode(new_ids, skip_special_tokens=True)
```

**Check it works** (run in a cell):

```python
for strategy in ("greedy", "top_p"):
    print(f"\n=== {strategy} ===")
    print(decode_text("Hi my name is", strategy=strategy, max_new_tokens=40))
```

- [ ] Greedy runs without error
- [ ] Top-p runs and output **differs** from greedy on the same prompt
- [ ] You understand `input_len` slicing (only **new** tokens decoded)

**Preset prompts** (use these everywhere—notebook, Gradio, screenshots):

- `Once upon a time`
- `What is 2+2?`
- `Suggest a party theme.`

---

## Step 2 — Optional: ipywidgets in Jupyter (45 min, skip if you want Gradio only)

Only in `llm_playground.ipynb` **§5**. Good for learning; the portfolio uses Gradio on the site.

1. Import widgets:

```python
import ipywidgets as widgets
from IPython.display import display, Markdown
```

2. Create controls:

| Widget | Type | Default |
|--------|------|---------|
| Prompt | `widgets.Textarea` | `"Hi my name is"` |
| Strategy | `widgets.RadioButtons` | `("greedy", "top_p")` |
| Max tokens | `widgets.IntSlider` | 8–128, value 48 |
| Top-p | `widgets.FloatSlider` | 0.5–1.0, value 0.9 |
| Go | `widgets.Button` | description `"Generate"` |
| Out | `widgets.Output` | |

3. On button click: call `decode_text(...)` and `display(Markdown(result))`.

4. Hide the top-p slider when strategy is `greedy` (optional: `observe` on strategy widget).

- [ ] Widgets render in JupyterLab
- [ ] Generate button produces text in the output area

---

## Step 3 — Gradio tab in `project_1/space/` (1–2 hours)

If `space/` does not exist yet, create it at the **lab repo root**:

```text
project_1/
  space/
    app.py
    requirements.txt
```

### `space/requirements.txt`

```text
torch>=2.10.0
transformers>=5.1.0
gradio>=5.0.0
```

### Playground tab snippet (add to `app.py`)

Load model **once** at import time (same as other tabs). Add a fourth tab `"Playground"`:

```python
import gradio as gr
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# ... load tokenizer, model once ...

def playground_generate(prompt, strategy, max_new_tokens, top_p, temperature):
  # paste decode_text body here, or call shared function
  ...

with gr.Blocks(title="LLM Playground") as demo:
    with gr.Tabs():
        # ... Tokens, Next token, Greedy vs top-p tabs ...
        with gr.Tab("Playground"):
            prompt = gr.Textbox(label="Prompt", lines=3, value="Hi my name is")
            strategy = gr.Radio(["greedy", "top_p"], value="top_p", label="Strategy")
            max_new_tokens = gr.Slider(8, 128, value=48, step=1, label="Max new tokens")
            top_p = gr.Slider(0.5, 1.0, value=0.9, label="Top-p")
            temperature = gr.Slider(0.1, 2.0, value=1.0, label="Temperature")
            btn = gr.Button("Generate", variant="primary")
            out = gr.Textbox(label="Generated text", lines=8)
            btn.click(
                playground_generate,
                inputs=[prompt, strategy, max_new_tokens, top_p, temperature],
                outputs=out,
            )

demo.launch()
```

**Local test:**

```bash
cd project_1/space
pip install -r requirements.txt   # or use llm_playground conda env
python app.py
```

- [ ] Browser opens; Playground tab generates text
- [ ] Greedy vs top-p behave as in Step 1
- [ ] Empty prompt shows a friendly message (no crash)

**Tip:** Reuse the same `decode_text` logic from Step 1—do not fork two implementations.

---

## Step 4 — Deploy to Hugging Face Space (30 min)

1. Create a new Space on [huggingface.co/spaces](https://huggingface.co/spaces): **SDK = Gradio**, hardware **CPU** (free tier).
2. Push `space/app.py` + `space/requirements.txt` (or connect GitHub repo subfolder).
3. Wait for build; open the Space URL.
4. Test Playground tab on the live URL.

- [ ] Space builds green
- [ ] First generation works (may take 30–60s first time while model downloads)
- [ ] Copy Space URL: `https://huggingface.co/spaces/<user>/<name>`

Record URL in [portfolio/README.md](../README.md) deployment table.

---

## Step 5 — Wire to moonboots.tech (COMPANYSITE) (30 min)

Repo: `~/moonbootspleb/moonboots/COMPANYSITE`

### 5a. Environment

Create or update `.env.example`:

```bash
VITE_LLM_PLAYGROUND_SPACE_URL=https://huggingface.co/spaces/<user>/<name>
VITE_COLAB_NOTEBOOK_URL=https://colab.research.google.com/github/<user>/<repo>/blob/main/llm_playground.ipynb
VITE_LLM_PLAYGROUND_GITHUB_URL=https://github.com/<user>/<repo>
```

Add the same vars in Vercel → Project → Environment Variables.

### 5b. Page section

On `LlmPlaygroundPage` (when you create it), add a section:

```tsx
<section id="playground" className="scroll-mt-24 space-y-4">
  <p className="text-xs font-mono uppercase tracking-[0.18em] text-white/38">
    Decoding playground
  </p>
  <h2 className="font-display text-2xl font-semibold text-white">
    Prompt in, text out
  </h2>
  <p className="text-white/55 max-w-2xl">{/* paste copy from above */}</p>
  <SpaceEmbed />  {/* same iframe as Tier 1 — visitors open Playground tab */}
  <p className="text-sm text-white/40">
    In the embed, select the <strong className="text-white/55">Playground</strong> tab.
  </p>
</section>
```

You do **not** need a second iframe—one Space, four tabs.

- [ ] `/work/llm-playground#playground` scrolls to section
- [ ] iframe loads Space; Playground tab works
- [ ] “Open in new tab” fallback link present

---

## UI checklist (Gradio tab)

| Control | Maps to |
|---------|---------|
| Prompt | `prompt` argument |
| Strategy radio | `do_sample` False vs True |
| Max new tokens | `max_new_tokens` |
| Top-p slider | `top_p` (only when sampling) |
| Temperature | `temperature` (only when sampling) |
| Generate button | runs `model.generate` |
| Output box | decoded new tokens only |

**Visual:** Gradio’s default dark UI is fine inside the iframe; the **page around** it on moonboots.tech should follow COMPANYSITE `DESIGN.md` (charcoal canvas, brand grey borders).

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `CUDA out of memory` | Use CPU Space or `model.to("cpu")` locally |
| Generation very slow | Lower `max_new_tokens`; keep GPT-2 only |
| Output includes full prompt repeated | Slice with `input_len` as in Step 1 |
| Top-p identical every run | Expected if temperature=0; raise temperature or remove fixed seed |
| iframe blank on site | Check `VITE_*` var set on Vercel; redeploy |
| Space build fails | Pin `torch` / `transformers` versions in `requirements.txt` |

---

## Definition of done

- [ ] `decode_text()` works in notebook with greedy + top-p
- [ ] Gradio **Playground** tab works locally and on HF Space
- [ ] COMPANYSITE section `#playground` explains “use Playground tab” + embeds Space
- [ ] Colab link present for full lab + Qwen
- [ ] Status below updated to `done` when all above are checked

---

## Reference links

- Lab notebook: [llm_playground.ipynb](../../llm_playground.ipynb) §3.1–3.2, §5
- Related demo spec: [greedy-vs-top-p.md](greedy-vs-top-p.md) (side-by-side; playground is single-panel)
- Site wiring plan: COMPANYSITE `/work/llm-playground`, `VITE_LLM_PLAYGROUND_SPACE_URL`
- Hugging Face: [text generation docs](https://huggingface.co/docs/transformers/en/main_classes/text_generation)

## Status

`done` — Space Playground tab + COMPANYSITE Part 3 `#live-demo-playground`.
