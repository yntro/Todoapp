# Todoapp

A task management web application built with **Django**.

The project started as a basic personal To-Do application and was expanded to support **user accounts, profiles, teams, task assignment, manager permissions, team task management, and a manager dashboard**.

## Features

### User accounts

* User registration and login
* Logout
* Password reset
* User profile management
* Email field during registration
* Automatic `Profile` creation for new users

### Personal tasks

* Create tasks
* View personal tasks
* Update tasks
* Delete tasks
* Track task status

  * In progress
  * Completed
* Tasks are ordered by creation date

### Teams

Users can belong to a team.

Each profile contains:

* Team
* Manager status

Managers can manage tasks belonging to users in their own team.

### Team task management

Managers can:

* Create tasks for team members
* Update team tasks
* Delete team tasks
* Assign tasks only to users belonging to their team
* View tasks belonging to their team

### Manager dashboard

Managers have access to a dashboard containing:

* Number of team members
* Total number of team tasks
* Number of completed tasks
* Number of tasks in progress
* Per-user task statistics

### Custom administration

The project includes a custom administration area for managing:

* Users
* User profiles
* Teams
* Team membership
* Manager permissions

Access is restricted using Django authentication and permission checks.

## Tech Stack

* **Python**
* **Django 6.1**
* **SQLite**
* **Bootstrap 5**
* **django-crispy-forms**
* **crispy-bootstrap5**
* **TinyMCE**
* **Pillow**
* **python-dotenv**

The exact package versions are maintained in `requirements.txt`.

## Project Structure

```text
Todoapp/
│
├── manage.py
├── requirements.txt
│
├── todo/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── todoapp/
    ├── apps.py
    ├── forms.py
    ├── models.py
    ├── signals.py
    ├── urls.py
    ├── views.py
    │
    ├── migrations/
    ├── static/
    └── templates/
```

The repository currently follows this Django project/application structure.

## Models

### Task

A task contains:

* Title
* Description
* Creation date
* Assigned user
* Completion status

Tasks have a foreign-key relationship to Django's built-in `User` model.

### Profile

Extends Django's built-in `User` model with:

* Team
* Manager status

A profile has a one-to-one relationship with a user.

### Team

A team contains:

* Name
* Manager

Users are connected to teams through their profiles.

## Permissions

The application uses Django's authentication and class-based view mixins to control access.

For example:

* Logged-in users can manage their own tasks.
* Managers can access team task functionality.
* Managers can only assign tasks to members of their own team.
* Manager functionality requires the user's profile to have `is_manager=True`.

## Signals

A Django `post_save` signal automatically creates a `Profile` when a new `User` is created.

This keeps the `User` and `Profile` records synchronized.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yntro/Todoapp.git
cd Todoapp
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Create a superuser

```bash
python manage.py createsuperuser
```

### 6. Start the development server

```bash
python manage.py runserver
```

The application will then be available at:

```text
http://127.0.0.1:8000/
```

## Environment Variables

The project includes `python-dotenv`, so environment variables can be stored in a `.env` file.

Example:

```env
SECRET_KEY=your-secret-key
DEBUG=True
```

Do not commit sensitive values such as production secret keys to the repository.

## Development

Useful Django commands:

```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Run development server
python manage.py runserver

# Create a superuser
python manage.py createsuperuser

# Open Django shell
python manage.py shell
```

## Learning Goals

This project is primarily a Django learning project and demonstrates practical use of:

* Django models
* ForeignKey and OneToOne relationships
* ModelForms
* Class-Based Views
* `LoginRequiredMixin`
* `UserPassesTestMixin`
* Django authentication
* Custom permissions
* QuerySets
* Template inheritance
* Context data
* Django signals
* Bootstrap
* Crispy Forms
* Team-based task assignment

## Repository

[GitHub Repository](https://github.com/yntro/Todoapp)
