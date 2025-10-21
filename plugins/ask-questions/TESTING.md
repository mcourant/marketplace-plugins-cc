# Testing the Ask Questions Plugin

This guide explains how to test the plugin locally before installing it from the marketplace.

## Method 1: Test Locally (Development)

### Prerequisites
- Clone this repository
- Navigate to the marketplace root directory

### Installation Steps

1. **Navigate to the marketplace directory**:
   ```bash
   cd /path/to/marketplace-plugins-cc
   ```

2. **Install the plugin locally**:
   ```
   /plugin install ./plugins/ask-questions
   ```

3. **Verify installation**:
   ```
   /plugin list
   ```
   You should see `ask-questions` in the list.

4. **Test the slash command**:
   ```
   /ask-questions status
   ```
   This should show the current configuration.

5. **Test the hook**:
   - Submit any prompt to Claude
   - The plugin should automatically append your custom text
   - Check if "Pose des questions si nécessaires" appears in the context

### Uninstall (for testing updates)

```
/plugin uninstall ask-questions
```

Then reinstall to test your changes.

## Method 2: Install from Marketplace

### Add the Marketplace

```
/plugin marketplace add https://github.com/mcourant/marketplace-plugins-cc
```

### Install the Plugin

```
/plugin install ask-questions
```

## Testing Checklist

- [ ] Plugin installs without errors
- [ ] `/ask-questions status` command works
- [ ] `/ask-questions enable` command works
- [ ] `/ask-questions disable` command works
- [ ] `/ask-questions set-prompt "New text"` command works
- [ ] Hook appends text when enabled
- [ ] Hook doesn't append text when disabled
- [ ] Config persists between Claude Code sessions

## Troubleshooting

### Commands not showing up?

1. Verify the plugin is installed:
   ```
   /plugin list
   ```

2. Check if `commands/` directory exists at plugin root:
   ```bash
   ls -la ~/.claude/plugins/ask-questions/
   ```
   You should see a `commands/` directory (NOT inside `.claude-plugin/`).

### Hook not working?

1. Check the script is executable:
   ```bash
   ls -la ~/.claude/plugins/ask-questions/scripts/user-prompt-submit.py
   ```

2. Test the script manually:
   ```bash
   echo '{"prompt": "test"}' | ~/.claude/plugins/ask-questions/scripts/user-prompt-submit.py
   ```

3. Check the config file exists:
   ```bash
   cat ~/.claude/plugins/ask-questions/config.json
   ```

### Config not updating?

The config file is located at:
- Installed: `~/.claude/plugins/ask-questions/config.json`
- Local test: `./plugins/ask-questions/config.json`

Make sure you're editing the correct file for your installation method.

## Development Workflow

1. Make changes to the plugin files
2. Uninstall the plugin: `/plugin uninstall ask-questions`
3. Reinstall: `/plugin install ./plugins/ask-questions`
4. Test your changes
5. Repeat as needed

## Plugin Structure

The plugin should have this structure:

```
ask-questions/
├── .claude-plugin/
│   └── plugin.json          # Metadata only
├── commands/                 # Slash commands (auto-discovered)
│   └── ask-questions.md
├── scripts/                  # Hook scripts
│   └── user-prompt-submit.py
├── config.json              # User configuration
├── README-plugin.md
└── LICENSE
```

**Important**: `commands/`, `scripts/`, and `config.json` MUST be at the plugin root, NOT inside `.claude-plugin/`.

## Debugging Tips

### Enable verbose logging

Check Claude Code's logs for plugin-related errors:
```bash
tail -f ~/.claude/logs/main.log
```

### Test the hook script directly

```bash
cd plugins/ask-questions
export CLAUDE_PLUGIN_ROOT=$(pwd)
echo '{"prompt": "test prompt"}' | python3 scripts/user-prompt-submit.py
```

Expected output:
```json
{"hookSpecificOutput": {"additionalContext": "\n\nPose des questions si nécessaires"}}
```

## Need Help?

If you encounter issues:
1. Check the main [README](./README-plugin.md)
2. Verify your plugin structure matches the expected layout
3. Check Claude Code version compatibility
4. Open an issue on GitHub with details about your setup
