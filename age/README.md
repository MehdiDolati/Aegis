# Agent Governance Engine (AGE)

> Executable governance for ASES compliance.

---

# Overview

AGE is the executable implementation of ASES. It validates compliance with the standard through automated checks, quality gate enforcement, and compliance reporting.

---

# Current Status

**Planned** — AGE is not yet implemented.

This directory contains the planned architecture and roadmap.

---

# Planned Capabilities

## Policy Enforcement

- Validate rules against project state
- Enforce quality gates
- Block progression on gate failures

## Artifact Validation

- Verify required artifacts exist
- Validate artifact structure
- Check artifact completeness

## Traceability Management

- Build traceability matrices
- Detect orphan requirements
- Detect orphan code
- Validate bidirectional links

## Quality Gate Enforcement

- Run automated checks
- Validate evidence
- Block or warn on failures

## Compliance Reporting

- Generate compliance reports
- Track compliance over time
- Identify gaps

---

# Planned Architecture

```text
AGE Core
   ↓
┌─────────────────────────────────────┐
│                                     │
│   Policy Engine    Gate Executor    │
│        ↓               ↓           │
│   Rule Validator   Evidence Checker│
│        ↓               ↓           │
│   Artifact Scanner  Trace Builder  │
│                                     │
└─────────────────────────────────────┘
   ↓
Compliance Report
```

---

# Planned Interfaces

## CLI Interface

```bash
age validate --policy policy.yaml
age check --gate VER-001
age report --feature FEAT-0001
```

## API Interface

```yaml
POST /api/v1/validate
GET /api/v1/gates/{gate_id}
GET /api/v1/report/{feature_id}
```

## Agent Integration

```yaml
# In agent adapter
on_phase_complete:
  - age validate --phase {phase}
  - age check --gate {gate}
```

---

# Roadmap

| Phase | Milestone | Status |
|-------|-----------|--------|
| 1 | ASES Standard | Complete |
| 2 | Rule Schemas | Complete |
| 3 | Core Rules | Complete |
| 4 | AGE Core | Planned |
| 5 | CLI Interface | Planned |
| 6 | Agent Integration | Planned |
| 7 | Web Dashboard | Planned |

---

# Contributing

AGE contributions are welcome. See the roadmap and pick a milestone.

---

# References

- [ASES.md](../aegis/ASES.md) — Master standard
- [Rules](../aegis/rules/) — Machine-readable rules
- [Schemas](../schemas/) — Rule schemas
