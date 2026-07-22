# Codex Adapter

> Integrate Aegis with Codex.

---

# Overview

This adapter provides instructions for using Aegis with Codex.

---

# Setup

## 1. Copy Instructions

Copy `CODEX.md` to your project root.

```bash
cp adapters/codex/CODEX.md ./CODEX.md
```

## 2. Configure Codex

Configure Codex to read the instructions file.

## 3. Set Up Policies

Copy a policy file to your project:

```bash
cp policies/certus-policy.yaml ./project-policy.yaml
```

---

# Usage

Codex will follow:
1. ASES phases
2. Required artifacts
3. Quality gates

---

# Best Practices

| Practice | Description |
|----------|-------------|
| Provide context | Reference files and patterns |
| Verify with tests | Run tests before completion |
| Document changes | Update documentation |

---

# References

- [ASES.md](../../aegis/ASES.md)
- [Agent Interaction Standards](../../aegis/agent-interaction-standards.md)
