# MiMoCode Adapter

> Integrate Aegis with MiMoCode.

---

# Overview

This adapter provides instructions for using Aegis with MiMoCode.

---

# Setup

## 1. Copy Instructions

Copy `AGENTS.md` to your project root.

```bash
cp adapters/mimocode/AGENTS.md ./AGENTS.md
```

## 2. Configure MiMoCode

Create or update `.mimocode/config.yaml`:

```yaml
agent:
  name: aegis-compliant
  rules:
    - AGENTS.md
```

## 3. Set Up Policies

Copy a policy file to your project:

```bash
cp policies/certus-policy.yaml ./project-policy.yaml
```

---

# Usage

MiMoCode will automatically:
1. Read AGENTS.md at session start
2. Follow ASES phases
3. Generate required artifacts
4. Pass quality gates

---

# Best Practices

| Practice | Description |
|----------|-------------|
| Plan before code | Use plan mode for complex tasks |
| Verify everything | Run tests before completion |
| Manage context | Clear between unrelated tasks |
| Use subagents | Delegate research tasks |

---

# References

- [ASES.md](../../aegis/ASES.md)
- [Agent Interaction Standards](../../aegis/agent-interaction-standards.md)
