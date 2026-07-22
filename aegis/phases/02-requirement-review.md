# Phase 2: Requirement Review

> Validate that requirements are complete, consistent, and unambiguous.

---

# Purpose

Before proceeding to design, AI agents must validate the specification for:
- Ambiguity
- Missing information
- Contradictions
- Technical conflicts

---

# Required Artifacts

| Artifact | Required |
|----------|----------|
| Requirement Validation Report | Yes |
| Ambiguity List | If issues found |
| Contradiction Report | If issues found |

---

# Validation Checklist

| Check | Description |
|-------|-------------|
| Ambiguity | Are any requirements unclear or open to interpretation? |
| Completeness | Are all necessary requirements documented? |
| Consistency | Do any requirements contradict each other? |
| Feasibility | Are all requirements technically achievable? |
| Testability | Can every acceptance criterion be verified? |
| Traceability | Can every requirement be traced to a business need? |

---

# Quality Gates

| Gate ID | Description | Severity |
|---------|-------------|----------|
| REV-001 | Validation report exists | Error |
| REV-002 | No unresolved ambiguities | Error |
| REV-003 | No unresolved contradictions | Error |
| REV-004 | All requirements are testable | Error |
| REV-005 | Technical conflicts resolved | Error |

---

# Exit Criteria

Phase 2 is complete when:

- [ ] Validation report exists
- [ ] All ambiguities resolved or documented
- [ ] All contradictions resolved
- [ ] All requirements are testable
- [ ] All REV gates pass

---

# AI Agent Responsibilities

The AI agent must:

1. Read the Feature Specification
2. Check each requirement for clarity
3. Verify acceptance criteria are testable
4. Identify contradictions between requirements
5. Flag technical conflicts
6. Generate validation report
7. Ask questions for unclear requirements

---

# References

- [ASES.md](../ASES.md) — Master standard
- [Phase 1: Specification](01-specification.md) — Prerequisite
