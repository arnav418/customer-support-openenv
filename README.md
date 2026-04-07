---
title: Customer Support Environment
emoji: "🤖"
colorFrom: "blue"
colorTo: "green"
sdk: docker
app_port: 8000
---

# Customer Support OpenEnv Environment

## Overview

This project implements a real-world OpenEnv environment simulating a customer support system.  
An AI agent interacts with the environment to resolve user issues like payment failures, app crashes, and billing problems.

---

## Objective

Train and evaluate agents on realistic customer support scenarios using OpenEnv APIs:

- /reset
- /step
- /state

---

## Environment Design

### Tasks

| Query                                 | Answer       | Difficulty |
| ------------------------------------- | ------------ | ---------- |
| My payment failed                     | refund       | Easy       |
| App crashes after login on Android 13 | troubleshoot | Medium     |
| Charged twice across payment methods  | refund       | Hard       |

---

### Action

- message (string): Agent response

---

### Observation

- observation (string): Feedback message
- reward (float): Score based on correctness
- done (bool): Episode completion
- info (dict): Metadata (difficulty, expected answer, steps)

---

### Reward Logic

| Condition        | Reward |
| ---------------- | ------ |
| Correct answer   | 1.0    |
| Partial keywords | 0.5    |
| Weak match       | 0.2    |
| Wrong answer     | -0.2   |

---

## Baseline Agent

A rule-based agent is implemented in `baseline.py`.

### Run:

```bash
python baseline.py
```

### Why This Environment?

This environment simulates real-world customer support workflows, making it useful for training and evaluating AI agents in practical scenarios.

It includes:

- Multi-difficulty tasks (easy → hard)
- Realistic user queries
- Structured reward feedback
- Deterministic grading

---

# NEXT STEP

Now just run:

```bash
openenv push
```
