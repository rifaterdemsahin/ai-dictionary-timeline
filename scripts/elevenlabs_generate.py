#!/usr/bin/env python3
"""
ElevenLabs Voiceover Generation Pipeline for Claude Associate Engine.
Pulls API secrets securely from Azure Key Vault (dp-kv-deliverypilot).
Synthesizes professional narration with word-level timestamps for Remotion kinetic typography.

Selected Voice:
- Voice: Brian (nPczCjzI2devNBz1zQrb) - Authoritative, deep baritone tech educator
- Model: eleven_turbo_v2_5 (sub-120ms latency, high acoustic clarity)
"""

import json
import os
import sys
import base64
import urllib.request
import urllib.error
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR / "scripts"))
from azure_vault import get_secret

OUTPUT_DIR = ROOT_DIR / "outputs" / "audio"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Selected Voice Configurations
VOICE_BRIAN_ID = "nPczCjzI2devNBz1zQrb"     # Selected Primary Voice (Authoritative Tech Educator)
VOICE_RACHEL_ID = "21m00Tcm4TlvDq8ikWAM"    # Dual-Track Secondary Voice (Clear Conversational)
SELECTED_MODEL = "eleven_turbo_v2_5"

VOICE_SETTINGS = {
    "stability": 0.45,
    "similarity_boost": 0.85,
    "style": 0.10,
    "use_speaker_boost": True
}

def get_elevenlabs_client():
    """Retrieve API key from Azure Key Vault or fallback and instantiate ElevenLabs client"""
    api_key = get_secret("ELEVENLABS-API-KEY") or get_secret("ELEVEN_API_KEY")
    if not api_key:
        return None, None

    try:
        from elevenlabs.client import ElevenLabs
        client = ElevenLabs(api_key=api_key)
        return client, api_key
    except ImportError:
        return None, api_key

def synthesize_with_timestamps(text: str, voice_id: str = VOICE_BRIAN_ID, output_prefix: str = "voiceover"):
    """
    Synthesizes speech using ElevenLabs with word-level character alignment.
    Saves:
      1. outputs/audio/{output_prefix}.mp3 (Audio stream)
      2. outputs/audio/{output_prefix}_timestamps.json (Word/character timing alignment)
    """
    client, api_key = get_elevenlabs_client()
    
    if not api_key:
        print("⚠️ Warning: ELEVENLABS-API-KEY not resolved from Azure Key Vault or environment.")
        print("   Running in mock/simulation mode for validation.")
        return generate_mock_voiceover(text, output_prefix)

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}/with-timestamps"
    payload = {
        "text": text,
        "model_id": SELECTED_MODEL,
        "voice_settings": VOICE_SETTINGS
    }

    headers = {
        "xi-api-key": api_key,
        "Content-Type": "application/json"
    }

    req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers=headers)

    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            audio_bytes = base64.b64decode(data.get("audio_base64", ""))
            alignment = data.get("alignment", {})

            mp3_path = OUTPUT_DIR / f"{output_prefix}.mp3"
            json_path = OUTPUT_DIR / f"{output_prefix}_timestamps.json"

            with open(mp3_path, "wb") as f:
                f.write(audio_bytes)

            with open(json_path, "w", encoding="utf-8") as f:
                json.dump({
                    "voice_id": voice_id,
                    "voice_name": "Brian",
                    "model": SELECTED_MODEL,
                    "text": text,
                    "duration_seconds": alignment.get("character_end_times_seconds", [15.0])[-1] if alignment.get("character_end_times_seconds") else 15.0,
                    "alignment": alignment
                }, f, indent=2)

            print(f"✅ Voiceover saved: {mp3_path} ({len(audio_bytes)} bytes)")
            print(f"✅ Subtitle alignment saved: {json_path}")
            return str(mp3_path), str(json_path)

    except urllib.error.HTTPError as e:
        err = e.read().decode('utf-8')
        print(f"❌ ElevenLabs API Error ({e.code}): {err}")
        return generate_mock_voiceover(text, output_prefix)

def generate_mock_voiceover(text: str, output_prefix: str):
    """Simulate audio and word-level alignment for local builds without live API keys"""
    words = text.split()
    chars = list(text)
    total_duration = min(15.5, max(12.0, len(words) * 0.35))
    step = total_duration / max(1, len(chars))

    mock_alignment = {
        "characters": chars,
        "character_start_times_seconds": [round(i * step, 3) for i in range(len(chars))],
        "character_end_times_seconds": [round((i + 1) * step, 3) for i in range(len(chars))]
    }

    mp3_path = OUTPUT_DIR / f"{output_prefix}.mp3"
    json_path = OUTPUT_DIR / f"{output_prefix}_timestamps.json"

    # Write placeholder MP3 frame
    with open(mp3_path, "wb") as f:
        f.write(b"ID3\x04\x00\x00\x00\x00\x00#TSSE\x00\x00\x00\x0f\x00\x00\x03Lavf58.76.100\x00\xff\xfb\x90\x44")

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump({
            "voice_id": VOICE_BRIAN_ID,
            "voice_name": "Brian",
            "model": SELECTED_MODEL,
            "simulated": True,
            "text": text,
            "duration_seconds": total_duration,
            "alignment": mock_alignment
        }, f, indent=2)

    print(f"⚡ [Simulated] Audio placeholder created: {mp3_path}")
    print(f"⚡ [Simulated] Remotion timestamp alignment created: {json_path}")
    return str(mp3_path), str(json_path)

def batch_generate_curriculum(limit: int = 1):
    """Generate voiceovers for terms in data/claude-associate-terms.json"""
    terms_file = ROOT_DIR / "data" / "claude-associate-terms.json"
    if not terms_file.exists():
        print(f"❌ Terms file not found: {terms_file}")
        return

    with open(terms_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    terms = data.get("terms", []) if isinstance(data, dict) else data

    print(f"\n🎙️ Starting ElevenLabs Voiceover Generation (Limit: {limit}/{len(terms)})")
    print(f"   Selected Voice: Brian ({VOICE_BRIAN_ID}) | Engine: {SELECTED_MODEL}")
    print(f"   Azure Key Vault: dp-kv-deliverypilot\n")

    for i, term in enumerate(terms[:limit]):
        term_id = term.get("id", f"term_{i+1}")
        # Build 16-second full narration from video16sBlueprint or Tell-Show-Do-Apply
        blueprint = term.get("video16sBlueprint", {})
        narration = f"{blueprint.get('hook', '')} {blueprint.get('body', '')} {blueprint.get('cta', '')}".strip()
        if not narration:
            narration = term.get("shortDefinition", "") or term.get("definition", "")

        print(f"[{i+1}/{limit}] Generating audio for: {term.get('term')} ({term_id})")
        synthesize_with_timestamps(narration, voice_id=VOICE_BRIAN_ID, output_prefix=f"{term_id}_brian")

if __name__ == "__main__":
    count = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else 1
    batch_generate_curriculum(limit=count)
