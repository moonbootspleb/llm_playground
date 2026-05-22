---
title: LLM Playground
emoji: 🌙
colorFrom: gray
colorTo: blue
sdk: gradio
sdk_version: "6.0.0"
python_version: "3.11"
app_file: app.py
pinned: false
short_description: Tokenization, next-token prediction, and decoding demos (GPT-2 on CPU).
models:
  - openai-community/gpt2
---

# LLM Playground — Hugging Face Space

Gradio app for interactive portfolio demos (tokenizer explorer, next-token microscope, greedy vs top-p, decoding playground).

| | |
|---|---|
| **Live Space** | [moonbootspleb/moonboots](https://huggingface.co/spaces/moonbootspleb/moonboots) |
| **Deploy remote** | `git@hf.co:spaces/moonbootspleb/moonboots` |

This folder is the source copy in the [llm_playground](https://github.com/moonbootspleb/llm_playground) GitHub repo at `demos-1/moonboots/`. To deploy:

```bash
cd demos-1/moonboots
# push to Hugging Face (see ../README.md or DEVELOPER.md)
```

See [DEVELOPER.md](DEVELOPER.md) for full setup, tabs, and demo spec links (`../portfolio/demos/`).
