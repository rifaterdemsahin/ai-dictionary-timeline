#!/usr/bin/env python3
"""
Azure Key Vault Secret Fetcher for Claude Associate Engine.
Retrieves generation API keys (ElevenLabs, Fal.ai, etc.) from Azure Key Vault
with fallback to environment variables and local .env files.
"""

import os
from pathlib import Path
from typing import Optional

# Load local .env if present
def load_dotenv():
    env_file = Path(__file__).resolve().parent.parent / '.env'
    if env_file.exists():
        with open(env_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    k, v = line.split('=', 1)
                    os.environ.setdefault(k.strip(), v.strip())

load_dotenv()

DEFAULT_VAULT_NAME = os.environ.get("AZURE_KEYVAULT_NAME", "dp-kv-deliverypilot")

def get_secret(secret_name: str, vault_name: Optional[str] = None) -> Optional[str]:
    """
    Retrieve a secret from Azure Key Vault using DefaultAzureCredential.
    Falls back to environment variables if Azure Key Vault is unreachable or unconfigured.
    
    Common secret names:
    - ELEVENLABS-API-KEY / ELEVEN_API_KEY
    - FAL-AI-KEY / FAL_KEY
    """
    vault = vault_name or DEFAULT_VAULT_NAME
    env_var_alias = secret_name.replace('-', '_').upper()
    
    # 1. Try Azure Key Vault via official SDK
    try:
        from azure.identity import DefaultAzureCredential
        from azure.keyvault.secrets import SecretClient

        vault_url = f"https://{vault}.vault.azure.net"
        credential = DefaultAzureCredential(exclude_interactive_browser_credential=False)
        client = SecretClient(vault_url=vault_url, credential=credential)
        
        # Secret names in Azure KV can use dashes
        fetched = client.get_secret(secret_name)
        if fetched and fetched.value:
            return fetched.value.strip()
    except Exception as e:
        # Fall back to local environment or .env
        pass

    # 2. Fallback to direct environment variables (e.g. ELEVENLABS_API_KEY or ELEVENLABS-API-KEY)
    if secret_name in os.environ:
        return os.environ[secret_name].strip()
    if env_var_alias in os.environ:
        return os.environ[env_var_alias].strip()

    return None

if __name__ == "__main__":
    import sys
    name = sys.argv[1] if len(sys.argv) > 1 else "ELEVENLABS-API-KEY"
    print(f"Resolving secret '{name}'...")
    val = get_secret(name)
    if val:
        masked = val[:4] + "..." + val[-4:] if len(val) > 8 else "***"
        print(f"✅ Resolved '{name}': {masked}")
    else:
        print(f"⚠️ Secret '{name}' not found in Azure Key Vault or environment.")
