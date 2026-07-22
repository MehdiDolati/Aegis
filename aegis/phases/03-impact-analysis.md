# Phase 3: Impact Analysis

> Understand what will change before making changes.

---

# Purpose

Before implementation, assess the full impact of the proposed changes across the system.

---

# Required Artifacts

| Artifact | Required |
|----------|----------|
| Impact Assessment | Yes |
| Affected Files List | Yes |
| Risk Level Assessment | Yes |

---

# Impact Areas

| Area | Assessment Required |
|------|---------------------|
| Source Files | Which files will be modified? |
| Components | Which components are affected? |
| Database | Any schema or data changes? |
| API | Any endpoint changes? |
| UI | Any user-facing changes? |
| Security | Any security implications? |
| Performance | Any performance impact? |
| Dependencies | Any new dependencies? |
| Infrastructure | Any deployment changes? |

---

# Risk Levels

| Level | Description | Action |
|-------|-------------|--------|
| Low | Minimal impact, easily reversible | Proceed with standard review |
| Medium | Moderate impact, some risk | Additional review required |
| High | Significant impact, high risk | Architecture review required |
| Critical | System-wide impact, breaking changes | Full team review required |

---

# Quality Gates

| Gate ID | Description | Severity |
|---------|-------------|----------|
| IMP-001 | Impact Assessment exists | Error |
| IMP-002 | All affected files identified | Error |
| IMP-003 | Risk level assessed | Error |
| IMP-004 | High/Critical risks reviewed | Error |

---

# Exit Criteria

Phase 3 is complete when:

- [ ] Impact Assessment document exists
- [ ] All affected areas identified
- [ ] Risk level determined
- [ ] High/Critical risks reviewed by appropriate authority
- [ ] All IMP gates pass

---

# References

- [ASES.md](../ASES.md) — Master standard
- [Phase 2: Requirement Review](02-requirement-review.md) — Prerequisite
