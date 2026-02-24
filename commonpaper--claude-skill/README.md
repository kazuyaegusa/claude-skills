# Common Paper API Skill for Claude Code

A Claude Code skill that lets you query and manage contracts via the [Common Paper](https://commonpaper.com) REST API using natural language.

## What it does

Ask Claude Code about your contracts in plain English:

- **Count & search** — "How many signed NDAs do we have?" / "Do we have a contract with Acme?"
- **Send agreements** — "Send an NDA to jane@example.com from ben@company.com"
- **Manage agreements** — Void, reassign, resend signature emails
- **Financial queries** — "What's our largest CSA by deal value?"
- **Renewal tracking** — "Which contracts expire in the next 90 days?"
- **Signer lookups** — "Who signed the deal with Microsoft?"

Supports all Common Paper agreement types: NDA, CSA, DPA, PSA, Partnership, BAA, LOI, Software License, Design Partner, Pilot, and custom types.

## Installation

1. Clone this repo into your Claude Code skills directory:

```bash
git clone https://github.com/CommonPaper/claude-skill.git ~/.claude/skills/commonpaper
```

2. Add the skill to your `~/.claude/settings.json`:

```json
{
  "skills": ["commonpaper"]
}
```

3. Invoke it in Claude Code with `/commonpaper` followed by your question:

```
/commonpaper how many signed contracts do I have?
```

## Setup

On first use, Claude will ask for your Common Paper API token. You can generate one from your account's **Integrations** tab at [app.commonpaper.com](https://app.commonpaper.com).

The token is saved locally to `~/.claude/skills/commonpaper/cp-api-token` with `600` permissions (readable only by you). It is never displayed in chat output.

## Requirements

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) CLI
- A [Common Paper](https://commonpaper.com) account with API access
- `curl` and `jq` (pre-installed on most systems)

## Security

- API tokens are stored locally with restrictive file permissions
- Tokens are never displayed in chat output or passed as literal command-line arguments
- User inputs are sanitized before being used in API queries

## Known issues

- API tokens are scoped to an organization in your Common Paper account. If you can't retrieve agreements you expect to see, it's likely you were the recipient of that agreement and it's owned by another organization. We only have API support for agreements sent by the organization associated with the API token.

## License

MIT
