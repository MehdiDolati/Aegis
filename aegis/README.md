# Agent Software Engineering Standard (ASES)

> Engineering governance for AI-assisted software development.

---

# Overview

ASES defines how AI coding agents should participate in professional software development. It establishes requirements for artifacts, quality gates, traceability, documentation, verification, and maintainability.

---

# Quick Start

1. Read [ASES.md](ASES.md) — The master standard
2. Read [phases/](phases/) — Detailed phase requirements
3. Configure your project policy — See [policies/](../policies/)
4. Set up your agent adapter — See [adapters/](../adapters/)

---

# Documents

| Document | Description |
|----------|-------------|
| [ASES.md](ASES.md) | Master standard |
| [traceability.md](traceability.md) | Traceability requirements |
| [quality-gates.md](quality-gates.md) | Quality gate definitions |
| [artifacts.md](artifacts.md) | Required artifacts catalog |
| [testing-standards.md](testing-standards.md) | Testing requirements |
| [documentation-standards.md](documentation-standards.md) | Documentation requirements |
| [security-standards.md](security-standards.md) | Security requirements |
| [agent-interaction-standards.md](agent-interaction-standards.md) | Human-AI collaboration |
| [trustworthiness.md](trustworthiness.md) | Trustworthiness dimensions (arXiv:2602.06310) |
| [behavioral-rules.md](behavioral-rules.md) | Accumulated behavioral rules (arXiv:2607.13091) |
| [contracts.md](contracts.md) | Task-level contracts (arXiv:2603.15691) |
| [iso25010-mapping.md](iso25010-mapping.md) | ISO 25010 quality mapping (arXiv:2511.10271) |

---

# Phases

| Phase | Name | Key Artifact |
|-------|------|--------------|
| 1 | Specification | Feature Specification |
| 2 | Requirement Review | Validation Report |
| 3 | Impact Analysis | Impact Assessment |
| 4 | Solution Design | Implementation Plan |
| 5 | Controlled Implementation | Source Code + Tests |
| 6 | Verification | Test Results |
| 7 | Documentation | Updated Docs |
| 8 | Maintainability Audit | Maintainability Report |
| 9 | Technical Debt Review | Debt Report |
| 10 | Final Review | Implementation Report |

---

# Rules

Machine-readable rules are defined in [rules/](rules/). These rules can be validated by the Agent Governance Engine (AGE).

---

# Related

- [RFC-0001](../docs/rfcs/RFC-0001-project-vision.md) — Project Vision
- [RFC-0002](../docs/rfcs/RFC-0002-ases-standard.md) — ASES Proposal
- [Policies](../policies/) — Project-specific configurations
- [Adapters](../adapters/) — Agent integration guides
