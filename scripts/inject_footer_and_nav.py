#!/usr/bin/env python3
"""
Standardize Top Navigation and Global Footer across all pages in pages/.
Ensures:
1. Complete 10-link navigation with 'active' class on current page
2. Comprehensive 4-column Global Footer with links to Skool, YouTube, GitHub, GitHub Pages, and all curriculum tools
3. Consistent CSS styling
"""

import re
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
PAGES_DIR = ROOT_DIR / "pages"

PAGE_CONFIG = [
    {"file": "flashcards.html", "name": "⚡ Flashcards"},
    {"file": "slideshow.html", "name": "🎬 Keyframe Slideshow"},
    {"file": "prompts.html", "name": "📜 Prompts Log"},
    {"file": "production-cost.html", "name": "💰 Production Cost"},
    {"file": "youtube-vs-adwords.html", "name": "📊 Shorts vs AdWords"},
    {"file": "execution-logic.html", "name": "🚀 Execution Logic"},
    {"file": "tell-show-do-apply.html", "name": "🎧 Tell-Show-Do-Apply"},
    {"file": "sanity-check.html", "name": "🩺 Sanity Check"},
    {"file": "generated-code.html", "name": "💻 Generated Code"},
    {"file": "model-selection.html", "name": "🧠 Model Selection"},
    {"file": "voice-selection.html", "name": "🎙️ Voice Selection"},
    {"file": "architecture.html", "name": "🏛️ Architecture"},
]

FOOTER_CSS = """
    /* Comprehensive Global Footer */
    .global-footer {
      background: #000000;
      border-top: 1px solid var(--border);
      padding: 60px 20px 30px 20px;
      color: var(--muted);
      font-size: 13.5px;
      margin-top: 60px;
    }
    .footer-inner {
      max-width: 1200px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: 2fr 1fr 1fr 1.5fr;
      gap: 36px;
      margin-bottom: 40px;
    }
    @media (max-width: 900px) {
      .footer-inner { grid-template-columns: 1fr 1fr; }
    }
    @media (max-width: 600px) {
      .footer-inner { grid-template-columns: 1fr; }
    }
    .footer-brand {
      display: flex;
      align-items: center;
      gap: 10px;
      color: #fafafa;
      font-weight: 700;
      font-size: 17px;
      margin-bottom: 12px;
    }
    .footer-desc {
      font-size: 13px;
      line-height: 1.6;
      color: var(--muted);
      max-width: 380px;
      margin-bottom: 16px;
    }
    .footer-heading {
      font-size: 13px;
      font-weight: 700;
      color: #ffffff;
      text-transform: uppercase;
      letter-spacing: 0.8px;
      margin-bottom: 16px;
    }
    .footer-links-list {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 9px;
      padding: 0;
      margin: 0;
    }
    .footer-links-list a {
      color: var(--muted);
      text-decoration: none;
      transition: color 0.2s ease;
    }
    .footer-links-list a:hover {
      color: var(--accent);
    }
    .footer-badge-pill {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(74, 222, 128, 0.1);
      border: 1px solid rgba(74, 222, 128, 0.25);
      color: var(--green);
      font-size: 12px;
      padding: 4px 10px;
      border-radius: 9999px;
      font-weight: 600;
      margin-top: 6px;
    }
    .footer-bottom-bar {
      max-width: 1200px;
      margin: 0 auto;
      padding-top: 24px;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
      font-size: 12.5px;
    }
"""

FOOTER_HTML = """  <!-- Global Footer -->
  <footer class="global-footer">
    <div class="footer-inner">
      <!-- Col 1: Brand & Overview -->
      <div>
        <div class="footer-brand">
          <div class="nav-brand-dot"></div>
          <span>Claude Associate Engine</span>
        </div>
        <p class="footer-desc">
          Automated media architecture and 16-second vertical video generation engine for the Anthropic Claude Certified Associate examination.
        </p>
        <div class="footer-badge-pill">
          <span>●</span> Port 30085 Active &bull; All 7 Gating Stages Passing
        </div>
      </div>

      <!-- Col 2: Learning & Study Tools -->
      <div>
        <div class="footer-heading">Curriculum Tools</div>
        <ul class="footer-links-list">
          <li><a href="../index.html">📖 Terms Dictionary</a></li>
          <li><a href="./flashcards.html">⚡ Exam Flashcards</a></li>
          <li><a href="./slideshow.html">🎬 Keyframe Slideshow</a></li>
          <li><a href="./tell-show-do-apply.html">🎧 Tell-Show-Do-Apply</a></li>
          <li><a href="../data/claude-associate-terms.json" target="_blank">🔗 Raw Terms JSON</a></li>
        </ul>
      </div>

      <!-- Col 3: Economics & Operations -->
      <div>
        <div class="footer-heading">Pipeline &amp; Scaling</div>
        <ul class="footer-links-list">
          <li><a href="./production-cost.html">💰 Production Cost Model</a></li>
          <li><a href="./model-selection.html">🧠 Model Selection &amp; Rationale</a></li>
          <li><a href="./voice-selection.html">🎙️ ElevenLabs Voice Architecture</a></li>
          <li><a href="./architecture.html">🏛️ System Architecture &amp; UML</a></li>
          <li><a href="./youtube-vs-adwords.html">📊 Shorts vs AdWords CAC</a></li>
          <li><a href="./execution-logic.html">🚀 Two-Stage Execution Logic</a></li>
          <li><a href="./sanity-check.html">🩺 Sanity Check Audit</a></li>
          <li><a href="./generated-code.html">💻 Generated Codebase</a></li>
          <li><a href="./prompts.html">📜 Prompt History Log</a></li>
        </ul>
      </div>

      <!-- Col 4: Ecosystem & External -->
      <div>
        <div class="footer-heading">Community &amp; Code</div>
        <ul class="footer-links-list">
          <li><a href="https://rifaterdemsahin.github.io/ai-dictionary-timeline/" target="_blank" style="color: var(--cyan); font-weight: 700;">🌐 GitHub Pages Live Site ↗</a></li>
          <li><a href="https://www.skool.com/delivery-pilot-8938" target="_blank" style="color: var(--accent); font-weight: 600;">👥 Delivery Pilot Skool ↗</a></li>
          <li><a href="https://www.youtube.com/shorts/KVKJRdkH-B8" target="_blank">🎥 Audited YouTube Short (KVKJRdkH-B8) ↗</a></li>
          <li><a href="https://github.com/rifaterdemsahin/ai-dictionary-timeline" target="_blank">🐙 GitHub Repository ↗</a></li>
        </ul>
      </div>
    </div>

    <div class="footer-bottom-bar">
      <div>&copy; 2026 Rifat Erdem Sahin &bull; Delivery Pilot AI Systems Architecture</div>
      <div style="display: flex; gap: 12px; align-items: center; flex-wrap: wrap;">
        <span style="color: var(--muted);">Live on GitHub Pages:</span>
        <a href="https://rifaterdemsahin.github.io/ai-dictionary-timeline/" target="_blank" style="color: var(--cyan); text-decoration: underline; font-weight: 600;">https://rifaterdemsahin.github.io/ai-dictionary-timeline/ ↗</a>
      </div>
    </div>
  </footer>
"""

def generate_nav_html(active_file):
    links = [
        f'<a href="../index.html" class="nav-link{" active" if active_file == "index.html" else ""}">📖 Terms Dictionary</a>',
        f'<a href="./flashcards.html" class="nav-link{" active" if active_file == "flashcards.html" else ""}">⚡ Flashcards</a>',
        f'<a href="./slideshow.html" class="nav-link{" active" if active_file == "slideshow.html" else ""}">🎬 Keyframe Slideshow</a>',
        f'<a href="./prompts.html" class="nav-link{" active" if active_file == "prompts.html" else ""}">📜 Prompts Log</a>',
        f'<a href="./production-cost.html" class="nav-link{" active" if active_file == "production-cost.html" else ""}">💰 Production Cost</a>',
        f'<a href="./model-selection.html" class="nav-link{" active" if active_file == "model-selection.html" else ""}">🧠 Model Selection</a>',
        f'<a href="./voice-selection.html" class="nav-link{" active" if active_file == "voice-selection.html" else ""}">🎙️ Voice Selection</a>',
        f'<a href="./architecture.html" class="nav-link{" active" if active_file == "architecture.html" else ""}">🏛️ Architecture</a>',
        f'<a href="./youtube-vs-adwords.html" class="nav-link{" active" if active_file == "youtube-vs-adwords.html" else ""}">📊 Shorts vs AdWords</a>',
        f'<a href="./execution-logic.html" class="nav-link{" active" if active_file == "execution-logic.html" else ""}">🚀 Execution Logic</a>',
        f'<a href="./tell-show-do-apply.html" class="nav-link{" active" if active_file == "tell-show-do-apply.html" else ""}">🎧 Tell-Show-Do-Apply</a>',
        f'<a href="./sanity-check.html" class="nav-link{" active" if active_file == "sanity-check.html" else ""}">🩺 Sanity Check</a>',
        f'<a href="./generated-code.html" class="nav-link{" active" if active_file == "generated-code.html" else ""}">💻 Generated Code</a>',
        '<a href="../data/claude-associate-terms.json" target="_blank" class="nav-link">🔗 Terms JSON</a>'
    ]
    return '\n        '.join(links)

def update_page(filename):
    fpath = PAGES_DIR / filename
    if not fpath.exists():
        print(f"Skipping {filename} (not found)")
        return

    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update navigation links inside <div class="nav-links">...</div>
    new_nav_links = generate_nav_html(filename)
    content = re.sub(
        r'<div class="nav-links">[\s\S]*?</div>',
        f'<div class="nav-links">\n        {new_nav_links}\n      </div>',
        content,
        count=1
    )

    # 2. Ensure Footer CSS is present
    if ".global-footer" not in content:
        content = content.replace("</style>", f"{FOOTER_CSS}\n  </style>", 1)

    # 3. Replace old <footer> with Global Footer
    if "<footer" in content:
        content = re.sub(r'<footer[\s\S]*?</footer>', FOOTER_HTML.strip(), content, count=1)
    else:
        # Insert before </body>
        content = content.replace("</body>", f"{FOOTER_HTML}\n</body>", 1)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ Updated nav & footer in pages/{filename}")

def main():
    for item in PAGE_CONFIG:
        update_page(item["file"])

if __name__ == "__main__":
    main()
