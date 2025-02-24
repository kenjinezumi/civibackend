# CiviBackend

A **FastAPI** + **PostgreSQL** backend (locally installed, no Docker), using **Poetry** for dependencies and **Alembic** for migrations. This backend supports a hierarchical form structure (**Forms → Sections → Questions**).

## Table of Contents

- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Database Setup](#database-setup)
- [Migrations](#migrations)
- [Running the App](#running-the-app)
- [Using the API](#using-the-api)
- [Troubleshooting](#troubleshooting)
- [License](#license)

---

## Prerequisites

1. **Python 3.10+** installed locally.
2. **Poetry** for dependency management.
   - Install via:
     ```bash
     curl -sSL https://install.python-poetry.org | python3 -
     ```
3. **PostgreSQL** installed and running locally on `localhost:5432`.
   - On **macOS** (Homebrew):
     ```bash
     brew update
     brew install postgresql
     brew services start postgresql
     ```
   - On **Linux** (Debian/Ubuntu):
     ```bash
     sudo apt-get update
     sudo apt-get install postgresql
     sudo service postgresql start
     ```
   - On **Windows**: Download from [postgresql.org](https://www.postgresql.org/download/windows/) and run the installer.

---

# CiviBackend

A **FastAPI** + **PostgreSQL** backend (locally installed, no Docker), using **Poetry** for dependencies and **Alembic** for migrations. This backend supports a hierarchical form structure (**Forms → Sections → Questions**).

---

## Project Structure

```plaintext
civibackend/
├── alembic/
│   ├── env.py
│   └── versions/
├── app/
│   ├── core/
│   │   └── config.py
│   ├── db/
│   │   ├── base.py
│   │   └── session.py
│   ├── models/
│   │   ├── form.py
│   │   ├── section.py
│   │   └── question.py
│   ├── repositories/
│   │   └── form_repository.py
│   ├── services/
│   │   └── form_service.py
│   ├── controllers/
│   │   └── form_controller.py
│   ├── routers/
│   │   └── form_router.py
│   ├── schemas/
│   │   └── form_schema.py
│   └── main.py
├── alembic.ini
├── pyproject.toml
└── README.md
```

## Installation

### **1. Clone the Repository**
```bash
git clone https://github.com/kenjinezumi/civibackend.git
cd civibackend
```

### **2. Install Poetry (if not installed)**
```bash
curl -sSL https://install.python-poetry.org | python3 -
```
Ensure poetry is available by checking:

```bash
poetry --version
```
---

## Activate the Virtual Environment

```bash
poetry shell
```

Database Setup
==============

### 1\. Ensure PostgreSQL is Running

Start PostgreSQL depending on your operating system:

-   **macOS (Homebrew)**:

    bash

    WrapCopy

    `brew services start postgresql`

-   **Linux (Ubuntu/Debian)**:

    bash

    WrapCopy

    `sudo service postgresql start`

-   **Windows**: Open **pgAdmin** or start PostgreSQL from **Services**.

### 2\. Create a Local Database

If you have a user named meal, create a database named meal_dev:

bash

WrapCopy

`createdb meal_dev -U meal`

Or inside psql:

sql

WrapCopy

`CREATE DATABASE meal_dev OWNER meal;`

### 3\. Verify the Database Connection

Check that you can connect:

bash

WrapCopy

`psql -U meal -h localhost -d meal_dev`

If connected, your PostgreSQL setup is correct.

### 4\. Configure the Database URL

Set up your database URL in .env or app/core/config.py. Example **.env** file:

ini

WrapCopy

`SQLALCHEMY_DATABASE_URI=postgresql://meal:mypass@localhost:5432/meal_dev`

* * * * *

Migrations
==========

We use **Alembic** to manage database schema changes.

### 1\. Ensure the Database URL is Set

Make sure .env or config.py has the correct database connection string.

### 2\. Generate a Migration

If models were changed:

bash

WrapCopy

`alembic revision --autogenerate -m "Initial tables"`

### 3\. Apply Migrations

bash

WrapCopy

`alembic upgrade head`

This will create or update the database schema.

* * * * *

Running the App
===============

To start the FastAPI backend:

bash

WrapCopy

`poetry run uvicorn app.main:app --reload`

### Access the API

-   **Swagger Docs**: <http://127.0.0.1:8000/docs>

-   **Redoc Docs**: <http://127.0.0.1:8000/redoc>

* * * * *

Using the API
=============

### 1\. Create a Form with Sections & Questions

bash

WrapCopy

`curl -X POST http://127.0.0.1:8000/forms \ -H "Content-Type: application/json" \ -d '{ "title": "Survey 2023", "description": "Example form", "published": false, "sections": [ { "title": "Personal Info", "questions": [ {"label": "Name?", "type": "text", "required": true}, {"label": "Age?", "type": "number"} ] } ] }'`

### 2\. List All Forms

bash

WrapCopy

`curl -X GET http://127.0.0.1:8000/forms`

### 3\. Retrieve a Form by ID

bash

WrapCopy

`curl -X GET http://127.0.0.1:8000/forms/1`

### 4\. Update a Form

bash

WrapCopy

`curl -X PUT http://127.0.0.1:8000/forms/1 \ -H "Content-Type: application/json" \ -d '{"title": "Updated Form Title"}'`

### 5\. Delete a Form

bash

WrapCopy

`curl -X DELETE http://127.0.0.1:8000/forms/1`

* * * * *

Troubleshooting
===============

### 1\. role "postgres" does not exist

Your local PostgreSQL installation might not have created a postgres superuser. Try:

bash

WrapCopy

`psql -U meal -h localhost`

Or create the role manually inside psql:

sql

WrapCopy

`CREATE ROLE postgres WITH SUPERUSER LOGIN PASSWORD 'mypassword';`

### 2\. database "meal_dev" does not exist

If PostgreSQL is running but the database doesn't exist, create it manually:

bash

WrapCopy

`createdb meal_dev -U meal`

### 3\. cannot drop table forms because other objects depend on it

Alembic might have mistakenly added drop_table("forms") in a migration. To fix:

-   Open the migration file in alembic/versions/

-   **Remove** or **comment out** any op.drop_table("forms") line

-   Re-run the migration:

    bash

    WrapCopy

    `alembic upgrade head`

### 4\. Circular Import Errors

-   Ensure base.py **only** defines Base = declarative_base() and does **not** import models.

-   Instead, import models in alembic/env.py or a models/__init__.py.

### 5\. "Target database is not up to date"

-   Run:

    bash

    WrapCopy

    `alembic upgrade head`

-   If still an issue, check for pending migrations.

* * * * *

License
=======

This project is licensed under the **MIT License**. See <LICENSE> for details.

* * * * *

You now have a **fully working** FastAPI + PostgreSQL backend running **locally** (without Docker).\
You can extend it by adding **authentication, data exports, or more business logic**.\
Happy coding! 🚀

* * * * *

📌 How to Use This
------------------

1.  **Copy the content above** and save it as **README.md** in your project root (civibackend/).

3.  **Ensure the database details (e.g., meal_dev, meal) match your actual setup.**

5.  **Commit the changes:**

    bash

    WrapCopy

    `git add README.md git commit -m "Add project documentation"`

* * * * *