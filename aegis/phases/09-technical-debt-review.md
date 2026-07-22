# Phase 9: Technical Debt Review

> Make debt explicit and intentional.

---

# Purpose

Review any technical debt introduced by the implementation and ensure it is documented and planned for resolution.

---

# Required Artifacts

| Artifact | Required |
|----------|----------|
| Technical Debt Report | Yes |
| Debt Introduced | Yes |
| Debt Resolved | Yes |

---

# Technical Debt Categories

| Category | Description |
|----------|-------------|
| Intentional | Deliberately deferred for later |
| Unintentional | Discovered during implementation |
| Accumulated | Existing debt affected by changes |
| Resolved | Existing debt addressed |

---

# Debt Documentation

Every instance of technical debt must include:

| Field | Required |
|-------|----------|
| ID | Yes |
| Description | Yes |
| Category | Yes |
| Severity | Yes |
| Impact | Yes |
| Planned Resolution | Yes |
| Target Date | If intentional |

---

# Debt Severity

| Severity | Description | Action |
|----------|-------------|--------|
| Low | Minor, no immediate impact | Document and defer |
| Medium | Moderate impact on maintainability | Plan resolution within sprint |
| High | Significant impact on development | Plan immediate resolution |
| Critical | Blocks future development | Resolve before release |

---

# Quality Gates

| Gate ID | Description | Severity |
|---------|-------------|----------|
| DEBT-001 | Debt Report exists | Error |
| DEBT-002 | All debt documented | Error |
| DEBT-003 | No critical debt unresolved | Error |
| DEBT-004 | Resolution plan for high debt | Error |

---

# Exit Criteria

Phase 9 is complete when:

- [ ] Technical Debt Report exists
- [ ] All debt documented with ID and description
- [ ] No critical debt unresolved
- [ ] Resolution plan for high-severity debt
- [ ] All DEBT gates pass

---

# References

- [ASES.md](../ASES.md) — Master standard
- [Phase 8: Maintainability Audit](08-maintainability-audit.md) — Prerequisite
