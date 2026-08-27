# Resource-Oriented at the Core: An API Architecture for Governing at Scale

## The Thesis

All API value ultimately traces back to data. Every business action — placing an order, updating a patient record, adjusting a price — is, underneath, a read or write against some resource. If that's true, then the architecture should say so explicitly: **build one tightly-governed, resource-oriented API layer that is the canonical interface to data, and let everything else — business workflows, UI-specific views, agent-facing tools — be built *on top of* it, not beside it.**

This isn't a new idea in isolation — it's the same insight behind MuleSoft's System/Process/Experience API model, and behind Data Mesh's separation of governed data products from the domains that consume them. What's worth arguing for here is the *governance* consequence of that layering: concentrate control where data actually lives, and treat everything above it as replaceable.

## Layer 1: The Resource Layer — the only layer that touches data directly

The resource-oriented API layer exposes data as **resources**, not as workflows or screens: `/patients/{id}`, `/orders/{id}`, `/claims/{id}`. It follows REST discipline strictly — resources identified by URI, standard verbs, representations independent of any consumer. It does not know or care whether the caller is a mobile app, a partner integration, or an AI agent.

This is the layer where **data governance and API governance become the same governance**:

- **Ownership** — every resource maps to a data domain with a named owner, same as a data catalog entry.
- **Classification and access control** — field-level sensitivity (PII, PHI, financial) is enforced here, once, not reimplemented in every downstream API that happens to touch the same field.
- **Schema and lineage** — the resource API *is* the contract; changes to it are the only legitimate way the underlying data model surfaces externally.
- **Authentication/authorization** — identity and entitlement checks live here and only here. Nothing above this layer is allowed to make its own authorization decision about data access; it can only pass through or narrow what the resource layer already granted.

This is deliberately the slowest-moving, most heavily reviewed layer in the architecture. Adding a resource, or a field to a resource, should require going through the same rigor as adding a new data asset to a governed data platform — because that's what it actually is.

## Layer 2: The Process/Business Layer — this is where the original claim needs a correction

Here's the part of the original framing worth pushing back on: **"other APIs with business logic or UI-oriented logic" is doing too much work by treating those as one category.** They are not the same risk class, and collapsing them is where the architecture would leak.

**Business logic must stay governed, almost as tightly as the resource layer** — because business logic encodes *invariants*, not presentation. "An order cannot be cancelled after it has shipped." "A discount cannot be applied twice." "A claim above $X requires secondary approval." These rules are not decoration on top of data; they are part of what makes the data *correct*. If three different teams each build their own "cancel order" endpoint with slightly different business rules, you don't get harmless UI sprawl — you get **data integrity drift**, silently, because each variant writes back to the same resource through a different, unaudited path.

So the architecture needs three layers, not two:

1. **Resource/System layer** — tightly governed, aligned with data governance. (as above)
2. **Process/Business layer** — a smaller, deliberately curated set of APIs that encode business invariants and cross-resource orchestration (e.g., `POST /orders/{id}/cancel`, `POST /claims/{id}/approve`). This layer is *built on* the resource layer and *must* enforce every invariant by writing through it — never around it. It is governed more lightly than the resource layer (teams can add new business operations without a data-governance review), but it is still catalogued, owned, and versioned, because business-rule consistency across the company depends on it.
3. **Experience/UI layer** — thin, presentation-shaped APIs (BFFs, GraphQL gateways, agent-facing tool wrappers) that aggregate, filter, and format calls to the layers below. This is the *only* layer where the original claim — "we do not care about sprawl" — actually holds.

## Why sprawl is genuinely tolerable at the Experience layer (and only there)

The reason unmanaged growth is dangerous at the resource layer but tolerable at the experience layer isn't arbitrary — it comes down to what each layer is allowed to *own*:

| | Resource layer | Process layer | Experience layer |
|---|---|---|---|
| Owns data | Yes | No (writes through resource layer) | No |
| Owns business invariants | No | Yes | No |
| Owns identity/authz decisions | Yes (source of truth) | No (inherits) | No (inherits) |
| Can be deleted with no consequence beyond its own callers | No | No | **Yes** |

An experience-layer API that just reshapes calls to Layer 1 and Layer 2 is, by construction, stateless and disposable. If a team builds a bespoke BFF for one mobile screen and it never gets cleaned up, that's clutter — annoying, worth periodic pruning — but it cannot corrupt data, bypass an authorization rule, or create two conflicting versions of a business rule, **provided the architecture enforces one non-negotiable constraint**: experience-layer APIs are prohibited from talking directly to the underlying data store or reimplementing auth/business logic themselves. They may only call down through Layer 2 (or Layer 1 for pure reads). That constraint is what makes "we don't care about sprawl here" true rather than wishful.

This is structurally the same trade Data Mesh makes with **federated computational governance**: strict, centrally-defined rules for how data products are exposed and governed, combined with domain teams having full autonomy to build and evolve what sits on top of those products. Autonomy is safe precisely because the thing that matters (the data product's contract, quality, and access rules) is governed centrally; everything downstream of that contract is free to multiply.

## Enforcement, not policy: how to make this real

A layering diagram is not an architecture until it's enforced mechanically:

- **The resource layer sits behind a gateway that rejects any unauthenticated or unauthorized call by default** — no experience or process API can get data it wasn't entitled to, no matter how it was built.
- **Only the resource layer may hold a direct database connection or data-store credential.** Process and experience layers are network-restricted to calling APIs, not stores — this is what actually prevents a bespoke UI API from becoming a second source of truth.
- **A CI/CD registration gate applies to Layers 1 and 2**, not Layer 3: new resources and new business operations must be catalogued with an owner and a spec before they ship. Experience-layer APIs can deploy freely.
- **Business invariants live in code that only the process layer imports**, so two process APIs can't silently diverge on what "cancel" means — they call the same underlying rule implementation.

## Implication for AI agents

This layering also answers a question implicit in a lot of current agent-integration pain: **which layer should an agent talk to?** Not the experience layer — it's UI-shaped, undocumented in machine-readable form, and multiplies per screen. Agents should be pointed at the process layer (for actions) and the resource layer (for reads), because those are the layers with stable contracts, enforced invariants, and real governance. Every bespoke "agent API" built at the experience layer instead is just sprawl one level up, dressed as an integration.

## Conclusion

The instinct that "the API must align with resources, not the UI" is correct as a foundation, but the architecture needs one more distinction to be defensible: **business logic is not UI logic.** Business rules must be governed nearly as tightly as the data they act on, because they are the mechanism by which data stays correct. What can genuinely be left to multiply without oversight is the thin presentation layer above both — and only because it is architecturally prevented from owning data, identity, or invariants of its own. Concentrate governance where consequence lives; let autonomy flourish exactly where it's structurally harmless.

## Sources

- [API Handyman — Organizing APIs in System, Business, and Experience Layers](https://apihandyman.io/organizing-apis-in-layers-system-business-and-experience-apis/)
- [Customer Experience APIs: The missing layer — Medium/navalia](https://medium.com/navalia/customer-experience-apis-the-missing-layer-58ecb93faa4b)
- [What is Data Mesh? — Reltio](https://www.reltio.com/glossary/data-infrastructure/what-is-a-data-mesh/)
- [Data Mesh: Federated Computational Governance — Starburst](https://www.starburst.io/blog/data-mesh-and-starburst-federated-computational-governance/)
- [The 4 principles of data mesh — dbt Labs](https://www.getdbt.com/blog/the-four-principles-of-data-mesh)
