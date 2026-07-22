# Trustworthiness Standard

> Evidence-centric inspection for AI software engineers.

---

# Overview

Trustworthiness is a key property of AI software engineers. This document defines the dimensions of trustworthiness and how to evaluate them through evidence-centric inspection.

Based on research: "Trustworthy AI Software Engineers" (arXiv:2602.06310)

---

# Trustworthiness Dimensions

## 1. Technical Quality

AI agents must produce code that is:
- **Correct** — Meets functional requirements
- **Performant** — Meets performance requirements
- **Secure** — Follows security best practices
- **Maintainable** — Easy to understand and modify

### Evidence

| Signal | Description |
|--------|-------------|
| Test results | All tests pass |
| Coverage metrics | Coverage meets threshold |
| Security scan | No vulnerabilities found |
| Code review | Human approval |

---

## 2. Transparency and Accountability

AI agents must:
- **Explain decisions** — Justify why code was written a certain way
- **Maintain audit trails** — Log significant actions
- **Acknowledge uncertainty** — State confidence levels
- **Accept responsibility** — Don't blame others for mistakes

### Evidence

| Signal | Description |
|--------|-------------|
| Decision logs | Documented reasoning |
| Commit messages | Clear explanation of changes |
| ADRs | Architectural decisions documented |
| Uncertainty statements | Confidence levels expressed |

---

## 3. Epistemic Humility

AI agents must:
- **Recognize limitations** — Know what they don't know
- **Ask for help** — When uncertain, ask
- **Verify assumptions** — Don't assume, verify
- **Correct mistakes** — When wrong, fix it

### Evidence

| Signal | Description |
|--------|-------------|
| Questions asked | Appropriate clarifications requested |
| Assumptions stated | Explicit assumptions documented |
| Corrections made | Errors acknowledged and fixed |
| Help requested | Expert input sought when needed |

---

## 4. Societal and Ethical Alignment

AI agents must:
- **Follow norms** — Adhere to professional standards
- **Respect users** — Consider user impact
- **Protect privacy** — Handle data responsibly
- **Act ethically** — Make ethical decisions

### Evidence

| Signal | Description |
|--------|-------------|
| Standards compliance | Follows coding standards |
| Privacy checks | Data handling reviewed |
| Ethical review | Impact assessed |
| User consideration | User needs considered |

---

# Evidence-Centric Inspection

Instead of trusting raw outputs, developers should evaluate:

## Selective Signals

| Signal Type | Examples |
|-------------|----------|
| Test evidence | Test output, coverage reports |
| Review evidence | Code review comments, approvals |
| Documentation evidence | Updated docs, ADRs |
| Security evidence | Security scan results |

## Justifications

| Justification Type | Examples |
|--------------------|----------|
| Design rationale | Why this architecture? |
| Trade-off explanations | Why this approach? |
| Risk acknowledgments | What could go wrong? |
| Limitation statements | What can't this do? |

---

# Trustworthiness Checklist

Before accepting AI-generated code, verify:

- [ ] **Technical Quality**
  - [ ] Tests pass
  - [ ] Coverage meets threshold
  - [ ] No security issues
  - [ ] Code reviewed

- [ ] **Transparency**
  - [ ] Decisions explained
  - [ ] Audit trail maintained
  - [ ] Uncertainty stated

- [ ] **Epistemic Humility**
  - [ ] Limitations acknowledged
  - [ ] Assumptions stated
  - [ ] Questions asked when uncertain

- [ ] **Ethical Alignment**
  - [ ] Standards followed
  - [ ] Privacy protected
  - [ ] User impact considered

---

# Quality Gates

| Gate ID | Description | Severity |
|---------|-------------|----------|
| TRUST-001 | Decisions are explained | Warning |
| TRUST-002 | Assumptions are stated | Info |
| TRUST-003 | Uncertainty is acknowledged | Info |
| TRUST-004 | Evidence is provided | Error |

---

# References

- Trustworthy AI Software Engineers (arXiv:2602.06310)
- [ASES.md](ASES.md) — Master standard
