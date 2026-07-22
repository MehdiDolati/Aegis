# Phase 4: Solution Design

> Design the solution before implementing it.

---

# Purpose

Before writing code, create a design that outlines the implementation approach, task breakdown, and architectural decisions.

---

# Required Artifacts

| Artifact | Required |
|----------|----------|
| Implementation Plan | Yes |
| Task Breakdown | Yes |
| ADR | If architectural decision |

---

# Design Artifacts

## Implementation Plan

The implementation plan must include:

| Section | Required |
|---------|----------|
| Approach overview | Yes |
| Files to modify | Yes |
| Files to create | Yes |
| API changes | If applicable |
| Database changes | If applicable |
| Configuration changes | If applicable |

## Task Breakdown

Decompose the implementation into manageable tasks:

```text
Epic
   ↓
Feature
   ↓
Tasks
   ↓
Subtasks
   ↓
Verification
```

Each task should be:
- Small enough to verify independently
- Large enough to be meaningful
- Traceable to a requirement

## Architecture Decision Record (ADR)

Required when making significant architectural decisions.

Use the [ADR Template](../../templates/adr.md).

---

# Quality Gates

| Gate ID | Description | Severity |
|---------|-------------|----------|
| DES-001 | Implementation Plan exists | Error |
| DES-002 | Task Breakdown exists | Error |
| DES-003 | Plan reviewed and approved | Error |
| DES-004 | ADR created for architectural decisions | Error |

---

# Exit Criteria

Phase 4 is complete when:

- [ ] Implementation Plan documented
- [ ] Task Breakdown complete
- [ ] Plan reviewed and approved
- [ ] ADR created (if applicable)
- [ ] All DES gates pass

---

# AI Agent Responsibilities

The AI agent must:

1. Read the Feature Specification
2. Read the Impact Assessment
3. Create an implementation plan
4. Break down into tasks
5. Identify architectural decisions
6. Create ADRs as needed
7. Present plan for human review

---

# References

- [ASES.md](../ASES.md) — Master standard
- [Phase 3: Impact Analysis](03-impact-analysis.md) — Prerequisite
- [ADR Template](../../templates/adr.md)
