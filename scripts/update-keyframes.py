import json

STYLE_ANCHOR = "3D isometric glassmorphic interface, Anthropic terracotta accents (#CC785C) and deep obsidian (#18181B) metallic chassis, clean octane render, studio lighting, hyper-realistic, vertical 9:16 aspect ratio"

with open('data/claude-associate-terms.json', 'r') as f:
    data = json.load(f)

for term in data['terms']:
    tid = term['id']
    title = term['term']
    domain = term['domain']
    hook = term['video16sBlueprint']['hook']
    concept = term['video16sBlueprint']['conceptPart1']
    example = term['video16sBlueprint']['conceptPart2']
    tip = term['video16sBlueprint']['ctaExamTip']

    # Initial frame prompts: starting metaphor / hook visual state
    initial_prompt = f"Initial state representing '{title}' in Claude AI architecture: {hook}. Glowing terracotta UI terminal wireframe, sleek dark obsidian console, floating translucent panels displaying Anthropic iconography, {STYLE_ANCHOR}"

    # End frame prompts: resolved architectural motion / exam takeaway state
    end_prompt = f"Resolved target state for '{title}' concept: {example}. Translucent illuminated 3D glass data nodes connecting into a glowing gold Anthropic verification badge, crystal-clear code pathways, {tip}, {STYLE_ANCHOR}"

    camera_motion = "Cinematic slow forward dolly zoom with subtle 15-degree lateral orbit, smooth depth-of-field transition focusing on illuminated data flows"

    term['keyframeVisualSpec'] = {
        "initialFramePrompt": initial_prompt,
        "endFramePrompt": end_prompt,
        "cameraMotion": camera_motion,
        "styleAnchor": STYLE_ANCHOR
    }

with open('data/claude-associate-terms.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"Successfully added keyframeVisualSpec to all {len(data['terms'])} terms.")
