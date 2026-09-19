#!/usr/bin/env python3
"""
Standardize Top Navigation and Global Footer across all pages in pages/ and index.html.
Ensures:
1. Logical Grouped Navigation: Research / Script / Design with interactive dropdowns
2. Comprehensive 4-column Global Footer with links to Skool, YouTube, GitHub, and tools
3. Zero dead links, complete relative path support, and mobile responsiveness
"""

import re
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
PAGES_DIR = ROOT_DIR / "pages"

NAV_GROUPS = [
    {
        "id": "research",
        "title": "🔬 Research",
        "badge": "Analysis & Economics",
        "hubFile": "research.html",
        "items": [
            {"file": "research.html", "name": "🧭 Research Hub", "desc": "Strategic rationale, unit economics & gating"},
            {"file": "time-estimation.html", "name": "⏱️ Time Estimation", "desc": "New course velocity & turnaround model"},
            {"file": "flashcards.html", "name": "⚡ Exam Flashcards", "desc": "Interactive flip-card study deck"},
            {"file": "youtube-vs-adwords.html", "name": "📊 Shorts vs AdWords", "desc": "Empirical CAC & traffic analysis"},
            {"file": "production-cost.html", "name": "💰 Production Cost", "desc": "Granular $0.63 unit economics"},
            {"file": "model-selection.html", "name": "🧠 Model Selection", "desc": "Claude, fal.ai Kling & ElevenLabs"},
            {"file": "sanity-check.html", "name": "🩺 Sanity Check", "desc": "7-stage automated quality gating"}
        ]
    },
    {
        "id": "script",
        "title": "✍️ Script",
        "badge": "Curriculum & Prompts",
        "hubFile": "script.html",
        "items": [
            {"file": "script.html", "name": "🧭 Script Hub", "desc": "16s narrative pacing & educational mechanics"},
            {"file": "dictionary.html", "name": "📖 Terms Dictionary", "desc": "24 certified curriculum terms"},
            {"file": "json-viewer.html", "name": "🔍 JSON Viewer", "desc": "Live schema explorer & DOM inspector"},
            {"file": "voice-selection.html", "name": "🎙️ Voice Selection", "desc": "ElevenLabs Brian (112Hz / 165 WPM)"},
            {"file": "execution-logic.html", "name": "🚀 Execution Logic", "desc": "Two-stage calibration calendar"},
            {"file": "prompts.html", "name": "📜 Prompts Log", "desc": "25 prompt session creation history"}
        ]
    },
    {
        "id": "design",
        "title": "🎨 Design",
        "badge": "Architecture & Parameters",
        "hubFile": "design.html",
        "items": [
            {"file": "design.html", "name": "🧭 Design Hub", "desc": "Architecture rationale, UML & parameters"},
            {"file": "architecture.html", "name": "🏛️ System Architecture", "desc": "5 UML diagrams with Excalidraw pan/zoom"},
            {"file": "parameters.html", "name": "⚙️ System Parameters", "desc": "38 engine parameters & sandbox"},
            {"file": "generated-code.html", "name": "💻 Generated Code", "desc": "Full repository filesystem explorer"}
        ]
    },
    {
        "id": "previz",
        "title": "🎬 Previz",
        "badge": "Storyboard & Pre-visualization",
        "hubFile": "previz.html",
        "items": [
            {"file": "previz.html", "name": "🧭 Previz Hub", "desc": "Pre-visualization rationale & visual pipeline"},
            {"file": "slideshow.html", "name": "🎬 Keyframe Slideshow", "desc": "Seedream 4.0 9:16 visual gallery"},
            {"file": "tell-show-do-apply.html", "name": "🎧 Tell-Show-Do-Apply", "desc": "4-phase audio-visual storyboard & SFX"},
            {"file": "specs.html", "name": "📋 Production Spec", "desc": "Anchor Video #01 master executable spec"}
        ]
    }
]

PAGE_CONFIG = [
    {"file": "research.html", "name": "🔬 Research Hub"},
    {"file": "time-estimation.html", "name": "⏱️ Time Estimation"},
    {"file": "script.html", "name": "✍️ Script Hub"},
    {"file": "design.html", "name": "🎨 Design Hub"},
    {"file": "previz.html", "name": "🎬 Previz Hub"},
    {"file": "dictionary.html", "name": "📖 Terms Dictionary"},
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
    {"file": "parameters.html", "name": "⚙️ Parameters"},
    {"file": "specs.html", "name": "📋 Production Spec"},
    {"file": "json-viewer.html", "name": "🔍 JSON Viewer"},
]

GLOBAL_CSS = """
    /* Top Navigation Dropdown Styles */
    .nav-dropdown {
      position: relative;
      display: inline-block;
    }
    .nav-dropdown-btn {
      color: var(--muted);
      background: transparent;
      border: 1px solid transparent;
      font-size: 13px;
      font-weight: 600;
      padding: 6px 12px;
      border-radius: 6px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s ease;
      font-family: inherit;
      text-decoration: none;
    }
    .nav-dropdown:hover .nav-dropdown-btn,
    .nav-dropdown-btn:hover {
      color: #fafafa;
      background: rgba(255, 255, 255, 0.06);
    }
    .nav-dropdown-btn.active {
      color: var(--accent);
      background: rgba(204, 120, 92, 0.12);
      border-color: rgba(204, 120, 92, 0.3);
    }
    .dropdown-chevron {
      font-size: 10px;
      opacity: 0.7;
      transition: transform 0.2s ease;
    }
    .nav-dropdown:hover .dropdown-chevron {
      transform: rotate(180deg);
    }
    .nav-dropdown-menu {
      display: none;
      position: absolute;
      top: 100%;
      left: 0;
      min-width: 280px;
      background: #141418;
      border: 1px solid var(--border);
      border-radius: 10px;
      box-shadow: 0 12px 36px rgba(0, 0, 0, 0.85);
      padding: 8px;
      z-index: 1000;
      margin-top: 4px;
      backdrop-filter: blur(16px);
    }
    .nav-dropdown:hover .nav-dropdown-menu {
      display: block;
      animation: navMenuFadeIn 0.18s cubic-bezier(0.16, 1, 0.3, 1);
    }
    @keyframes navMenuFadeIn {
      from { opacity: 0; transform: translateY(-6px); }
      to { opacity: 1; transform: translateY(0); }
    }
    .dropdown-header-badge {
      padding: 6px 10px 4px 10px;
      font-size: 10.5px;
      text-transform: uppercase;
      letter-spacing: 0.8px;
      color: var(--muted);
      font-weight: 700;
      border-bottom: 1px solid rgba(255, 255, 255, 0.06);
      margin-bottom: 6px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .dropdown-item {
      display: block;
      padding: 8px 10px;
      border-radius: 6px;
      text-decoration: none;
      color: #e4e4e7;
      font-size: 13px;
      font-weight: 500;
      transition: all 0.15s ease;
    }
    .dropdown-item:hover {
      background: rgba(255, 255, 255, 0.07);
      color: var(--accent);
      transform: translateX(2px);
    }
    .dropdown-item.active {
      background: rgba(204, 120, 92, 0.15);
      color: var(--accent);
      font-weight: 600;
      border-left: 2px solid var(--accent);
    }
    .dropdown-item-desc {
      display: block;
      font-size: 11px;
      color: var(--muted);
      font-weight: 400;
      margin-top: 2px;
      line-height: 1.3;
    }
    .nav-action-pill {
      background: rgba(56, 189, 248, 0.12);
      border: 1px solid rgba(56, 189, 248, 0.3);
      color: var(--cyan);
      padding: 5px 12px;
      border-radius: 9999px;
      font-size: 12px;
      font-weight: 600;
      text-decoration: none;
      transition: all 0.2s ease;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }
    .nav-action-pill:hover, .nav-action-pill.active {
      background: rgba(56, 189, 248, 0.22);
      color: #ffffff;
      border-color: var(--cyan);
    }

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

def generate_footer_html(is_root=False):
    prefix = "./pages/" if is_root else "./"
    root_link = "./index.html" if is_root else "../index.html"

    return f"""  <!-- Global Footer -->
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

      <!-- Col 2: Research & Script -->
      <div>
        <div class="footer-heading">🔬 Research &amp; ✍️ Script</div>
        <ul class="footer-links-list">
          <li><a href="{root_link}" style="font-weight: 700; color: var(--cyan);">🌐 Global Navigation Portal</a></li>
          <li><a href="{prefix}research.html" style="font-weight: 700; color: #fafafa;">🧭 Research Hub</a></li>
          <li><a href="{prefix}script.html" style="font-weight: 700; color: #fafafa;">🧭 Script Hub</a></li>
          <li><a href="{prefix}dictionary.html">📖 Terms Dictionary</a></li>
          <li><a href="{prefix}json-viewer.html">🔍 Interactive JSON Viewer</a></li>
          <li><a href="{prefix}flashcards.html">⚡ Exam Flashcards</a></li>
          <li><a href="{prefix}voice-selection.html">🎙️ Voice Selection</a></li>
          <li><a href="{prefix}production-cost.html">💰 Production Cost Model</a></li>
          <li><a href="{prefix}time-estimation.html">⏱️ Course Time Estimation</a></li>
          <li><a href="{prefix}model-selection.html">🧠 Model Selection</a></li>
          <li><a href="{prefix}execution-logic.html">🚀 Execution Logic</a></li>
          <li><a href="{prefix}prompts.html">📜 Prompt History Log</a></li>
        </ul>
      </div>

      <!-- Col 3: Design & Previz -->
      <div>
        <div class="footer-heading">🎨 Design &amp; 🎬 Previz</div>
        <ul class="footer-links-list">
          <li><a href="{prefix}design.html" style="font-weight: 700; color: #fafafa;">🧭 Design Hub</a></li>
          <li><a href="{prefix}previz.html" style="font-weight: 700; color: #fafafa;">🧭 Previz Hub</a></li>
          <li><a href="{prefix}slideshow.html">🎬 Keyframe Slideshow</a></li>
          <li><a href="{prefix}tell-show-do-apply.html">🎧 Tell-Show-Do-Apply</a></li>
          <li><a href="{prefix}specs.html">📋 Production Video Spec</a></li>
          <li><a href="{prefix}architecture.html">🏛️ System Architecture &amp; UML</a></li>
          <li><a href="{prefix}parameters.html">⚙️ System Parameters</a></li>
          <li><a href="{prefix}youtube-vs-adwords.html">📊 Shorts vs AdWords</a></li>
          <li><a href="{prefix}generated-code.html">💻 Generated Codebase</a></li>
          <li><a href="{prefix}sanity-check.html">🩺 Sanity Check Audit</a></li>
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
  </footer>"""

def generate_nav_bar(active_file, is_root=False):
    prefix = "./pages/" if is_root else "./"
    root_link = "./index.html" if is_root else "../index.html"

    nav_elements = []

    # Global Navigation link to index.html
    is_global_active = active_file == "index.html"
    nav_elements.append(f'<a href="{root_link}" class="nav-link{" active" if is_global_active else ""}">🌐 Global Navigation</a>')

    # Four pillar groups: Research, Script, Design, Previz
    for group in NAV_GROUPS:
        group_files = [it["file"] for it in group["items"]]
        is_group_active = active_file in group_files or active_file == group.get("hubFile")

        items_html = []
        items_html.append(f'<div class="dropdown-header-badge"><span>{group["badge"]}</span><span>{len(group["items"])} Pages</span></div>')

        for it in group["items"]:
            href = f"{prefix}{it['file']}"
            is_item_active = active_file == it["file"]
            active_class = " active" if is_item_active else ""
            items_html.append(
                f'<a href="{href}" class="dropdown-item{active_class}">'
                f'{it["name"]}'
                f'<span class="dropdown-item-desc">{it["desc"]}</span>'
                f'</a>'
            )

        dropdown_menu = '\n            '.join(items_html)
        hub_href = f"{prefix}{group['hubFile']}"
        group_html = (
            f'<div class="nav-dropdown">\n'
            f'          <a href="{hub_href}" class="nav-dropdown-btn{" active" if is_group_active else ""}">\n'
            f'            <span>{group["title"]}</span>\n'
            f'            <span class="dropdown-chevron">▾</span>\n'
            f'          </a>\n'
            f'          <div class="nav-dropdown-menu">\n'
            f'            {dropdown_menu}\n'
            f'          </div>\n'
            f'        </div>'
        )
        nav_elements.append(group_html)

    nav_links_inner = '\n        '.join(nav_elements)

    return f"""  <!-- Top Navigation Bar -->
  <nav class="top-nav">
    <div class="nav-inner">
      <a href="{root_link}" class="nav-brand">
        <div class="nav-brand-dot"></div>
        <span>Claude Associate Engine</span>
      </a>
      <div class="nav-links">
        {nav_links_inner}
      </div>
    </div>
  </nav>"""

def update_file(fpath, filename, is_root=False):
    if not fpath.exists():
        print(f"Skipping {filename} (not found)")
        return

    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update navigation bar atomically
    nav_bar_html = generate_nav_bar(filename, is_root=is_root)
    if '<nav class="top-nav">' in content:
        content = re.sub(
            r'<nav class="top-nav">[\s\S]*?</nav>',
            nav_bar_html,
            content,
            count=1
        )
    else:
        content = content.replace("<body>", f"<body>\n\n{nav_bar_html}", 1)

    # 2. Ensure Global CSS is present
    if ".nav-dropdown" not in content:
        content = content.replace("</style>", f"{GLOBAL_CSS}\n  </style>", 1)
    elif ".global-footer" not in content:
        content = content.replace("</style>", f"{GLOBAL_CSS}\n  </style>", 1)

    # 3. Replace old <footer> with Global Footer
    footer_html = generate_footer_html(is_root=is_root)
    if "<footer" in content:
        content = re.sub(r'<footer[\s\S]*?</footer>', footer_html.strip(), content, count=1)
    else:
        content = content.replace("</body>", f"{footer_html}\n</body>", 1)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ Updated nav & footer in {'index.html' if is_root else 'pages/' + filename}")

def main():
    # Update all files in pages/
    for item in PAGE_CONFIG:
        update_file(PAGES_DIR / item["file"], item["file"], is_root=False)

    # Update root index.html
    update_file(ROOT_DIR / "index.html", "index.html", is_root=True)

if __name__ == "__main__":
    main()
