# Aegis Engineering Instructions

> Follow these instructions when working on this project.

---

# Project Context

This project follows the Agent Software Engineering Standard (ASES).

- Standard: [ASES.md](aegis/ASES.md)
- Policy: [project-policy.yaml](project-policy.yaml)

---

# Engineering Lifecycle

Every feature must follow these phases:

1. **Specification** — Create Feature Specification
2. **Requirement Review** — Validate requirements
3. **Impact Analysis** — Assess impact
4. **Solution Design** — Create implementation plan
5. **Controlled Implementation** — Implement within scope
6. **Verification** — Test everything
7. **Documentation** — Update documentation
8. **Maintainability Audit** — Check code quality
9. **Technical Debt Review** — Document debt
10. **Final Review** — Complete sign-off

---

# Required Artifacts

For every feature, you must create:

- [ ] Feature Specification
- [ ] Impact Assessment
- [ ] Implementation Plan
- [ ] Task Breakdown
- [ ] Source Code
- [ ] Unit Tests
- [ ] Integration Tests
- [ ] Documentation Updates
- [ ] Implementation Report
- [ ] Traceability Matrix

---

# Quality Gates

Every phase transition requires passing quality gates.

Gate severity:
- **Error**: Must be resolved before proceeding
- **Warning**: Should be addressed
- **Info**: Informational only

---

# Rules

Follow these rules:

1. **No scope drift** — Stay within approved scope
2. **No unauthorized refactoring** — Only refactor within scope
3. **Verify everything** — Run tests before completion
4. **Document everything** — Update documentation
5. **Trace everything** — Link requirements to code

---

# Testing

- Write unit tests for all new code
- Write integration tests for API changes
- Write E2E tests for user-facing features
- Ensure all tests pass before completion
- Maintain test coverage above threshold

---

# Documentation

- Update User Manual for user-facing features
- Update API Documentation for API changes
- Create Release Notes for releases
- Keep documentation current

---

# Security

- Never hardcode secrets
- Validate all inputs
- Review dependencies
- Implement authentication/authorization

---

# References

- [ASES Standard](aegis/ASES.md)
- [Quality Gates](aegis/quality-gates.md)
- [Testing Standards](aegis/testing-standards.md)
- [Documentation Standards](aegis/documentation-standards.md)
