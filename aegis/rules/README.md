# ASES Rules

> Machine-readable rules for the Agent Software Engineering Standard.

---

# Overview

Rules define what must be done at each phase of the engineering lifecycle. They are machine-readable and can be validated by the Agent Governance Engine (AGE).

---

# Rule Files

| File | Phase | Description |
|------|-------|-------------|
| [specification-rules.yaml](specification-rules.yaml) | Phase 1 | Specification requirements |
| [design-rules.yaml](design-rules.yaml) | Phase 2-4 | Design and review requirements |
| [implementation-rules.yaml](implementation-rules.yaml) | Phase 5 | Implementation requirements |
| [verification-rules.yaml](verification-rules.yaml) | Phase 6 | Verification requirements |
| [documentation-rules.yaml](documentation-rules.yaml) | Phase 7 | Documentation requirements |
| [maintainability-rules.yaml](maintainability-rules.yaml) | Phase 8 | Maintainability requirements |
| [traceability-rules.yaml](traceability-rules.yaml) | Cross-phase | Traceability requirements |
| [security-rules.yaml](security-rules.yaml) | Cross-phase | Security requirements |

---

# Rule Structure

Every rule has:

| Field | Description |
|-------|-------------|
| id | Unique identifier |
| title | Short description |
| description | Detailed explanation |
| severity | error / warning / info |
| phase | Applicable SDLC phase |
| gate | Associated quality gate |
| evidence | Required evidence |
| exceptions | When rule can be skipped |

---

# Usage

Rules can be used to:
1. Validate compliance with ASES
2. Generate checklists for agents
3. Build automated governance tools
4. Create project-specific policies

---

# References

- [ASES.md](../ASES.md) — Master standard
- [Schemas](../../schemas/) — Rule schema
