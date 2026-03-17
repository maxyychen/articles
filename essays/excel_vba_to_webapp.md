# From Excel VBA to a Modern Web App — My Experience Using AI as a Development Partner

I recently completed a project that changed how I think about software development. A user came to me with an Excel file full of VBA macros and a simple request: "Can you turn this into a web application with a better user experience?"

Instead of jumping straight into code, I decided to use AI — specifically Claude Code — as my development partner. Here's what I learned.

---

## The Process Matters More Than the Tool

It would have been easy to hand the Excel file to AI and say "build me a web app." But that approach almost always leads to rework. Instead, I followed a structured process — and let AI participate at every stage.

**Step 1: Understand before you build.**
I asked the user to provide everything — workflow documentation, SOPs, reference materials. Context is king, and AI is only as good as the information you feed it.

**Step 2: Generate requirements, not code.**
My first instruction to Claude Code was not "build this." It was "write a System Requirement Document." I also asked it to generate clarifying questions — the kind a senior business analyst would ask. I sent both the SRD and the questions back to the user for review. We went through multiple rounds of this until the requirements were rock solid.

**Step 3: Design before implementation.**
Next, I had Claude Code produce System Design and Architecture documents — API specs, UI layouts, technology choices (Django). Again, the user reviewed everything before a single line of code was written.

**Step 4: Build, test, and deploy.**
Only then did implementation begin. Claude Code wrote the codebase and created unit tests that mapped directly to the requirements. I deployed it to a test server and gave the user access to a live prototype.

**Step 5: Listen, refine, repeat.**
The user tested the prototype and gave feedback. I fed that feedback back to Claude Code. We iterated until they were happy.

**Step 6: Document everything.**
Finally, Claude Code generated a user manual and a maintenance SOP. The system was ready — not just to launch, but to live.

---

## What I Learned

**AI doesn't replace process — it accelerates it.** The same software development lifecycle that has always worked still works. Requirements, design, implementation, testing, deployment, documentation. AI just makes each phase faster and more thorough.

**The human in the middle is essential.** I served as the bridge between the end user who understood the business and the AI that could generate code and documents. I translated domain knowledge into prompts, and AI output into meaningful conversations with the user. That role — part project manager, part translator — is where the real value lies.

**AI is surprisingly good at asking questions.** One of the most valuable things Claude Code did was generate clarifying questions during the requirements phase. It spotted gaps and ambiguities that could have become costly bugs later. Using AI as a business analyst, not just a coder, was a game changer.

**Iteration beats perfection.** No first draft was final — not the SRD, not the design, not the code. Every deliverable went through feedback loops. AI made those loops fast enough that iteration felt natural, not burdensome.

---

## The Takeaway

The future of software development is not "AI writes all the code." It is humans and AI working together through a disciplined process — where AI amplifies human judgment rather than replacing it.

If you are exploring how to integrate AI into your development workflow, my advice is simple: do not skip the fundamentals. Gather requirements. Write documentation. Review before you build. Test before you ship. Document before you hand over.

AI makes all of these steps faster. But it is the process that makes the result reliable.

---

*Built with Claude Code. Managed with discipline. Delivered with confidence.*

#AI #SoftwareDevelopment #ClaudeCode #WebDevelopment #Django #DigitalTransformation #ProjectManagement #AIAssistedDevelopment
