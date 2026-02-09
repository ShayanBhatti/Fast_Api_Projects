# FastAPI Todo App (File-Based CRUD)

A simple Todo application built with **FastAPI**, **Jinja2**, and **Bootstrap**.  
Tasks are stored locally in a JSON file (no database).

---

## 🚀 How to Start the Project

### 1. Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate   # Windows
2. Install dependencies
pip install -r requirements.txt
3. Project structure (required)
project/
│
├── main.py
├── routes.py
├── models.py
├── storage.py
├── tasks.json
└── templates/
    └── index.html
tasks.json must exist and contain:

[]
4. Run the server
uvicorn main:app --reload
5. Open in browser
http://127.0.0.1:8000/
⚙️ How This Project Works
Core Flow
HTML Form → FastAPI Route → JSON File → HTML Template
Components
FastAPI
Handles routes for adding, completing, and deleting tasks.

Jinja2 Templates
Renders tasks dynamically into HTML using server-side rendering.

JSON File Storage (tasks.json)
Acts as a lightweight local database.

Bootstrap UI
Displays tasks as colorful cards with hover effects.

🧠 Task Data Model
Each task contains:

id (UUID)

title

description

estimated_time (minutes)

completed (true/false)

created_at

🔁 Working Mechanism
Add Task

HTML form submits data using POST /add

FastAPI creates a task object

Task is appended to tasks.json

User is redirected back to /

Complete Task

Button sends POST /complete/{id}

Task completed status is updated in JSON

Delete Task

Button sends POST /delete/{id}

Task is removed from JSON file

Homepage (/)

Loads all tasks from JSON

Displays them using Bootstrap cards

Incomplete tasks shown first

✅ No Database Used
This project intentionally avoids a database to:

Keep logic simple

Focus on FastAPI + MVC structure

Demonstrate file-based persistence

📌 Notes
Restart server after code changes if not using --reload

JSON storage is not thread-safe (okay for learning/demo)

Designed to be upgraded later to a real database


If you want, next logical upgrades would be:
- Edit task via modal
- Priority levels
- Due dates
- Database migration (SQLite → PostgreSQL)

That’s how small apps grow into real systems.
