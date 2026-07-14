# PAT-001 Figure Descriptions

**Patent family:** PAT-001 — Transition-Table-Native Dynamic Micro-Node Computing

**Status:** Working figure plan for filing review. These descriptions organize already documented architecture and verified runtime behavior. They are not legal conclusions and do not establish claim scope, novelty, priority, or inventorship.

## Figure set

### FIG. 1 — Governed micro-node system overview

Show a manifest or governed transition request entering a bounded runtime that contains:

1. manifest/request intake;
2. transition-table role resolver;
3. authority checker;
4. admissibility gate;
5. bounded decision role;
6. receipt issuer;
7. governed return-path carrier; and
8. reconstruction witness.

External systems should be drawn outside the bounded micro-node. The figure should distinguish operational output from execution authority and show that no governed result exits without terminal decision evidence and a receipt.

### FIG. 2 — Transition-table-native role sequence

Show the ordered role sequence:

```text
Observer
→ Interpreter
→ Authority Checker
→ Admissibility Gate
→ Decision Role
→ Receipt Issuer
→ Return-Path Carrier
→ Reconstruction Witness
```

Include terminal outcomes `ALLOW`, `DENY`, and `FAIL_CLOSED`. Show missing required evidence and unknown standing routing to fail-closed or denial rather than implicit success.

### FIG. 3 — Request, role-evidence, and receipt binding

Show the request fields being canonicalized and hashed, including transition identifier, origin system, return path, action, actor, target, scope, policy reference, and delegation reference.

Show the receipt binding:

- request hash;
- terminal decision;
- role-evidence hash;
- optional previous receipt hash; and
- resulting receipt hash.

### FIG. 4 — Governed return and reconstruction witness

Show the terminal decision and receipt hash placed into a governed return payload directed to the declared origin or destination. Show the reconstruction witness binding request, role results, receipt, and return-payload hashes.

### FIG. 5 — Capability-resolution and conditional construction flow

Working concept requiring corroboration before reliance:

```text
manifest admitted
→ required capability/addressability resolved
→ active-node registry queried
→ admissible capable node available?
   ├─ yes: route within existing bounded authority
   └─ no: authorize minimum manifest-derived node construction
```

The drawing must label the registry/query and construction stages as implementation-evidence gaps until canonical executable support is verified.

### FIG. 6 — Minimum-addressability construction boundary

Show a manifest-defined scope on one side and a constructed node on the other. The node receives only the capability, authority, tools, context, inputs, outputs, and expiry behavior required for the admitted scope. Explicitly show excluded capability remaining outside the node boundary.

### FIG. 7 — Ephemeral lifecycle and durable evidence

Working concept requiring corroboration before reliance. Show:

```text
constructed or selected node
→ governed execution
→ receipt + reconstruction evidence persisted
→ task complete
→ default expiry/destruction
```

Durable evidence remains after runtime state expires.

### FIG. 8 — Usage-evidenced delayed expiry

Working claim-refinement figure. Show delayed expiry only when an external usage signal, such as an active conversation, stream, pending response, or coupled operation, remains valid. Show that heartbeat/liveness alone does not renew the lease.

### FIG. 9 — Bounded context retention without authority expansion

Show retained context inside an existing boundary while authority, addressability, tooling, and permitted outputs remain unchanged. Any requested expansion must return through manifest admission and transition-table evaluation.

### FIG. 10 — Comparative conventional and governed runtime posture

Compare:

- persistent generalized agent or worker with retained excess capability; and
- manifest-bounded micro-node with explicit role coverage, fail-closed behavior, receipt generation, governed return, reconstruction, and expiry.

Avoid unsupported performance measurements. The comparison should be architectural, not quantitative.

## Drawing preparation rules

- Use neutral component names and numbered reference labels.
- Keep verified July 2 runtime behavior visually distinct from later claim refinements.
- Do not depict an unverified registry, constructor, expiry controller, or lease mechanism as completed implementation.
- Keep human filing, certification, and patent-office submission outside the runtime figures.
- Preserve source references for every illustrated component in the claim-element evidence map.
