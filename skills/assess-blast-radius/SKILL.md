---
name: assess-blast-radius
description: Use when a proposed or completed change touches a shared contract, boundary, state shape, dependency, or behavior whose downstream consumers are materially uncertain.
---

# Assess Blast Radius

Add concrete impact obligations to the primary owner. Do not take ownership of the final result.

## Start from the changed boundary

Name the symbol, contract, schema, event, configuration, generated artifact, state transition, command, or public behavior that may change. Trace outward to actual:

- callers and consumers;
- serializers, generated code, migrations, fixtures, and caches;
- failure, retry, authorization, and concurrency paths;
- versioned or out-of-repository dependencies.

Use search, dependency metadata, history, and runtime evidence. Do not replace tracing with a generic risk checklist.

## Convert impact into safety facts

For each material consumer, state what could break and the smallest observation that would clear or expose the risk. Prove the one or two highest-value safety facts when cheap and within the owner's authority.

Escalate to `coordinate-change` when impact crosses independently versioned components. Stop expanding when a path is unsupported speculation or no longer material to the requested outcome.

## Return obligations to the owner

Report:

- the changed boundary;
- confirmed consumers and evidence;
- concrete risks;
- safety facts already cleared;
- unproven obligations and why they matter.

Do not claim exhaustive coverage unless the dependency boundary itself is authoritative and complete.
