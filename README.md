# Maxime's Claude Code Plugin Marketplace

A personal marketplace for Claude Code plugins, making it easy to discover and install custom productivity enhancements.

## Available Plugins

### Ask Questions
Automatically append a customizable prompt to all your messages to Claude, ensuring it asks clarifying questions instead of making assumptions.

**Features:**
- Automatically append custom text to every prompt
- Fully configurable - enable/disable and customize the text
- Simple slash commands for easy management
- Lightweight and non-intrusive

[Read more about Ask Questions →](./plugins/ask-questions/README-plugin.md)

## Installation

### Add This Marketplace

Add this marketplace to your Claude Code:
```
/plugin marketplace add https://github.com/mcourant/marketplace-plugins-cc
```

### Install Plugins

Once the marketplace is added, install any plugin:
```
/plugin install ask-questions
```

That's it! The plugin will automatically create its configuration in `~/.claude/config/ask-questions.json` on first use.

### Configuration

The configuration is stored globally in `~/.claude/config/ask-questions.json` and shared across all your projects.

You can customize it using the built-in command:
```
/ask-question set-prompt "Your custom prompt here"
```

Or edit the file directly:
```bash
nano ~/.claude/config/ask-questions.json
```

## Plugin List

| Plugin | Description | Category | Version |
|--------|-------------|----------|---------|
| ask-questions | Automatically append customizable prompts to messages | Productivity | 1.0.0 |

## Creating Your Own Plugins

Interested in creating your own Claude Code plugins? Check out the [official plugin documentation](https://docs.claude.com/en/docs/claude-code/plugins).

## Marketplace Structure

```
marketplace-plugins-cc/
├── .claude-plugin/
│   └── marketplace.json          # Marketplace manifest
├── plugins/
│   └── ask-questions/            # Individual plugin
│       ├── .claude-plugin/
│       │   └── plugin.json       # Plugin metadata
│       ├── commands/
│       │   └── ask-question.md   # Slash command
│       ├── hooks/
│       │   └── hooks.json        # Hook definitions
│       ├── scripts/
│       │   └── user-prompt-submit.py  # Hook script
│       ├── config.json           # Default config template
│       └── README-plugin.md
└── README.md

Global Configuration (auto-created on first use):
~/.claude/config/ask-questions.json  # User configuration (shared across projects)
```

## Contributing

Want to add your plugin to this marketplace? Feel free to submit a pull request!

## License

Individual plugins may have their own licenses. See each plugin's directory for details.

## Support

For issues with specific plugins, please check the plugin's individual documentation. For marketplace-related issues, open an issue on this repository.
