# Agent Interaction Standards

> How humans should interact with AI coding agents.

---

# Overview

Effective human-AI collaboration requires specific practices. This document defines how humans should interact with AI coding agents to achieve optimal results.

---

# Core Practices

## 1. Plan Before Implementation

For complex tasks, require the AI to first outline its implementation plan before writing code.

```text
Plan Mode
   ↓
Review Plan
   ↓
Approve/Modify
   ↓
Implement
```

This catches misunderstandings early.

---

## 2. Provide Specific Context

The more precise your instructions, the fewer corrections you'll need.

| Strategy | Description |
|----------|-------------|
| Scope the task | Specify file, scenario, testing preferences |
| Point to sources | Direct to documentation or code |
| Reference patterns | Point to existing codebase patterns |
| Describe symptoms | Provide symptom, location, expected fix |

---

## 3. Verify Before Accept

Never accept code without understanding it.

| Check | Description |
|-------|-------------|
| Read the code | Understand what it does |
| Run the tests | Verify it works |
| Check edge cases | Consider boundary conditions |
| Review for security | Look for vulnerabilities |

---

## 4. Manage Context Aggressively

Context window fills up fast. Manage it carefully.

| Practice | Description |
|----------|-------------|
| Clear between tasks | Use /clear between unrelated tasks |
| Start fresh sessions | New session for new tasks |
| Use subagents | Delegate research to subagents |
| Summarize long sessions | Compact when context is full |

---

## 5. Use Checkpoints for Rollback

Every prompt creates a checkpoint. Use them.

| Practice | Description |
|----------|-------------|
| Frequent commits | Make small, meaningful commits |
| Use rewind | Restore to previous state when needed |
| Don't fear rollback | Regenerating code is low-cost |

---

## 6. Course-Correct Early

Don't let the AI go too far down the wrong path.

| Signal | Action |
|--------|--------|
| Unexpected behavior | Stop and redirect |
| Repeated mistakes | Clear context and retry |
| Going off scope | Remind of scope boundaries |

---

# Task Decomposition

Decompose complex tasks into manageable units.

```text
Large Feature
   ↓
Task 1: Component A
   ↓
Task 2: Component B
   ↓
Task 3: Integration
   ↓
Task 4: Tests
   ↓
Task 5: Documentation
```

Each task should be:
- Small enough to verify independently
- Large enough to be meaningful
- Clearly defined with acceptance criteria

---

# Verification Patterns

## In-Prompt Verification

Ask the AI to run checks in the same message:

```text
Implement the function and run the tests
```

## Session-Level Verification

Set verification as a goal condition:

```text
Keep working until all tests pass
```

## Adversarial Review

Use a separate subagent to review:

```text
Use a subagent to review this code for edge cases
```

---

# Common Failure Patterns

| Pattern | Problem | Solution |
|---------|---------|----------|
| Kitchen sink session | Multiple unrelated tasks | Clear between tasks |
| Correcting over and over | Context pollution | Clear and retry with better prompt |
| Over-specified instructions | Important rules lost | Prune to essentials |
| Trust-then-verify gap | Plausible but incorrect | Always verify |
| Infinite exploration | Context fills up | Scope investigations |

---

# Quality Gates

| Gate ID | Description | Severity |
|---------|-------------|----------|
| AGENT-001 | Plan created before implementation | Warning |
| AGENT-002 | Code reviewed before acceptance | Error |
| AGENT-003 | Tests run before completion | Error |
| AGENT-004 | Context managed appropriately | Info |

---

# References

- [ASES.md](ASES.md) — Master standard
- Agentic Coding 6 Principles & 28 Practices
- Claude Code Best Practices (Anthropic)
