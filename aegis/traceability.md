# Traceability Standard

> Every artifact must be traceable.

---

# Overview

Traceability ensures that every engineering artifact can be linked to its origin and destination. This enables:
- Impact analysis when changes occur
- Verification that all requirements are implemented
- Detection of orphan requirements or code
- Regression prediction

---

# Traceability Chain

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

Every link in this chain must be explicit and documented.

---

# Traceability Matrix

For each feature, maintain a traceability matrix:

| Requirement | Code | Tests | Documentation | Status |
|-------------|------|-------|---------------|--------|
| AC-1 | OrderService.cs | OrderTests.cs | User Manual | PASS |
| AC-2 | ApiController.cs | ApiTests.cs | API Docs | PASS |
| AC-3 | RiskEngine.cs | RiskE2E.spec.ts | Admin Guide | PASS |

---

# Bidirectional Traceability

Traceability must work in both directions:

- **Forward**: From requirement to implementation
- **Backward**: From implementation to requirement

This ensures:
- Every requirement has an implementation
- Every implementation has a requirement
- No orphan requirements exist
- No orphan code exists

---

# Orphan Detection

AI agents must detect:

| Orphan Type | Description | Action |
|-------------|-------------|--------|
| Orphan Requirement | Requirement with no implementation | Flag for resolution |
| Orphan Code | Code with no requirement | Justify or remove |
| Orphan Test | Test with no requirement | Justify or remove |
| Orphan Documentation | Doc with no feature | Update or remove |

---

# Change Impact Report

Before any change, generate an impact report:

```text
Feature Change
   ↓
Affected Modules
   ↓
Affected APIs
   ↓
Affected Tests
   ↓
Affected Documentation
   ↓
Affected Users
```

---

# Regression Prediction

After any change, predict regression risk:

```text
This change
   ↓
Affects these features
   ↓
May break these tests
   ↓
Requires regression testing
```

---

# Quality Gates

| Gate ID | Description | Severity |
|---------|-------------|----------|
| TRACE-001 | Traceability Matrix exists | Error |
| TRACE-002 | No orphan requirements | Error |
| TRACE-003 | No orphan code | Warning |
| TRACE-004 | All links bidirectional | Error |

---

# References

- [ASES.md](ASES.md) — Master standard
- [Phase 10: Final Review](phases/10-final-review.md)
