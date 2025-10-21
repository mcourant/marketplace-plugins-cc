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
│       │   ├── plugin.json
│       │   ├── config.json
│       │   ├── commands/
│       │   └── scripts/
│       └── README-plugin.md
└── README.md
```

## Contributing

Want to add your plugin to this marketplace? Feel free to submit a pull request!

## License

Individual plugins may have their own licenses. See each plugin's directory for details.

## Support

For issues with specific plugins, please check the plugin's individual documentation. For marketplace-related issues, open an issue on this repository.
