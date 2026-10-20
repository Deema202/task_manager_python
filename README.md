# 📝 Todo Terminal Manager (CLI)

A dynamic, interactive Command-Line Interface (CLI) application built with Python and SQLite for managing tasks, users, and categories efficiently.

---

## 🌟 Key Features
- **User & Profile Management:** Create, view, update, and remove users and their personal details.
- **Task Management:** Add new tasks, set due dates, update status, and easily mark tasks as complete ✅.
- **Tagging System:** Categorize tasks using custom tags with many-to-many relationship mapping.
- **Interactive Terminal UI:** Built-in interactive prompts and formatted ASCII tables for a smooth CLI experience.

---

## 🛠️ Project Architecture & Tech Stack

The project follows a clean **3-Tier Architecture** pattern separating data setup, database operations (CRUD), and presentation logic:

```text
todo-cli-app/
│
├── database/
│   ├── __init__.py
│   └── db_setup.py         # Creates tables, foreign keys, and relations
│
├── models/
│   ├── __init__.py
│   └── database_ops.py     # Data Access Layer (SQL queries & CRUD operations)
│
├── main.py                 # Interactive CLI interface and user interaction logic
├── requirements.txt        # External Python dependencies
└── README.md               # Project documentation