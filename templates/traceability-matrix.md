# Traceability Matrix

> Link requirements to implementation and verification.

---

# Document Information

| Field | Value |
|-------|-------|
| Matrix ID | TRC-XXXX |
| Feature ID | FEAT-XXXX |
| Feature Title | |
| Created | |
| Updated | |

---

# Traceability Links

| Requirement | Specification | Tasks | Code | Tests | Documentation | Status |
|-------------|---------------|-------|------|-------|---------------|--------|
| AC-1 | FEAT-0001 §3.1 | T-001 | OrderService.cs | OrderTests.cs | User Manual | Complete |
| AC-2 | FEAT-0001 §3.2 | T-002 | ApiController.cs | ApiTests.cs | API Docs | Complete |
| AC-3 | FEAT-0001 §3.3 | T-003 | RiskEngine.cs | RiskE2E.spec.ts | Admin Guide | Complete |

---

# Requirement Coverage

| Requirement | Covered | Evidence |
|-------------|---------|----------|
| AC-1 | Yes | OrderTests.cs |
| AC-2 | Yes | ApiTests.cs |
| AC-3 | Yes | RiskE2E.spec.ts |

---

# Code Traceability

| Code File | Requirements | Tests |
|-----------|--------------|-------|
| OrderService.cs | AC-1 | OrderTests.cs |
| ApiController.cs | AC-2 | ApiTests.cs |
| RiskEngine.cs | AC-3 | RiskE2E.spec.ts |

---

# Test Traceability

| Test File | Requirements | Code |
|-----------|--------------|------|
| OrderTests.cs | AC-1 | OrderService.cs |
| ApiTests.cs | AC-2 | ApiController.cs |
| RiskE2E.spec.ts | AC-3 | RiskEngine.cs |

---

# Orphan Detection

## Orphan Requirements

Requirements with no implementation:

| Requirement | Status | Action |
|-------------|--------|--------|
| | | |

## Orphan Code

Code with no requirement:

| Code File | Status | Action |
|-----------|--------|--------|
| | | |

## Orphan Tests

Tests with no requirement:

| Test File | Status | Action |
|-----------|--------|--------|
| | | |

---

# Summary

| Metric | Count | Percentage |
|--------|-------|------------|
| Total Requirements | | |
| Covered Requirements | | |
| Coverage | | |
| Orphan Requirements | | |
| Orphan Code | | |
| Orphan Tests | | |

---

# References

- Feature Specification
- ASES Traceability Standard
