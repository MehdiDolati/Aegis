# Quality Gates

> Every phase transition requires passing quality gates.

---

# Overview

Quality gates are checkpoints that must be passed before proceeding to the next phase. They ensure quality is built in, not inspected in.

---

# Gate Structure

Every gate must have:

| Field | Description |
|-------|-------------|
| ID | Unique identifier |
| Title | Short description |
| Description | Detailed explanation |
| Severity | Error / Warning / Info |
| Phase | Which phase this gate belongs to |
| Validator | How to verify this gate |
| Evidence | What evidence is required |
| Exceptions | When this gate can be skipped |

---

# Severity Levels

| Severity | Behavior |
|----------|----------|
| Error | Blocks progression. Must be resolved before proceeding. |
| Warning | Flags risk. Should be addressed. May proceed with approval. |
| Info | Informational. No blocking. |

---

# Gate Types

## Specification Gates

| Gate ID | Description | Severity |
|---------|-------------|----------|
| SPEC-001 | Feature Specification exists | Error |
| SPEC-002 | User Story is complete | Error |
| SPEC-003 | Acceptance Criteria are defined | Error |
| SPEC-004 | Definition of Done is specified | Error |
| SPEC-005 | Dependencies are identified | Warning |
| SPEC-006 | Risks are identified | Warning |
| SPEC-007 | Open Questions are listed | Info |

## Review Gates

| Gate ID | Description | Severity |
|---------|-------------|----------|
| REV-001 | Validation report exists | Error |
| REV-002 | No unresolved ambiguities | Error |
| REV-003 | No unresolved contradictions | Error |
| REV-004 | All requirements are testable | Error |
| REV-005 | Technical conflicts resolved | Error |

## Impact Gates

| Gate ID | Description | Severity |
|---------|-------------|----------|
| IMP-001 | Impact Assessment exists | Error |
| IMP-002 | All affected files identified | Error |
| IMP-003 | Risk level assessed | Error |
| IMP-004 | High/Critical risks reviewed | Error |

## Design Gates

| Gate ID | Description | Severity |
|---------|-------------|----------|
| DES-001 | Implementation Plan exists | Error |
| DES-002 | Task Breakdown exists | Error |
| DES-003 | Plan reviewed and approved | Error |
| DES-004 | ADR created for architectural decisions | Error |

## Implementation Gates

| Gate ID | Description | Severity |
|---------|-------------|----------|
| IMPL-001 | Code compiles/builds | Error |
| IMPL-002 | Unit tests pass | Error |
| IMPL-003 | No scope drift detected | Error |
| IMPL-004 | Commit messages are descriptive | Warning |
| IMPL-005 | No unauthorized refactoring | Error |

## Verification Gates

| Gate ID | Description | Severity |
|---------|-------------|----------|
| VER-001 | All unit tests pass | Error |
| VER-002 | All integration tests pass | Error |
| VER-003 | E2E tests pass (if applicable) | Error |
| VER-004 | All acceptance criteria verified | Error |
| VER-005 | Test coverage meets threshold | Warning |
| VER-006 | No test quality issues | Warning |

## Documentation Gates

| Gate ID | Description | Severity |
|---------|-------------|----------|
| DOC-001 | User Manual updated (if applicable) | Error |
| DOC-002 | API Documentation updated (if applicable) | Error |
| DOC-003 | Release Notes created | Error |
| DOC-004 | Documentation matches implementation | Error |
| DOC-005 | No outdated documentation | Warning |

## Maintainability Gates

| Gate ID | Description | Severity |
|---------|-------------|----------|
| MAINT-001 | No dead code | Error |
| MAINT-002 | No unused imports | Error |
| MAINT-003 | Complexity within threshold | Warning |
| MAINT-004 | No code duplication | Warning |
| MAINT-005 | Architecture compliance | Error |

## Debt Gates

| Gate ID | Description | Severity |
|---------|-------------|----------|
| DEBT-001 | Debt Report exists | Error |
| DEBT-002 | All debt documented | Error |
| DEBT-003 | No critical debt unresolved | Error |
| DEBT-004 | Resolution plan for high debt | Error |

## Final Gates

| Gate ID | Description | Severity |
|---------|-------------|----------|
| FINAL-001 | Implementation Report exists | Error |
| FINAL-002 | Traceability Matrix complete | Error |
| FINAL-003 | All phase gates passed | Error |
| FINAL-004 | Reviewer sign-off obtained | Error |

---

# References

- [ASES.md](ASES.md) — Master standard
- [phases/](phases/) — Phase-specific gates
