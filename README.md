# Django Task Reminder

This is a simple application for managing to-lists.

Users would be allowed to:
   - Add, Modify, and remove tasks.
   - Assign tasks to other users.
   - set Reminders for their tasks.
   
For notifications, this project uses DWR-910 4G LTE USB Router to send sms to users.

## How to run

1. Make sure `python3` and `pip` are installed in your system.
2. clone the project and make the development environment ready:

```bash
git clone https://github.com/arianshnsz/Django-Task-Reminder.git
python -m venv .venv # create virtual environment called .venv
source .venv/bin/activate
pip install -r requirements.txt # install the required packages
```
<details>

<summary> 
4. Generate the Django Secrete key (click to the steps): 
</summary>

   * Access the Python Interactive Shell:
   
   ```bash
   django-admin shell
   ```
   
   * Import the `get_random_secret_key()` function from `django.core.management.utils`:
   
   ```bash
   from django.core.management.utils import get_random_secret_key
   ```
   
   * Generate the Secrete key using `get_random_secret_key()` function:
   
   ```bash
   get_random_secret_key()
   ```
   
   * In the existing directory, create a file name `.env` and paste the following line inside it:
   
   ```
   SECRET_KEY = "... paste your generated secret key ..."
   ```
</details>

5. Create database tables:
   ```bash
   python manage.py migrate
   ```
6. Run the project using `python manage.py runserver` and visit the following website.

7. (Optional) Connect to DWR-910 device and run the sms script for sending sms to users:

   ```bash
   python manage.py runscript task_notigication
   ```
   This will run `scripts/task_notification.py`.
   
## TODO

- [ ] add SIM800 module
- [ ] accept request before assigning tasks
