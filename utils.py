import os
from pathlib import Path

def ensure_file_exists(filepath):
    if not Path(filepath).exists():
        raise FileNotFoundError(f"File not found: {filepath}")

def validate_api_key():
    if not os.environ.get('ANTHROPIC_API_KEY'):
        raise ValueError("ANTHROPIC_API_KEY environment variable not set")
