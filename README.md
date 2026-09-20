> https://rifaterdemsahin.github.io/ai-dictionary-timeline/

# ai-dictionary-timeline

Programmatic 16-Second AI Short Pipeline for Claude Associate Certification concepts using Fal.ai, MCP, and Remotion.

## Overview
- **Model Control:** fal.ai (Seedream keyframes + Kling video interpolation + ElevenLabs TTS)
- **Workflow Orchestration:** Model Context Protocol (MCP) server
- **Composition & Rendering:** Remotion (React + TypeScript)
- **Local Preview Server:** Port `30085` (`http://localhost:30085`)

## Structure & Datasets
- [`data/claude-associate-terms.json`](file:///Users/rifaterdemsahin/projects/ai-dictionary-timeline/data/claude-associate-terms.json): 24 core terms across 6 exam domains mapped to 16-second video blueprints and exam traps.
- [`data/claude-flashcards.json`](file:///Users/rifaterdemsahin/projects/ai-dictionary-timeline/data/claude-flashcards.json): High-yield exam drill flashcards dataset.
- [`pages/flashcards.html`](file:///Users/rifaterdemsahin/projects/ai-dictionary-timeline/pages/flashcards.html): Interactive flashcard viewer with live search and raw JSON inspector.
- [`index.html`](file:///Users/rifaterdemsahin/projects/ai-dictionary-timeline/index.html): Curriculum terms dictionary and video blueprint viewer with top menu and live search.
