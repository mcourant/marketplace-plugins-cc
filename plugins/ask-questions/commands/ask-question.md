---
description: Manage the Ask Questions plugin to automatically append custom text to your prompts
parameters:
  - name: action
    description: Action to perform (enable, disable, status, set-prompt)
    required: true
  - name: text
    description: Custom prompt text (only for set-prompt action)
    required: false
---

# Ask Questions Plugin Manager

You are managing the Ask Questions plugin which automatically appends custom text to all user prompts.

## User Request

The user wants to: {{action}} {{text}}

## Available Actions

1. **enable** - Enable the plugin to automatically append text to prompts
2. **disable** - Disable the plugin
3. **status** - Show current plugin configuration
4. **set-prompt** - Change the custom prompt text (requires text parameter)

## Instructions

Based on the action requested:

### For "enable":
1. Read the current config from `~/.claude/config/ask-questions.json`
2. Set `enabled` to `true`
3. Write the updated config back
4. Confirm to the user that the plugin is now enabled

### For "disable":
1. Read the current config from `~/.claude/config/ask-questions.json`
2. Set `enabled` to `false`
3. Write the updated config back
4. Confirm to the user that the plugin is now disabled

### For "status":
1. Read the current config from `~/.claude/config/ask-questions.json`
2. Display:
   - Whether the plugin is enabled or disabled
   - The current custom prompt text
   - How to change settings

### For "set-prompt":
1. If no text parameter is provided, ask the user for the new prompt text
2. Read the current config from `~/.claude/config/ask-questions.json`
3. Update `customPrompt` with the new text
4. Write the updated config back
5. Confirm the change to the user

## Important Notes

- The config file is located at: `~/.claude/config/ask-questions.json` (global configuration)
- Always validate that the config file exists before reading (if not, run ./install-config.sh)
- Preserve the JSON structure when updating
- Use the Edit tool to modify the config file
- The plugin will automatically use the new settings on the next prompt

## Example Interactions

**Enable:**
```
/ask-question enable
```
Response: "Ask Questions plugin is now enabled. Your prompts will be automatically appended with: 'Pose des questions si nécessaires'"

**Disable:**
```
/ask-question disable
```
Response: "Ask Questions plugin is now disabled."

**Status:**
```
/ask-question status
```
Response: "Ask Questions plugin status:
- Enabled: true
- Custom prompt: 'Pose des questions si nécessaires'

To change settings:
- Enable: /ask-question enable
- Disable: /ask-question disable
- Change prompt: /ask-question set-prompt 'your new text'"

**Set Prompt:**
```
/ask-question set-prompt Please ask clarifying questions
```
Response: "Custom prompt updated to: 'Please ask clarifying questions'"
