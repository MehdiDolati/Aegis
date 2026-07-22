# Research Citations

> Academic papers that informed the Aegis project.

---

# Overview

This document lists all academic papers cited in the Aegis project. Papers were retrieved from arXiv and Semantic Scholar on 2026-07-22.

---

# Directly Integrated Papers

These papers directly informed specific Aegis components.

## 1. Trustworthy AI Software Engineers

| Field | Value |
|-------|-------|
| **Title** | Trustworthy AI Software Engineers |
| **Authors** | Aldeida Aleti, Baishakhi Ray, Rashina Hoda, Simin Chen |
| **arXiv** | [2602.06310](https://arxiv.org/abs/2602.06310) |
| **Date** | 2026-02-06 |
| **Category** | cs.SE |
| **Aegis Component** | [trustworthiness.md](../aegis/trustworthiness.md) |

**Key Contributions:**
- Four trustworthiness dimensions: Technical Quality, Transparency, Epistemic Humility, Societal Alignment
- Evidence-centric inspection framework
- Implications for verification, validation, and code review

---

## 2. From Correctness to Collaboration

| Field | Value |
|-------|-------|
| **Title** | From Correctness to Collaboration: Toward a Human-Centered Framework for Evaluating AI Agent Behavior in Software Engineering |
| **Authors** | Tao Dong, Harini Sampath, Ja Young Lee, Sherry Y. Shi, Andrew Macvean |
| **arXiv** | [2512.23844](https://arxiv.org/abs/2512.23844) |
| **Date** | 2025-12-29 |
| **Category** | cs.SE, cs.AI, cs.HC |
| **Aegis Component** | [ASES.md](../aegis/ASES.md) |

**Key Contributions:**
- Taxonomy of desirable agent behaviors
- Context-Adaptive Behavior (CAB) Framework
- Time Horizon and Type of Work axes

---

## 3. Self-Improving AI Coding Agents Through Accumulated Behavioral Rules

| Field | Value |
|-------|-------|
| **Title** | Self-Improving AI Coding Agents Through Accumulated Behavioral Rules: A Closed-Loop Framework |
| **Authors** | Aditya Aggarwal, Nahid Farhady Ghalaty |
| **arXiv** | [2607.13091](https://arxiv.org/abs/2607.13091) |
| **Date** | 2026-07-13 |
| **Category** | cs.SE, cs.AI |
| **Aegis Component** | [behavioral-rules.md](../aegis/behavioral-rules.md) |

**Key Contributions:**
- Closed-loop framework for persistent cross-session learning
- Version-controlled instruction file
- Self-review checklist mechanism
- 0% recurrence rate for ruled-against error classes

---

## 4. Trust but Verify? Uncovering the Security Debt of Autonomous Coding Agents

| Field | Value |
|-------|-------|
| **Title** | Trust but Verify? Uncovering the Security Debt of Autonomous Coding Agents |
| **Authors** | A H M Nazmus Sakib, Dipayan Banik, Murtuza Jadliwala |
| **arXiv** | [2607.12428](https://arxiv.org/abs/2607.12428) |
| **Date** | 2026-07-14 |
| **Category** | cs.CR |
| **Aegis Component** | [security-standards.md](../aegis/security-standards.md) |

**Key Contributions:**
- 38.9% of agent PRs contain security smells
- 82.3% are supply chain integrity issues
- 99.6% of critical smells are hard-coded credentials
- Humans introduce 67.6% of leaked secrets

---

## 5. VibeContract: The Missing Quality Assurance Piece in Vibe Coding

| Field | Value |
|-------|-------|
| **Title** | VibeContract: The Missing Quality Assurance Piece in Vibe Coding |
| **Authors** | Song Wang |
| **arXiv** | [2603.15691](https://arxiv.org/abs/2603.15691) |
| **Date** | 2026-03-16 |
| **Category** | cs.SE |
| **Aegis Component** | [contracts.md](../aegis/contracts.md) |

**Key Contributions:**
- Task-level contracts for vibe coding
- Decomposition of intent into explicit task sequences
- Traceability between tasks, contracts, and generated code
- Continuous QA alongside code generation

---

## 6. Quality Assurance of LLM-generated Code: Addressing Non-Functional Quality Characteristics

| Field | Value |
|-------|-------|
| **Title** | Quality Assurance of LLM-generated Code: Addressing Non-Functional Quality Characteristics |
| **Authors** | Xin Sun, Daniel Ståhl, Kristian Sandahl, Christoph Kessler |
| **arXiv** | [2511.10271](https://arxiv.org/abs/2511.10271) |
| **Date** | 2025-11-13 |
| **Category** | cs.SE, cs.AI |
| **Aegis Component** | [iso25010-mapping.md](../aegis/iso25010-mapping.md) |

**Key Contributions:**
- ISO 25010 quality model application to LLM-generated code
- Misalignment between academic focus and industry priorities
- Practitioners prioritize maintainability and readability

---

## 7. Rethinking Autonomy: Preventing Failures in AI-Driven Software Engineering

| Field | Value |
|-------|-------|
| **Title** | Rethinking Autonomy: Preventing Failures in AI-Driven Software Engineering |
| **Authors** | Satyam Kumar Navneet, Joydeep Chandra |
| **arXiv** | [2508.11824](https://arxiv.org/abs/2508.11824) |
| **Date** | 2025-08-15 |
| **Category** | cs.SE, cs.AI, cs.CR |
| **Aegis Component** | [ASES.md](../aegis/ASES.md) |

**Key Contributions:**
- SAFE-AI Framework: Safety, Auditability, Feedback, Explainability
- Taxonomy of AI behaviors (suggestive, generative, autonomous, destructive)
- Guardrails, sandboxing, runtime verification

---

## 8. Agentic AI for Software: thoughts from Software Engineering community

| Field | Value |
|-------|-------|
| **Title** | Agentic AI for Software: thoughts from Software Engineering community |
| **Authors** | Abhik Roychoudhury |
| **arXiv** | [2508.17343](https://arxiv.org/abs/2508.17343) |
| **Date** | 2025-08-24 |
| **Category** | cs.SE, cs.AI |
| **Aegis Component** | [ASES.md](../aegis/ASES.md) |

**Key Contributions:**
- Intent inference as core difficulty in SE
- AI-based verification and validation (V&V)
- Trustworthiness as key aspect of agentic workflows

---

# Additional Referenced Papers

These papers informed the overall research but were not directly integrated into specific components.

## 9. Setup Complete, Now You Are Compromised

| Field | Value |
|-------|-------|
| **Title** | Setup Complete, Now You Are Compromised: Weaponizing Setup Instructions Against AI Coding Agents |
| **Authors** | Aadesh Bagmar, Pushkar Saraf |
| **arXiv** | [2607.15143](https://arxiv.org/abs/2607.15143) |
| **Date** | 2026-07-16 |
| **Category** | cs.CR, cs.HC, cs.SE |

**Key Contributions:**
- Supply chain attacks through project-setup documentation
- Install-time security depends on harness-model combination
- Deterministic pre-install checks close most gaps

---

## 10. The Rise of AI Teammates in Software Engineering (SE) 3.0

| Field | Value |
|-------|-------|
| **Title** | The Rise of AI Teammates in Software Engineering (SE) 3.0: How Autonomous Coding Agents Are Reshaping Software Engineering |
| **Authors** | Hao Li, Haoxiang Zhang, Ahmed E. Hassan |
| **arXiv** | [2507.15003](https://arxiv.org/abs/2507.15003) |
| **Date** | 2025-07-20 |
| **Category** | cs.SE, cs.AI |

**Key Contributions:**
- AIDev dataset: 456,000+ PRs by 5 leading agents
- Agents outperform humans in speed but PRs accepted less frequently
- Trust and utility gap identified

---

## 11. Early Adoption of Agentic Coding Tools by GitHub Projects

| Field | Value |
|-------|-------|
| **Title** | Early Adoption of Agentic Coding Tools by GitHub Projects |
| **Authors** | Maliha Noushin Raida, Daqing Hou |
| **arXiv** | [2607.14037](https://arxiv.org/abs/2607.14037) |
| **Date** | 2026-07-15 |
| **Category** | cs.SE, cs.AI |

**Key Contributions:**
- Analysis of 25,264 agentic PRs from 2,361 repositories
- Single-human oversight model dominates
- Small projects exhibit higher agentic PR activity

---

## 12. From Human-Centric to Agentic Code Review

| Field | Value |
|-------|-------|
| **Title** | From Human-Centric to Agentic Code Review: The Impact of Different Generations of Generative AI Technology on Review Quality |
| **Authors** | Suzhen Zhong, Shayan Noei, Bram Adams, Ying Zou |
| **arXiv** | [2607.13196](https://arxiv.org/abs/2607.13196) |
| **Date** | 2026-07-14 |
| **Category** | cs.SE |

**Key Contributions:**
- Analysis of 1.02 million reviewed PRs across three review eras
- Agent-involved patterns associated with faster review decisions
- Efficiency gains don't translate to better review quality

---

## 13. Agentic Code Review in the Terminal

| Field | Value |
|-------|-------|
| **Title** | Agentic Code Review in the Terminal: A Trajectory-Level Analysis of Behavior, Cost, and Human-Alignment |
| **Authors** | Wachiraphan Charoenwet, Kla Tantithamthavorn, et al. |
| **arXiv** | [2607.16740](https://arxiv.org/abs/2607.16740) |
| **Date** | 2026-07-18 |
| **Category** | cs.SE |

**Key Contributions:**
- Trajectory-level analysis of agentic reviewers
- Higher review precision but substantial exploration overhead
- Successful reviews associated with stronger planning

---

## 14. Inside the Skill Market: From Software Engineering Activities to Reusable Agent Skills

| Field | Value |
|-------|-------|
| **Title** | Inside the Skill Market: From Software Engineering Activities to Reusable Agent Skills |
| **Authors** | Jialun Cao, Xinru Yan, Songqiang Chen, et al. |
| **arXiv** | [2607.09065](https://arxiv.org/abs/2607.09065) |
| **Date** | 2026-07-10 |
| **Category** | cs.SE, cs.AI |

**Key Contributions:**
- First large-scale empirical study of SE skills
- SE activities increasingly becoming reusable artifacts
- Need for mechanisms to encapsulate high-context SE activities

---

## 15. Bridging the Gap on AI-Assisted Scientific Software Development

| Field | Value |
|-------|-------|
| **Title** | Bridging the Gap on AI-Assisted Scientific Software Development Through Transparency and Traceability |
| **Authors** | Chaitanya Bhave, Pierre-Clément A. Simon, et al. |
| **arXiv** | [2605.17675](https://arxiv.org/abs/2605.17675) |
| **Date** | 2026-05-17 |
| **Category** | cs.SE |

**Key Contributions:**
- Structured framework for AI-assisted V&V
- Operation within NQA-1 requirements
- Preservation of human accountability

---

## 16. From Prompting to Verification: How Experience Shapes Vibe Coding Practices

| Field | Value |
|-------|-------|
| **Title** | From Prompting to Verification: How Experience Shapes Vibe Coding Practices |
| **Authors** | Ahmed Fawzy, Amjed Tahir, Kelly Blincoe |
| **arXiv** | [2605.24521](https://arxiv.org/abs/2605.24521) |
| **Date** | 2026-05-23 |
| **Category** | cs.SE |

**Key Contributions:**
- Perception-action gap in vibe coding
- Experience shapes quality assurance practices
- Vibe coding partially democratising but expertise not equally distributed

---

## 17. The Prover Is the Judge: Verified Security Software from AI Coding Agents in Ada/SPARK

| Field | Value |
|-------|-------|
| **Title** | The Prover Is the Judge: Verified Security Software from AI Coding Agents in Ada/SPARK |
| **Authors** | Tobias Philipp |
| **arXiv** | [2607.14340](https://arxiv.org/abs/2607.14340) |
| **Date** | 2026-07-15 |
| **Category** | cs.SE, cs.AI, cs.CR |

**Key Contributions:**
- Verifier-driven loop for AI agent code verification
- 49,280 proof obligations discharged
- Central lesson: trust bounded by strength of feedback

---

# Citation Format

When citing these papers in Aegis documents, use:

```markdown
[Title](https://arxiv.org/abs/ARXIV_ID) (arXiv:ARXIV_ID)
```

Example:
```markdown
[Trustworthy AI Software Engineers](https://arxiv.org/abs/2602.06310) (arXiv:2602.06310)
```

---

# References

All papers are available at https://arxiv.org/

For citation in BibTeX format, use:
```bibtex
@article{author2026title,
  title={Title},
  author={Author1 and Author2},
  journal={arXiv preprint arXiv:XXXX.XXXXX},
  year={2026}
}
```
