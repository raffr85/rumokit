---
name: verify-project-name
description: Use when an agent must verify a specific project's behavior through its real product surface.
---

# Verify the Project

Replace `project-name` in the skill name and directory with the project's concise identifier.

## Preconditions and diagnosis

List required tools, environment, safe credentials or fixtures, exact checks, and recoverable failure guidance.

Identify the expected checkout or build, environment, account or tenant, and process or port ownership. Distinguish the intended instance from a healthy but unrelated one.

## Launch and readiness

Provide exact project commands, working directories, expected ports or processes, and a positive readiness observation.

## State setup and isolation

Describe deterministic fixtures, tenant or account selection, unique test data, and how parallel or repeated runs avoid collisions.

## Drive the product surface

For each supported feature, record the public entry point, actions, expected behavior, negative or preservation case, and authoritative observable.

## Evidence

Record artifact identity, actions, expected and actual results, and useful logs, screenshots, responses, or state reads.

## Cleanup and recovery

Provide exact cleanup, shutdown, rollback, and stale-state recovery steps.

Retain the evidence needed to explain the result before cleanup. Name the resources this task owns and preserve unrelated processes, fixtures, and failure evidence.

## Feature map

| Feature or claim | Entry point | Required state | Authoritative evidence | Known gap |
| --- | --- | --- | --- | --- |
