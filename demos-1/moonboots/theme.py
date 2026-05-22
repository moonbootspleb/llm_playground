"""Gradio theme aligned with COMPANYSITE / DESIGN.md (moonboots.tech)."""

import gradio as gr

# DESIGN.md tokens
CANVAS = "#070708"
CANVAS_RAISED = "#0f1012"
ORBITAL = "#14151a"
BRAND = "#707070"
BRAND_BRIGHT = "#8a8a8a"
INK = "#f4f4f5"
BODY = "rgba(255, 255, 255, 0.55)"
MUTE = "rgba(255, 255, 255, 0.38)"
HAIRLINE = "rgba(255, 255, 255, 0.08)"
HAIRLINE_STRONG = "rgba(255, 255, 255, 0.15)"
GLOW = "rgba(112, 112, 112, 0.18)"

# Match COMPANYSITE BlogShell: px-4 sm:px-6
EMBED_PAD_X = "1rem"
EMBED_PAD_X_SM = "1.5rem"
EMBED_PAD_Y = "0.75rem"

FONT_IMPORT = (
    "@import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@"
    "0,9..40,400;0,9..40,500;0,9..40,600;1,9..40,400&family=JetBrains+Mono:wght@400;"
    "500&family=Syne:wght@600&display=swap');"
)

MOONBOOTS_CSS = f"""
{FONT_IMPORT}

:root, .gradio-container {{
    --moonboots-canvas: {CANVAS};
    --moonboots-raised: {CANVAS_RAISED};
    --moonboots-orbital: {ORBITAL};
    --moonboots-brand: {BRAND};
    --moonboots-brand-bright: {BRAND_BRIGHT};
}}

/* Full-width embed: match parent iframe / blog column (no Gradio max-width gutter) */
html, body {{
    margin: 0 !important;
    padding: 0 !important;
    width: 100% !important;
    background: {CANVAS} !important;
}}

.gradio-container {{
    background: {CANVAS} !important;
    font-family: 'DM Sans', ui-sans-serif, system-ui, sans-serif !important;
    color: {INK} !important;
    width: 100% !important;
    max-width: none !important;
    min-width: 0 !important;
    padding: {EMBED_PAD_Y} {EMBED_PAD_X} 1rem {EMBED_PAD_X} !important;
    margin: 0 auto !important;
    box-sizing: border-box !important;
}}

@media (min-width: 640px) {{
    .gradio-container {{
        padding: 1rem {EMBED_PAD_X_SM} 1.25rem {EMBED_PAD_X_SM} !important;
    }}
}}

.gradio-container .main,
.gradio-container .wrap,
.gradio-container .contain,
.gradio-container .panel,
.gradio-container .tabs,
.gradio-container .tabitem,
.gradio-container .column,
.gradio-container .row,
.gradio-container footer {{
    background: transparent !important;
    width: 100% !important;
    max-width: none !important;
    min-width: 0 !important;
    box-sizing: border-box !important;
}}

.gradio-container .main {{
    padding: 0 !important;
}}

.gradio-container .wrap,
.gradio-container .contain {{
    padding: 0 !important;
    gap: 0.875rem !important;
}}

.gradio-container .tab-nav {{
    margin-bottom: 0.25rem !important;
}}

.gradio-container .block,
.gradio-container .form {{
    width: 100% !important;
    max-width: none !important;
    margin-left: 0 !important;
    margin-right: 0 !important;
}}

.gradio-container .examples {{
    width: 100% !important;
    max-width: none !important;
}}

.gradio-container .examples table {{
    width: 100% !important;
}}

/* Tabs */
.gradio-container .tab-nav button {{
    font-family: 'JetBrains Mono', ui-monospace, monospace !important;
    font-size: 0.7rem !important;
    letter-spacing: 0.12em !important;
    text-transform: uppercase !important;
    color: {MUTE} !important;
    border-color: {HAIRLINE} !important;
    background: transparent !important;
}}

.gradio-container .tab-nav button.selected {{
    color: {INK} !important;
    border-color: {BRAND} !important;
    background: {GLOW} !important;
}}

/* Panels / blocks */
.gradio-container .block,
.gradio-container .form,
.gradio-container .panel {{
    background: {CANVAS_RAISED} !important;
    border-color: {HAIRLINE} !important;
    border-radius: 1rem !important;
}}

.gradio-container label span,
.gradio-container .block-title {{
    font-family: 'JetBrains Mono', ui-monospace, monospace !important;
    font-size: 0.7rem !important;
    letter-spacing: 0.14em !important;
    text-transform: uppercase !important;
    color: {MUTE} !important;
}}

/* Inputs */
.gradio-container textarea,
.gradio-container input[type="text"],
.gradio-container input[type="number"] {{
    background: {ORBITAL} !important;
    border: 1px solid {HAIRLINE_STRONG} !important;
    color: {INK} !important;
    border-radius: 0.75rem !important;
    font-family: 'JetBrains Mono', ui-monospace, monospace !important;
    font-size: 0.9rem !important;
}}

.gradio-container textarea:focus,
.gradio-container input:focus {{
    border-color: {BRAND} !important;
    box-shadow: 0 0 0 1px {GLOW} !important;
}}

/* Primary buttons */
.gradio-container button.primary,
.gradio-container .lg.primary {{
    background: {BRAND} !important;
    border: none !important;
    color: #fff !important;
    border-radius: 0.75rem !important;
    font-weight: 600 !important;
    box-shadow: 0 0 40px {GLOW} !important;
}}

.gradio-container button.primary:hover {{
    background: {BRAND_BRIGHT} !important;
}}

/* Secondary / ghost */
.gradio-container button.secondary,
.gradio-container button:not(.primary):not(.tab-nav button) {{
    background: rgba(255, 255, 255, 0.04) !important;
    border: 1px solid {HAIRLINE_STRONG} !important;
    color: {INK} !important;
}}

/* Examples table */
.gradio-container .examples table {{
    background: {ORBITAL} !important;
    border: 1px solid {HAIRLINE} !important;
    border-radius: 0.75rem !important;
}}

.gradio-container .examples td {{
    color: {BODY} !important;
    border-color: {HAIRLINE} !important;
}}

/* Markdown prose */
.gradio-container .markdown-prose,
.gradio-container .prose {{
    color: {BODY} !important;
}}

.gradio-container .markdown-prose h1,
.gradio-container .markdown-prose h2,
.gradio-container .markdown-prose h3 {{
    font-family: 'Syne', ui-sans-serif, system-ui, sans-serif !important;
    color: #fff !important;
    font-weight: 600 !important;
}}

.gradio-container .markdown-prose code {{
    font-family: 'JetBrains Mono', ui-monospace, monospace !important;
    background: {ORBITAL} !important;
    border: 1px solid {HAIRLINE} !important;
}}

/* Sliders */
.gradio-container input[type="range"] {{
    accent-color: {BRAND} !important;
}}

/* Radio */
.gradio-container .radio-item selected {{
    background: {GLOW} !important;
}}

footer {{
    display: none !important;
}}

/* Blog iframe only (?embed=true → body.embed). Do NOT use .gradio-embed — too broad in Gradio 6. */
body.embed .tab-nav button:not(:first-child),
html.embed .tab-nav button:not(:first-child) {{
    display: none !important;
}}
"""


THEME_OVERRIDES = {
    "body_background_fill": CANVAS,
    "body_background_fill_dark": CANVAS,
    "background_fill_primary": CANVAS_RAISED,
    "background_fill_secondary": ORBITAL,
    "block_background_fill": CANVAS_RAISED,
    "block_border_color": HAIRLINE,
    "block_border_width": "1px",
    "block_label_text_color": MUTE,
    "block_title_text_color": INK,
    "body_text_color": "rgba(255, 255, 255, 0.85)",
    "body_text_color_subdued": BODY,
    "button_primary_background_fill": BRAND,
    "button_primary_background_fill_hover": BRAND_BRIGHT,
    "button_primary_text_color": "#ffffff",
    "button_primary_border_color": "transparent",
    "button_secondary_background_fill": "rgba(255, 255, 255, 0.04)",
    "button_secondary_background_fill_hover": "rgba(255, 255, 255, 0.08)",
    "button_secondary_border_color": HAIRLINE_STRONG,
    "button_secondary_text_color": INK,
    "input_background_fill": ORBITAL,
    "input_border_color": HAIRLINE_STRONG,
    "input_placeholder_color": MUTE,
    "border_color_primary": HAIRLINE_STRONG,
    "border_color_accent": BRAND,
    "color_accent": BRAND,
    "color_accent_soft": GLOW,
    "link_text_color": BRAND_BRIGHT,
    "link_text_color_hover": "#ffffff",
    "link_text_color_visited": BRAND,
    "panel_background_fill": CANVAS_RAISED,
    "panel_border_color": HAIRLINE,
    "table_border_color": HAIRLINE,
    "checkbox_label_background_fill": ORBITAL,
    "checkbox_label_background_fill_selected": GLOW,
    "slider_color": BRAND,
    "stat_background_fill": ORBITAL,
    "shadow_drop": "none",
    "shadow_spread": "0px",
    "shadow_drop_active": "none",
}


def _apply_theme_overrides(theme, overrides: dict):
    """Apply .set() keys supported by the installed Gradio version."""
    import re

    pending = dict(overrides)
    while pending:
        try:
            return theme.set(**pending)
        except TypeError as err:
            match = re.search(r"unexpected keyword argument '(\w+)'", str(err))
            if not match or match.group(1) not in pending:
                raise
            del pending[match.group(1)]
    return theme


def build_moonboots_theme():
    """Gradio Base theme tuned to MoonBoots DESIGN.md."""
    try:
        font = gr.themes.GoogleFont("DM Sans")
        font_mono = gr.themes.GoogleFont("JetBrains Mono")
    except Exception:
        font = ("DM Sans", "ui-sans-serif", "system-ui", "sans-serif")
        font_mono = ("JetBrains Mono", "ui-monospace", "monospace")

    theme = gr.themes.Base(
        primary_hue=gr.themes.colors.gray,
        secondary_hue=gr.themes.colors.gray,
        neutral_hue=gr.themes.colors.gray,
        spacing_size=gr.themes.sizes.spacing_md,
        radius_size=gr.themes.sizes.radius_lg,
        text_size=gr.themes.sizes.text_md,
        font=font,
        font_mono=font_mono,
    )
    return _apply_theme_overrides(theme, THEME_OVERRIDES)


HERO_HTML = """
<div class="mb-hero" style="margin-bottom:1.25rem;padding-bottom:1.25rem;border-bottom:1px solid rgba(255,255,255,0.08);">
  <p style="margin:0 0 0.5rem;font-family:'JetBrains Mono',ui-monospace,monospace;font-size:0.75rem;
     letter-spacing:0.18em;text-transform:uppercase;color:rgba(255,255,255,0.38);">
    LLM playground
  </p>
  <h1 style="margin:0 0 0.75rem;font-family:'Syne',ui-sans-serif,system-ui,sans-serif;font-size:1.875rem;
     font-weight:600;letter-spacing:-0.02em;color:#ffffff;line-height:1.15;">
    From tokens to text
  </h1>
  <p style="margin:0;font-family:'DM Sans',ui-sans-serif,system-ui,sans-serif;font-size:1rem;
     line-height:1.6;color:rgba(255,255,255,0.55);max-width:42rem;">
    Interactive GPT-2 demos: tokenization, next-token probabilities, and decoding strategies.
    The first model tab may take a minute while weights download on CPU.
  </p>
</div>
"""
