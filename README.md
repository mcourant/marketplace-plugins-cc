# Ask Questions - Claude Code Plugin

A Claude Code plugin that automatically appends a customizable prompt (like "Ask questions if needed") to all your messages to Claude. This helps ensure Claude asks clarifying questions instead of making assumptions.

## Features

- Automatically append custom text to every prompt you submit
- Fully configurable - enable/disable and customize the text
- Simple slash commands for easy management
- Lightweight and non-intrusive

## Installation

### Option 1: Install from Marketplace (Recommended)

1. Add the marketplace to Claude Code:
   ```
   /plugin marketplace add https://github.com/yourusername/claude-plugins-marketplace
   ```

2. Install the plugin:
   ```
   /plugin install ask-questions
   ```

### Option 2: Local Installation (for testing)

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/ask-questions-plugin.git
   cd ask-questions-plugin
   ```

2. Install the plugin locally in Claude Code:
   ```
   /plugin install .
   ```

## Usage

### Basic Commands

The plugin provides the `/ask-questions` command with the following actions:

#### Check Status
```
/ask-questions status
```
Shows whether the plugin is enabled and what text is being appended.

#### Enable Plugin
```
/ask-questions enable
```
Enables the plugin to start appending text to your prompts.

#### Disable Plugin
```
/ask-questions disable
```
Disables the plugin temporarily without uninstalling it.

#### Change Custom Prompt
```
/ask-questions set-prompt Your custom text here
```
Updates the text that gets appended to your prompts.

### Examples

**Example 1: Using the default prompt**
```
/ask-questions status
```
Output: Plugin is enabled with prompt: "Pose des questions si nécessaires"

**Example 2: Customizing the prompt**
```
/ask-questions set-prompt Please ask clarifying questions before proceeding
```

**Example 3: Temporarily disabling**
```
/ask-questions disable
```
Your prompts will be sent without any additional text until you re-enable.

## How It Works

The plugin uses Claude Code's `UserPromptSubmit` hook to automatically append text to every prompt you submit:

1. When you submit a prompt, the hook is triggered
2. The plugin reads your configuration from `.claude-plugin/config.json`
3. If enabled, it appends your custom text to the prompt
4. Claude receives your original prompt plus the additional context

## Configuration

The plugin's configuration is stored in `.claude-plugin/config.json`:

```json
{
  "enabled": true,
  "customPrompt": "Pose des questions si nécessaires"
}
```

You can modify this file directly or use the `/ask-questions` commands.

## Use Cases

- **Encourage exploration**: Add "Ask questions if you need more context"
- **Prevent assumptions**: Add "Please confirm before making changes"
- **Improve accuracy**: Add "Ask clarifying questions to ensure you understand correctly"
- **Project-specific reminders**: Add custom instructions relevant to your workflow

## Uninstalling

To remove the plugin:
```
/plugin uninstall ask-questions
```

## Development

### Project Structure
```
ask-questions-plugin/
├── .claude-plugin/
│   ├── plugin.json          # Plugin manifest
│   ├── config.json          # User configuration
│   ├── commands/
│   │   └── ask-questions.md # Slash command definitions
│   └── scripts/
│       └── user-prompt-submit.py  # Hook implementation
└── README.md
```

### Local Testing

1. Make changes to the plugin files
2. Reinstall the plugin:
   ```
   /plugin install .
   ```
3. Test your changes by submitting prompts

### Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

MIT License - see LICENSE file for details

## Credits

Created to make Claude Code conversations more interactive and ensure proper clarification before action.

## Troubleshooting

### Plugin not working?

1. Check if it's enabled:
   ```
   /ask-questions status
   ```

2. Verify the plugin is installed:
   ```
   /plugin list
   ```

3. Check the configuration file exists:
   ```bash
   cat .claude-plugin/config.json
   ```

4. Reinstall the plugin:
   ```
   /plugin uninstall ask-questions
   /plugin install ask-questions
   ```

### Need help?

Open an issue on GitHub with:
- Your Claude Code version
- Steps to reproduce the problem
- Expected vs actual behavior
