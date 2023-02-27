# Django-Task-Reminder

This project allows users to manage their to-do lists and also set reminders for them.

Users also would be allowed to assign tasks for each other .

## How to run

1. Make sure `python3` and `pip` are installed in your system.
2. clone the project and make the development environment ready:

```bash
git clone https://github.com/arianshnsz/Django-Task-Reminder.git
python -m venv .venv # create virtual environment called .venv
source .venv/bin/activate
pip install -r requirements.txt
```

4. Generate the Django Secrete key:

   4.1 Access the Python Interactive Shell:
   
   ```bash
   django-admin shell
   ```
   
   4.2 Import the `get_random_secret_key()` function from `django.core.management.utils`:
   
   ```bash
   from django.core.management.utils import get_random_secret_key
   ```
   
   4.3 Generate the Secrete key `using get_random_secret_key()` function:
   
   ```bash
   get_random_secret_key()
   ```
   
   4.4 In the existing directory, create a file name `.env` and paste the following line inside it:
   
   ```
   SECRET_KEY = "... your generated secret key from part 4 ..."
   ```
   
5. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
6. Create database tables:
   ```bash
   python manage.py migrate
   ```
7. Run the project using `python manage.py runserver` and visit the following website.
