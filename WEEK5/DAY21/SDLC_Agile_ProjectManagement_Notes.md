# SDLC, Agile & Software Project Management: Complete Notes

**Topics covered:** SDLC phases · Agile methodology · Scrum basics & sprints · Project planning & task estimation · Git/GitHub version control · Documentation & reporting practices

---

## Table of Contents
1. [SDLC](#1-sdlc-software-development-life-cycle)
2. [SDLC Models](#2-sdlc-models)
3. [Agile Methodology](#3-agile-methodology)
4. [Scrum](#4-scrum-basics--sprints)
5. [User Stories, Estimation & Backlogs](#5-user-stories-estimation--backlogs)
6. [Project Planning & Task Estimation](#6-project-planning--task-estimation)
7. [Git/GitHub Version Control](#7-gitgithub-version-control)
8. [Documentation & Reporting](#8-documentation--reporting-practices)
9. [Expected Interview Questions with Answers](#9-expected-interview-questions-with-answers)
10. [Quick Revision](#10-quick-revision)

---

## 1. SDLC (Software Development Life Cycle)

**Definition:** A structured process teams follow to plan, build, test, deliver and maintain software, from idea to production.

**Why it matters:** Without a process, projects run over budget, miss requirements and break in production. SDLC gives a roadmap, clear responsibilities and quality checkpoints.

Analogy: opening a restaurant. You plan, decide the menu, design the kitchen, cook, taste-test, open the doors, then keep improving.

### The 7 phases

| # | Phase | What happens | Output | RAG chatbot example |
|---|-------|--------------|--------|---------------------|
| 1 | **Planning** | Define goals, feasibility, scope, budget, timeline | Project plan | "Chatbot that answers from documents" |
| 2 | **Requirements** | Gather functional and non-functional needs | SRS / backlog | Upload PDFs, cite sources, respond in < 5s |
| 3 | **Design** | Architecture, database, APIs, UI | Design docs, diagrams | FastAPI + ChromaDB + LLM |
| 4 | **Development** | Write the code | Working software | Ingestion, retrieval, API endpoints |
| 5 | **Testing** | Verify it works and meets requirements | Test reports, bug fixes | Unit tests, answer-quality checks |
| 6 | **Deployment** | Release to users | Live application | Docker, Azure App Service |
| 7 | **Maintenance** | Fix, monitor, improve | Patches, new versions | Tune retrieval, monitor cost |

### Requirement types
- **Functional:** what the system does ("user can upload a PDF").
- **Non-functional:** how well it does it (performance, security, scalability, availability, usability).

### Types of testing
- **Unit:** one function/module.
- **Integration:** modules working together.
- **System:** the whole application.
- **UAT (User Acceptance Testing):** the customer confirms it meets their needs.
- **Regression:** old features still work after changes.

---

## 2. SDLC Models

| Model | How it works | Pros | Cons | Best for |
|-------|--------------|------|------|----------|
| **Waterfall** | Phases run strictly one after another | Simple, well documented | Rigid, late feedback, changes costly | Fixed, well-known requirements |
| **V-Model** | Each dev phase has a matching test phase | Strong verification | Rigid | Safety-critical systems |
| **Iterative / Incremental** | Build in repeated increments | Early working versions | Needs good planning | Growing products |
| **Spiral** | Iterations driven by risk analysis | Manages risk | Complex, costly | Large, risky projects |
| **Agile** | Short cycles with continuous feedback | Flexible, fast value | Needs customer involvement | Changing requirements |
| **DevOps** | Dev + Ops with automation and CI/CD | Fast, reliable releases | Culture and tooling investment | Continuous delivery |

**Waterfall vs Agile**

| | Waterfall | Agile |
|---|---|---|
| Flow | Sequential | Iterative |
| Change | Expensive | Welcomed |
| Delivery | At the end | Every sprint |
| Customer involvement | Start and end | Continuous |
| Documentation | Heavy | Lightweight |
| Risk | Found late | Found early |

---

## 3. Agile Methodology

**Agile** is an approach to building software in **small, frequent increments**, getting feedback each time and adapting. Instead of baking a whole cake for 8 months, bake a cupcake every 2 weeks and ask "how's this?".

### Agile Manifesto: 4 values
1. **Individuals and interactions** over processes and tools
2. **Working software** over comprehensive documentation
3. **Customer collaboration** over contract negotiation
4. **Responding to change** over following a plan

(The items on the right still matter; the left is valued *more*.)

### Core Agile principles (summary)
- Deliver working software frequently (weeks, not months).
- Welcome changing requirements, even late.
- Business people and developers work together daily.
- Build around motivated, self-organising teams.
- Simplicity: maximise the amount of work *not* done.
- Reflect and improve regularly.

### Agile frameworks
- **Scrum:** fixed-length sprints, defined roles (most popular).
- **Kanban:** continuous flow, visual board, WIP limits.
- **XP (Extreme Programming):** pair programming, TDD, CI.
- **SAFe:** Agile at large-enterprise scale.

### Scrum vs Kanban

| | Scrum | Kanban |
|---|---|---|
| Cadence | Fixed sprints | Continuous flow |
| Roles | PO, Scrum Master, Developers | No required roles |
| Changes mid-iteration | Discouraged | Anytime |
| Metric | Velocity | Cycle time, WIP |
| Board | Sprint board | Always-on board |

Kanban board columns: `Backlog → To Do → In Progress → In Review → Done`. **WIP limits** cap how many items can be in progress to avoid overload.

---

## 4. Scrum Basics & Sprints

### Roles

| Role | Responsibility |
|------|----------------|
| **Product Owner (PO)** | Owns the product vision; decides *what* to build and its priority; manages the product backlog |
| **Scrum Master** | Facilitates Scrum, removes blockers, coaches the team; a servant-leader, **not a boss** |
| **Developers (Team)** | Self-organising; decide *how* to build; deliver the increment |

### Artifacts
- **Product Backlog:** ordered list of everything the product may need (owned by the PO).
- **Sprint Backlog:** items selected for the current sprint plus the plan to deliver them.
- **Increment:** the usable, "Done" product at the end of a sprint.

### Events

| Event | Time box (2-week sprint) | Purpose |
|-------|--------------------------|---------|
| **Sprint** | 1-4 weeks (commonly 2) | Fixed period in which work is done |
| **Sprint Planning** | ≤ 4 hrs | Decide *what* and *how* for the sprint; set the **Sprint Goal** |
| **Daily Scrum (Stand-up)** | 15 min | Sync and plan the next 24 hours |
| **Sprint Review** | ≤ 2 hrs | Demo to stakeholders and gather feedback (about the **product**) |
| **Sprint Retrospective** | ≤ 1.5 hrs | Team inspects its way of working (about the **process**) |
| **Backlog Refinement** | Ongoing | Clarify, split and estimate upcoming items |

### The Scrum loop
```
Product Backlog → Sprint Planning → Sprint Backlog
      ↑                                   ↓
 Review & Retro ← Increment ← Sprint (Daily Scrum each day)
```

### Daily stand-up: 3 questions
1. What did I do yesterday?
2. What will I do today?
3. Any blockers?

Example note:
```
Yesterday: Completed PDF loader and chunking.
Today: Build embeddings + ChromaDB storage.
Blockers: Unsure about the best chunk size, will test 500 vs 1000 tokens.
```

### Definitions
- **Sprint Goal:** one sentence describing what the sprint achieves (e.g., "Working end-to-end MVP: upload → retrieve → answer").
- **Definition of Ready (DoR):** a story is clear enough to start (has acceptance criteria, is estimated, has no blockers).
- **Definition of Done (DoD):** shared checklist every story must meet (code reviewed, tests pass, documented, deployed to test env).

### Charts
- **Burndown chart:** remaining work vs time; shows if the sprint is on track.
- **Velocity chart:** story points completed per sprint.

---

## 5. User Stories, Estimation & Backlogs

### Hierarchy
```
Epic (big feature)  →  Story (user-facing piece)  →  Task (technical step)
"Document Upload"      "As a user, I upload a PDF"    "Write PDF parser"
```

### User story format
> **As a** `<role>`, **I want** `<goal>`, **so that** `<benefit>`.

Example: *As a student, I want to upload my notes as a PDF, so that the chatbot can answer questions from them.*

### INVEST checklist
**I**ndependent · **N**egotiable · **V**aluable · **E**stimable · **S**mall · **T**estable

### Acceptance criteria (Given / When / Then)
```
Given I have uploaded a PDF
When I ask a question about its content
Then the chatbot answers with a source citation
```

### Story points & velocity
- **Story points:** relative size of work (Fibonacci: 1, 2, 3, 5, 8, 13), not hours.
- **Planning Poker:** team members vote; discuss big differences; re-vote.
- **Velocity:** points a team completes per sprint, used to forecast how much fits in future sprints.

### Sample backlog (capstone)

| ID | User story | Points | Priority |
|----|-----------|--------|----------|
| US-01 | As a user, I want to upload documents so the chatbot can answer from them | 5 | High |
| US-02 | As a user, I want a chat UI so I get answers quickly | 5 | High |
| US-03 | As a user, I want source citations so I can trust answers | 3 | High |
| US-04 | As a developer, I want a Dockerised app so deployment is consistent | 3 | Medium |
| US-05 | As a developer, I want CI tests so bugs are caught early | 3 | Medium |
| US-06 | As a user, I want conversation history so follow-ups work | 5 | Medium |
| US-07 | As an admin, I want usage logs so I can monitor cost and errors | 2 | Low |

### Sample sprint plan
**Sprint 1, Goal:** *Working end-to-end MVP: ingest → retrieve → answer.*

| Task | Story | Estimate | Status |
|------|-------|----------|--------|
| Repo + environment setup | US-04 | 2h | To Do |
| Document loader + chunking | US-01 | 4h | To Do |
| Embeddings + vector DB | US-01 | 4h | To Do |
| FastAPI `/ask` endpoint | US-02 | 4h | To Do |
| Source citations | US-03 | 3h | To Do |
| Dockerfile + compose | US-04 | 3h | To Do |

**Sprint 2:** history, logging, CI tests, Azure deployment, documentation, demo.

### Prioritisation: MoSCoW
- **M**ust have · **S**hould have · **C**ould have · **W**on't have (this time)

---

## 6. Project Planning & Task Estimation

### What is a project?
A temporary effort with a defined **goal, scope, timeline, budget and resources**. Project management = planning, executing, monitoring and closing.

### The triple constraint
```
        Scope
        /   \
     Time —— Cost        (Quality sits in the middle)
```
Change one and the others are affected. More scope needs more time or money. Less time means cutting scope.

### Planning steps
1. **Define goal and scope:** what's in and what's *out*.
2. **Break down the work (WBS):** Project → modules → tasks.
3. **Estimate** effort per task.
4. **Sequence tasks** and identify dependencies.
5. **Assign owners** and set milestones.
6. **Identify risks** and mitigations.
7. **Track and report** progress.

### Work Breakdown Structure (WBS) example
```
Capstone: AI Document Assistant
├── 1. Setup (repo, env, board)
├── 2. Data & Ingestion (loaders, chunking, embeddings)
├── 3. Backend (FastAPI, RAG pipeline, endpoints)
├── 4. Frontend (UI)
├── 5. DevOps (Docker, CI, cloud deploy)
├── 6. Testing & Evaluation
└── 7. Documentation & Demo
```

### Estimation techniques

| Technique | How it works |
|-----------|--------------|
| **Expert judgement / analogy** | Compare with similar past work |
| **Story points / Planning Poker** | Relative sizing by the team |
| **Three-point (PERT)** | `E = (O + 4M + P) / 6` |
| **Bottom-up** | Estimate small tasks, then sum |
| **Buffer** | Add 20-30% for unknowns |

**PERT example:** Optimistic = 2 days, Most likely = 3, Pessimistic = 8
`E = (2 + 4×3 + 8) / 6 = 22/6 ≈ 3.7 days`

**Estimation tips**
- Break tasks to ≤ 1 day each; small tasks are estimated more accurately.
- AI/ML work is uncertain (data quality, API limits, tuning), so keep more buffer.
- Re-estimate as you learn more.

### Timeline tools
- **Gantt chart:** tasks on a time axis with dependencies.
- **Milestones:** checkpoints (MVP ready, deployed, demo).
- **Critical path:** the longest chain of dependent tasks. If one slips, the whole project slips.

Sample 2-week timeline:

| Days | Milestone |
|------|-----------|
| 1-2 | Setup + data ingestion |
| 3-5 | RAG pipeline + API |
| 6-7 | UI + integration |
| 8 | Dockerise + CI |
| 9 | Deploy to cloud |
| 10 | Testing, docs, demo |

### Risk management

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| LLM rate limits / cost | Med | High | Cache, small test set, budget alerts |
| Poor answer quality | Med | High | Evaluation set, tune chunking/retrieval |
| Scope creep | High | Med | Strict MVP; extras go to backlog |
| Late deployment issues | Med | Med | Deploy early, not on the last day |
| API key leak | Low | High | `.env`, `.gitignore`, secrets manager |

**Scope creep:** uncontrolled addition of features. Prevent it by agreeing scope upfront, sending new requests to the backlog, and being transparent about their time/cost impact.

### Roles in a project
Project Manager · Tech Lead · Developer · QA/Tester · DevOps Engineer · Stakeholder / Client.

---

## 7. Git/GitHub Version Control

**Git:** distributed version control system that tracks every change, enables parallel work and lets you undo mistakes.
**GitHub:** hosting platform adding collaboration (pull requests, issues, projects, Actions).

### Core workflow
```
Working Directory → (git add) → Staging Area → (git commit) → Local Repo → (git push) → GitHub
```

### Essential commands
```bash
git init                       # start a repo
git clone <url>                # copy a remote repo
git status                     # see changes
git add .                      # stage all changes
git commit -m "feat: message"  # save snapshot
git log --oneline              # history
git diff                       # see unstaged changes
git branch                     # list branches
git checkout -b feature/x      # create + switch  (or: git switch -c feature/x)
git merge feature/x            # merge into current branch
git pull                       # fetch + merge from remote
git push -u origin feature/x   # push branch
git stash / git stash pop      # temporarily shelve changes
git restore <file>             # discard unstaged changes
git revert <commit>            # undo a commit safely (new commit)
git reset --soft HEAD~1        # undo last commit, keep changes
git tag v1.0.0                 # mark a release
```

### Branching strategy
```
main              ← stable, deployable
 └─ dev           ← integration branch (optional)
     ├─ feature/pdf-loader
     ├─ feature/api
     └─ fix/citation-bug
```

### Pull request (PR) workflow
1. Create branch from `main`.
2. Make small commits.
3. Push and open a **Pull Request**.
4. Teammates review, comment, request changes.
5. CI checks pass → **merge**.
6. Delete the branch.

Link issues in the PR: `Closes #12`.

### Conventional commit messages

| Prefix | Use |
|--------|-----|
| `feat:` | New feature |
| `fix:` | Bug fix |
| `docs:` | Documentation |
| `refactor:` | Code restructure |
| `test:` | Tests |
| `chore:` | Maintenance |
| `ci:` | CI/CD changes |

Example: `feat: add PDF loader with chunking`

### Merge vs Rebase
- **Merge:** combines branches, preserving history with a merge commit (safe).
- **Rebase:** replays your commits on top of another branch for a linear history. **Never rebase shared/public branches.**

### Merge conflicts
Occur when two branches change the same lines. Git marks them:
```
<<<<<<< HEAD
your version
=======
their version
>>>>>>> feature/x
```
Edit the file to keep the correct code, remove markers, then `git add` and `git commit`.

### Good practices
- Small, frequent commits with meaningful messages.
- Never commit secrets; use `.gitignore` for `.env`, `venv/`, data, model files.
- Protect `main` (require PR + passing checks).
- Tag releases (`v1.0.0`).
- Pull before you push to reduce conflicts.

### If you accidentally commit an API key
1. **Revoke/rotate the key immediately.** Assume it's compromised.
2. Remove it from the code and from history (`git filter-repo` or BFG), then force-push.
3. Add the file to `.gitignore`.
4. Move the secret to an environment variable or secrets manager (e.g., Azure Key Vault).

Deleting it in a later commit is **not enough**; it stays in history.

### GitHub project management tools
- **Issues:** one per task/bug/feature.
- **Labels:** categorise (`bug`, `feature`, `documentation`, `priority: high`, `backend`, `devops`).
- **Milestones:** group issues toward a goal.
- **Projects (board):** Kanban `Backlog → To Do → In Progress → In Review → Done`.
- **Actions:** CI/CD automation.

```bash
gh issue create --title "Build PDF ingestion" --label feature,backend
gh pr create --fill
```

### Recommended repo skeleton
```
capstone-project/
├── README.md
├── LICENSE
├── .gitignore
├── .env.example
├── requirements.txt
├── Dockerfile
├── docs/
│   ├── architecture.md
│   └── sprint-plan.md
├── src/
├── tests/
└── .github/
    ├── ISSUE_TEMPLATE/
    ├── pull_request_template.md
    └── workflows/ci.yml
```

---

## 8. Documentation & Reporting Practices

Code nobody can understand or run is only half-finished.

### Types of documentation

| Document | Purpose |
|----------|---------|
| **README.md** | Front door: what it is, how to install and run |
| **Architecture doc** | How components fit together (with diagrams) |
| **API docs** | Endpoints and examples (FastAPI auto-generates `/docs`) |
| **ADR (Architecture Decision Record)** | Why a key technical decision was made |
| **CHANGELOG** | What changed in each version |
| **Code comments / docstrings** | Explain *why*, not just what |
| **User guide** | How end users use the product |

### README template
```markdown
# Project Name
One-line description.

## Problem & Solution
## Features
## Architecture (diagram)
## Tech Stack
## Getting Started
### Prerequisites
### Installation
### Run (Docker / local)
## Usage / API Examples
## Project Structure
## Testing
## Deployment
## Screenshots / Demo
## Roadmap
## Contributing
## License
## Author
```

### Reporting
**Weekly status report template**
```
Week 8 Status
Done:         Ingestion, embeddings, /ask endpoint
In progress:  Source citations
Next:         Docker + CI
Blockers:     LLM rate limits
Risks:        Answer quality on long documents
% Complete:   45%
```

**Metrics to track:** velocity, burndown, open bugs, test coverage, deployment frequency.

**Good reporting habits:** be honest and brief, report problems early, quantify progress, state next steps clearly.

---

## 9. Expected Interview Questions with Answers

**Q1. What are the phases of SDLC?**
Planning, requirements, design, development, testing, deployment, maintenance. Example: for a RAG chatbot, requirements = upload PDFs + citations; design = FastAPI + ChromaDB + LLM; deployment = Docker + Azure.

**Q2. Waterfall vs Agile?**
Waterfall is sequential with heavy upfront planning and late feedback; changes are costly. Agile is iterative with delivery every sprint and continuous feedback; it welcomes change.

**Q3. Explain Scrum.**
Three roles (Product Owner, Scrum Master, Developers), three artifacts (product backlog, sprint backlog, increment), and events (sprint, planning, daily stand-up, review, retrospective).

**Q4. Sprint Review vs Retrospective?**
Review is about the *product* (demo to stakeholders, feedback). Retrospective is about the *process* (what the team improves).

**Q5. What if requirements change mid-sprint?**
Inform the Product Owner. Normally the change goes to the backlog for the next sprint. If urgent, swap it with equal-sized work. Cancel the sprint only in rare cases.

**Q6. What is a Definition of Done?**
A shared checklist every story must satisfy: code reviewed, tests pass, documented, deployed to test, acceptance criteria met.

**Q7. Story points and velocity?**
Story points are relative effort estimates. Velocity is the points completed per sprint, used for forecasting.

**Q8. Epic vs story vs task?**
Epic = large feature; story = user-facing slice; task = technical step.

**Q9. What does a Scrum Master do?**
Facilitates the process, removes blockers, coaches the team. Not a manager.

**Q10. How is Agile used in ML projects?**
ML is experimental, so use short sprints with goals like "baseline model", "improve retrieval", "deploy API", and let evaluation results drive the next sprint.

**Q11. How do you plan a project?**
Define scope, build a WBS, estimate, sequence with dependencies, assign owners and milestones, identify risks, track progress.

**Q12. How do you estimate tasks?**
Break them small, use past experience, three-point or story-point estimates, and add a 20-30% buffer.

**Q13. What is scope creep and how do you handle it?**
Uncontrolled addition of features. Agree scope upfront, add new requests to the backlog, communicate impact, and prioritise.

**Q14. What is the critical path?**
The longest chain of dependent tasks; any delay there delays the whole project.

**Q15. Explain your Git workflow.**
Feature branches from `main`, small commits with clear messages, push, pull request with review, CI checks, merge, delete branch.

**Q16. Merge vs rebase?**
Merge keeps history with a merge commit. Rebase rewrites history into a straight line; never rebase shared branches.

**Q17. How do you resolve a merge conflict?**
Open the conflicted file, keep the correct code, remove the markers, `git add`, `git commit`.

**Q18. You committed an API key. What do you do?**
Rotate/revoke the key first, remove it from history (`git filter-repo`/BFG), add to `.gitignore`, and move secrets to env vars or a vault.

**Q19. How do you prioritise tasks?**
By value and urgency, using methods like MoSCoW.

**Q20. How do you handle a missed deadline?**
Tell stakeholders early, find the cause, re-plan or cut scope, and review it in the retrospective.

**Q21. What should a good README contain?**
Description, features, tech stack, setup, usage examples, project structure, screenshots, license.

**Q22. Milestone vs task?**
A task is a unit of work; a milestone is a checkpoint marking a major achievement (e.g., "MVP working").

---

## 10. Quick Revision

| Topic | Remember |
|-------|----------|
| **SDLC** | Planning → Requirements → Design → Development → Testing → Deployment → Maintenance |
| **Agile** | Small increments, feedback, welcome change; 4 manifesto values |
| **Scrum roles** | Product Owner (what), Scrum Master (process), Developers (how) |
| **Scrum events** | Sprint, Planning, Daily (15 min), Review (product), Retro (process) |
| **Backlog items** | Epic → Story → Task; INVEST; Given/When/Then |
| **Estimation** | Story points, Planning Poker, PERT `(O+4M+P)/6`, 20-30% buffer |
| **Planning** | Scope → WBS → Estimate → Sequence → Assign → Risks → Track |
| **Constraints** | Scope, Time, Cost (+ Quality) |
| **Git flow** | Branch → Commit → Push → PR → Review → Merge |
| **Secrets** | Never commit; if leaked, rotate first |
| **Docs** | README, architecture, API docs, ADR, CHANGELOG, status reports |

**One-line summary:** Plan the work (SDLC, WBS, estimates), build it iteratively (Agile/Scrum sprints), manage the code (Git/GitHub, PRs), and communicate progress clearly (documentation and reports).
