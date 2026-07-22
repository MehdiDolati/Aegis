# Documentation Standards

> Documentation is part of the product.

---

# Overview

Documentation is not optional. A feature is incomplete until its required documentation is complete.

---

# Documentation Types

## User Documentation

| Document | When Required |
|----------|---------------|
| User Manual | User-facing features |
| Administrator Guide | Admin features |
| FAQ | Common questions |
| Troubleshooting Guide | Complex features |

## Developer Documentation

| Document | When Required |
|----------|---------------|
| API Documentation | API changes |
| Architecture Documentation | Architectural decisions |
| Code Comments | Complex logic |
| README Updates | Project changes |

## Release Documentation

| Document | When Required |
|----------|---------------|
| Release Notes | Every release |
| Changelog | Every release |
| Migration Guide | Breaking changes |
| Known Issues | Identified problems |

---

# Documentation Quality

| Quality | Description |
|---------|-------------|
| Accuracy | Matches implementation |
| Completeness | All features documented |
| Clarity | Easy to understand |
| Currency | Up-to-date |
| Accessibility | Available to audience |

---

# Documentation Freshness

Documentation must be updated when:

| Trigger | Action |
|---------|--------|
| New feature | Create documentation |
| Changed feature | Update documentation |
| Bug fix | Update if user-facing |
| Breaking change | Create migration guide |
| Deprecation | Update deprecation notice |

## Freshness Check

```text
Last code change: YYYY-MM-DD
Last doc update: YYYY-MM-DD
Freshness: PASS/FAIL
```

If code was updated more recently than documentation, documentation is stale.

---

# Documentation Structure

## Feature Documentation

```text
# Feature Name

## Purpose
## Prerequisites
## How to Use
## Examples
## Limitations
## Related Features
```

## API Documentation

```text
# Endpoint

## Method
## URL
## Parameters
## Request Body
## Response
## Errors
## Examples
```

---

# Quality Gates

| Gate ID | Description | Severity |
|---------|-------------|----------|
| DOC-001 | Required docs exist | Error |
| DOC-002 | Docs match implementation | Error |
| DOC-003 | No outdated docs | Warning |
| DOC-004 | Docs are accessible | Warning |

---

# References

- [ASES.md](ASES.md) — Master standard
- [Phase 7: Documentation](phases/07-documentation.md)
