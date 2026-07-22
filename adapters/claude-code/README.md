# Claude Code Adapter

> Integrate Aegis with Claude Code.

---

# Overview

This adapter provides instructions for using Aegis with Claude Code.

---

# Setup

## 1. Copy Instructions

Copy `CLAUDE.md` to your project root.

```bash
cp adapters/claude-code/CLAUDE.md ./CLAUDE.md
```

## 2. Configure Claude Code

Claude Code automatically reads `CLAUDE.md` at session start.

## 3. Set Up Policies

Copy a policy file to your project:

```bash
cp policies/certus-policy.yaml ./project-policy.yaml
```

---

# Usage

Claude Code will automatically:
1. Read CLAUDE.md at session start
2. Follow ASES phases
3. Generate required artifacts
4. Pass quality gates

---

# Best Practices

| Practice | Description |
|----------|-------------|
| Use plan mode | Explore and plan before implementing |
| Provide context | Reference files and patterns |
| Verify with tests | Run tests before completion |
| Use subagents | Delegate research and review |
| Manage context | Clear between tasks |

---

# References

- [ASES.md](../../aegis/ASES.md)
- [Agent Interaction Standards](../../aegis/agent-interaction-standards.md)
- Claude Code Best Practices (Anthropic)
