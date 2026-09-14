# Django To-Do List

A simple To-Do List web app built with Django, featuring per-user authentication, full CRUD functionality, Bootstrap styling, and task filtering.

## Features

- **User Authentication** — register, login, and logout (powered by Django's built-in auth system)
- **Per-User Task Isolation** — each user only sees and manages their own tasks
- **CRUD Operations** — create, view, edit, toggle status, and delete tasks
- **Task Filtering** — filter tasks by All / Pending / Done
- **Responsive UI** — styled with Bootstrap 5 (via CDN)

## Tech Stack

- **Backend:** Django 6.1
- **Database:** SQLite
- **Frontend:** Django Templates + Bootstrap 5
- **Language:** Python 3.12

## Getting Started

### Prerequisites

- Python 3.10 or higher installed

### Installation

1. Clone the repository

   ```bash
   git clone https://github.com/michaelsant26/django-todolist.git
   cd django-todolist
   ```

2. Create and activate a virtual environment

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Mac/Linux
   source venv/bin/activate
   ```

3. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations

   ```bash
   python manage.py migrate
   ```

5. Create a superuser (optional, for admin panel access)

   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server

   ```bash
   python manage.py runserver
   ```

7. Open your browser at `http://127.0.0.1:8000/`

## Project Structure

```
todolist_project/
├── config/          # Project settings and root URL configuration
├── todo/            # Main app: models, views, forms, templates
│   ├── templates/todo/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── forms.py
├── manage.py
└── requirements.txt
```

## Future Improvements

- Task due dates and priority levels
- Task categories/labels
- Deployment to a live hosting platform

## License

This project is open source and available for learning purposes.
