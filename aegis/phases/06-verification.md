# Phase 6: Verification

> Verify that the implementation meets requirements.

---

# Purpose

Ensure the implementation is correct, complete, and meets all acceptance criteria through comprehensive testing.

---

# Required Artifacts

| Artifact | Required |
|----------|----------|
| Unit Test Results | Yes |
| Integration Test Results | Yes |
| E2E Test Results | If applicable |
| Acceptance Criteria Verification | Yes |

---

# Verification Types

## Unit Tests

| Requirement | Description |
|-------------|-------------|
| Coverage | Meet project threshold |
| Quality | Meaningful assertions |
| Isolation | No external dependencies |
| Naming | Clear test names |

## Integration Tests

| Requirement | Description |
|-------------|-------------|
| API endpoints | Test all modified endpoints |
| Database | Test data operations |
| Services | Test service interactions |

## E2E Tests

| Requirement | Description |
|-------------|-------------|
| User workflows | Test complete user journeys |
| Browser tests | If UI changes |
| Cross-browser | If required by policy |

## Acceptance Criteria Verification

| AC | Status | Evidence |
|----|--------|----------|
| AC-1 | PASS/FAIL | Test/Screenshot/Log |
| AC-2 | PASS/FAIL | Test/Screenshot/Log |

Every acceptance criterion must have verified evidence.

---

# Quality Gates

| Gate ID | Description | Severity |
|---------|-------------|----------|
| VER-001 | All unit tests pass | Error |
| VER-002 | All integration tests pass | Error |
| VER-003 | E2E tests pass (if applicable) | Error |
| VER-004 | All acceptance criteria verified | Error |
| VER-005 | Test coverage meets threshold | Warning |
| VER-006 | No test quality issues | Warning |

---

# Test Quality Requirements

Tests must be:

| Quality | Description |
|---------|-------------|
| Meaningful | Test real behavior, not just coverage |
| Independent | Tests don't depend on each other |
| Deterministic | Same input always produces same output |
| Readable | Test names describe what is tested |
| Maintained | Tests updated with code changes |

---

# Exit Criteria

Phase 6 is complete when:

- [ ] All tests pass
- [ ] All acceptance criteria verified
- [ ] Test coverage meets threshold
- [ ] No test quality issues
- [ ] All VER gates pass

---

# References

- [ASES.md](../ASES.md) — Master standard
- [Testing Standards](../testing-standards.md) — Detailed requirements
- [Phase 5: Controlled Implementation](05-controlled-implementation.md) — Prerequisite
