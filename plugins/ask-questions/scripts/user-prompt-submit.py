#!/usr/bin/env python3
"""
User Prompt Submit Hook for Ask Questions Plugin
Automatically appends a customizable prompt to all user messages
"""

import json
import os
import sys
from pathlib import Path


def get_plugin_root():
    """Get the plugin root directory from environment variable"""
    return os.environ.get('CLAUDE_PLUGIN_ROOT', '')


def load_config():
    """Load the plugin configuration"""
    plugin_root = get_plugin_root()
    if not plugin_root:
        # Fallback: try to find config relative to this script
        script_dir = Path(__file__).parent.parent
        config_path = script_dir / 'config.json'
    else:
        config_path = Path(plugin_root) / 'config.json'

    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        # Default config if file doesn't exist
        return {
            "enabled": True,
            "customPrompt": "Pose des questions si nécessaires"
        }
    except json.JSONDecodeError:
        # Invalid JSON, use defaults
        return {
            "enabled": True,
            "customPrompt": "Pose des questions si nécessaires"
        }


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
        sys.exit(0)

    # Get the custom prompt text
    custom_prompt = config.get('customPrompt', 'Pose des questions si nécessaires')

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
