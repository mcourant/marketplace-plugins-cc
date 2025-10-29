#!/usr/bin/env python3
"""
User Prompt Submit Hook for Ask Questions Plugin
Automatically appends a customizable prompt to all user messages
"""

import json
import os
import sys
from pathlib import Path


def load_config():
    """Load the plugin configuration from global ~/.claude/config/ask-questions.json"""
    # Always read from global config location
    config_path = Path.home() / '.claude' / 'config' / 'ask-questions.json'

    # Default configuration
    default_config = {
        "enabled": True,
        "customPrompt": "Pose des questions si nécessaires"
    }

    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        # Create config file with defaults if it doesn't exist
        config_dir = config_path.parent
        config_dir.mkdir(parents=True, exist_ok=True)

        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(default_config, f, indent=2)

        return default_config
    except json.JSONDecodeError:
        # Invalid JSON, use defaults
        return default_config


def main():
    """Main hook execution"""
    # Read input from stdin (contains the user prompt and metadata)
    try:
        input_data = json.loads(sys.stdin.read())
    except json.JSONDecodeError:
        # If we can't parse input, just allow the prompt through
        sys.exit(0)

    # Load plugin configuration
    config = load_config()

    # If plugin is disabled, just allow the prompt through without modification
    if not config.get('enabled', True):
        sys.stderr.write("[ask-questions: OFF]\n")
        sys.stderr.flush()
        sys.exit(0)

    # Get the custom prompt text
    custom_prompt = config.get('customPrompt', 'Pose des questions si nécessaires')

    # Log status to stderr
    sys.stderr.write(f"[ask-questions: ON] Ajout: \"{custom_prompt}\"\n")
    sys.stderr.flush()

    # Return JSON output with additionalContext to append the text
    output = {
        "hookSpecificOutput": {
            "additionalContext": f"\n\n{custom_prompt}"
        }
    }

    print(json.dumps(output))
    sys.exit(0)


if __name__ == '__main__':
    main()
