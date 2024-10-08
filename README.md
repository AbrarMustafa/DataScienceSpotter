
## Overview
The project is structured in a modular way, with separate apps for `books` and `authors`.

## Requirements
- Python 3.8+ (Recommended Python:3.9.6)
- Django 4.2+
- Relational DB e.g Postgres

## Setup

### 1. Clone the Repository
```bash
git clone https://github.com/AbrarMustafa/DataScienceSpotter.git
cd DataScienceSpotter
```

### 2. Create a Virtual Environment
If using VSCode’s default command palette, the virtual environment will be created as `.venv`. To activate it:

- **On macOS/Linux:**
  ```bash
  source .venv/bin/activate
  ```
- **On Windows:**
  ```bash
  .venv\Scripts\activate
  ```

### 3. Install Dependencies
```bash
pip3 install -r requirements.txt
```

### 4. Set Up the Database
Run the following commands to create the database and apply migrations:
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

### 5. Create a Superuser
To access the Django admin panel, create a superuser:
```bash
python3 manage.py createsuperuser
```

### 6. Run the Development Server
Start the Django development server:
```bash
python3 manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser to access the application.

## Testing
To run the tests for the project:
```bash
python3 manage.py test
```

## Directory Structure
```
DataScienceSpotter/
├── books/                  # Books app
├── authors/                # Authors app
├── DataScienceSpotter/     # Main project configuration
├── .venv/                  # Virtual environment
├── manage.py               # Django's CLI utility
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

## Seed Json File Data
```bash
python3 manage.py seed_authors
python3 manage.py seed_books
```

## Register Fake User Request "localhost"
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/api/register/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "username": "author1",
    "password": "author1",
    "password2": "author1"
  }'
```

