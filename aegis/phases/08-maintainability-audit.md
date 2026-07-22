# Phase 8: Maintainability Audit

> Ensure the code remains maintainable.

---

# Purpose

Audit the implementation for maintainability issues before considering it complete.

---

# Required Artifacts

| Artifact | Required |
|----------|----------|
| Maintainability Report | Yes |
| Dead Code Analysis | Yes |
| Complexity Analysis | Yes |

---

# Maintainability Checks

| Check | Description | Threshold |
|-------|-------------|-----------|
| Dead Code | Unused classes, methods, variables | None allowed |
| Unused Imports | Import statements not used | None allowed |
| Complexity | Cyclomatic complexity | Per project policy |
| Duplication | Code duplication | Per project policy |
| Naming | Consistent naming conventions | Per project policy |
| Architecture | Compliance with architecture | No violations |

---

# Dead Code Detection

The following are considered dead code:

| Type | Detection |
|------|-----------|
| Unused classes | No references found |
| Unused methods | No callers found |
| Unused variables | No reads found |
| Unused imports | No usage found |
| Unreachable code | After return/throw |
| Commented code | Should be removed |

---

# Complexity Metrics

| Metric | Description | Warning | Error |
|--------|-------------|---------|-------|
| Cyclomatic Complexity | Decision points per method | > 10 | > 20 |
| Class Length | Lines per class | > 300 | > 500 |
| Method Length | Lines per method | > 30 | > 50 |
| Parameters | Parameters per method | > 4 | > 7 |

---

# Quality Gates

| Gate ID | Description | Severity |
|---------|-------------|----------|
| MAINT-001 | No dead code | Error |
| MAINT-002 | No unused imports | Error |
| MAINT-003 | Complexity within threshold | Warning |
| MAINT-004 | No code duplication | Warning |
| MAINT-005 | Architecture compliance | Error |

---

# Exit Criteria

Phase 8 is complete when:

- [ ] No dead code detected
- [ ] No unused imports
- [ ] Complexity within thresholds
- [ ] No significant duplication
- [ ] Architecture compliant
- [ ] All MAINT gates pass

---

# References

- [ASES.md](../ASES.md) — Master standard
- [Phase 7: Documentation](07-documentation.md) — Prerequisite
