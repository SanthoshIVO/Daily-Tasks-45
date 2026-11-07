# 🚀 Comprehensive FastAPI & Git/GitHub Master Guide
**Author:** Software & AI/ML Engineer (5+ Years Experience)
**Project Context:** FastAPI To-Do Application

---

## 📚 Part 1: FastAPI - From Basics to Advanced

### 1. Introduction to FastAPI
**Definition:** FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.8+ based on standard Python type hints.

**Core Meaning:** It combines the speed of **Starlette** (for web parts) and **Pydantic** (for data parts) to provide a developer-friendly experience with automatic documentation.

#### 🌟 Key Features
- **Fast:** Extremely high performance, on par with NodeJS and Go.
- **Fast to code:** Increases development speed by 200% to 300%.
- **Fewer bugs:** Reduces about 40% of human-induced errors.
- **Automatic Docs:** Generates Swagger UI and ReDoc automatically.

---

### 2. The Architecture of the Project
In this project, we follow a **Layered Architecture** (Controller-Router-Model pattern):

| Layer | File | Purpose |
| :--- | :--- | :--- |
| **Main Entry** | `main.py` | Initializes the app and includes routers. |
| **Router** | `router.py` | Defines endpoints (URLs) and maps them to controller functions. |
| **Controller** | `controller.py` | Contains the **Business Logic**. Where the "magic" happens. |
| **Model** | `models.py` | Defines the Database Schema (SQLAlchemy). |
| **DTO/Schema** | `dtos.py` | Data Transfer Objects for validation (Pydantic). |
| **Utils/DB** | `db.py`, `settings.py` | Database connection and environment configuration. |

---

### 3. Deep Dive: Concepts & Examples

#### A. Pydantic (DTOs)
**Definition:** Used for data validation and settings management. It ensures that the data coming into your API is exactly what you expect.

*Example from `src/user/dtos.py`:*
```python
class UserSchema(BaseModel):
    name: str
    username: str
    password: str
    email: str
```
**Use Case:** If a client sends an integer instead of a string for `name`, FastAPI returns a `422 Unprocessable Entity` error automatically.

#### B. SQLAlchemy (ORM)
**Definition:** Object Relational Mapper. It allows you to interact with a SQL database using Python classes instead of writing raw SQL queries.

*Example from `src/tasks/models.py`:*
```python
class TaskModel(Base):
    __tablename__ = "usertasks"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    user_id = Column(Integer, ForeignKey("user_table.id"))
```
**Use Case:** Creating a task is as simple as `new_task = TaskModel(...)` and `db.add(new_task)`.

#### C. Dependency Injection (`Depends`)
**Definition:** A way to declare things that your function needs to work. FastAPI handles the "injection" of these dependencies.

*Example from `src/tasks/router.py`:*
```python
def create_task(body: TaskSchema, db: Session = Depends(get_db), user: UserModel = Depends(is_authenticated)):
```
**Use Case:** `get_db` provides a database session for every request and closes it automatically after the request is finished.

#### D. JWT Authentication (Security)
**Definition:** JSON Web Tokens. A compact, URL-safe means of representing claims to be transferred between two parties.

**Flow in this project:**
1. **Login:** User provides credentials $\rightarrow$ Server verifies $\rightarrow$ Server generates a signed JWT token.
2. **Request:** Client sends token in `Authorization` header.
3. **Verify:** Server decodes token using `SECRET_KEY` $\rightarrow$ Extracts `user_id` $\rightarrow$ Allows access.

---

### 4. 🎯 Interview Questions & Scenarios

#### 💡 Normal Interview Questions
1. **What is the difference between `BaseModel` (Pydantic) and `Base` (SQLAlchemy)?**
   - *Answer:* `BaseModel` is for data validation and serialization (JSON $\leftrightarrow$ Python object). `Base` is for database mapping (Python object $\leftrightarrow$ Database row).
2. **What is the purpose of `async def` in FastAPI?**
   - *Answer:* It allows the server to handle other requests while waiting for I/O operations (like DB queries or API calls), preventing the server from blocking.
3. **How does FastAPI handle documentation?**
   - *Answer:* It uses the OpenAPI specification to automatically generate `/docs` (Swagger UI) and `/redoc`.

#### 🛠 Scenario-Based Questions
**Scenario 1: "Your API is slow when fetching thousands of tasks. How do you optimize it?"**
- *Engineer's Answer:* I would implement **Pagination**. Instead of `db.query(TaskModel).all()`, I would use `.limit(10).offset(0)` to fetch data in chunks. I would also check for "N+1" query problems and use `joinedload` for related user data.

**Scenario 2: "A user is able to delete another user's task by guessing the `task_id`. How do you fix this?"**
- *Engineer's Answer:* This is an **IDOR (Insecure Direct Object Reference)** vulnerability. I would add a check in the controller: `if task.user_id != current_user.id: raise HTTPException(403, "Not authorized")`. (Note: This is already implemented in the `update_task` function of this project!).

---

## 🌿 Part 2: Git & GitHub Master Notes

### 1. Normal Git Notes (The Basics)

| Command | Meaning | Example |
| :--- | :--- | :--- |
| `git init` | Initialize a new local repository. | `git init` |
| `git add .` | Stage all changes for the next commit. | `git add .` |
| `git commit -m "msg"` | Save staged changes with a descriptive message. | `git commit -m "Add user login"` |
| `git push origin main` | Upload local commits to the remote server. | `git push origin main` |
| `git pull` | Fetch and merge changes from remote to local. | `git pull origin main` |
| `git branch` | List, create, or delete branches. | `git branch feature-auth` |
| `git checkout -b name` | Create a new branch and switch to it. | `git checkout -b fix-bug` |
| `git merge name` | Merge changes from one branch into the current. | `git merge feature-auth` |

### 2. GitHub Workflow (The Collaborative Way)
1. **Fork/Clone:** Copy the repo to your local machine.
2. **Branching:** Never work on `main`. Create a feature branch (`git checkout -b feature-x`).
3. **Commit:** Save changes locally.
4. **Push:** Push the branch to GitHub.
5. **Pull Request (PR):** Request the maintainer to merge your branch into `main`.
6. **Code Review:** Team members suggest changes.
7. **Merge:** Branch is merged and deleted.

---

### 3. Git Scenarios (Real-world Engineering)

#### Scenario A: "I committed a secret API key to GitHub. What do I do?"
- **The Wrong Way:** Just deleting the key in a new commit. (The key is still in the git history!).
- **The Engineer's Way:**
  1. **Rotate the Key:** Immediately deactivate the API key in the provider's dashboard.
  2. **Clean History:** Use `git filter-repo` or BFG Repo-Cleaner to permanently scrub the file from all commits.
  3. **Force Push:** `git push origin main --force` to overwrite the remote history.

#### Scenario B: "I'm in the middle of a feature, but my boss wants an urgent bug fix on `main`. I can't commit my half-finished work. Now what?"
- **The Solution: `git stash`**
  1. `git stash` $\rightarrow$ Saves current changes in a temporary area and cleans the working directory.
  2. `git checkout main` $\rightarrow$ Switch to main and fix the bug.
  3. `git commit` & `git push` the fix.
  4. `git checkout feature-branch` $\rightarrow$ Go back to your work.
  5. `git stash pop` $\rightarrow$ Bring back your half-finished changes.

#### Scenario C: "Two people edited the same line in the same file. Git says 'Merge Conflict'. How to solve it?"
- **Process:**
  1. Open the conflicting file. Look for markers: `<<<<<<< HEAD`, `=======`, `>>>>>>> branch-name`.
  2. Manually choose which code to keep (or combine both).
  3. Remove the markers.
  4. `git add <file>` $\rightarrow$ `git commit` $\rightarrow$ `git push`.

---
**Final Tip from the Engineer:** Always write commit messages in the **Imperative Mood** (e.g., "Add user authentication" instead of "Added user authentication"). It's the industry standard! 🚀
