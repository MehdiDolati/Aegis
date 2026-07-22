# RFC-0002 — Agent Software Engineering Standard (ASES)

| Field | Value |
|-------|-------|
| **RFC** | RFC-0002 |
| **Title** | Agent Software Engineering Standard (ASES) |
| **Status** | Accepted |
| **Version** | 1.0.0 |
| **Authors** | Mehdi Dolati, Aegis Project |
| **Created** | 2026-07-22 |
| **Category** | Standard |

---

# Abstract

This RFC proposes the Agent Software Engineering Standard (ASES), a comprehensive engineering standard that defines how AI coding agents should participate in professional software development.

ASES establishes requirements for artifacts, quality gates, traceability, documentation, verification, and maintainability across a 10-phase engineering lifecycle.

---

# Motivation

AI coding agents are becoming capable software developers. However, current AI-assisted workflows often optimize for implementation speed while neglecting engineering discipline.

The result is code that:
- Lacks proper specifications
- Has insufficient testing
- Is poorly documented
- Has no traceability
- Accumulates technical debt

ASES addresses this by defining a complete engineering process that ensures AI-assisted development produces maintainable, verifiable, traceable, and production-ready software.

---

# Problem Statement

Current AI coding agents exhibit recurring engineering shortcomings:

1. **Missing specifications** — Code written without clear requirements
2. **Insufficient testing** — Tests missing or low quality
3. **Documentation drift** — Documentation not updated with changes
4. **No traceability** — Requirements not linked to code
5. **Scope creep** — Implementation exceeds approved scope
6. **Technical debt** — Debt accumulated without documentation
7. **Inconsistent practices** — Different agents produce different quality

---

# Proposed Solution

## Core Principles

ASES is built on 6 core principles:

1. **Developer Accountability** — Humans are ultimately responsible
2. **Understand and Verify** — No blind acceptance of AI code
3. **Security First** — Protect sensitive data
4. **Code Quality and Consistency** — Same standards for AI and human code
5. **Human-Led Design** — Critical decisions led by humans
6. **AI Awareness** — Recognize limitations and adapt

## Engineering Lifecycle

ASES defines a 10-phase engineering lifecycle:

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

## Required Artifacts

Every phase produces specific artifacts. Artifacts are the evidence that engineering work was performed correctly.

## Quality Gates

Every phase transition requires passing quality gates. Gates ensure quality is built in, not inspected in.

Gate severity levels:
- **Error** — Blocks progression, must be resolved
- **Warning** — Flags risk, should be addressed
- **Info** — Informational, no blocking

## Traceability

Every engineering artifact must be traceable:

```text
Epic
   ↓
Feature Specification
   ↓
Tasks
   ↓
Source Code
   ↓
Unit Tests
   ↓
Integration Tests
   ↓
E2E Tests
   ↓
Documentation
   ↓
Release
```

## Testing Standards

- Every Acceptance Criterion must have at least one test
- Unit test coverage must meet project threshold
- E2E tests required for user-facing features
- Tests must be meaningful, not just coverage numbers

## Documentation Standards

- Documentation is part of the product
- Documentation must be updated with code changes
- Documentation freshness must be validated

## Security Standards

- Sensitive data must not be hardcoded
- Agent security settings must be verified
- Dependencies must be reviewed

---

# Design Principles

ASES follows these design principles:

1. **Executable-by-Design** — Human-readable standards have machine-readable representations
2. **Vendor Neutrality** — Works with any AI coding agent
3. **Technology Agnostic** — Works with any programming language or framework
4. **Incremental Adoption** — Can be adopted gradually
5. **Extensible** — Can be customized per project

---

# Impact

## Affected Components

- ASES Standard (new)
- Project Policies
- Agent Adapters
- Templates

## Migration Strategy

Projects can adopt ASES incrementally:

1. Start with core phases (Specification, Implementation, Verification)
2. Add quality gates as needed
3. Implement full traceability over time

---

# Risks

| Risk | Severity | Mitigation |
|------|----------|------------|
| Adoption resistance | Medium | Provide clear benefits, incremental adoption |
| Overhead perception | Medium | Show time saved from fewer bugs and rework |
| Tooling gaps | Low | Build tooling incrementally |

---

# Alternatives Considered

| Alternative | Pros | Cons | Why Not |
|-------------|------|------|---------|
| No standard | No overhead | Inconsistent quality | Rejected |
| ISO 12207 only | Established | Not AI-specific | Adapted |
| Custom per project | Flexible | No consistency | Rejected |

---

# Future Work

1. **AGE Implementation** — Build the Agent Governance Engine
2. **More Adapters** — Add adapters for more AI agents
3. **Tooling** — Build automated validation tools
4. **Certification** — Develop ASES certification program
5. **Community** — Build community around the standard

---

# Open Questions

1. What is the optimal test coverage threshold?
2. How to handle prototype/spike exceptions?
3. What metrics best measure ASES compliance?

---

# References

- RFC-0001 — Project Vision, Scope, and Design Principles
- ISO/IEC/IEEE 12207:2017 — Software life cycle processes
- Agentic Coding 6 Principles & 28 Practices
- Claude Code Best Practices (Anthropic)

---

# Implementation

This RFC is implemented in:

- `aegis/ASES.md` — Master standard
- `aegis/phases/` — Phase definitions
- `aegis/rules/` — Machine-readable rules
- `aegis/*.md` — Supporting standards
- `schemas/` — YAML schemas
- `policies/` — Project policies
- `adapters/` — Agent integration guides
- `templates/` — Artifact templates
- `examples/` — Reference examples
