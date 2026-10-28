# Git and GitHub Notes

These notes introduce Git, GitHub, the everyday commands you will use, and
some scenario-based interview questions.

## 1. Git and GitHub: what is the difference?

- **Git** is a version control system on your computer. It records changes as
  commits, lets you compare versions, and helps you work on separate branches.
- **GitHub** is an online service for hosting Git repositories. It adds
  collaboration features such as pull requests, code review, issues, and
  project discussions.
- You can use Git without GitHub. GitHub uses Git to store and share
  repositories.

## 2. The basic Git workflow

Git work usually moves through these steps:

1. **Working directory**: files you are editing.
2. **Staging area**: changes you selected for the next commit.
3. **Local repository**: commits saved on your computer.
4. **Remote repository**: a copy hosted elsewhere, often on GitHub.

```text
Edit files -> git add -> git commit -> git push
```

`git add` stages changes; it does not upload them. `git commit` saves a
snapshot locally; it does not upload it. `git push` sends local commits to a
remote repository.

## 3. First-time setup

Set the name and email that Git will record on your commits:

```powershell
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global color.ui auto
```

Check the configuration:

```powershell
git config --global --list
```

Use an email address appropriate for your GitHub account if you want GitHub
to associate your commits with that account. The `--global` option applies
these settings to your user account on this computer.

## 4. Start or get a repository

### Start tracking an existing folder

```powershell
git init
```

This creates a Git repository in the current folder. It does not create a
GitHub repository or upload anything.

### Copy a repository from a URL

```powershell
git clone https://github.com/OWNER/REPOSITORY.git
```

Cloning downloads the repository and sets up a remote, commonly named
`origin`.

## 5. Check, stage, compare, and commit

```powershell
git status
```

Shows the current branch and which changes are untracked, modified, staged,
or committed.

```powershell
git add README.md
git add .
```

Stages one file, or all changes under the current folder. Review what `git
add .` will include with `git status`; avoid staging generated files,
credentials, or unrelated work.

```powershell
git diff
git diff --staged
```

- `git diff` shows unstaged changes.
- `git diff --staged` shows staged changes—the changes that would go into
  the next commit.

```powershell
git restore --staged README.md
```

Unstages a file while keeping its edits in your working directory. The older
equivalent is `git reset README.md`.

```powershell
git commit -m "Add Git and GitHub notes"
```

Creates a local commit from the staged changes. Write a short message that
describes the change.

### A common daily sequence

```powershell
git status
git add README.md
git diff --staged
git commit -m "Explain basic Git workflow"
git push
```

## 6. Branches and merging

A branch is an independent line of work. It lets you make a change without
immediately changing the main branch.

```powershell
git branch
git branch feature/login-page
git switch feature/login-page
```

`git branch` lists local branches. The `*` marks the current branch. The
second command creates a branch; the third switches to it.

Create and switch in one command:

```powershell
git switch -c feature/login-page
```

Older instructions may use `git checkout` for both creating and switching:

```powershell
git checkout -b feature/login-page
git checkout main
```

When the feature is ready, switch to the branch that should receive it and
merge:

```powershell
git switch main
git merge feature/login-page
```

If Git reports a merge conflict, edit the conflicted files, remove the
conflict markers after choosing the correct content, then stage and commit
the resolution.

## 7. Remotes and GitHub updates

A **remote** is a named URL for another copy of the repository. `origin` is
the conventional name for the remote created by `git clone`.

```powershell
git remote -v
```

Shows the remote URLs.

```powershell
git remote add origin https://github.com/OWNER/REPOSITORY.git
```

Connects an existing local repository to a remote. You generally do this
once, and only if a remote has not already been set.

```powershell
git fetch origin
```

Downloads remote commits and branch information without merging them into
your current branch.

```powershell
git pull
```

Fetches from the configured upstream branch and integrates those changes
into the current branch. Review your working tree and commit or stash your
own changes first if needed.

```powershell
git push -u origin main
```

Uploads the local `main` branch to `origin` and sets its upstream tracking
branch. After that, `git push` is usually enough for that branch.

If your branch has another name, replace `main` with that branch name.

## 8. History and inspecting changes

```powershell
git log
git log --oneline --graph --decorate
```

Shows commit history. The second version is a compact, graph-style view.

```powershell
git show <commit-id>
```

Shows details and changes for a commit. Replace `<commit-id>` with a commit
hash from `git log`.

```powershell
git log --stat
git log --follow -- path/to/file
```

- `git log --stat` summarizes which files each commit changed.
- `git log --follow -- path/to/file` follows a file's history across
  renames.

```powershell
git log main..feature/login-page
git diff main...feature/login-page
```

- The log command lists commits reachable from `feature/login-page` but not
  from `main`.
- The three-dot diff compares the feature branch's changes since it split
  from `main`.

## 9. Rename and remove tracked files

```powershell
git mv old-name.txt new-name.txt
git rm old-name.txt
```

These commands rename or remove a tracked file and stage the change. Git can
also detect a rename when you move a file outside Git and then stage the
result.

## 10. Temporarily put changes aside with stash

Use a stash when you need to switch branches but are not ready to commit your
current changes.

```powershell
git stash push -m "Work in progress"
git stash list
git stash pop
```

- `git stash push` saves tracked working-tree changes and reverts them from
  the working tree.
- `git stash list` lists saved stashes.
- `git stash pop` reapplies the latest stash and removes it from the stash
  list if applying succeeds.

By default, untracked files are not included. To include them, use
`git stash push -u -m "Work in progress"`. If applying a stash causes
conflicts, resolve them like other merge conflicts.

```powershell
git stash drop
```

Discards the latest stash. This is destructive; check `git stash list` first.

## 11. Undoing and rewriting changes safely

Choose the undo command based on what you want to undo:

```powershell
git restore path/to/file
```

Discards unstaged edits in that file and restores it from the index. The
discarded edits may be difficult or impossible to recover.

```powershell
git restore --staged path/to/file
```

Unstages the file but keeps its working-tree edits.

```powershell
git revert <commit-id>
```

Creates a new commit that reverses the selected commit. This is usually the
safer choice for changes already shared with others.

```powershell
git reset --hard <commit-id>
```

Moves the current branch to the selected commit and resets both the staging
area and working tree. **This can permanently discard uncommitted changes
and commits that are no longer referenced.** Do not use it as a routine
undo command or on shared history unless you understand the consequences.

`git rebase main` reapplies the current branch's commits on top of `main`.
Rebase can make history easier to read, but it rewrites commit IDs. Avoid
rebasing commits that others already use unless your team agrees.

## 12. Ignore files with `.gitignore`

Create a file named `.gitignore` at the repository root and list patterns
that Git should ignore:

```gitignore
# Python virtual environment and cache files
.venv/
__pycache__/
*.py[cod]

# Local environment variables (may contain secrets)
.env

# Example: ignore log files
logs/
*.log
```

Patterns such as `*.log` match files by name; a trailing slash such as
`logs/` indicates a directory. `.gitignore` prevents untracked matching files
from being added by accident, but it does not stop tracking files already
committed. To stop tracking a file while keeping it locally:

```powershell
git rm --cached path/to/file
```

Never commit passwords, API keys, or other secrets.

## 13. Pull requests: a common GitHub collaboration flow

1. Create a feature branch: `git switch -c feature/my-change`.
2. Make changes and inspect them: `git status` and `git diff`.
3. Stage and commit: `git add ...` and `git commit -m "Describe the change"`.
4. Push the branch: `git push -u origin feature/my-change`.
5. On GitHub, open a **pull request (PR)** to propose merging the branch.
6. Respond to review feedback by committing and pushing more changes.
7. After approval and checks, merge the PR using the repository's chosen
   merge method.

A pull request is a GitHub collaboration and review feature; it is not a Git
command.

## 14. Scenario-based interview questions

### Q1. You edited a file but are not ready to include it in your next commit.
What do you do?

**Answer:** Do not stage it, or unstage it with
`git restore --staged <file>`. The latter keeps the edits in the working
directory. Verify with `git status`.

### Q2. You staged the wrong file. How do you fix it without losing its edits?

**Answer:** Run `git restore --staged <file>`. This removes the file from the
staging area but preserves its working-tree changes.

### Q3. You committed a change locally, but have not pushed it. You want to
undo it while keeping the code edits.

**Answer:** One option is `git reset --soft HEAD~1`, which removes the latest
commit but keeps its changes staged. You can then edit or recommit. Check
`git status` and `git log` first. Do not use this on a commit already shared
with teammates without coordinating.

### Q4. You pushed a bad commit to a shared branch. What is the safer way to
undo it?

**Answer:** Use `git revert <commit-id>` and push the new reversing commit.
This preserves shared history instead of rewriting it.

### Q5. You need to quickly switch branches, but your edits are unfinished.
What can you do?

**Answer:** Commit the work-in-progress if appropriate, or save it with
`git stash push -m "Work in progress"`. Switch branches, then reapply it
later with `git stash pop`.

### Q6. What is the difference between `git fetch` and `git pull`?

**Answer:** `git fetch` downloads remote changes but does not integrate them
into the current branch. `git pull` fetches and then integrates the upstream
changes.

### Q7. Your push is rejected because the remote branch has commits you do not
have. What should you do?

**Answer:** Fetch and inspect the remote changes, then integrate them using
the workflow your team follows (often `git pull --rebase` or `git pull`).
Resolve conflicts if needed, run relevant tests, and push again. Avoid
force-pushing to a shared branch.

### Q8. Two people changed the same lines and Git reports a conflict. How do
you resolve it?

**Answer:** Open each conflicted file, review both versions and the conflict
markers (`<<<<<<<`, `=======`, `>>>>>>>`), edit the file to the intended
result, stage it, and complete the merge or rebase. Run tests afterward.

### Q9. You accidentally committed a generated file. How can you prevent it
from being committed again?

**Answer:** Add a matching pattern to `.gitignore`. If the file is already
tracked, remove it from the Git index with `git rm --cached <file>`, then
commit both changes. This leaves the local file in place.

### Q10. What is the difference between a branch and a remote?

**Answer:** A branch is a named line of commits. A remote is a named
connection to another repository, such as a GitHub repository. A local
branch can track a branch on a remote.

### Q11. Why use a pull request instead of pushing directly to `main`?

**Answer:** A pull request lets teammates review changes, discuss them, and
check automated tests before merging. It improves collaboration and helps
catch problems before they reach the shared main branch.

### Q12. Does adding `.env` to `.gitignore` remove a secret that was already
committed?

**Answer:** No. `.gitignore` does not remove tracked history. If a secret was
exposed, revoke or rotate it immediately, then follow the team's process for
removing it from repository history. Removing it from the latest version
alone does not make an exposed secret safe.

## 15. Quick reference

| Goal | Command |
|---|---|
| See repository state | `git status` |
| Stage a file | `git add <file>` |
| Unstage but keep edits | `git restore --staged <file>` |
| See unstaged changes | `git diff` |
| See staged changes | `git diff --staged` |
| Save staged changes | `git commit -m "message"` |
| List branches | `git branch` |
| Create and switch branch | `git switch -c <branch>` |
| Download remote updates only | `git fetch` |
| Download and integrate updates | `git pull` |
| Upload commits | `git push` |
| View commit history | `git log --oneline --graph` |
| Safely reverse a shared commit | `git revert <commit-id>` |
