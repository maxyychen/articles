# Treat Your AI Agent Like a New Hire

**What decades of personnel security already taught us about governing non-human workers.**

---

Would you give a new intern unlimited production database access on their first day? No manager. No acceptable use policy. No background check. Just hand them the admin credentials and tell them to "be careful."

Of course not.

Then why did we do exactly that with our AI agents?

---

## Agents are employees. We just forgot to onboard them.

Every conversation I have about "AI governance" eventually lands on the same realization: this isn't a new problem. It's an old problem wearing new clothes.

An AI agent is a worker. It has credentials. It accesses systems. It makes decisions. It can cause harm — intentionally (through adversarial input) or unintentionally (through error, drift, or hallucination).

The security profession has spent forty years figuring out how to govern workers like that. We call them *humans*. The controls already exist — we just need to apply them to our new non-human colleagues.

Here's the mapping.

---

## 1. Segregation of Duties: the highest-leverage idea you're probably ignoring

A classic example from financial controls: the person who prints the checks must not be able to change the payee. The person who requests a payment must not be the one who approves it. One person, end-to-end control of a sensitive transaction, is how fraud happens.

Now look at your agent architecture. Is there a single agent that:
- Drafts the email **and** sends it?
- Generates the SQL **and** executes it?
- Proposes the code change **and** merges it to main?
- Summarizes the invoice **and** approves the payment?

If yes, you've violated segregation of duties. The fix isn't more guardrails on one agent — it's splitting the workflow so a second actor (another agent, or a human) has to approve before execution.

Collusion between two agents is possible but harder, slower, and far more detectable. That's the whole point.

## 2. Role-Based Access Control + Least Privilege

Give each agent the minimum tools and data it needs — not a kitchen-sink toolbelt "in case it needs it later."

- Scope credentials to the specific APIs required.
- Use just-in-time tokens instead of long-lived keys.
- Separate "read" agents from "write" agents.
- Don't let the customer support agent query the HR database because both live in the same vector store.

Fewer privileges → smaller blast radius when (not if) something goes wrong.

## 3. Need-to-Know: data scoping, not just access scoping

RBAC controls which tools the agent can call. Need-to-know controls what data the agent can see. Retrieval filters, row-level security on embeddings, field-level redaction — these are not optional.

An agent that "just summarizes documents" doesn't need to see salary columns.

## 4. The Human Lifecycle, Applied

**Onboarding** → Staged rollout. Sandbox first, then shadow mode, then limited production, then broad deployment. Don't ship an agent the way you'd hire an intern on a handshake.

**Acceptable Use Policy** → Your system prompt, guardrails, and refusal policies are the agent's AUP. Write them like a policy document, not a clever prompt. Version them. Review them.

**Role-based training** → Domain fine-tuning, specialized prompts, curated retrieval corpora. A legal-review agent and a marketing-copy agent should not be running the same base configuration.

**Mandatory vacation / job rotation** → Periodic re-evaluation. Shadow-mode audits where a second model reviews the first's outputs. Catches drift the same way rotation catches human fraud.

**Termination** → Can you revoke an agent's access in under five minutes? Kill switch, credential rotation, session invalidation. If the answer is "we'd have to redeploy," you've failed the termination control.

## 5. Background checks → Model evals and provenance

You wouldn't hire someone without a reference check. Don't deploy a model without:
- Red-teaming results
- Capability evals relevant to the agent's role
- Provenance (who trained it, on what, with what alignment process)
- A model card, the AI equivalent of a résumé

## 6. Insider threat → Prompt injection is social engineering

The biggest category of human-caused incidents is insider threat — trusted people doing untrusted things, often because they were manipulated.

Prompt injection is the same problem. An agent with legitimate access is tricked — by a malicious document, a poisoned webpage, a crafted email — into acting against your interests. The agent didn't go rogue. It was socially engineered.

Defend accordingly: assume the agent's inputs are hostile, log every tool call, and require human approval for irreversible actions. This is the "dual control" principle your bank uses for wire transfers.

---

## What *is* genuinely new

Three things don't map neatly onto the human playbook, and they deserve explicit attention:

1. **Speed.** A human fraudster processes one transaction at a time. An agent processes ten thousand per minute. Detection windows that were fine for humans are catastrophic for agents.

2. **Non-determinism.** The same input can produce different outputs. Your audit strategy has to handle probabilistic behavior, not just deterministic logs.

3. **Accountability must be pre-assigned to a human decision-maker.** You can fire a human. You can replace a model — but replacement isn't accountability. Before deploying an agent, name the **business owner** who is accepting the risk: the executive whose process the agent serves. They own the outcome, the same way they'd own the outcome of any other business decision. The AI team builds it; the business owner is answerable for it. Without this assignment *before* deployment, you'll find yourself with no one responsible when things go wrong.

These are real differences. But they're refinements to the governance model, not replacements for it.

---

#AIGovernance #InformationSecurity #AIAgents #CyberSecurity #RiskManagement
