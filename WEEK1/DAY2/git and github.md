# Git & GitHub Mastery Notes

> Learn Git by following **one project from start to finish**, the way a real team works.
> Every command comes with: **what it does → when you use it → a real scenario.**

**Example project:** `money-mentor` — a small GenAI app (Python + FastAPI) that gives budgeting advice.

---

## Table of Contents

1. [The Big Picture (explain this first)](#1-the-big-picture)
2. [One-time Setup](#2-one-time-setup)
3. [Starting a Project](#3-starting-a-project)
4. [The Daily Cycle: status → add → commit → push](#4-the-daily-cycle)
5. [Viewing History](#5-viewing-history)
6. [Branching](#6-branching)
7. [Merging and Conflicts](#7-merging-and-conflicts)
8. [Working with GitHub (remote)](#8-working-with-github-remote)
9. [Pull Requests and Code Review](#9-pull-requests-and-code-review)
10. [Undoing Things (the lifesaver section)](#10-undoing-things)
11. [Stash](#11-stash)
12. [Rebase, Cherry-pick, Tags](#12-rebase-cherry-pick-tags)
13. [.gitignore and Secrets](#13-gitignore-and-secrets)
14. [Real-Time Scenarios (end to end)](#14-real-time-scenarios)
15. [Cheat Sheet](#15-cheat-sheet)
16. [Interview Q&A](#16-interview-qa)

---

## 1. The Big Picture

### What is Git?
Git is a **version control system** installed on your computer. It records the history of your files so you can go back, compare, and work with others without overwriting each other's work.

### What is GitHub?
GitHub is a **website that hosts Git repositories online**. Git is the tool, GitHub is the place to store and share.

> **Analogy:** Git = Google Docs' "version history" feature. GitHub = Google Drive where it's stored and shared.

### The 4 areas (most important concept)

```
Working Directory  --git add-->  Staging Area  --git commit-->  Local Repo  --git push-->  Remote (GitHub)
 (your files)                    (ready to save)                (saved history)             (online copy)

                  <-------------------------- git pull / git fetch ---------------------------
```

| Area | Meaning | Real-life analogy |
|---|---|---|
| Working Directory | Files you are editing now | Your desk with papers |
| Staging Area | Changes you picked for the next save | Putting papers in a box |
| Local Repository | Saved snapshots (commits) on your PC | Sealing the box and labelling it |
| Remote Repository | Copy on GitHub | Sending the box to the warehouse |

### Key terms

| Term | Meaning |
|---|---|
| Repository (repo) | A project folder tracked by Git |
| Commit | A saved snapshot with a message and a unique ID (hash) |
| Branch | A separate line of work |
| HEAD | Pointer to where you are right now |
| origin | Default nickname for your GitHub remote |
| main | The default primary branch |
| Clone | Download a repo with full history |
| Fork | Your own copy of someone else's GitHub repo |
| Pull Request (PR) | A request to merge your branch, with review |

---

## 2. One-time Setup

```bash
git --version
```
Checks Git is installed.

```bash
git config --global user.name "Santhosh S S"
git config --global user.email "you@example.com"
```
Tells Git who you are. This name/email appears on every commit.

```bash
git config --global init.defaultBranch main
git config --global core.editor "code --wait"
git config --list
```
Sets the default branch name to `main`, VS Code as editor, and shows all settings.

**Scenario:** On a new laptop, your commits show "unknown author". You forgot `git config`. Run the two commands above. Old commits are not changed, only new ones.

### Connect to GitHub
- **HTTPS:** uses a Personal Access Token (not your password).
- **SSH (recommended):**
```bash
ssh-keygen -t ed25519 -C "you@example.com"
# add the contents of ~/.ssh/id_ed25519.pub to GitHub -> Settings -> SSH keys
ssh -T git@github.com
```

---

## 3. Starting a Project

### Option A: Start from scratch locally

```bash
mkdir money-mentor
cd money-mentor
git init
```
`git init` creates a hidden `.git` folder. Now Git tracks this folder.

### Option B: Download an existing project

```bash
git clone https://github.com/<username>/money-mentor.git
cd money-mentor
```
`git clone` downloads all files **plus full history**, and sets `origin` automatically.

**Scenario:** Your teammate says "repo is ready". You run `git clone <url>` and start working. You never need `git init` here.

---

## 4. The Daily Cycle

We will build `money-mentor` step by step.

### Step 1: Create files

```
money-mentor/
├── app.py
├── requirements.txt
└── README.md
```

### Step 2: `git status` (run this constantly)

```bash
git status
```
Shows: untracked files (new), modified files, staged files, current branch.

```
Untracked files:
        app.py
        requirements.txt
        README.md
```

### Step 3: `git add` (move to staging)

```bash
git add app.py            # one file
git add app.py README.md  # multiple files
git add src/              # a folder
git add .                 # everything in current folder
git add -p                # choose chunks interactively
```

**Why staging exists:** You changed 5 files but only 2 belong to one fix. Stage those 2, commit them with one clear message, then commit the rest separately. This keeps history clean.

### Step 4: `git commit` (save a snapshot)

```bash
git commit -m "Add basic FastAPI app with health endpoint"
```

Shortcut for already-tracked files (skips `git add`):
```bash
git commit -am "Fix typo in app.py"
```

Fix the last commit message (before pushing):
```bash
git commit --amend -m "Add FastAPI app with health endpoint"
```

Add a forgotten file to the last commit:
```bash
git add forgotten_file.py
git commit --amend --no-edit
```

#### Writing good commit messages

| Bad | Good |
|---|---|
| `update` | `Add budget summary endpoint` |
| `fix bug` | `Fix crash when income is zero` |
| `changes` | `Refactor LLM call into services/llm.py` |

Rule: start with a verb, say **what and why**, keep it under about 70 characters.

### Step 5: `git push` (send to GitHub)

First create an empty repo on GitHub, then:

```bash
git remote add origin https://github.com/<username>/money-mentor.git
git branch -M main
git push -u origin main
```
`-u` links your local `main` to `origin/main`, so later you just type `git push`.

### The daily routine in one block

```bash
git pull                      # get latest first
# ... write code ...
git status                    # what changed?
git diff                      # see exact lines
git add .
git commit -m "Add expense category validation"
git push
```

---

## 5. Viewing History

```bash
git log                        # full history
git log --oneline              # one line per commit
git log --oneline --graph --all   # visual branch tree
git log -5                     # last 5 commits
git log --author="Santhosh"    # by author
git log -- app.py              # history of one file
git show a1b2c3d               # details of one commit
```

```bash
git diff                       # unstaged changes
git diff --staged              # staged changes (what will be committed)
git diff main feature/login    # compare two branches
```

```bash
git blame app.py               # who changed each line, and when
```

**Scenario:** The `/summary` endpoint suddenly returns wrong totals. Run `git log --oneline -- app.py` to see recent changes, then `git show <hash>` on the suspicious one, or `git blame app.py` to see who touched that line and why.

---

## 6. Branching

### Why branches?
`main` should always work. New features and fixes are built on separate branches so a half-finished feature never breaks the working app.

```bash
git branch                       # list local branches
git branch -a                    # include remote branches
git branch feature/chat-ui       # create
git switch feature/chat-ui       # move to it
git switch -c feature/chat-ui    # create + switch (most used)
git checkout -b feature/chat-ui  # older equivalent
git branch -d feature/chat-ui    # delete (after merge)
git branch -D feature/chat-ui    # force delete (unmerged)
git branch -m old-name new-name  # rename
```

### Branch naming (team convention)

| Prefix | Use |
|---|---|
| `feature/` | New functionality: `feature/expense-tracker` |
| `bugfix/` | Normal bug: `bugfix/zero-income-crash` |
| `hotfix/` | Urgent production fix |
| `docs/` | Documentation only |

### Scenario: Building a feature safely

```bash
git switch main
git pull
git switch -c feature/expense-tracker

# code, then:
git add .
git commit -m "Add expense model"
git add .
git commit -m "Add POST /expenses endpoint"
git push -u origin feature/expense-tracker
```
`main` stays untouched while you work.

---

## 7. Merging and Conflicts

### Merge

```bash
git switch main
git pull
git merge feature/expense-tracker
```

Two types:
- **Fast-forward:** `main` had no new commits, so Git just moves the pointer forward. No merge commit.
- **Three-way merge:** both branches have new commits, so Git creates a **merge commit**.

```bash
git merge --no-ff feature/x   # always create a merge commit
git merge --abort             # cancel a merge that went wrong
```

### Merge conflicts

A conflict happens when **two people change the same line** and Git can't decide.

**Scenario:** You and your teammate both edited the `MODEL_NAME` line in `app.py`.

```bash
git switch main
git merge feature/new-model
# CONFLICT (content): Merge conflict in app.py
```

The file now looks like this:

```python
<<<<<<< HEAD
MODEL_NAME = "gemini-1.5-flash"
=======
MODEL_NAME = "gemini-2.0-flash"
>>>>>>> feature/new-model
```

- Above `=======` is **your** version (current branch).
- Below is **their** version (incoming branch).

**Fix steps:**
1. Open the file, decide which line to keep (or combine them).
2. Delete the `<<<<<<<`, `=======`, `>>>>>>>` markers.
3. Then:
```bash
git add app.py
git commit            # completes the merge
```

Helpful commands:
```bash
git status                      # lists conflicted files
git diff --name-only --diff-filter=U
git merge --abort               # give up and go back
```

**Tip:** VS Code shows "Accept Current / Accept Incoming / Accept Both" buttons above each conflict.

**Avoiding conflicts:** pull often, keep branches short-lived, make small commits, talk to teammates about who edits which file.

---

## 8. Working with GitHub (remote)

```bash
git remote -v                          # list remotes
git remote add origin <url>            # add remote
git remote set-url origin <new-url>    # change URL
git remote remove origin
```

### fetch vs pull (common interview question)

```bash
git fetch            # download new commits, DO NOT change your files
git pull             # fetch + merge into your current branch
git pull --rebase    # fetch + rebase (cleaner history)
```

> `git fetch` = "check the mailbox". `git pull` = "check the mailbox and open everything".

```bash
git push                          # push current branch
git push -u origin feature/x      # first push of a new branch
git push origin --delete feature/x   # delete remote branch
git push --force-with-lease       # safer force push (after rebase/amend)
```

> **Never `git push --force` on shared branches like `main`.** It can erase teammates' work.

### Scenario: Push rejected

```
! [rejected] main -> main (fetch first)
```
Meaning: GitHub has commits you don't have locally.
```bash
git pull --rebase
git push
```

### Fork workflow (open source)
1. Click **Fork** on GitHub.
2. `git clone` your fork.
3. Add the original as `upstream`:
```bash
git remote add upstream https://github.com/original-owner/project.git
git fetch upstream
git merge upstream/main     # keep your fork updated
```
4. Create a branch, commit, push to your fork, open a PR to the original.

---

## 9. Pull Requests and Code Review

A **Pull Request** is a request: "please review my branch and merge it into `main`."

### Full PR flow for `money-mentor`

```bash
git switch main && git pull
git switch -c feature/budget-chart
# code + commits
git push -u origin feature/budget-chart
```

On GitHub:
1. Click **Compare & pull request**.
2. Write a title and description (what changed, why, how to test, screenshots).
3. Add reviewers.
4. Reviewer leaves comments; you fix them locally:
```bash
git add .
git commit -m "Address review: rename variable, add validation"
git push                      # PR updates automatically
```
5. After approval, click **Merge**. Options:

| Merge type | Result |
|---|---|
| Create a merge commit | Keeps all commits plus a merge commit |
| Squash and merge | All PR commits become one clean commit |
| Rebase and merge | Commits replayed linearly, no merge commit |

6. Clean up:
```bash
git switch main
git pull
git branch -d feature/budget-chart
```

### Branch protection (team setting)
Repo → Settings → Branches: require PR review, require passing checks, block direct pushes to `main`.

### Issues
Use GitHub Issues to track bugs and tasks. Writing `Fixes #12` in a PR description **auto-closes issue 12** on merge.

---

## 10. Undoing Things

The safest way to remember: **"Has it been pushed?"**

### Not committed yet

```bash
git restore app.py               # discard changes in a file (cannot be undone!)
git restore --staged app.py      # unstage, keep the changes
git clean -n                     # preview untracked files that would be deleted
git clean -fd                    # delete untracked files/folders
```

### Committed but NOT pushed

```bash
git commit --amend -m "new message"   # fix last commit

git reset --soft HEAD~1    # undo commit, keep changes STAGED
git reset --mixed HEAD~1   # undo commit, keep changes UNSTAGED (default)
git reset --hard HEAD~1    # undo commit AND delete changes (dangerous)
```

| Reset type | Commit | Staging | Files |
|---|---|---|---|
| `--soft` | removed | kept | kept |
| `--mixed` | removed | cleared | kept |
| `--hard` | removed | cleared | **deleted** |

### Already pushed (shared)

Use **revert**. It creates a *new* commit that cancels an old one, so history is not rewritten.

```bash
git revert a1b2c3d
git push
```

> **reset rewrites history (private use only). revert adds history (safe for shared branches).**

### Scenario 1: Wrong file committed, not pushed
```bash
git reset --soft HEAD~1
git restore --staged wrong_file.py
git commit -m "Add expense endpoint"
```

### Scenario 2: Bad commit already on `main`
```bash
git log --oneline
git revert 9f8e7d6
git push
```

### Scenario 3: "I broke everything, help!"  → `reflog`
```bash
git reflog
# a1b2c3d HEAD@{0}: reset: moving to HEAD~3
# 7e6d5c4 HEAD@{1}: commit: Add budget chart   <- the "lost" commit

git reset --hard 7e6d5c4
```
`reflog` records every place HEAD has been, so even "deleted" commits can usually be recovered for around 30 days or more.

### Go back and look at an old commit
```bash
git switch --detach a1b2c3d     # look around (detached HEAD)
git switch main                 # come back
```

---

## 11. Stash

Stash = temporarily shelve uncommitted work.

```bash
git stash                        # save and clean working directory
git stash push -m "half-done chart"
git stash list
git stash pop                    # restore latest and remove from stash
git stash apply                  # restore but keep in stash
git stash drop stash@{0}
git stash clear                  # delete all
git stash -u                     # include untracked files
```

### Scenario: Urgent bug while mid-feature
You are halfway through `feature/budget-chart` when your lead says "production bug, fix now!"

```bash
git stash push -m "budget chart WIP"
git switch main
git pull
git switch -c hotfix/login-crash
# fix, then
git add . && git commit -m "Fix login crash on empty token"
git push -u origin hotfix/login-crash
# PR, merge...
git switch feature/budget-chart
git stash pop                    # continue where you left off
```

---

## 12. Rebase, Cherry-pick, Tags

### Rebase
Replays your commits on top of another branch, giving a straight-line history.

```bash
git switch feature/budget-chart
git fetch origin
git rebase origin/main
```

If conflicts appear: fix → `git add .` → `git rebase --continue` (or `git rebase --abort`).

```
Merge:   main:  A---B---C-------M
                     \         /
         feature:     D---E---F

Rebase:  main:  A---B---C
                         \
         feature:         D'--E'--F'
```

**Golden rule:** never rebase commits that others have already pulled (public branches).

Clean up your messy commits before a PR:
```bash
git rebase -i HEAD~4     # squash, reword, reorder the last 4 commits
```
In the editor: `pick` keep, `squash` merge into previous, `reword` change message, `drop` remove.

| | merge | rebase |
|---|---|---|
| History | Preserves true history | Linear and clean |
| Safe on shared branches | Yes | No |
| Creates merge commit | Yes | No |

### Cherry-pick
Copy **one specific commit** to your current branch.

```bash
git switch release/1.0
git cherry-pick 9f8e7d6
```
**Scenario:** A bug fix was committed on `main`, but the `release/1.0` branch also needs it. Cherry-pick just that commit.

### Tags (mark releases)

```bash
git tag v1.0.0                              # lightweight
git tag -a v1.0.0 -m "First stable release" # annotated (preferred)
git tag                                     # list
git push origin v1.0.0                      # push one tag
git push origin --tags                      # push all tags
git tag -d v1.0.0                           # delete locally
```

---

## 13. .gitignore and Secrets

Create `.gitignore` in the project root:

```gitignore
# Python
__pycache__/
*.pyc
venv/
.venv/

# Secrets
.env
*.key

# IDE and OS
.vscode/
.DS_Store

# Data/models
*.csv
models/
```

```bash
git rm --cached .env          # stop tracking a file that was already committed
git rm -r --cached venv/
git check-ignore -v .env      # why is this ignored?
```

### Scenario: You pushed your API key by mistake
1. **Revoke/regenerate the key immediately** (most important; removing it from GitHub does not un-leak it).
2. Remove from tracking: `git rm --cached .env`, add `.env` to `.gitignore`, commit, push.
3. To erase from history, use `git filter-repo` or BFG Repo-Cleaner.
4. Use environment variables or a `.env` file (ignored) plus a committed `.env.example` with fake values.

---

## 14. Real-Time Scenarios

### Scenario A: Your first day in a team

```bash
git clone git@github.com:team/money-mentor.git
cd money-mentor
git switch -c feature/add-currency-support
# write code
git status
git add .
git commit -m "Add INR/USD currency conversion"
git push -u origin feature/add-currency-support
# open Pull Request on GitHub
```

### Scenario B: Teammate merged before you, your branch is behind

```bash
git fetch origin
git rebase origin/main        # or: git merge origin/main
# fix conflicts if any
git push --force-with-lease   # needed only after a rebase
```

### Scenario C: Committed on the wrong branch (committed to `main` by mistake)

```bash
git branch feature/my-work     # create branch at current commit
git reset --hard origin/main   # move main back to the remote state
git switch feature/my-work     # your commit is safe here
```

### Scenario D: Accidentally deleted a branch

```bash
git reflog
git switch -c feature/recovered <hash-from-reflog>
```

### Scenario E: Find which commit introduced a bug (git bisect)

```bash
git bisect start
git bisect bad                 # current version is broken
git bisect good v1.0.0         # this old version worked
# Git checks out a middle commit; you test it, then say:
git bisect good    # or: git bisect bad
# repeat until Git names the guilty commit
git bisect reset
```
Binary search over history: finds the culprit among 1000 commits in about 10 steps.

### Scenario F: Release workflow

```bash
git switch main && git pull
git tag -a v1.1.0 -m "Add expense tracker and charts"
git push origin v1.1.0
# On GitHub: Releases -> Draft new release -> choose tag v1.1.0
```

### Scenario G: Contribute to open source

1. Fork the repo on GitHub.
2. `git clone` your fork, add `upstream`.
3. `git switch -c fix/typo-in-docs`
4. Commit, push to your fork.
5. Open a PR from your fork to the original repo.
6. Respond to maintainer feedback with more commits.

---

## 15. Cheat Sheet

| Task | Command |
|---|---|
| Setup name/email | `git config --global user.name "X"` |
| New repo | `git init` |
| Download repo | `git clone <url>` |
| Check state | `git status` |
| Stage | `git add .` |
| Commit | `git commit -m "msg"` |
| Push | `git push` |
| Get latest | `git pull` |
| Create + switch branch | `git switch -c name` |
| Switch branch | `git switch name` |
| Merge | `git merge name` |
| History | `git log --oneline --graph` |
| See changes | `git diff` |
| Discard file changes | `git restore file` |
| Unstage | `git restore --staged file` |
| Undo last commit (keep work) | `git reset --soft HEAD~1` |
| Safe undo (pushed) | `git revert <hash>` |
| Shelve work | `git stash` / `git stash pop` |
| Recover lost work | `git reflog` |
| Copy one commit | `git cherry-pick <hash>` |
| Tag release | `git tag -a v1.0 -m "msg"` |

### Dangerous commands (think twice)
- `git reset --hard`: deletes uncommitted work
- `git push --force`: can erase others' commits
- `git clean -fd`: permanently deletes untracked files
- `git rebase` on shared branches

---

## 16. Interview Q&A

**Q: Difference between Git and GitHub?**
Git is a distributed version control tool on your machine. GitHub is a cloud platform that hosts Git repos and adds collaboration features like PRs, issues and Actions.

**Q: What is the staging area?**
A middle step where you select exactly which changes go into the next commit, so commits stay small and meaningful.

**Q: `git fetch` vs `git pull`?**
`fetch` only downloads changes. `pull` = `fetch` + `merge` (or rebase).

**Q: `merge` vs `rebase`?**
Merge keeps true history with a merge commit. Rebase rewrites commits for a linear history; avoid it on shared branches.

**Q: `reset` vs `revert`?**
`reset` moves the branch pointer back and rewrites history (local use). `revert` adds a new commit that cancels an old one (safe for shared branches).

**Q: How do you resolve a merge conflict?**
Open the conflicted file, choose or combine the correct code, remove the markers, `git add` the file, then commit.

**Q: What is HEAD?**
A pointer to the current commit/branch you are on.

**Q: What is a detached HEAD?**
HEAD points directly to a commit instead of a branch. Commits made there can be lost unless you create a branch.

**Q: How do you undo a pushed commit?**
`git revert <hash>` and push.

**Q: What is `git stash`?**
Temporarily saves uncommitted changes so you can switch tasks, then restore them with `git stash pop`.

**Q: What is a fork vs a clone?**
A fork is a copy of a repo on GitHub under your account. A clone is a copy on your local machine.

**Q: What is `.gitignore`?**
A file listing patterns of files Git should not track (secrets, build output, virtual environments).

**Q: How do you recover a deleted commit or branch?**
`git reflog` to find the hash, then `git switch -c <name> <hash>` or `git reset --hard <hash>`.

**Q: What is CI/CD with GitHub?**
GitHub Actions run automated workflows (tests, linting, deployment) on events like push or PR, defined in `.github/workflows/*.yml`.

---

### How to explain Git in 60 seconds (practice this)

> "Git is a version control system that tracks changes in my code as snapshots called commits. I work in three steps: I edit files, stage the changes with `git add`, and save them with `git commit`. For new features I create a branch so `main` stays stable. When it's ready I push the branch to GitHub, open a Pull Request, a teammate reviews it, and it's merged into `main`. If something breaks, I can inspect history with `git log`, undo with `reset` or `revert`, and recover almost anything with `reflog`. GitHub is where the repo lives online so the whole team can collaborate."

---

*Tip: type every command yourself on a practice repo. Create a conflict on purpose, break something, then fix it with `reflog`. That hands-on practice is what makes your explanation confident.*