# Security Standards

> Security is not optional.

---

# Overview

Security must be considered at every phase. Sensitive data must be protected, and security vulnerabilities must be identified and resolved.

Based on research: "Trust but Verify? Uncovering the Security Debt of Autonomous Coding Agents" (arXiv:2607.12428)

---

# Key Research Findings

- **38.9%** of agent PRs contain security smells
- **82.3%** are supply chain integrity issues
- **99.6%** of critical smells are hard-coded credentials
- Humans introduce **67.6%** of leaked secrets
- Review processes miss **81.1%** of credentials

---

# Security Requirements

## Data Protection

| Requirement | Description |
|-------------|-------------|
| No hardcoded secrets | API keys, passwords must not be in code |
| Secure storage | Use environment variables or secret managers |
| Data classification | Classify data by sensitivity |
| Access control | Implement least privilege |

## Input Validation

| Requirement | Description |
|-------------|-------------|
| Validate all inputs | Never trust user input |
| Sanitize outputs | Prevent XSS and injection |
| Parameterized queries | Prevent SQL injection |
| File upload validation | Validate type, size, content |

## Authentication & Authorization

| Requirement | Description |
|-------------|-------------|
| Secure authentication | Use proven authentication methods |
| Session management | Secure session handling |
| Authorization checks | Verify permissions at every access |
| Audit logging | Log security-relevant events |

## Dependencies

| Requirement | Description |
|-------------|-------------|
| Known vulnerabilities | Check for known CVEs |
| License compliance | Verify license compatibility |
| Minimal dependencies | Reduce attack surface |
| Regular updates | Keep dependencies current |

## Supply Chain Security

| Requirement | Description |
|-------------|-------------|
| Package verification | Verify package names and sources |
| Registry validation | Use trusted registries only |
| Version pinning | Pin dependency versions |
| Integrity checks | Verify package integrity |

## Credential Security

| Requirement | Description |
|-------------|-------------|
| No hardcoded secrets | Never commit secrets to code |
| Secret scanning | Run secret scanning before commit |
| Credential rotation | Rotate credentials regularly |
| Access review | Review credential access |

---

# Agent Security

When using AI coding agents:

| Requirement | Description |
|-------------|-------------|
| Sensitive data separation | Never paste secrets into prompts |
| Workspace indexing | Exclude sensitive files from indexing |
| Data usage settings | Opt-out of training data usage |
| Permission verification | Verify agent security settings |
| Pre-install verification | Verify packages before installation |
| Source validation | Validate package sources |

---

# Security Checklist

- [ ] No hardcoded secrets
- [ ] Input validation implemented
- [ ] Output sanitization implemented
- [ ] Authentication required
- [ ] Authorization verified
- [ ] Dependencies reviewed
- [ ] Supply chain verified
- [ ] Secret scanning passed
- [ ] Sensitive data protected
- [ ] Audit logging enabled

---

# Quality Gates

| Gate ID | Description | Severity |
|---------|-------------|----------|
| SEC-001 | No hardcoded secrets | Error |
| SEC-002 | Input validation implemented | Error |
| SEC-003 | Dependencies reviewed | Error |
| SEC-004 | Authentication required | Error |
| SEC-005 | Authorization verified | Error |
| SEC-006 | Supply chain verified | Error |
| SEC-007 | Secret scanning passed | Error |

---

# References

- [ASES.md](ASES.md) — Master standard
- Trust but Verify? Uncovering the Security Debt (arXiv:2607.12428)
- Setup Complete, Now You Are Compromised (arXiv:2607.15143)
- OWASP Top 10
- [Phase 3: Impact Analysis](phases/03-impact-analysis.md)
