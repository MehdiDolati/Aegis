# Aegis Schemas

> Machine-readable definitions for Aegis components.

---

# Overview

Schemas define the structure of Aegis components in YAML format. These schemas enable:
- Validation of rules and policies
- Tool integration
- Automated governance

---

# Schemas

| Schema | Description |
|--------|-------------|
| [rule.schema.yaml](rule.schema.yaml) | Rule definition |
| [policy.schema.yaml](policy.schema.yaml) | Policy definition |
| [gate.schema.yaml](gate.schema.yaml) | Quality gate definition |
| [artifact.schema.yaml](artifact.schema.yaml) | Artifact definition |
| [traceability.schema.yaml](traceability.schema.yaml) | Traceability matrix |

---

# Usage

Schemas can be used to:
1. Validate YAML files against the schema
2. Generate documentation from schemas
3. Build tooling for governance enforcement
4. Ensure consistency across projects

---

# References

- [ASES.md](../aegis/ASES.md) — Master standard
- [Rules](../aegis/rules/) — Rule definitions
- [Policies](../policies/) — Policy definitions
