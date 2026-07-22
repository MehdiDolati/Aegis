# Task-Level Contracts

> The missing quality assurance piece in vibe coding.

---

# Overview

Vibe coding—generating code via natural-language prompts—accelerates development but introduces quality challenges. Task-level contracts provide the missing QA piece by decomposing intent into explicit, verifiable contracts.

Based on research: "VibeContract: The Missing Quality Assurance Piece in Vibe Coding" (arXiv:2603.15691)

---

# What is a Contract?

A task-level contract captures:

| Element | Description |
|---------|-------------|
| Input | What the task receives |
| Output | What the task produces |
| Constraints | Rules that must be followed |
| Behavior | Expected behavior in various scenarios |

---

# Contract Structure

```yaml
contract:
  id: CTR-0001
  task_id: T-0001
  feature_id: FEAT-0001
  
  input:
    - type: string
      name: email
      description: User email address
      constraints:
        - must be valid email format
        - must be unique in system
  
  output:
    - type: object
      name: user
      description: Created user object
      fields:
        - id: integer
        - email: string
        - created_at: timestamp
  
  constraints:
    - Password must be hashed with bcrypt
    - Email must be verified before activation
    - User must have default role
  
  behavior:
    - success: Returns user object with 201 status
    - duplicate_email: Returns 409 Conflict
    - invalid_input: Returns 400 Bad Request
    - server_error: Returns 500 Internal Server Error
```

---

# Contract Types

## Functional Contract

Defines what the code must do:

```yaml
functional:
  - requirement: FR-001
    contract: CTR-001
    description: User can log in with valid credentials
    verification: Unit test + Integration test
```

## Non-Functional Contract

Defines quality attributes:

```yaml
non_functional:
  - performance:
      response_time: < 500ms
      throughput: > 100 req/s
  
  - security:
      authentication: Required
      authorization: Role-based
      encryption: TLS 1.3
  
  - reliability:
      availability: 99.9%
      error_rate: < 0.1%
```

## Interface Contract

Defines API contracts:

```yaml
interface:
  endpoint: POST /api/users
  request:
    content_type: application/json
    body:
      email: string (required)
      password: string (required)
  response:
    success:
      status: 201
      body: User object
    error:
      status: 4xx/5xx
      body: Error object
```

---

# Contract Lifecycle

```text
Intent
   ↓
Contract Definition
   ↓
Contract Validation
   ↓
Implementation
   ↓
Contract Verification
   ↓
Deployment
```

---

# Contract Validation

Before implementation, validate:

| Check | Description |
|-------|-------------|
| Completeness | All requirements have contracts |
| Consistency | No conflicting contracts |
| Feasibility | Contracts are achievable |
| Traceability | Contracts link to requirements |

---

# Contract Verification

After implementation, verify:

| Check | Description |
|-------|-------------|
| Functional | Code meets functional contracts |
| Non-Functional | Quality attributes met |
| Interface | API contracts satisfied |
| Edge Cases | Boundary conditions handled |

---

# Traceability

Maintain traceability between:

```text
Requirement
   ↓
Contract
   ↓
Implementation
   ↓
Tests
   ↓
Documentation
```

---

# Quality Gates

| Gate ID | Description | Severity |
|---------|-------------|----------|
| CTR-001 | Contract exists for each task | Error |
| CTR-002 | Contract is validated | Error |
| CTR-003 | Contract is verified | Error |
| CTR-004 | Traceability is maintained | Warning |

---

# Benefits

Research shows contracts provide:

- **Structured development workflow**
- **Predictable, auditable processes**
- **Continuous QA alongside generation**
- **Improved correctness and maintainability**

---

# References

- VibeContract: The Missing Quality Assurance Piece in Vibe Coding (arXiv:2603.15691)
- [ASES.md](ASES.md) — Master standard
