#!/usr/bin/env python3
"""
Add tailored high-converting pinned comments for YouTube Shorts to all 24 Claude Associate terms.
Each comment is structured for:
1. Hook & Topic Re-engagement
2. Exam Trap Warning / Value Offer
3. Direct CTA to Skool Platform: https://www.skool.com/delivery-pilot-8938
4. Algorithmic Engagement Question (to boost comment count & Shorts algorithm distribution)
"""

import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "claude-associate-terms.json"

PINNED_COMMENTS = {
    "artifacts": {
        "pinnedComment": "📌 Mastered Artifacts vs Inline Markdown? Don't let this trick question cost you points on the Claude Certified Associate Exam! 🎯 Grab the full interactive 24-term exam blueprint and flashcards free inside Delivery Pilot: 👉 https://www.skool.com/delivery-pilot-8938\n\n👇 Quick Quiz: Would you put a 25-line React component or a 3-line curl command in an Artifact window? Drop your answer below!",
        "hookTopic": "Artifacts vs Inline Markdown Decision Matrix"
    },
    "inline-markdown": {
        "pinnedComment": "📌 Should Claude open a side Artifact or stay directly in chat? Keeping conversational replies and short snippets inline protects user workflow! ⚡ Master all Claude UI mechanics and exam blueprints inside Delivery Pilot: 👉 https://www.skool.com/delivery-pilot-8938\n\n👇 When do you prefer inline chat over an Artifact window? Let's discuss in the comments!",
        "hookTopic": "Inline Chat Flow & Workspace Ergonomics"
    },
    "task-decomposition": {
        "pinnedComment": "📌 Single giant prompts hallucinate—deconstructed sequential steps succeed! 🛠️ Want our plug-and-play task decomposition prompts and Claude Associate study guide? Join 100+ AI builders free in Delivery Pilot: 👉 https://www.skool.com/delivery-pilot-8938\n\n👇 What complex prompt are you trying to break down right now? Drop it below!",
        "hookTopic": "Task Decomposition & Multi-Step Prompts"
    },
    "xml-tagging": {
        "pinnedComment": "📌 Why does Anthropic demand XML tags instead of markdown headers? It mathematically prevents prompt injection and separates instructions from untrusted data! 🛡️ Grab our production XML template library inside Delivery Pilot: 👉 https://www.skool.com/delivery-pilot-8938\n\n👇 Do you use <instructions> and <context> tags in your production prompts yet? Vote yes or no below!",
        "hookTopic": "XML Tagging & Injection Defense"
    },
    "system-prompts": {
        "pinnedComment": "📌 System prompts define the model's immutable boundary rules. Never leak role instructions into user turns! 🔒 Grab our battle-tested system prompt architectures for Claude 3.5 Sonnet inside Delivery Pilot: 👉 https://www.skool.com/delivery-pilot-8938\n\n👇 What's your number one rule inside your Claude system prompt? Share it below!",
        "hookTopic": "System Prompts & Boundary Architecture"
    },
    "model-tier-tradeoffs": {
        "pinnedComment": "📌 Haiku vs Sonnet vs Opus: Picking Opus for high-volume routing will destroy your monthly cloud bill! 💸 Grab our model selection decision tree and Claude Associate prep deck in Delivery Pilot: 👉 https://www.skool.com/delivery-pilot-8938\n\n👇 Haiku 3.5 for speed or Sonnet 3.5 for code? Which model is your default workhorse?",
        "hookTopic": "Claude Model Family Selection"
    },
    "context-window": {
        "pinnedComment": "📌 Having a 200,000-token context window doesn't mean you should dump raw unindexed garbage into it! Learn context hygiene, prompt caching, and cost control inside Delivery Pilot: 👉 https://www.skool.com/delivery-pilot-8938\n\n👇 What's the biggest context window payload you've ever sent to an LLM? Let me know below!",
        "hookTopic": "200k Context Window Management"
    },
    "prompt-caching": {
        "pinnedComment": "📌 90% cost reduction and 85% lower latency on static context! But remember: the 1,024-token minimum threshold trips up most exam takers. 💡 Get our caching cost calculator & code templates in Delivery Pilot: 👉 https://www.skool.com/delivery-pilot-8938\n\n👇 Are you caching your system prompts and documentation yet? Drop your setup below!",
        "hookTopic": "Prompt Caching & 1024-Token Thresholds"
    },
    "tool-use-stop-reason": {
        "pinnedComment": "📌 The #1 exam trap: Claude DOES NOT run your database queries! It pauses with stop_reason='tool_use' and waits for your client loop. ⚙️ Get the complete Python/TypeScript tool-use loop code inside Delivery Pilot: 👉 https://www.skool.com/delivery-pilot-8938\n\n👇 Have you built an external tool execution loop with Claude Messages API? Share your use case below!",
        "hookTopic": "stop_reason='tool_use' Loop Mechanics"
    },
    "mcp-protocol": {
        "pinnedComment": "📌 Model Context Protocol (MCP) is the universal USB-C standard for AI agents and enterprise tools. Connect local files, databases, and APIs effortlessly! 🔌 Join our MCP builder sessions in Delivery Pilot: 👉 https://www.skool.com/delivery-pilot-8938\n\n👇 What MCP server do you use most: filesystem, git, or database? Let us know below!",
        "hookTopic": "Model Context Protocol (MCP) Integration"
    },
    "claude-projects": {
        "pinnedComment": "📌 Custom project instructions + uploaded grounding files = team-wide consistency. Avoid context bloat by pruning outdated project docs! 📁 Grab our Project setup guide & Claude Associate cards inside Delivery Pilot: 👉 https://www.skool.com/delivery-pilot-8938\n\n👇 How many custom Projects do you have active in Claude right now?",
        "hookTopic": "Claude Projects & Team Knowledge Bases"
    },
    "chain-of-thought": {
        "pinnedComment": "📌 Force Claude to show its work! Wrapping complex multi-step reasoning in <thinking> tags cuts math and logic hallucinations by over 70%. 🧠 Grab our full Chain-of-Thought prompting guide inside Delivery Pilot: 👉 https://www.skool.com/delivery-pilot-8938\n\n👇 Do you use scratchpad <thinking> tags in your API calls? Drop your thoughts below!",
        "hookTopic": "Chain-of-Thought (<thinking>) Scratchpads"
    },
    "few-shot-prompting": {
        "pinnedComment": "📌 Don't just explain what you want—show 2 to 3 pristine input/output examples! Few-shot prompting calibrates edge cases better than paragraphs of text. 📚 Get our few-shot templates inside Delivery Pilot: 👉 https://www.skool.com/delivery-pilot-8938\n\n👇 Zero-shot or Few-shot: Which one solved your hardest prompt bug? Tell us below!",
        "hookTopic": "Few-Shot Prompt Engineering"
    },
    "hallucination-mitigation": {
        "pinnedComment": "📌 Always provide a safe 'I don't know' exit hatch! Unconstrained LLMs will invent plausible falsehoods when grounding data is missing. 🛡️ Download our Hallucination Defense Playbook in Delivery Pilot: 👉 https://www.skool.com/delivery-pilot-8938\n\n👇 What's the funniest or worst hallucination an AI model ever gave you? Share below!",
        "hookTopic": "Hallucination Defense & Grounding Hatches"
    },
    "human-in-the-loop": {
        "pinnedComment": "📌 Autonomous agents must never commit destructive database writes or trigger financial transactions without a human approval step! 🛑 Get our HITL architecture diagrams inside Delivery Pilot: 👉 https://www.skool.com/delivery-pilot-8938\n\n👇 At what risk level do you require manual human sign-off in your AI pipelines?",
        "hookTopic": "Human-in-the-Loop (HITL) Guardrails"
    },
    "temperature": {
        "pinnedComment": "📌 Temperature = 0.0 for deterministic JSON schemas and code; Temperature = 0.7 for creative copywriting. Never mix them up on the exam! 🌡️ Grab our complete parameter calibration cheat sheet inside Delivery Pilot: 👉 https://www.skool.com/delivery-pilot-8938\n\n👇 What temperature setting do you use for code generation: 0.0, 0.2, or higher?",
        "hookTopic": "Temperature & Top-p Calibration"
    },
    "json-schema-tools": {
        "pinnedComment": "📌 Valid JSON schemas guarantee clean tool parsing. Always specify 'required' arrays and explicit field descriptions! 📄 Get our production JSON schema validator and templates in Delivery Pilot: 👉 https://www.skool.com/delivery-pilot-8938\n\n👇 What is your biggest challenge when writing JSON schemas for function calling?",
        "hookTopic": "JSON Schema Tool Declarations"
    },
    "research-mode": {
        "pinnedComment": "📌 Research mode transforms Claude into an autonomous multi-source investigator. Always verify citation timestamps against authoritative ground truth! 🌐 Join our AI research workflow community in Delivery Pilot: 👉 https://www.skool.com/delivery-pilot-8938\n\n👇 What is your favorite live connector in Claude: web search, Google Docs, or GitHub?",
        "hookTopic": "Research Mode & Grounded Web Connectors"
    },
    "prompt-iteration": {
        "pinnedComment": "📌 Never optimize prompts based on gut feeling! Build a golden evaluation set of 20 edge-case test queries and measure regression systematically. 🔄 Get our prompt testing workbook inside Delivery Pilot: 👉 https://www.skool.com/delivery-pilot-8938\n\n👇 How many prompt iterations does it usually take you to reach production quality?",
        "hookTopic": "Systematic Prompt Iteration & Regression Testing"
    },
    "evaluation-metrics": {
        "pinnedComment": "📌 LLM-as-a-judge vs deterministic exact match: how do you grade your agent outputs? 📊 Download our Claude Associate evaluation rubric and benchmark guide inside Delivery Pilot: 👉 https://www.skool.com/delivery-pilot-8938\n\n👇 Do you use programmatic assertions or human grading for your AI apps?",
        "hookTopic": "Evaluation & LLM Benchmarking"
    },
    "stakeholder-value-communication": {
        "pinnedComment": "📌 The hardest part of AI engineering isn't the code—it's communicating realistic ROI, latency SLAs, and safety guardrails to non-technical executives! 💼 Download our executive AI slide deck inside Delivery Pilot: 👉 https://www.skool.com/delivery-pilot-8938\n\n👇 How do you explain LLM hallucinations to leadership? Drop your best analogy below!",
        "hookTopic": "Executive AI Communication & Value Delivery"
    },
    "task-alignment-model-fit": {
        "pinnedComment": "📌 Right-sizing models: Pair Haiku for high-concurrency ingestion, Sonnet for tool execution, and Opus for multi-perspective synthesis. 📐 Grab our Task-to-Model alignment matrix inside Delivery Pilot: 👉 https://www.skool.com/delivery-pilot-8938\n\n👇 What percentage of your production traffic goes to Haiku vs Sonnet?",
        "hookTopic": "Task-to-Model Alignment Matrix"
    },
    "token-budgeting": {
        "pinnedComment": "📌 Day 1 of understanding LLMs: How AI models read text! Tokenization, token IDs, and context budgets dictate your cloud bill. 🧠 Grab the interactive Tokenization & Claude Associate cheat sheet free inside Delivery Pilot: 👉 https://www.skool.com/delivery-pilot-8938\n\n👇 Question: What’s your biggest struggle with LLM context windows or token limits? Let me know below!",
        "hookTopic": "Tokenization, Token IDs & Context Budgets (KVKJRdkH-B8)"
    },
    "output-formatting": {
        "pinnedComment": "📌 Need guaranteed JSON outputs with zero conversational filler like 'Sure! Here is the JSON:'? Use prefill assistant turns or tool schemas! 📦 Grab our zero-chatter JSON prompt templates in Delivery Pilot: 👉 https://www.skool.com/delivery-pilot-8938\n\n👇 Do you use prefilled assistant turns like '{' to force Claude to return valid JSON? Let us know below!",
        "hookTopic": "Strict Output Formatting & Zero-Chatter JSON"
    }
}

def main():
    if not DATA_FILE.exists():
        print(f"Error: {DATA_FILE} not found!")
        return

    with open(DATA_FILE, "r") as f:
        data = json.load(f)

    updated_count = 0
    for term in data.get("terms", []):
        t_id = term.get("id")
        if t_id in PINNED_COMMENTS:
            info = PINNED_COMMENTS[t_id]
            term["pinnedComment"] = info["pinnedComment"]
            term["pinnedCommentHookTopic"] = info["hookTopic"]
            updated_count += 1
        else:
            # Fallback high-converting template if any new term is added
            t_name = term.get("term", "AI Concept")
            term["pinnedComment"] = (
                f"📌 Mastered {t_name}? Don't let this exam trap trip you up on the Claude Certified Associate Exam! 🎯 "
                f"Grab the full 24-term interactive flashcard deck and blueprints inside Delivery Pilot: "
                f"👉 https://www.skool.com/delivery-pilot-8938\n\n"
                f"👇 What questions do you have about {t_name}? Drop your thoughts below!"
            )
            term["pinnedCommentHookTopic"] = f"{t_name} Exam Blueprint"
            updated_count += 1

    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

    print(f"✅ Successfully added high-converting pinned comments to all {updated_count} terms in {DATA_FILE}")

if __name__ == "__main__":
    main()
