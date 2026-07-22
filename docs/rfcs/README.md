# Aegis Request for Comments (RFC)

> **Version:** 1.0.0  
> **Status:** Active  
> **Last Updated:** 2026-07-22

---

# Purpose

The Request for Comments (RFC) process is the official mechanism for proposing, discussing, approving, and documenting significant changes within the Aegis project.

Every major engineering decision should be documented as an RFC before becoming part of the project's standards, governance model, architecture, or implementation.

The RFC process ensures that Aegis evolves in a transparent, collaborative, and historically traceable manner.

---

# Scope

The RFC process applies to, but is not limited to, changes affecting:

- Agent Software Engineering Standard (ASES)
- Agent Governance Engine (AGE)
- Repository governance
- Engineering processes
- Quality gates
- Traceability model
- Policy model
- Artifact model
- Reference architectures
- Standard templates
- Public APIs
- Plugin architecture

Minor editorial improvements or documentation corrections do not require an RFC.

---

# Guiding Principles

The RFC process is based on the following principles:

- Repository-first knowledge
- Open discussion
- Transparent decision making
- Historical traceability
- Vendor neutrality
- Backward compatibility whenever possible
- Engineering before implementation
- Executable-by-design philosophy

---

# Engineering Workflow

Every significant engineering change follows the same lifecycle.

```text
Idea
   │
   ▼
RFC Draft
   │
   ▼
Discussion
   │
   ▼
Revision
   │
   ▼
Accepted
   │
   ▼
Implementation
   │
   ▼
Standard
   │
   ▼
Executable Specification
   │
   ▼
Governance Enforcement
```

Implementation should never precede an accepted RFC.

---

# RFC Lifecycle

## Draft

Initial proposal under development.

A Draft RFC may change significantly.

---

## Proposed

The proposal is considered complete enough for community discussion and review.

---

## Accepted

The proposal has been approved.

Implementation work may begin.

---

## Implemented

The proposal has been fully reflected in the project.

This may include updates to:

- ASES
- AGE
- Policies
- Templates
- Documentation
- Tooling

---

## Rejected

The proposal has been reviewed and declined.

Rejected RFCs remain part of the repository for historical reference.

---

## Withdrawn

The author has voluntarily withdrawn the proposal.

---

## Superseded

A newer RFC replaces the proposal.

The superseding RFC should be referenced.

---

## Deprecated

The proposal remains implemented but is no longer recommended for future use.

---

# RFC Status Values

| Status | Description |
|----------|-------------|
| Draft | Initial work in progress |
| Proposed | Under review |
| Accepted | Approved |
| Implemented | Reflected in the project |
| Rejected | Declined |
| Withdrawn | Removed by author |
| Superseded | Replaced by another RFC |
| Deprecated | No longer recommended |

---

# RFC Numbering

RFC identifiers use sequential numbering.

Examples:

- RFC-0001
- RFC-0002
- RFC-0003

Identifiers are permanent.

Numbers are never reused.

---

# RFC Naming

RFC filenames should follow the format:

```text
RFC-XXXX-short-title.md
```

Examples:

```text
RFC-0001-project-vision.md

RFC-0002-repository-architecture.md

RFC-0003-meta-model.md
```

Use lowercase letters and hyphens for file names.

---

# RFC Structure

Every RFC should include the following sections.

## Required

- Title
- Status
- Authors
- Version
- Created Date
- Abstract
- Motivation
- Problem Statement
- Proposed Solution
- Design Principles
- Impact
- Risks
- Future Work

## Optional

- Alternatives Considered
- Migration Strategy
- Compatibility
- Security Considerations
- Performance Considerations
- Open Questions

---

# Relationship with ADRs

RFCs and ADRs serve different purposes.

## RFC

Explains:

> Why should this change exist?

RFCs describe ideas before implementation.

---

## ADR

Explains:

> Why was this architectural decision chosen?

ADRs document architecture decisions made while implementing accepted RFCs.

Typical engineering flow:

```text
Idea

↓

RFC

↓

ADR

↓

ASES

↓

Executable Specification

↓

AGE

↓

Implementation
```

---

# Repository Rules

The following changes require an accepted RFC:

- New engineering standards
- Breaking architectural changes
- New governance mechanisms
- New policy models
- Changes to repository governance
- New executable specifications
- New compliance models

The following changes typically do not require an RFC:

- Typographical fixes
- Documentation improvements
- Formatting changes
- Broken link fixes
- Minor examples

---

# Repository Philosophy

The Git repository is the single source of truth.

Engineering knowledge must never exist exclusively in:

- Chat conversations
- Meetings
- Emails
- Personal notes
- External documents

Important decisions must be preserved as RFCs or ADRs.

---

# Design Philosophy

Aegis follows an **Executable-by-Design** philosophy.

Engineering knowledge should exist in two complementary forms:

1. Human-readable documentation
2. Machine-readable specifications

Whenever practical, documentation should have an executable representation.

---

# Versioning

RFCs may evolve over time.

Every RFC should maintain:

- Version
- Status
- Revision history (when applicable)

Accepted RFCs should not be modified in ways that change their intent.

Significant changes require a new RFC.

---

# Referencing RFCs

RFCs should be referenced by identifier.

Examples:

```text
RFC-0001

RFC-0007

RFC-0012
```

When one RFC supersedes another, the relationship should be explicitly documented.

---

# Acceptance Criteria

An RFC is considered complete when:

- The engineering problem is clearly defined.
- The motivation is justified.
- The proposed solution is understandable.
- The impact is documented.
- Risks are identified.
- Future work is described.
- The proposal aligns with the vision of Aegis.

---

# Governance

The Aegis project follows an RFC-driven governance model.

No significant evolution of:

- ASES
- AGE
- Project Policies
- Engineering Workflows

should bypass the RFC process.

---

# References

- RFC-0001 — Project Vision, Scope and Design Principles *(constitutional document)*
- Architecture Decision Records (ADRs)
- Agent Software Engineering Standard (ASES)
- Agent Governance Engine (AGE)

---

# License

Unless otherwise specified, RFC documents are distributed under the same license as the Aegis project.
