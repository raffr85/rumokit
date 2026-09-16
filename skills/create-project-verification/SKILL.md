---
name: create-project-verification
description: Use when a repository lacks reusable instructions for an agent to launch, drive, observe, isolate, and clean up a real product surface needed for repeated verification.
---

# Create Project Verification

Create a project-local skill that teaches an agent how to exercise this product's authoritative surface. This is product capability, not a generic benchmark harness.

## Discover the real verification path

Inspect existing scripts, documentation, application entry points, environments, accounts or fixtures, health checks, test tooling, and cleanup procedures. Run the current path where safe. Do not invent commands from framework conventions.

Choose the nearest surface that can establish the important claims: rendered UI, public API, CLI, worker behavior, migration result, device, or integrated service. Separate prerequisites the agent can establish from credentials or external state that require an owner.

## Encode reusable operations

Create a narrowly named skill in the project's supported local skill directory, preferring `.agents/skills/verify-project-name/` when compatible and replacing `project-name` with the real project identifier. Use [assets/project-verification-skill.md](assets/project-verification-skill.md) as a starting point.

Include exact instructions for:

- environment and dependency diagnosis;
- safe launch and readiness detection;
- deterministic state or fixture setup;
- driving representative features through public surfaces;
- collecting authoritative evidence;
- isolation, reset, cleanup, and common failures;
- maintaining a small feature-to-check map.

Keep secrets and machine-specific values out of the skill. Reuse existing project commands instead of wrapping them without need.

## Validate before handing off

Run at least one representative path from the new instructions and confirm cleanup. Report what the skill can prove, what remains manual or unavailable, and where it lives. Do not claim universal application coverage from one exercised path.
