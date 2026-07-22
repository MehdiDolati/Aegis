# Cursor Adapter

> Integrate Aegis with Cursor.

---

# Overview

This adapter provides instructions for using Aegis with Cursor.

---

# Setup

## 1. Copy Rules

Copy `.cursorrules` to your project root.

```bash
cp adapters/cursor/.cursorrules ./.cursorrules
```

## 2. Configure Cursor

Cursor automatically reads `.cursorrules` at session start.

## 3. Set Up Policies

Copy a policy file to your project:

```bash
cp policies/certus-policy.yaml ./project-policy.yaml
```

---

# Usage

Cursor will automatically:
1. Read .cursorrules at session start
2. Follow ASES phases
3. Generate required artifacts
4. Pass quality gates

---

# Best Practices

| Practice | Description |
|----------|-------------|
| Use Composer | For complex multi-file changes |
| Provide context | Reference files and patterns |
| Verify with tests | Run tests before completion |

---

# References

- [ASES.md](../../aegis/ASES.md)
- [Agent Interaction Standards](../../aegis/agent-interaction-standards.md)
