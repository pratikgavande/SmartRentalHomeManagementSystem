# Smart Rental Home Management System

A Django-based rental home management application for property listings, booking requests, and landlord/tenant workflows.

## Project structure

- `manage.py` - Django project management script
- `myproject/` - Django project settings and application configuration
- `myapp/` - main application logic, templates, static assets, and models
- `myvenv/` - local Python virtual environment (currently included in the repository)
- `staticfiles/` - collected static assets
- `room_images/` and `media/` - property image assets

## Requirements

- Python 3.14
- Django 6.0.4

## Setup

1. Open a terminal in the project root:
   `C:\Users\prati\Downloads\Rental_home-main\Rental_home-main`

2. Activate the existing virtual environment (recommended):
   - PowerShell: `myvenv\Scripts\Activate.ps1`
   - Command Prompt: `myvenv\Scripts\activate.bat`

3. Install dependencies if needed:
   - `pip install -r requirements.txt`

   > Note: This repository currently does not include a `requirements.txt` file. If it is missing, install Django manually with:
   > `pip install django==6.0.4`

4. Run database migrations:
   - `python manage.py migrate`

5. Start the development server:
   - `python manage.py runserver`

6. Open the application in your browser:
   - `http://127.0.0.1:8000/`

## Notes

- The repository currently includes the local virtual environment folder `myvenv/` and collected static files in `staticfiles/`.
- For a cleaner Git history, it is usually best to remove `myvenv/` and `staticfiles/` from version control and add them to `.gitignore`.
- If you need to create a new virtual environment:
  - `python -m venv myvenv`
  - `myvenv\Scripts\Activate.ps1`
  - `pip install django==6.0.4`

## Common commands

- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py createsuperuser`
- `python manage.py collectstatic`

## License

This repository does not include a license file by default.
