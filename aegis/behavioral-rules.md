# Behavioral Rules

> Accumulated rules for persistent cross-session learning.

---

# Overview

AI coding agents repeat the same classes of mistakes across sessions because they lack a mechanism to retain corrections from human review feedback. Behavioral rules address this by codifying accepted review comments as persistent rules.

Based on research: "Self-Improving AI Coding Agents Through Accumulated Behavioral Rules" (arXiv:2607.13091)

---

# Framework

## Components

1. **Version-Controlled Instruction File** — Accumulating rule set
2. **Self-Review Checklist** — Executed before code submission
3. **Automated Validation** — Ensures rule set integrity

---

# Version-Controlled Instruction File

Store behavioral rules in a version-controlled file:

```markdown
# Behavioral Rules

## Rule Categories

### Code Style
- BR-001: Use consistent naming conventions
- BR-002: Follow project formatting standards

### Testing
- BR-003: Write tests for all new code
- BR-004: Ensure tests are deterministic

### Security
- BR-005: Never hardcode secrets
- BR-006: Validate all inputs

### Documentation
- BR-007: Update documentation with code changes
- BR-008: Write clear commit messages
```

---

# Self-Review Checklist

Before code submission, agents must execute:

```markdown
## Self-Review Checklist

### Code Quality
- [ ] Code follows naming conventions
- [ ] No dead code
- [ ] No unused imports
- [ ] Complexity within threshold

### Testing
- [ ] Tests written for new code
- [ ] All tests pass
- [ ] Edge cases covered

### Security
- [ ] No hardcoded secrets
- [ ] Inputs validated
- [ ] Dependencies reviewed

### Documentation
- [ ] Relevant docs updated
- [ ] Commit message is descriptive
- [ ] Changes are traceable
```

---

# Rule Accumulation

Rules accumulate over time through:

## 1. Review Feedback

When a human reviewer catches an issue:
1. Document the issue
2. Create a rule to prevent it
3. Add to the instruction file
4. Validate rule integrity

## 2. Incident Analysis

When an incident occurs:
1. Analyze root cause
2. Create a rule to prevent recurrence
3. Add to the instruction file
4. Update self-review checklist

## 3. Pattern Detection

When patterns emerge:
1. Identify recurring issues
2. Create a rule to address the pattern
3. Add to the instruction file
4. Train on the pattern

---

# Rule Structure

Every behavioral rule must have:

| Field | Description |
|-------|-------------|
| ID | Unique identifier (BR-XXX) |
| Category | Rule category |
| Description | What the rule requires |
| Rationale | Why the rule exists |
| Evidence | How to verify compliance |
| Exceptions | When the rule can be skipped |

---

# Quality Gates

| Gate ID | Description | Severity |
|---------|-------------|----------|
| BR-001 | Behavioral rules file exists | Error |
| BR-002 | Self-review checklist executed | Error |
| BR-003 | Rules are followed | Warning |
| BR-004 | New rules are added when needed | Info |

---

# Benefits

Research shows behavioral rules achieve:

- **0% recurrence rate** for ruled-against error classes
- **Cross-session learning** without weight updates
- **Transfer across heterogeneous agent interfaces**
- **Shift from low-level to design-level review**

---

# References

- Self-Improving AI Coding Agents Through Accumulated Behavioral Rules (arXiv:2607.13091)
- [ASES.md](ASES.md) — Master standard
