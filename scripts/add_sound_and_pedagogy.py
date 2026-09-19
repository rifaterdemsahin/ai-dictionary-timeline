#!/usr/bin/env python3
"""
Enrich all 24 Claude Associate terms with:
1. Tell-Show-Do-Apply Pedagogical Design Framework
2. Sound Effects (SFX) Track with timing, decibel levels, and ducking specs
3. Dynamic Visual Transitions Timeline for Remotion composition
"""

import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "claude-associate-terms.json"

def enrich_terms():
    if not DATA_FILE.exists():
        print(f"Error: {DATA_FILE} not found!")
        return

    with open(DATA_FILE, "r") as f:
        data = json.load(f)

    terms = data.get("terms", [])
    for t in terms:
        vb = t.get("video16sBlueprint", {})
        
        # 1. Tell-Show-Do-Apply Pedagogical Architecture
        t["tellShowDoApply"] = {
            "framework": "Tell-Show-Do-Apply (Micro-learning Mastery)",
            "tell": {
                "phase": "TELL",
                "timecode": "00:00 - 00:04",
                "title": "State the Rule & Hook",
                "content": vb.get("hook", ""),
                "pedagogyObjective": "Break viewer trance, state the core concept thesis, and prime cognitive curiosity."
            },
            "show": {
                "phase": "SHOW",
                "timecode": "00:04 - 00:08",
                "title": "Visual Architecture Demonstration",
                "content": vb.get("conceptPart1", ""),
                "pedagogyObjective": "Ground the abstract concept in visible 3D system architecture and UI state transitions."
            },
            "do": {
                "phase": "DO",
                "timecode": "00:08 - 00:12",
                "title": "Hands-on Scenario & Exam Trap",
                "content": vb.get("conceptPart2", ""),
                "pedagogyObjective": "Confront the learner with a realistic misapplication scenario or high-failure exam trap."
            },
            "apply": {
                "phase": "APPLY",
                "timecode": "00:12 - 00:16",
                "title": "Definitive Rule & Skool CTA",
                "content": vb.get("ctaExamTip", ""),
                "pedagogyObjective": "Deliver the test-day recall trigger and channel learner to Delivery Pilot for interactive practice."
            }
        }

        # 2. Sound Effects & Transitions Specifications for Remotion
        t["soundAndTransitions"] = {
            "sfxTimeline": [
                {
                    "timecode": "00:00.2",
                    "phase": "TELL",
                    "sfxName": "Sub-Bass Drop + Fast Whoosh",
                    "category": "Hook Impact",
                    "targetVolumeDb": -6.0,
                    "duckingRule": "Punches on initial visual pop before primary voiceover begins"
                },
                {
                    "timecode": "00:04.1",
                    "phase": "SHOW",
                    "sfxName": "Hologram UI Chirp & Data Stream Hum",
                    "category": "Visual Reveal",
                    "targetVolumeDb": -14.0,
                    "duckingRule": "Side-chained dynamically behind ElevenLabs voiceover (-12dB duck)"
                },
                {
                    "timecode": "00:08.3",
                    "phase": "DO",
                    "sfxName": "Alert Ping & Low Frequency Tension Sweep",
                    "category": "Exam Trap Warning",
                    "targetVolumeDb": -9.0,
                    "duckingRule": "Sharp stinger punctuates the negative trap reveal"
                },
                {
                    "timecode": "00:13.0",
                    "phase": "APPLY",
                    "sfxName": "Gold Certification Chime + Sub Hit",
                    "category": "Victory & Resolution",
                    "targetVolumeDb": -7.0,
                    "duckingRule": "Resonant metallic sustain underneath final Skool community CTA callout"
                }
            ],
            "transitionsTimeline": [
                {
                    "timecode": "00:00 - 00:04",
                    "phase": "TELL",
                    "transitionType": "Kinetic Snap Zoom",
                    "cameraDirective": "1.2x scale snap with micro camera shake on first spoken hook keyword"
                },
                {
                    "timecode": "00:04 - 00:08",
                    "phase": "SHOW",
                    "transitionType": "Kling Morph & Lateral Whip Pan",
                    "cameraDirective": "15-degree lateral orbit smoothly blurring UI wireframe into illuminated 3D glass nodes"
                },
                {
                    "timecode": "00:08 - 00:12",
                    "phase": "DO",
                    "transitionType": "Split-Screen Comparison Wipe",
                    "cameraDirective": "Fast horizontal wipe cutting from production success flow to red-tinted failure trap"
                },
                {
                    "timecode": "00:12 - 00:16",
                    "phase": "APPLY",
                    "transitionType": "Cross-Dissolve & Badge Flare",
                    "cameraDirective": "Cinematic slow pull-back revealing Anthropic Terracotta badge and persistent Skool link overlay"
                }
            ],
            "remotionAudioMixConfig": {
                "sampleRate": 48000,
                "voiceoverGainDb": 0.0,
                "sfxMasterGainDb": -3.5,
                "musicBedGainDb": -22.0,
                "autoDuckingDb": -14.0,
                "crossfadeDurationMs": 150
            }
        }

    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

    print(f"✅ Successfully enriched {len(terms)} terms with Tell-Show-Do-Apply and Sound/Transitions specifications in {DATA_FILE}")

if __name__ == "__main__":
    enrich_terms()
