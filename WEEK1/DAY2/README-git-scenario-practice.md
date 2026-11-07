# Git and GitHub: Scenario Practice

Use this guide to practise choosing a Git command from the situation, not just
memorizing command names. Commands below assume you are inside the repository.

## The quick decision guide

| What happened? | Command to consider |
|---|---|
| I want to inspect what changed | `git status`, then the appropriate `git diff` |
| I changed a file but want to discard its unstaged edits | `git restore <file>` |
| I staged a file by mistake but want to keep its edits | `git restore --staged <file>` |
| I made a local commit and want to move it back to edits | `git reset` |
| A commit is already shared/pushed and should be undone | `git revert <commit>` |
| I need to pause uncommitted work temporarily | `git stash` |
| I lost track of a commit or moved a branch accidentally | `git reflog` |

> **Before undoing anything:** run `git status` and inspect the diff. If work
> matters, make a backup branch or copy before using a destructive command.

## `git diff`: what exactly am I comparing?

`git diff` compares versions of files. It does not change files or create a
commit.

| Command | Comparison | Use it to answer |
|---|---|---|
| `git diff` | Working directory vs staging area | What edits have I **not staged**? |
| `git diff --staged` | Staging area vs latest commit (`HEAD`) | What will my **next commit** contain? |
| `git diff HEAD` | Working directory (including staged edits) vs `HEAD` | What is everything I have changed since the last commit? |
| `git diff <branch-a>..<branch-b>` | The two branch tips | How do these branch snapshots differ? |
| `git diff <commit-a> <commit-b> -- <file>` | One file between two commits | What changed in this file between those snapshots? |

`git diff --cached` is an alias for `git diff --staged`.

### Example: check a change before committing

```bash
git status
git diff                    # review edits not staged yet
git add src/app.py
git diff --staged           # review exactly what is staged
git commit -m "Fix app validation"
```

If `git diff` prints nothing after `git add`, that can be expected: the edits
are staged, so inspect them with `git diff --staged`.

To see only changed file names, use `git diff --name-only`. To compare two
branches, use `git diff main...feature/login` when you want changes introduced
by the feature branch since it diverged from `main`.

## `revert` vs `reset` (and what “reverse” means)

There is no standard `git reverse` command. **Reverting** means making a new
commit whose changes undo an earlier commit. The command is `git revert`.

### `git revert <commit>`: undo by adding a commit

Use this for a commit that has already been pushed or shared with teammates.
It preserves the existing history and adds a new commit that reverses the
selected commit.

```bash
git log --oneline
git revert <commit-hash>
git push
```

If Git opens an editor, save and close it to accept the default revert message.
If there is a conflict, resolve the files, run `git add <file>`, then run
`git revert --continue`. To stop the revert operation, use `git revert --abort`.

**Scenario:** A broken bug fix is already on the team branch. Do not erase or
rewrite the shared history. Revert the bad commit, test the result, and push
the new revert commit.

### `git reset`: move the current branch to another commit

`reset` moves the current branch pointer (and `HEAD`) to a target commit. Its
three modes control what happens to the index (staging area) and working files:

| Mode | Branch/commit position | Staging area | Tracked working files |
|---|---|---|---|
| `--soft` | Moves to target | Keeps changes staged | Keeps changes |
| `--mixed` (default) | Moves to target | Unstages changes | Keeps changes |
| `--hard` | Moves to target | Resets to target | Resets to target; local tracked edits can be lost |

The table describes changes relative to the target commit. Untracked files are
not removed by `git reset --hard`; `git clean` is a separate, destructive
command.

#### Reset example: undo the latest local commit but keep it staged

```bash
git reset --soft HEAD~1
```

The branch moves back one commit, but the undone commit's changes stay staged.
You can recommit them, perhaps with a corrected message.

#### Reset example: undo the latest local commit and keep edits unstaged

```bash
git reset HEAD~1
```

This uses the default `--mixed` mode. The commit is removed from the current
branch history; the changes remain in the working directory but are unstaged.

#### Reset example: discard the latest local commit and its tracked changes

```bash
git status
git reset --hard HEAD~1
```

This throws away tracked changes in the working tree and index as it moves the
branch. Do not use it unless you are certain nothing there needs to be kept.

> **Shared-history rule:** Prefer `git revert` for commits others may have
> fetched. Reset rewrites the branch history and can disrupt collaborators.
> Avoid force-pushing to “fix” a shared branch unless the team explicitly
> coordinates that recovery.

## Scenario questions and answers

### 1. You edited a file, but have not staged it. You want to throw away only that file's edits.

**Question:** Which command do you use, and what should you check first?

**Answer:** Inspect the state and diff, then restore that file. This discards
its unstaged edits.

```bash
git status
git diff -- src/app.py
git restore -- src/app.py
```

Do not use `git restore` if those edits might be needed; copy or save them
first. To discard all unstaged tracked edits instead, `git restore .` is
broader and should be used with extra care.

### 2. You staged the wrong file, but its edits are useful.

**Question:** How do you remove it from the next commit without losing the edits?

**Answer:** Unstage it; do not restore the working copy.

```bash
git restore --staged -- README.md
git status
```

The file's edits remain in your working directory. On older Git versions,
`git reset HEAD -- README.md` also unstages that path.

### 3. Your last commit is local and has the wrong commit message.

**Question:** How can you correct it?

**Answer:** Amend the latest commit if it has not been shared.

```bash
git commit --amend -m "Use a clear commit message"
```

Amending replaces the commit with a new one. Do not amend a commit teammates
already rely on unless you have coordinated the history rewrite.

### 4. You committed the wrong file, but have not pushed.

**Question:** You want to redo the commit while keeping all the edits. Which reset mode?

**Answer:** `--mixed` moves the branch back and leaves the changes in the
working directory, unstaged. Then stage only the intended files.

```bash
git reset --mixed HEAD~1
git status
git add src/app.py
git diff --staged
git commit -m "Add app validation"
```

Use `--soft` instead if you want all the changes to stay staged. Avoid
`--hard` when you need to keep the work.

### 5. A bad commit was pushed to a shared branch.

**Question:** Should you reset the branch and force-push?

**Answer:** Usually no. Add a new commit that reverses the bad one.

```bash
git log --oneline
git revert <bad-commit-hash>
git push
```

This is the safe default because the shared commit remains in history.

### 6. You need to inspect your staged changes before committing.

**Question:** Which diff command shows what the next commit will include?

**Answer:** Use `git diff --staged`. Plain `git diff` only shows unstaged edits.

```bash
git status
git diff --staged
```

If the staged diff includes an accidental file, unstage only that path with
`git restore --staged -- <file>`, then inspect again.

### 7. A teammate pushed changes while you were working.

**Question:** How do you get the latest remote information without changing your branch yet?

**Answer:** Fetch first. Review the remote changes, then merge or rebase based
on your team's workflow.

```bash
git fetch origin
git log --oneline --graph --decorate --all
git diff HEAD..origin/main
```

After review, `git merge origin/main` incorporates the remote branch while
preserving your branch's commits. A team may instead use `git rebase
origin/main` on a private feature branch; do not rebase commits others already
use without coordination.

### 8. You have unfinished work and an urgent bug to fix on another branch.

**Question:** How do you temporarily put your uncommitted work aside?

**Answer:** Stash it, switch branches, fix the urgent issue, then restore the
stash.

```bash
git stash push -m "unfinished profile page"
git switch main
# make and commit the urgent fix
git switch feature/profile
git stash pop
```

`git stash pop` applies and removes the stash if successful. Use
`git stash apply` if you want to keep the saved stash entry as a backup.
Untracked files are excluded by default; add `-u` to include them.

### 9. You accidentally reset a local branch and cannot find a commit.

**Question:** What should you inspect before assuming the work is gone?

**Answer:** Check the reflog for the branch's previous positions, then create a
recovery branch at the desired commit.

```bash
git reflog
git switch -c recovery/my-work <commit-hash>
```

Creating a branch preserves the recovered commit without moving or overwriting
your current branch. Reflog entries expire eventually, so recover promptly.

### 10. You need one file from an older commit, not the whole old version of the project.

**Question:** How can you restore just that file's contents?

**Answer:** Restore the file from the chosen commit, review it, and commit the
result. This changes the working copy; it does not move the branch backward.

```bash
git log --oneline -- src/config.py
git restore --source=<commit-hash> -- src/config.py
git diff -- src/config.py
git add src/config.py
git commit -m "Restore config from earlier version"
```

### 11. You are about to commit but are unsure whether a secret or generated file is included.

**Question:** What should you do before committing?

**Answer:** Review the staged file list and staged patch. If a secret was
already pushed, revoke or rotate it immediately; deleting it in a later commit
does not make the exposed credential safe.

```bash
git status
git diff --staged --name-only
git diff --staged
```

If the unwanted file is staged, unstage it with
`git restore --staged -- <file>`. Add appropriate ignore rules, and remember
that `.gitignore` does not untrack a file already committed.

### 12. Your feature branch has a merge conflict after bringing in `main`.

**Question:** What is the safe resolution flow?

**Answer:** Identify conflicted files, edit each conflict to the intended
combined result, remove conflict markers, run tests, stage the resolutions, and
finish the merge or rebase.

```bash
git status
# edit conflicted files and run relevant tests
git add <resolved-file>
```

For a merge, finish with `git commit` if Git has not created the merge commit
automatically. For a rebase, finish with `git rebase --continue`. Use
`git merge --abort` or `git rebase --abort` to abandon the operation and return
to its starting state.

## A safe daily routine

```bash
git status
git pull
# make a small, focused change
git status
git diff
git add <specific-files>
git diff --staged
git commit -m "Describe the change"
git push
```

Prefer adding specific files over `git add .` when you are learning; it helps
prevent unrelated or sensitive files from entering a commit.

## Quick self-test

1. What does plain `git diff` show that `git diff --staged` does not?
2. Which reset mode keeps the changes staged?
3. Which reset mode keeps the changes but unstages them?
4. Which command usually undoes a commit that is already pushed?
5. Does `git restore --staged file.txt` delete the file's edits?

**Answers**

1. Plain `git diff` shows unstaged edits; `--staged` shows staged edits versus
   the latest commit.
2. `git reset --soft <target>`.
3. `git reset --mixed <target>`; `--mixed` is the default.
4. `git revert <commit>`.
5. No. It removes the file from the staging area and keeps its working-copy
   edits.
