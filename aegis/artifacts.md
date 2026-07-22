# Required Artifacts

> Every phase produces specific artifacts.

---

# Overview

ASES defines required artifacts for each phase. Artifacts are the evidence that engineering work was performed correctly.

---

# Artifact Catalog

## Phase 1: Specification

| Artifact | Format | Template |
|----------|--------|----------|
| Feature Specification | Markdown | [feature-spec.md](../templates/feature-spec.md) |
| User Story | Markdown | Included in Feature Spec |
| Acceptance Criteria | Markdown | Included in Feature Spec |
| Definition of Done | Markdown | Included in Feature Spec |

## Phase 2: Requirement Review

| Artifact | Format | Template |
|----------|--------|----------|
| Requirement Validation Report | Markdown | [validation-report.md](templates/validation-report.md) |
| Ambiguity List | Markdown | Included in Validation Report |
| Contradiction Report | Markdown | Included in Validation Report |

## Phase 3: Impact Analysis

| Artifact | Format | Template |
|----------|--------|----------|
| Impact Assessment | Markdown | [impact-assessment.md](../templates/impact-assessment.md) |
| Affected Files List | Markdown | Included in Impact Assessment |
| Risk Level Assessment | Markdown | Included in Impact Assessment |

## Phase 4: Solution Design

| Artifact | Format | Template |
|----------|--------|----------|
| Implementation Plan | Markdown | Custom |
| Task Breakdown | Markdown | Custom |
| ADR | Markdown | [adr.md](../templates/adr.md) |

## Phase 5: Controlled Implementation

| Artifact | Format | Template |
|----------|--------|----------|
| Source Code | Language-specific | N/A |
| Unit Tests | Language-specific | N/A |
| Scope Report | Markdown | Custom |
| Commit Messages | Git | N/A |

## Phase 6: Verification

| Artifact | Format | Template |
|----------|--------|----------|
| Unit Test Results | Test output | N/A |
| Integration Test Results | Test output | N/A |
| E2E Test Results | Test output | N/A |
| AC Verification | Markdown | Included in Implementation Report |

## Phase 7: Documentation

| Artifact | Format | Template |
|----------|--------|----------|
| User Manual Update | Markdown | [user-manual.md](../templates/user-manual.md) |
| API Documentation | OpenAPI/Markdown | Custom |
| Release Notes | Markdown | [release-notes.md](../templates/release-notes.md) |

## Phase 8: Maintainability Audit

| Artifact | Format | Template |
|----------|--------|----------|
| Maintainability Report | Markdown | [maintainability-report.md](../templates/maintainability-report.md) |
| Dead Code Analysis | Markdown | Included in Report |
| Complexity Analysis | Markdown | Included in Report |

## Phase 9: Technical Debt Review

| Artifact | Format | Template |
|----------|--------|----------|
| Technical Debt Report | Markdown | [technical-debt-report.md](../templates/technical-debt-report.md) |
| Debt Introduced | Markdown | Included in Report |
| Debt Resolved | Markdown | Included in Report |

## Phase 10: Final Review

| Artifact | Format | Template |
|----------|--------|----------|
| Implementation Report | Markdown | [implementation-report.md](../templates/implementation-report.md) |
| Traceability Matrix | Markdown | [traceability-matrix.md](../templates/traceability-matrix.md) |
| Reviewer Sign-off | Markdown | Included in Implementation Report |

---

# Artifact Validation

Every artifact must be:

| Criterion | Description |
|-----------|-------------|
| Complete | All required sections filled |
| Accurate | Content matches reality |
| Current | Up-to-date with latest changes |
| Traceable | Links to related artifacts |
| Approved | Reviewed and approved (if required) |

---

# References

- [ASES.md](ASES.md) — Master standard
- [templates/](../templates/) — Artifact templates
