import json

# Optimize scripts to be tightly paced (under 48 words total = 3 words/sec @ 16 seconds)
with open('data/claude-associate-terms.json') as f:
    data = json.load(f)

# Compact, punchy 16-second scripts tailored for vertical video timing
compact_scripts = {
    "artifacts": {
        "hook": "Why does Claude put some code in a side window?",
        "conceptPart1": "That's an Artifact! It's for standalone, reusable code over 15 lines.",
        "conceptPart2": "Quick answers and 3-line scripts always stay inline in chat.",
        "ctaExamTip": "Exam Tip: Standalone files equal Artifacts, quick chat stays inline!"
    },
    "inline-markdown": {
        "hook": "Should Claude open an Artifact or stay in chat?",
        "conceptPart1": "Inline Markdown is for conversation flow, explanations, and quick terminal snippets.",
        "conceptPart2": "Creating an Artifact for short text interrupts user flow.",
        "ctaExamTip": "Exam Tip: If code doesn't need file export, keep it inline!"
    },
    "task-decomposition": {
        "hook": "Why does Claude fail on three complex jobs at once?",
        "conceptPart1": "Single prompts overload reasoning. Decomposing breaks tasks into numbered stages.",
        "conceptPart2": "Claude computes intermediate states, reducing compounding errors.",
        "ctaExamTip": "Exam Tip: Decompose complex prompts into sequential steps!"
    },
    "xml-tagging": {
        "hook": "What is Anthropic's top prompt structure recommendation?",
        "conceptPart1": "XML tags! Semantic tags separate instructions from untrusted user data.",
        "conceptPart2": "This eliminates prompt injection and ambiguous instruction parsing.",
        "ctaExamTip": "Exam Rule: Always wrap context and rules in XML tags!"
    },
    "system-prompts": {
        "hook": "Where should you lock in Claude's persona?",
        "conceptPart1": "In the System Prompt parameter! Not in the user message.",
        "conceptPart2": "It persists behavioral boundaries and guardrails across 50 turns.",
        "ctaExamTip": "Exam Tip: Use top-level 'system' parameter for persistent role definitions!"
    },
    "model-tier-tradeoffs": {
        "hook": "Haiku, Sonnet, or Opus: Which should you deploy?",
        "conceptPart1": "Haiku delivers low latency at minimum cost for routing.",
        "conceptPart2": "Sonnet 3.5 is the enterprise workhorse for code and tools.",
        "ctaExamTip": "Exam Tip: Never default to the largest model—match latency and cost!"
    },
    "context-window": {
        "hook": "Claude has 200,000 tokens—should you ever reset chat?",
        "conceptPart1": "Yes! Huge contexts increase latency and cost on every turn.",
        "conceptPart2": "Summarizing previous turns keeps responses fast and accurate.",
        "ctaExamTip": "Exam Tip: When conversation shifts, restart or summarize context!"
      },
    "prompt-caching": {
        "hook": "How do you slash Claude API costs by 90%?",
        "conceptPart1": "Prompt Caching! Set ephemeral cache breakpoints on static prefixes.",
        "conceptPart2": "Subsequent calls read memory, reducing latency by 85%.",
        "ctaExamTip": "Exam Tip: Minimum cache size is 1,024 tokens with cache_control!"
    },
    "tool-use-stop-reason": {
        "hook": "Does Claude actually run tools on your server?",
        "conceptPart1": "No! Claude returns stop_reason='tool_use' with structured JSON arguments.",
        "conceptPart2": "Your client application executes the tool and returns results.",
        "ctaExamTip": "Exam Golden Rule: Claude decides parameters; client code executes!"
    },
    "mcp-protocol": {
        "hook": "What is Anthropic's Model Context Protocol?",
        "conceptPart1": "MCP is an open standard connecting AI to local files and tools.",
        "conceptPart2": "It replaces custom glue code with universal client-server connectors.",
        "ctaExamTip": "Exam Tip: Think of MCP like USB-C for AI integrations!"
    },
    "claude-projects": {
        "hook": "Does Claude Projects fine-tune the base model?",
        "conceptPart1": "No! Projects does not train weights. It provides in-context grounding.",
        "conceptPart2": "Team instructions and uploaded docs guide chats dynamically.",
        "ctaExamTip": "Exam Tip: Projects provide in-context reference, never model fine-tuning!"
    },
    "chain-of-thought": {
        "hook": "Why do thinking tags make Claude smarter?",
        "conceptPart1": "Chain-of-Thought gives the model token space to calculate intermediate states.",
        "conceptPart2": "Reasoning inside thinking tags decouples internal scratchpads from output.",
        "ctaExamTip": "Exam Tip: Use Chain-of-Thought for multi-step logic and math!"
    },
    "few-shot-prompting": {
        "hook": "Tired of prompts that Claude still misinterprets?",
        "conceptPart1": "Switch to Few-Shot! Show 2 to 3 pristine input-output examples.",
        "conceptPart2": "Claude mirrors demonstrated schema and edge-case decisions.",
        "ctaExamTip": "Exam Tip: Few-shot examples beat paragraphs of instructions!"
    },
    "hallucination-mitigation": {
        "hook": "Does temperature 0 stop Claude from hallucinating?",
        "conceptPart1": "No! Temperature 0 makes outputs deterministic, not factual.",
        "conceptPart2": "Factual grounding requires negative constraints and source citations.",
        "ctaExamTip": "Exam Rule: Always give Claude an explicit 'I don't know' escape hatch!"
    },
    "human-in-the-loop": {
        "hook": "When should an AI agent NEVER act alone?",
        "conceptPart1": "When financial transfers, medical advice, or legal contracts are executed.",
        "conceptPart2": "Human-in-the-loop requires human approval before live actions.",
        "ctaExamTip": "Exam Tip: Place human verification between AI drafts and execution!"
    },
    "temperature": {
        "hook": "What happens when temperature is 0 versus 1?",
        "conceptPart1": "Temperature controls randomness. Low temperature enforces precision.",
        "conceptPart2": "High temperature drives creative divergence for brainstorming.",
        "ctaExamTip": "Exam Takeaway: For code and JSON extraction, set temperature near 0!"
    },
    "json-schema-tools": {
        "hook": "Why did Claude pass the wrong parameter to your tool?",
        "conceptPart1": "Your JSON Schema was vague! Claude relies on property descriptions.",
        "conceptPart2": "Always specify parameter types and required constraints explicitly.",
        "ctaExamTip": "Exam Tip: Rich parameter descriptions prevent broken tool calls!"
    },
    "research-mode": {
        "hook": "Does Claude know yesterday's breaking tech news?",
        "conceptPart1": "Not without tools! Claude's base knowledge is frozen at cut-off.",
        "conceptPart2": "Live search and connectors fetch real-time information dynamically.",
        "ctaExamTip": "Exam Tip: Distinguish frozen training data from live tool retrieval!"
    },
    "prompt-iteration": {
        "hook": "How do top AI engineers write production prompts?",
        "conceptPart1": "They test and iterate! They benchmark against edge-case test sets.",
        "conceptPart2": "When failures occur, they refine constraints and add examples.",
        "ctaExamTip": "Exam Tip: Prompt development is an empirical testing cycle!"
    },
    "evaluation-metrics": {
        "hook": "Did your prompt change make Claude better or worse?",
        "conceptPart1": "Don't guess—evaluate! Test against structured benchmark datasets.",
        "conceptPart2": "Measure accuracy, latency, and format compliance against golden answers.",
        "ctaExamTip": "Exam Rule: Always test prompt updates against eval datasets!"
    },
    "stakeholder-value-communication": {
        "hook": "What is the biggest mistake when pitching AI?",
        "conceptPart1": "Promising 100% perfection! LLMs are probabilistic, not deterministic.",
        "conceptPart2": "Highlight speed, but establish transparent error-mitigation policies.",
        "ctaExamTip": "Exam Tip: Pair AI capability demos with honest error boundaries!"
    },
    "task-alignment-model-fit": {
        "hook": "Are you wasting 80% of your AI cloud budget?",
        "conceptPart1": "Simple routing and filters belong on Haiku for low cost.",
        "conceptPart2": "Reserve Sonnet 3.5 for heavy code and reasoning.",
        "ctaExamTip": "Exam Rule: Route classification to Haiku and deep logic to Sonnet!"
    },
    "token-budgeting": {
        "hook": "What should your app do on HTTP 429 rate limit?",
        "conceptPart1": "429 means Rate Limit Exceeded! Never retry in a tight loop.",
        "conceptPart2": "Use exponential backoff with jitter and leverage prompt caching.",
        "ctaExamTip": "Exam Tip: Handle 429 errors using exponential backoff with jitter!"
    },
    "output-formatting": {
        "hook": "How do you stop Claude from saying 'Here is your JSON'?",
        "conceptPart1": "Prefill the assistant response! Ending turns with '{' forces raw JSON.",
        "conceptPart2": "Pair prefilling with strict JSON schemas to eliminate backticks.",
        "ctaExamTip": "Exam Tip: Use assistant prefill to enforce pure machine-readable JSON!"
    }
}

for term in data['terms']:
    tid = term['id']
    if tid in compact_scripts:
        term['video16sBlueprint'] = compact_scripts[tid]

with open('data/claude-associate-terms.json', 'w') as f:
    json.dump(data, f, indent=2)

print("Updated all 24 terms with strictly timed 16-second scripts (<45 words).")
