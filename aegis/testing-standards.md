# Testing Standards

> Every acceptance criterion must have objective verification.

---

# Overview

Testing is mandatory. Implementation alone does not demonstrate correctness.

---

# Testing Pyramid

```text
        E2E Tests
       Integration Tests
      Unit Tests
```

- **Unit Tests**: Fast, isolated, numerous
- **Integration Tests**: Verify component interactions
- **E2E Tests**: Verify complete user workflows

---

# Unit Test Standards

## Requirements

| Requirement | Description |
|-------------|-------------|
| Coverage | Meet project threshold (default: 80%) |
| Isolation | No external dependencies |
| Determinism | Same input always produces same output |
| Naming | Clear, descriptive test names |
| Assertions | Meaningful assertions, not just coverage |

## Test Structure

```text
describe("Component", () => {
  it("should behavior when condition", () => {
    // Arrange
    // Act
    // Assert
  });
});
```

## Quality Criteria

| Criteria | Description |
|----------|-------------|
| Meaningful | Tests real behavior |
| Independent | Tests don't depend on each other |
| Fast | Tests run quickly |
| Readable | Tests are self-documenting |
| Maintained | Tests updated with code changes |

---

# Integration Test Standards

## Requirements

| Requirement | Description |
|-------------|-------------|
| API endpoints | Test all modified endpoints |
| Database | Test data operations |
| Services | Test service interactions |
| External systems | Mock external dependencies |

## Scope

Integration tests should cover:
- API request/response cycle
- Database operations
- Service-to-service communication
- Authentication/Authorization flows

---

# E2E Test Standards

## Requirements

| Requirement | Description |
|-------------|-------------|
| User workflows | Test complete user journeys |
| Browser tests | If UI changes |
| Cross-browser | If required by policy |
| Accessibility | If required by policy |

## Frameworks

| Framework | Use Case |
|-----------|----------|
| Playwright | Web applications |
| Cypress | Web applications |
| Appium | Mobile applications |

---

# Test Coverage

## Thresholds

| Metric | Default | Configurable |
|--------|---------|--------------|
| Line Coverage | 80% | Yes |
| Branch Coverage | 75% | Yes |
| Function Coverage | 85% | Yes |

## Coverage Reports

Generate coverage reports and include in:
- Implementation Report
- CI/CD pipeline
- Quality dashboard

---

# Test Quality

## Anti-Patterns to Avoid

| Anti-Pattern | Problem |
|--------------|---------|
| Testing implementation details | Tests break when refactoring |
| Shared state between tests | Tests are order-dependent |
| Slow tests | Developers skip them |
| Brittle assertions | Tests fail for wrong reasons |
| Missing edge cases | Bugs slip through |

## Best Practices

| Practice | Benefit |
|----------|---------|
| Test one thing per test | Clear failure messages |
| Use descriptive names | Self-documenting tests |
| Arrange-Act-Assert pattern | Readable tests |
| Mock external dependencies | Fast, isolated tests |
| Test edge cases | Comprehensive coverage |

---

# Quality Gates

| Gate ID | Description | Severity |
|---------|-------------|----------|
| TEST-001 | Unit tests exist | Error |
| TEST-002 | Unit tests pass | Error |
| TEST-003 | Integration tests exist (if applicable) | Error |
| TEST-004 | Integration tests pass | Error |
| TEST-005 | E2E tests exist (if applicable) | Error |
| TEST-006 | E2E tests pass | Error |
| TEST-007 | Coverage meets threshold | Warning |
| TEST-008 | Tests are meaningful | Warning |

---

# References

- [ASES.md](ASES.md) — Master standard
- [Phase 6: Verification](phases/06-verification.md)
