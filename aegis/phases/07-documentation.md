# Phase 7: Documentation

> Documentation is part of the product.

---

# Purpose

Ensure all user-facing and developer-facing documentation is updated to reflect the implementation.

---

# Required Artifacts

| Artifact | Required |
|----------|----------|
| User Manual Update | If user-facing |
| API Documentation Update | If API changes |
| Release Notes | Yes |
| Changelog | Yes |

---

# Documentation Types

## User Manual

Update when:
- New user-facing features
- Changed user workflows
- New error messages
- Changed permissions

## API Documentation

Update when:
- New endpoints
- Modified endpoints
- Changed request/response format
- New error codes

## Release Notes

Include:
- New features
- Bug fixes
- Breaking changes
- Known issues
- Migration instructions

## Changelog

Include:
- What changed
- Why it changed
- How to adapt

---

# Documentation Quality

| Requirement | Description |
|-------------|-------------|
| Accuracy | Documentation matches implementation |
| Completeness | All features documented |
| Clarity | Easy to understand |
| Currency | Up-to-date with latest changes |
| Accessibility | Available to intended audience |

---

# Quality Gates

| Gate ID | Description | Severity |
|---------|-------------|----------|
| DOC-001 | User Manual updated (if applicable) | Error |
| DOC-002 | API Documentation updated (if applicable) | Error |
| DOC-003 | Release Notes created | Error |
| DOC-004 | Documentation matches implementation | Error |
| DOC-005 | No outdated documentation | Warning |

---

# Exit Criteria

Phase 7 is complete when:

- [ ] All required documentation updated
- [ ] Documentation matches implementation
- [ ] No outdated references
- [ ] All DOC gates pass

---

# References

- [ASES.md](../ASES.md) — Master standard
- [Documentation Standards](../documentation-standards.md) — Detailed requirements
- [Phase 6: Verification](06-verification.md) — Prerequisite
