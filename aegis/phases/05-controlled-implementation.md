# Phase 5: Controlled Implementation

> Implement within scope, deliver incrementally.

---

# Purpose

Implement the solution while maintaining strict scope control and delivering in small, verifiable increments.

---

# Required Artifacts

| Artifact | Required |
|----------|----------|
| Source Code | Yes |
| Unit Tests | Yes |
| Scope Report | Yes |
| Commit Messages | Yes |

---

# Implementation Rules

## Scope Control

| Rule | Description |
|------|-------------|
| No unauthorized refactoring | Only refactor within approved scope |
| No scope creep | New requirements require new specification |
| No unauthorized dependencies | New dependencies require approval |
| Blast radius awareness | Minimize changes to unrelated files |

## Incremental Delivery

Each task should follow:

```text
Implement
   ↓
Build
   ↓
Verify
   ↓
Commit
   ↓
Next Task
```

## Commit Standards

Every commit must:
- Have a descriptive message
- Reference the related task/feature
- Pass all tests
- Not break existing functionality

---

# Quality Gates

| Gate ID | Description | Severity |
|---------|-------------|----------|
| IMP-001 | Code compiles/builds | Error |
| IMP-002 | Unit tests pass | Error |
| IMP-003 | No scope drift detected | Error |
| IMP-004 | Commit messages are descriptive | Warning |
| IMP-005 | No unauthorized refactoring | Error |

---

# Exit Criteria

Phase 5 is complete when:

- [ ] All tasks implemented
- [ ] All unit tests pass
- [ ] No scope drift
- [ ] All commits have descriptive messages
- [ ] All IMP gates pass

---

# AI Agent Responsibilities

The AI agent must:

1. Follow the implementation plan
2. Stay within approved scope
3. Write tests alongside implementation
4. Make incremental commits
5. Report any scope issues immediately
6. Not refactor outside approved scope

---

# References

- [ASES.md](../ASES.md) — Master standard
- [Phase 4: Solution Design](04-solution-design.md) — Prerequisite
- [Testing Standards](../testing-standards.md)
