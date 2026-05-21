# Demo walkthrough video

**Tier:** 3 | **Type:** Video | **Status:** placeholder

**Blog:** Part 4 · `#walkthrough-video` — embed when MP4/YouTube URL is ready

## Overview

A **60–90 second** screen recording that tours the lab’s core ideas: tokenize → predict next token → decode → contrast GPT-2 with Qwen.

## What visitors learn

A fast, passive introduction before they click interactives or Colab. Useful for portfolio visitors on mobile or recruiters with limited time.

## Connection to the lab

- [`llm_playground.ipynb`](../../llm_playground.ipynb) — highlights from **§1–4** (skip §6 inference engines or mention in final frame)

## Demo behavior

1. Video embedded on portfolio (YouTube, Vimeo, or self-hosted MP4).
2. Autoplay **off**; poster frame from tokenizer demo.
3. Optional chapters in description:
   - 0:00 — Hook: “LLMs predict the next token”
   - 0:15 — Tokenization (BPE chips)
   - 0:30 — Top-5 logits
   - 0:45 — Greedy vs top-p outputs
   - 1:00 — GPT-2 vs Qwen on “What is 2+2?”
   - 1:15 — CTA: links on screen

## Visual design

- Record at 1920×1080 or 1280×720; crop/zoom for readability.
- Large cursor; hide personal paths/desktop clutter.
- Optional light voiceover or captions (accessibility).
- End card: project title + GitHub + Colab QR or URL.

## Storyboard (script)

| Time | Visual | Narration / caption |
|------|--------|---------------------|
| 0–10s | Notebook title + prompt typed | “This project starts with text—but models need numbers.” |
| 10–25s | Run tokenizer cell; show tokens | “BPE splits text into subword tokens.” |
| 25–40s | §2.3 top-5 logits output | “One forward pass gives a probability distribution over the vocabulary.” |
| 40–55s | Side-by-side greedy vs top-p | “How you pick the next token changes the feel of the output.” |
| 55–75s | GPT-2 vs Qwen outputs | “Training objective and chat format change behavior—not just size.” |
| 75–90s | End card with links | “Full lab on GitHub and Colab—link below.” |

## Copy suggestions

> Prefer watching first? This 90-second walkthrough covers the same arc as the interactive demos.

> Recorded from the completed lab notebook after all exercises were filled in.

## Technical notes

- **Tools:** OBS, QuickTime, or Loom; edit in DaVinci Resolve / iMovie if needed.
- **Audio:** optional; captions recommended if silent.
- **Hosting:** YouTube unlisted or public; embed via iframe on portfolio.
- Re-record when Tier 1 UIs change significantly.

## Build checklist

- [ ] Complete notebook exercises for clean recording
- [ ] Record each segment; trim pauses and model download waits
- [ ] Add captions (YouTube auto or SRT)
- [ ] Upload and paste embed URL into portfolio README deployment table
- [ ] Set poster image on portfolio embed

## Status

`placeholder` — UI slot on COMPANYSITE Part 4; record and embed video separately.
