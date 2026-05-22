# LLM Playground

An interactive lab for understanding how large language models work—from tokenization through next-token prediction and text generation—without leaning on high-level frameworks for the core mechanics.

## Intent

This repository serves two goals, in order of priority.

### 1. Primary: Learn how LLMs work under the hood

The main deliverable is **`llm_playground.ipynb`**, a hands-on notebook where you implement and experiment with the foundations of language modeling:

- **Tokenization** — word-, character-, and subword-level (BPE); comparison with production tokenizers (`tiktoken`)
- **Language modeling** — load GPT-2, inspect architecture, count parameters, and interpret logits and next-token probabilities
- **Decoding** — greedy decoding and top-p (nucleus) sampling via Hugging Face `generate()`
- **Old vs. modern models** — contrast GPT-2 (text completion) with instruction-tuned Qwen3-0.6B (chat templates, reasoning-style behavior)
- **Looking ahead** — how inference engines (Ollama, vLLM, SGLang) fit into real serving

The emphasis is on building a **mental model**: what happens from raw text to generated output, and why each step exists. Later coursework introduces tools like Ollama and LangChain that abstract much of this; this project is the groundwork.

### 2. Secondary: Showcase that learning on a portfolio

A second goal is to **communicate what you learned** on a personal portfolio site: short write-ups, diagrams, and highly visual demos (e.g. token breakdowns, side-by-side GPT-2 vs. Qwen outputs, decoding comparisons) that let visitors explore ideas without reading the full notebook.

The notebook remains the source of truth for depth; the portfolio is the **curated, visual layer**—screenshots, recordings, embedded demos (e.g. Colab, Hugging Face Spaces), and explanations aimed at recruiters and peers.

Detailed specs for each planned demo live in [`portfolio/demos/`](portfolio/demos/). Those documents are the blueprint for what to build on the portfolio site (Gradio embeds, static sections, video, and copy). See the [portfolio hub](portfolio/README.md) for site layout, tiers, and implementation phases.

## What’s in this repo

| Path | Purpose |
|------|---------|
| `llm_playground.ipynb` | Main lab notebook (fill-in exercises + optional interactive playground) |
| `portfolio/README.md` | Portfolio hub: site structure, demo index, implementation roadmap |
| `portfolio/demos/*.md` | Per-demo specs (UX, copy, technical notes, build checklists) |
| `environment.yaml` | Conda environment (`llm_playground`) |
| `requirements.txt` | Python dependencies for local / uv setup |
| `env.sh` | Project-local `uv` and venv paths (source from repo root) |
| `demos-1/moonboots/` | Hugging Face Gradio app (Tokens, NextToken, Decoding, Playground tabs); deploy to [moonbootspleb/moonboots](https://huggingface.co/spaces/moonbootspleb/moonboots) |
| `demos-1/README.md` | Space folder index and HF deploy notes |

**Stack:** Python 3.11, PyTorch, Hugging Face Transformers, `tiktoken`, JupyterLab, optional `ipywidgets` for the playground UI.

**Models used in the notebook:** GPT-2 (small), Qwen3-0.6B (downloaded from Hugging Face on first run).

## Getting started

### Option A: Google Colab (no local install)

1. Open [Google Colab](https://colab.research.google.com/).
2. Upload `llm_playground.ipynb` or open it from GitHub.
3. Install dependencies in a cell if needed (see the notebook’s environment check).

### Option B: Local environment

**Conda:**

```bash
conda env create -f environment.yaml && conda activate llm_playground
```

**uv (faster):**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh   # skip if already installed
uv venv .venv --python 3.11 && source .venv/bin/activate
uv pip install -r requirements.txt
```

Optional — register the Jupyter kernel:

```bash
python -m ipykernel install --user --name=llm_playground --display-name "llm_playground"
```

Open the notebook in JupyterLab, select the `llm_playground` kernel, and work through the cells in order.

**Project-local tooling:** from the repo root, `source env.sh` puts the project’s `.venv` and `uv` cache on your `PATH`.

## Learning objectives (summary)

After completing the notebook, you should be able to:

- Explain how text becomes token IDs and why subword/BPE tokenization is the default for modern LLMs
- Load a pretrained causal LM and describe its main components at a high level
- Relate logits and softmax probabilities to “what token comes next”
- Compare greedy decoding vs. top-p sampling in behavior and tradeoffs
- Articulate the difference between completion-style models (GPT-2) and instruction-tuned chat models (Qwen3)
- Describe why production systems use dedicated inference servers instead of loading models inside every app process

## Portfolio demos

These demos will be **hosted on a personal portfolio site**—not only documented in this repo. Each demo has a detailed spec under [`portfolio/demos/`](portfolio/demos/). Interactive demos are intended as Gradio apps on Hugging Face Spaces (embedded via iframe) or linked from the site; static demos are diagrams, galleries, or scroll narratives.

**Recommended order on the portfolio page:** hero summary → Tier 1 interactives → GPT-2 vs Qwen write-up → Tier 2 supporting content → links to full notebook (Colab / GitHub).

| Demo | Tier | Type | Notebook | Spec | Status |
|------|------|------|----------|------|--------|
| [Tokenizer explorer](portfolio/demos/tokenizer-explorer.md) | 1 | Interactive (Space **Tokens**) | §1.3–1.4 | [spec](portfolio/demos/tokenizer-explorer.md) | done |
| [Next-token microscope](portfolio/demos/next-token-microscope.md) | 1 | Interactive (Space **NextToken**) | §2.3 | [spec](portfolio/demos/next-token-microscope.md) | done |
| [Greedy vs top-p](portfolio/demos/greedy-vs-top-p.md) | 1 | Interactive (Space **Decoding**) | §3.1–3.2 | [spec](portfolio/demos/greedy-vs-top-p.md) | done |
| [GPT-2 vs Qwen](portfolio/demos/gpt2-vs-qwen.md) | 1 | Write-up + static (blog Part 2) | §4.1–4.2 | [spec](portfolio/demos/gpt2-vs-qwen.md) | done |
| [Tokenization ladder](portfolio/demos/tokenization-ladder.md) | 2 | React (blog Part 3) | §1.1–1.3 | [spec](portfolio/demos/tokenization-ladder.md) | done |
| [Parameter scale calculator](portfolio/demos/parameter-scale-calculator.md) | 2 | React (blog Part 3) | §2.2 | [spec](portfolio/demos/parameter-scale-calculator.md) | done |
| [Transformer block diagram](portfolio/demos/transformer-block-diagram.md) | 2 | Static SVG (blog Part 3) | §2.1 | [spec](portfolio/demos/transformer-block-diagram.md) | done |
| [Decoding playground](portfolio/demos/decoding-playground.md) | 2 | Interactive (Space **Playground**) | §5 | [spec](portfolio/demos/decoding-playground.md) | done |
| [Pipeline story](portfolio/demos/pipeline-story.md) | 3 | Static scroll (blog Part 4) | Full arc | [spec](portfolio/demos/pipeline-story.md) | done |
| [Demo walkthrough video](portfolio/demos/demo-walkthrough-video.md) | 3 | Video placeholder (blog Part 4) | §1–4 | [spec](portfolio/demos/demo-walkthrough-video.md) | placeholder |
| [Failure modes gallery](portfolio/demos/failure-modes-gallery.md) | 3 | Static gallery (blog Part 4) | §1.1, §3.1, §4.2 | [spec](portfolio/demos/failure-modes-gallery.md) | done |

For the full index, blog mapping, and build phases, see [portfolio/README.md](portfolio/README.md).

## License

Add a license here if you plan to publish the repo publicly.
