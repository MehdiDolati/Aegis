# Phase 1: Specification

> Define what needs to be built before building it.

---

# Purpose

Every significant implementation must originate from an approved specification. This phase ensures the problem is understood, the scope is defined, and acceptance criteria are clear.

---

# Required Artifacts

## Feature Specification

A complete feature specification must include:

| Section | Required |
|---------|----------|
| Feature ID | Yes |
| Title | Yes |
| User Story | Yes |
| Business Value | Yes |
| Scope (In/Out) | Yes |
| Functional Requirements | Yes |
| Acceptance Criteria | Yes |
| Definition of Done | Yes |
| Dependencies | Yes |
| Risks | Yes |
| Open Questions | Yes |

Use the [Feature Specification Template](../../templates/feature-spec.md).

---

# Quality Gates

| Gate ID | Description | Severity |
|---------|-------------|----------|
| SPEC-001 | Feature Specification exists | Error |
| SPEC-002 | User Story is complete | Error |
| SPEC-003 | Acceptance Criteria are defined | Error |
| SPEC-004 | Definition of Done is specified | Error |
| SPEC-005 | Dependencies are identified | Warning |
| SPEC-006 | Risks are identified | Warning |
| SPEC-007 | Open Questions are listed | Info |

---

# Exit Criteria

Phase 1 is complete when:

- [ ] Feature Specification document exists
- [ ] All required sections are filled
- [ ] Acceptance Criteria are specific, measurable, and testable
- [ ] Definition of Done is explicit
- [ ] All SPEC gates pass

---

# Common Issues

| Issue | Resolution |
|-------|------------|
| Missing acceptance criteria | Return to author for completion |
| Vague user story | Clarify with specific scenarios |
| No definition of done | Define explicit completion criteria |
| Dependencies unknown | Research and document dependencies |

---

# References

- [ASES.md](../ASES.md) — Master standard
- [Quality Gates](../quality-gates.md) — Gate definitions
- [Feature Specification Template](../../templates/feature-spec.md)
