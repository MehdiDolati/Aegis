# Aegis

**Engineering Governance for AI Software Development**

> Building software with AI agents requires more than code generation.
> It requires engineering discipline.

Aegis is an open standard and governance framework designed to ensure that AI coding agents produce software that is not only functional, but also maintainable, verifiable, traceable, and production-ready.

Unlike traditional coding assistants, Aegis focuses on the entire software engineering lifecycle rather than code generation alone.

---

# Vision

AI agents are rapidly becoming capable software developers.

However, modern AI coding tools still lack a consistent engineering process.

Most agents can write code.

Very few can consistently produce:

* Complete feature specifications
* Traceable implementations
* Reliable automated tests
* Synchronized documentation
* Architecture compliance
* Technical debt reporting
* Long-term maintainability

Aegis exists to define that engineering process.

---

# Mission

Create an open, vendor-neutral engineering standard that enables AI agents to participate in professional software development with the same—or higher—quality standards expected from experienced engineering teams.

---

# Quick Start

1. Read the [ASES Standard](aegis/ASES.md)
2. Choose a [policy](policies/) for your project
3. Set up an [adapter](adapters/) for your AI agent
4. Start following the 10-phase lifecycle

---

# Project Components

## ASES

**Agent Software Engineering Standard**

The core standard defining how AI agents should participate in software engineering.

| Document | Description |
|----------|-------------|
| [ASES.md](aegis/ASES.md) | Master standard |
| [Traceability](aegis/traceability.md) | Traceability requirements |
| [Quality Gates](aegis/quality-gates.md) | Gate definitions |
| [Artifacts](aegis/artifacts.md) | Required artifacts |
| [Testing Standards](aegis/testing-standards.md) | Testing requirements |
| [Documentation Standards](aegis/documentation-standards.md) | Documentation requirements |
| [Security Standards](aegis/security-standards.md) | Security requirements |
| [Agent Interaction](aegis/agent-interaction-standards.md) | Human-AI collaboration |

### Phases

| Phase | Name | Document |
|-------|------|----------|
| 1 | Specification | [01-specification.md](aegis/phases/01-specification.md) |
| 2 | Requirement Review | [02-requirement-review.md](aegis/phases/02-requirement-review.md) |
| 3 | Impact Analysis | [03-impact-analysis.md](aegis/phases/03-impact-analysis.md) |
| 4 | Solution Design | [04-solution-design.md](aegis/phases/04-solution-design.md) |
| 5 | Controlled Implementation | [05-controlled-implementation.md](aegis/phases/05-controlled-implementation.md) |
| 6 | Verification | [06-verification.md](aegis/phases/06-verification.md) |
| 7 | Documentation | [07-documentation.md](aegis/phases/07-documentation.md) |
| 8 | Maintainability Audit | [08-maintainability-audit.md](aegis/phases/08-maintainability-audit.md) |
| 9 | Technical Debt Review | [09-technical-debt-review.md](aegis/phases/09-technical-debt-review.md) |
| 10 | Final Review | [10-final-review.md](aegis/phases/10-final-review.md) |

### Rules

Machine-readable rules for automated validation:

| File | Phase |
|------|-------|
| [specification-rules.yaml](aegis/rules/specification-rules.yaml) | Phase 1 |
| [design-rules.yaml](aegis/rules/design-rules.yaml) | Phase 2-4 |
| [implementation-rules.yaml](aegis/rules/implementation-rules.yaml) | Phase 5 |
| [verification-rules.yaml](aegis/rules/verification-rules.yaml) | Phase 6 |
| [documentation-rules.yaml](aegis/rules/documentation-rules.yaml) | Phase 7 |
| [maintainability-rules.yaml](aegis/rules/maintainability-rules.yaml) | Phase 8 |
| [traceability-rules.yaml](aegis/rules/traceability-rules.yaml) | Cross-phase |
| [security-rules.yaml](aegis/rules/security-rules.yaml) | Cross-phase |

---

## AGE

**Agent Governance Engine**

Executes ASES automatically. Currently in planning phase.

| Document | Description |
|----------|-------------|
| [README](age/README.md) | Overview and roadmap |
| [Architecture](age/architecture.md) | Planned architecture |

---

## Schemas

Machine-readable definitions for Aegis components.

| Schema | Description |
|--------|-------------|
| [rule.schema.yaml](schemas/rule.schema.yaml) | Rule definition |
| [policy.schema.yaml](schemas/policy.schema.yaml) | Policy definition |
| [gate.schema.yaml](schemas/gate.schema.yaml) | Quality gate |
| [artifact.schema.yaml](schemas/artifact.schema.yaml) | Artifact definition |
| [traceability.schema.yaml](schemas/traceability.schema.yaml) | Traceability matrix |

---

## Policies

Project-specific configuration built on top of ASES.

| Policy | Description |
|--------|-------------|
| [default-policy.yaml](policies/default-policy.yaml) | Base policy |
| [certus-policy.yaml](policies/certus-policy.yaml) | Certus project |
| [aspnet-policy.yaml](policies/aspnet-policy.yaml) | ASP.NET projects |
| [python-policy.yaml](policies/python-policy.yaml) | Python projects |
| [react-policy.yaml](policies/react-policy.yaml) | React projects |

---

## Templates

Reusable engineering artifacts.

| Template | Description |
|----------|-------------|
| [feature-spec.md](templates/feature-spec.md) | Feature Specification |
| [implementation-report.md](templates/implementation-report.md) | Implementation Report |
| [user-manual.md](templates/user-manual.md) | User Manual |
| [adr.md](templates/adr.md) | Architecture Decision Record |
| [rfc.md](templates/rfc.md) | Request for Comments |
| [test-plan.md](templates/test-plan.md) | Test Plan |
| [release-notes.md](templates/release-notes.md) | Release Notes |
| [impact-assessment.md](templates/impact-assessment.md) | Impact Assessment |
| [traceability-matrix.md](templates/traceability-matrix.md) | Traceability Matrix |
| [maintainability-report.md](templates/maintainability-report.md) | Maintainability Report |
| [technical-debt-report.md](templates/technical-debt-report.md) | Technical Debt Report |

---

## Adapters

Integration guides for AI coding agents.

| Agent | Directory |
|-------|-----------|
| MiMoCode | [adapters/mimocode/](adapters/mimocode/) |
| Claude Code | [adapters/claude-code/](adapters/claude-code/) |
| Codex | [adapters/codex/](adapters/codex/) |
| Cursor | [adapters/cursor/](adapters/cursor/) |

---

## Examples

Reference implementations demonstrating ASES compliance.

| Example | Description |
|---------|-------------|
| [sample-feature/](examples/sample-feature/) | Complete feature lifecycle |

---

# RFCs

| RFC | Title | Status |
|-----|-------|--------|
| [RFC-0001](docs/rfcs/RFC-0001-project-vision.md) | Project Vision, Scope, and Design Principles | Accepted |
| [RFC-0002](docs/rfcs/RFC-0002-ases-standard.md) | Agent Software Engineering Standard | Accepted |

---

# Research

Aegis is informed by academic research on AI coding agents and software engineering.

| Document | Description |
|----------|-------------|
| [Research Citations](docs/research-citations.md) | All 17 cited papers with details |

Key research areas:
- Trustworthiness of AI software engineers
- Security debt in agent-generated code
- Behavioral rules for persistent learning
- Task-level contracts for vibe coding
- ISO 25010 quality model alignment

---

# Design Principles

* AI is an engineering team member—not an engineering process.
* Every line of code must be traceable.
* Documentation is part of the product.
* Verification is mandatory.
* Maintainability is a deliverable.
* Engineering decisions must be explicit.
* Governance must be automated whenever possible.

---

# Long-Term Vision

Aegis aims to become for AI Software Engineering what OpenAPI became for REST APIs:

A common language, a shared standard, and an ecosystem that enables interoperability across tools, vendors, and engineering organizations.

---

# Project Status

**Version 0.2.0**

ASES Standard defined with research-backed enhancements. AGE implementation planned.

Community contributions and discussions are welcome.

---

# License

See [LICENSE](LICENSE) for details.
