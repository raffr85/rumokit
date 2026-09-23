---
name: coordinate-change
description: Use when a requested outcome crosses independently versioned repositories, services, packages, schemas, generated artifacts, owners, or release steps that must remain compatible.
---

# Coordinate a Change

Add dependency and integration topology to the primary owner. Cross-repository work may remain inline; coordination does not imply delegation.

## Reconstruct the real topology

Inventory the participating components and their current revisions or states. Trace concrete producer-consumer edges: API, schema, event, package, database, configuration, generated output, deployment, or operational dependency.

Do not assume the supplied repository list is complete. Search manifests, code, automation, history, and runtime configuration for hidden consumers. Mark unknowns explicitly. Distinguish components needing inspection, compatibility verification, and edits; the dependency inventory is not an edit list.

Establish how each affected component is actually built and shipped. Local workspace overrides can hide unpublished or incompatible dependencies. When delivery builds a component independently, verify that mode with its declared versions as well as any relevant integrated mode. Do not require isolated builds for components that are intentionally shipped only as one workspace.

Use [assets/dependency-map.md](assets/dependency-map.md) when the topology needs durable state.

## Design compatible movement

Check that the initiating change serves the accepted outcome before deriving caller migrations. An incidental shared-library fix does not become necessary because its adoption would require more changes. For a necessary shared fix, preserve affected consumers across repositories within the existing authorization; material new behavior still requires clarification.

For each edge, record ownership, old and new contract, compatibility direction, migration or generation step, allowed mixed-version states, rollback boundary, and integration evidence. Derive the dependency order as a directed graph, not a narrative sequence.

Make migration or generation steps idempotent when retries or resumption are possible, or expose the unsafe repeat boundary.

Parallel work is safe only when graph edges and writable state permit it. Use `delegate-work` only when delegation adds value.

## Return coordination obligations

Provide:

- component and revision inventory;
- dependency edges and unknown consumers;
- compatibility and migration rules;
- dependency and release order;
- per-component, per-edge, and integrated evidence;
- the integration owner and remaining external actions.

Do not collapse repository-local green checks into proof of the integrated system.
