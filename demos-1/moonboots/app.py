"""LLM Playground — Hugging Face Space (Gradio, GPT-2 on CPU)."""

import html
from dataclasses import dataclass

import gradio as gr
import tiktoken
import torch
import torch.nn.functional as F
from transformers import AutoModelForCausalLM, AutoTokenizer

from theme import (
    GLOW,
    HAIRLINE,
    HAIRLINE_STRONG,
    INK,
    MOONBOOTS_CSS,
    ORBITAL,
    build_moonboots_theme,
)

MAX_INPUT_CHARS = 2000
MODEL_ID = "gpt2"
TOP_K = 5

# --- Lightweight loads (Tokens tab) ---
_hf_tok = AutoTokenizer.from_pretrained(MODEL_ID)
_tik_gpt2 = tiktoken.get_encoding("gpt2")
_tik_cl100k = tiktoken.get_encoding("cl100k_base")

# --- GPT-2 (lazy: first model tab triggers download) ---
_gpt2_model = None


def _get_gpt2():
    global _gpt2_model
    if _gpt2_model is None:
        _gpt2_model = AutoModelForCausalLM.from_pretrained(MODEL_ID)
        _gpt2_model.eval()
    return _gpt2_model


def _clip(text: str) -> str:
    if len(text) > MAX_INPUT_CHARS:
        return text[:MAX_INPUT_CHARS]
    return text


# --- Tokens tab ---

# Brand-grey chip palette (DESIGN.md: no rainbow accents)
CHIP_BACKGROUNDS = [
    "rgba(112, 112, 112, 0.55)",
    "rgba(112, 112, 112, 0.35)",
    "rgba(255, 255, 255, 0.08)",
    "rgba(112, 112, 112, 0.42)",
]

LONG_ENGLISH_PRESET = (
    "Language models do not read raw text the way humans do. "
    "Instead, a tokenizer splits your prompt into a sequence of integer token IDs. "
    "That sequence length affects API cost, context window usage, and inference speed. "
    "The same sentence can produce different token counts under GPT-2 BPE, tiktoken gpt2, "
    "and the cl100k_base encoding used by newer OpenAI models—especially for emoji, "
    "code, punctuation, and non-English characters. "
    "This demo lets you paste any string and compare three encodings side by side, "
    "with per-token chips and optional numeric IDs, without loading a full language model."
)


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


def _chip_span(token: str, index: int) -> str:
    safe = html.escape(token if token else "·")
    bg = CHIP_BACKGROUNDS[index % len(CHIP_BACKGROUNDS)]
    style = (
        "display:inline-block;margin:2px 3px 2px 0;padding:2px 8px;"
        f"border-radius:0.5rem;background:{bg};color:{INK};"
        f"border:1px solid {HAIRLINE_STRONG};"
        "font-family:'JetBrains Mono',ui-monospace,monospace;font-size:0.85em"
    )
    return f'<span style="{style}">{safe}</span>'


def _render_column(col: TokenColumn) -> str:
    chips = "".join(_chip_span(t, i) for i, t in enumerate(col.tokens))
    ids_str = ", ".join(str(i) for i in col.ids)
    return f"""
    <div style="flex:1;min-width:200px;padding:12px;border:1px solid {HAIRLINE};
                border-radius:1rem;background:{ORBITAL};">
      <p style="margin:0 0 8px;font-family:'Syne',ui-sans-serif,system-ui,sans-serif;
                font-weight:600;color:#ffffff;font-size:0.95rem;">{html.escape(col.label)}</p>
      <p style="margin:0 0 10px;font-size:0.9em;color:rgba(255,255,255,0.55);
                font-family:'DM Sans',ui-sans-serif,system-ui,sans-serif;">
        <strong style="color:#fff;">{len(col.tokens)}</strong> tokens
      </p>
      <div style="line-height:1.6;word-break:break-word;">{chips or "<em>empty</em>"}</div>
      <details style="margin-top:10px;font-size:0.8em;color:rgba(255,255,255,0.38);
                      font-family:'JetBrains Mono',ui-monospace,monospace;">
        <summary style="cursor:pointer;letter-spacing:0.08em;text-transform:uppercase;">
          Token IDs
        </summary>
        <p style="margin:8px 0 0;word-break:break-all;color:rgba(255,255,255,0.55);">{ids_str}</p>
      </details>
    </div>
    """


def _count_summary(columns: list[TokenColumn]) -> str:
    counts = [(c.label, len(c.tokens)) for c in columns]
    values = [n for _, n in counts]
    if max(values) - min(values) < 2:
        return ""
    hi_label, hi_n = max(counts, key=lambda x: x[1])
    lo_label, lo_n = min(counts, key=lambda x: x[1])
    delta = hi_n - lo_n
    summary_style = (
        "margin:0 0 12px;padding:10px 12px;border-radius:0.75rem;"
        f"background:{GLOW};border:1px solid {HAIRLINE_STRONG};color:{INK};font-size:0.9em;"
        "font-family:'DM Sans',ui-sans-serif,system-ui,sans-serif"
    )
    plural = "s" if delta != 1 else ""
    return (
        f'<p style="{summary_style}">'
        f'<strong style="color:#fff;">{html.escape(hi_label)}</strong> uses {delta} more token'
        f"{plural} than <strong style=\"color:#fff;\">{html.escape(lo_label)}</strong> "
        f"({hi_n} vs {lo_n}).</p>"
    )


def render_token_explorer(columns: list[TokenColumn]) -> str:
    summary = _count_summary(columns)
    cols_html = "".join(_render_column(c) for c in columns)
    return f"""
    <div style="font-family:'DM Sans',ui-sans-serif,system-ui,sans-serif;color:{INK};">
      {summary}
      <div style="display:flex;flex-wrap:wrap;gap:12px;">{cols_html}</div>
    </div>
    """


def tokenize_compare(text: str) -> str:
    text = _clip(text)
    if not text.strip():
        return "<p style='color:rgba(255,255,255,0.6);'>Enter some text.</p>"
    return render_token_explorer(analyze_text(text))


# --- NextToken tab ---


def _render_topk_bars(prompt: str, top_probs, top_ids) -> str:
    max_pct = top_probs[0].item() * 100 if len(top_probs) else 1.0
    max_pct = max(max_pct, 0.01)
    bars = []
    for prob, tid in zip(top_probs, top_ids):
        token = _hf_tok.decode([tid.item()])
        safe_tok = html.escape(token if token else "·")
        pct = prob.item() * 100
        width = min(100, (pct / max_pct) * 100)
        bar_bg = "rgba(112, 112, 112, 0.55)"
        bars.append(
            f'<div style="margin:8px 0;">'
            f'<div style="display:flex;justify-content:space-between;align-items:baseline;'
            f'margin-bottom:4px;font-family:monospace;font-size:0.9em;color:{INK};">'
            f'<span>{safe_tok}</span>'
            f'<span style="color:rgba(255,255,255,0.55);">{pct:.2f}%</span></div>'
            f'<div style="height:8px;border-radius:4px;background:rgba(255,255,255,0.06);">'
            f'<div style="width:{width:.1f}%;height:100%;border-radius:4px;'
            f'background:{bar_bg};border:1px solid {HAIRLINE_STRONG};"></div></div></div>'
        )
    safe_prompt = html.escape(prompt)
    return (
        f'<p style="color:rgba(255,255,255,0.45);font-size:0.85em;margin:0 0 12px;">'
        f"Prompt: <code style='color:{INK};'>{safe_prompt}</code></p>"
        + "".join(bars)
    )


def next_token_topk(prompt: str) -> str:
    prompt = _clip(prompt)
    if not prompt.strip():
        return "<p>Enter a prompt.</p>"

    model = _get_gpt2()
    inputs = _hf_tok(prompt, return_tensors="pt")

    with torch.no_grad():
        logits = model(**inputs).logits[0, -1]

    probs = F.softmax(logits, dim=-1)
    top_probs, top_ids = torch.topk(probs, TOP_K)
    return _render_topk_bars(prompt, top_probs, top_ids)


def next_token_step(prompt: str, steps: int) -> str:
    prompt = _clip(prompt)
    if not prompt.strip():
        return "Enter a prompt."

    model = _get_gpt2()
    current = prompt
    lines = [f"**Start:** `{current}`"]

    for step in range(1, steps + 1):
        inputs = _hf_tok(current, return_tensors="pt")
        with torch.no_grad():
            logits = model(**inputs).logits[0, -1]
        next_id = torch.argmax(logits).item()
        piece = _hf_tok.decode([next_id])
        current = current + piece
        lines.append(f"**Step {step}** (greedy +1): `{piece}` → `{current}`")

    return "\n".join(lines)


# --- Shared decode helper ---


def decode_text(
    prompt: str,
    strategy: str = "top_p",
    max_new_tokens: int = 48,
    top_p: float = 0.9,
    temperature: float = 1.0,
) -> str:
    if not prompt.strip():
        return "Enter a prompt."

    model = _get_gpt2()
    inputs = _hf_tok(prompt, return_tensors="pt")
    input_len = inputs["input_ids"].shape[1]

    gen_kwargs: dict = {
        "max_new_tokens": int(max_new_tokens),
        "pad_token_id": _hf_tok.eos_token_id,
    }

    if strategy == "greedy":
        gen_kwargs["do_sample"] = False
    else:
        gen_kwargs["do_sample"] = True
        gen_kwargs["top_p"] = float(top_p)
        gen_kwargs["temperature"] = float(temperature)

    with torch.no_grad():
        out = model.generate(**inputs, **gen_kwargs)

    new_ids = out[0, input_len:]
    return _hf_tok.decode(new_ids, skip_special_tokens=True)


# --- Decoding tab ---


def decode_greedy_vs_top_p(prompt: str, max_new_tokens: int, top_p: float) -> tuple[str, str]:
    greedy = decode_text(prompt, strategy="greedy", max_new_tokens=max_new_tokens)
    sampled = decode_text(
        prompt, strategy="top_p", max_new_tokens=max_new_tokens, top_p=top_p
    )
    return greedy, sampled


DECODING_PRESETS = [
    "Once upon a time",
    "What is 2+2?",
    "Suggest a party theme.",
]

TOKEN_EXAMPLES = [
    ["The 🌟 star-programmer implemented AGI overnight."],
    ['def hello():\n    print("world")'],
    ["「こんにちは」 — and café"],
    [LONG_ENGLISH_PRESET],
]


# --- Gradio UI (Gradio 6: theme/css on launch(), not Blocks) ---

_moonboots_theme = build_moonboots_theme()

try:
    demo = gr.Blocks(title="LLM Playground", fill_width=True)
except TypeError:
    demo = gr.Blocks(title="LLM Playground")

with demo:
    with gr.Tabs():
        with gr.Tab("Tokens"):
            tok_inp = gr.Textbox(
                label="Text",
                lines=3,
                value="The 🌟 star-programmer implemented AGI overnight.",
            )
            tok_out = gr.HTML()
            tok_btn = gr.Button("Tokenize", variant="primary")
            tok_btn.click(tokenize_compare, inputs=tok_inp, outputs=tok_out)
            demo.load(tokenize_compare, inputs=tok_inp, outputs=tok_out)
            gr.Examples(examples=TOKEN_EXAMPLES, inputs=tok_inp)

        with gr.Tab("NextToken"):
            gr.Markdown(
                "One forward pass: softmax over the vocabulary at the last position. "
                "This is the core loop of autoregressive generation."
            )
            nt_status = gr.Markdown(
                value=(
                    "*First use downloads GPT-2 (~500MB) on CPU—Predict may take 20–30s.*"
                )
            )
            nt_inp = gr.Textbox(label="Prompt", lines=2, value="Hello my name")
            nt_out = gr.HTML(label="Top next tokens")
            nt_btn = gr.Button("Predict", variant="primary")

            def predict_with_status(prompt: str) -> tuple[str, str]:
                if not prompt.strip():
                    return "", "<p>Enter a prompt.</p>"
                status = "*Running forward pass…*"
                result = next_token_topk(prompt)
                return "", result

            nt_btn.click(predict_with_status, inputs=nt_inp, outputs=[nt_status, nt_out])

            gr.Markdown("### Greedy step-forward (up to 3 tokens)")
            nt_steps = gr.Slider(1, 3, value=3, step=1, label="Steps")
            nt_step_out = gr.Markdown()
            nt_step_btn = gr.Button("Step forward (greedy)")
            nt_step_btn.click(
                next_token_step,
                inputs=[nt_inp, nt_steps],
                outputs=nt_step_out,
            )

        with gr.Tab("Decoding"):
            gr.Markdown(
                "Same prompt, two policies: greedy (deterministic) vs top-p nucleus sampling."
            )
            dec_inp = gr.Textbox(label="Prompt", lines=2, value="Once upon a time")
            dec_max = gr.Slider(8, 80, value=32, step=1, label="Max new tokens")
            dec_top_p = gr.Slider(0.5, 1.0, value=0.9, label="Top-p (sampling panel)")
            with gr.Row():
                dec_greedy = gr.Textbox(label="Greedy", lines=6)
                dec_sampled = gr.Textbox(label="Top-p sampling", lines=6)
            dec_btn = gr.Button("Generate both", variant="primary")
            dec_regen = gr.Button("Regenerate top-p only")
            dec_btn.click(
                decode_greedy_vs_top_p,
                inputs=[dec_inp, dec_max, dec_top_p],
                outputs=[dec_greedy, dec_sampled],
            )

            def regen_top_p(prompt, max_new_tokens, top_p):
                return "", decode_text(
                    prompt, strategy="top_p", max_new_tokens=max_new_tokens, top_p=top_p
                )

            dec_regen.click(
                regen_top_p,
                inputs=[dec_inp, dec_max, dec_top_p],
                outputs=[dec_greedy, dec_sampled],
            )
            gr.Examples(examples=[[p] for p in DECODING_PRESETS], inputs=dec_inp)

        with gr.Tab("Playground"):
            gr.Markdown(
                "Single-panel `generate()` playground: pick strategy and hyperparameters, "
                "see only newly generated tokens."
            )
            pg_prompt = gr.Textbox(label="Prompt", lines=3, value="Hi my name is")
            pg_strategy = gr.Radio(["greedy", "top_p"], value="top_p", label="Strategy")
            pg_max = gr.Slider(8, 128, value=48, step=1, label="Max new tokens")
            pg_top_p = gr.Slider(0.5, 1.0, value=0.9, label="Top-p")
            pg_temp = gr.Slider(0.1, 2.0, value=1.0, label="Temperature")
            pg_out = gr.Textbox(label="Generated text", lines=8)
            pg_btn = gr.Button("Generate", variant="primary")
            pg_btn.click(
                decode_text,
                inputs=[pg_prompt, pg_strategy, pg_max, pg_top_p, pg_temp],
                outputs=pg_out,
            )
            gr.Examples(examples=[[p] for p in DECODING_PRESETS], inputs=pg_prompt)

demo.launch(theme=_moonboots_theme, css=MOONBOOTS_CSS)
