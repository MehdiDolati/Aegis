# ISO 25010 Mapping

> Mapping ASES quality gates to international quality standards.

---

# Overview

ISO/IEC 25010 defines a quality model for software systems. This document maps ASES quality gates to ISO 25010 quality characteristics.

Based on research: "Quality Assurance of LLM-generated Code" (arXiv:2511.10271)

---

# ISO 25010 Quality Model

## Quality Characteristics

| Characteristic | Description |
|----------------|-------------|
| Functional Suitability | Degree to which functions meet needs |
| Performance Efficiency | Performance relative to resources |
| Compatibility | Degree to which system can exchange info |
| Usability | Ease of use and learnability |
| Reliability | Degree of reliability under stated conditions |
| Security | Degree of protection against threats |
| Maintainability | Ease of modification and evolution |
| Portability | Ease of transfer to another environment |

---

# ASES to ISO 25010 Mapping

## Functional Suitability

| ISO 25010 Sub-Characteristic | ASES Gate | Description |
|------------------------------|-----------|-------------|
| Functional Completeness | SPEC-003 | All acceptance criteria defined |
| Functional Correctness | VER-004 | All acceptance criteria verified |
| Functional Appropriateness | IMP-003 | Risk level assessed |

## Performance Efficiency

| ISO 25010 Sub-Characteristic | ASES Gate | Description |
|------------------------------|-----------|-------------|
| Time Behaviour | NFR-PERF | Response time requirements |
| Resource Utilization | NFR-PERF | Resource usage requirements |
| Capacity | NFR-PERF | Capacity requirements |

## Compatibility

| ISO 25010 Sub-Characteristic | ASES Gate | Description |
|------------------------------|-----------|-------------|
| Co-existence | IMP-002 | Affected components identified |
| Interoperability | IMP-002 | API impact assessed |

## Usability

| ISO 25010 Sub-Characteristic | ASES Gate | Description |
|------------------------------|-----------|-------------|
| Appropriateness Recognisability | DOC-001 | User manual updated |
| Learnability | DOC-001 | Documentation clear |
| Operability | DOC-001 | Instructions provided |
| User Error Protection | SEC-002 | Input validation |
| User Interface Aesthetics | NFR-UI | UI requirements |
| Accessibility | NFR-A11Y | Accessibility requirements |

## Reliability

| ISO 25010 Sub-Characteristic | ASES Gate | Description |
|------------------------------|-----------|-------------|
| Maturity | VER-001 | Unit tests pass |
| Availability | NFR-AVAIL | Availability requirements |
| Fault Tolerance | VER-002 | Integration tests pass |
| Recoverability | NFR-RECOVER | Recovery requirements |

## Security

| ISO 25010 Sub-Characteristic | ASES Gate | Description |
|------------------------------|-----------|-------------|
| Confidentiality | SEC-001 | No hardcoded secrets |
| Integrity | SEC-002 | Input validation |
| Non-repudiation | TRACE-001 | Traceability complete |
| Accountability | TRUST-002 | Decisions explained |
| Authenticity | SEC-004 | Authentication required |

## Maintainability

| ISO 25010 Sub-Characteristic | ASES Gate | Description |
|------------------------------|-----------|-------------|
| Modularity | MAINT-005 | Architecture compliance |
| Reusability | MAINT-004 | No code duplication |
| Analysability | MAINT-003 | Complexity within threshold |
| Modifiability | MAINT-001 | No dead code |
| Testability | VER-005 | Test coverage meets threshold |

## Portability

| ISO 25010 Sub-Characteristic | ASES Gate | Description |
|------------------------------|-----------|-------------|
| Adaptability | NFR-PORT | Adaptability requirements |
| Installability | NFR-INSTALL | Installation requirements |
| Replaceability | NFR-REPLACE | Replaceability requirements |

---

# Non-Functional Requirements Template

```yaml
non_functional_requirements:
  performance:
    response_time: < 500ms
    throughput: > 100 req/s
    resource_usage: < 80% CPU
  
  security:
    authentication: Required
    authorization: Role-based
    encryption: TLS 1.3
    secrets: No hardcoding
  
  reliability:
    availability: 99.9%
    error_rate: < 0.1%
    recovery_time: < 5 minutes
  
  maintainability:
    complexity: < 10 cyclomatic
    duplication: < 5%
    coverage: > 80%
  
  usability:
    accessibility: WCAG 2.1 AA
    documentation: Complete
    error_messages: Clear
```

---

# Quality Gates

| Gate ID | Description | Severity |
|---------|-------------|----------|
| ISO-001 | Non-functional requirements defined | Warning |
| ISO-002 | Quality characteristics addressed | Info |
| ISO-003 | Quality metrics measured | Info |

---

# References

- ISO/IEC 25010:2011 — Systems and software Quality Requirements and Evaluation
- Quality Assurance of LLM-generated Code (arXiv:2511.10271)
- [ASES.md](ASES.md) — Master standard
