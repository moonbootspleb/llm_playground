# Interactive demos (Hugging Face Space)

The hosted Gradio app for portfolio interactives lives in **[`moonboots/`](moonboots/)** — one Space, four tabs (Tokens, NextToken, Decoding, Playground).

| | |
|---|---|
| **GitHub (this repo)** | [moonbootspleb/llm_playground](https://github.com/moonbootspleb/llm_playground) → `demos-1/moonboots/` |
| **Live Space** | [moonbootspleb/moonboots](https://huggingface.co/spaces/moonbootspleb/moonboots) |
| **Developer guide** | [moonboots/DEVELOPER.md](moonboots/DEVELOPER.md) |

Previously the Space was developed in a separate clone at `BYTEBTYEGO/demos-1/moonboots` outside this repo. That tree is now **`demos-1/moonboots/` here** (the old `space/` folder was merged into this path).

### Deploy to Hugging Face

From the Space folder:

```bash
cd demos-1/moonboots
git init   # only if you use a dedicated HF working copy
git remote add origin git@hf.co:spaces/moonbootspleb/moonboots
git add app.py requirements.txt theme.py README.md .gitattributes
git commit -m "Sync from llm_playground demos-1/moonboots"
git push origin main
```

Or copy these files into an existing HF Space clone and push. After `app.py` changes, redeploy so [moonboots.tech](https://moonboots.tech) embeds pick up the build.
