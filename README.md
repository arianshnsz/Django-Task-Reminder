# Django Task Reminder

This is a simple application for managing to-do lists.

Users would be allowed to:
   - Add, Modify, Finish, and Remove tasks.
   - Assign tasks to other users.
   - Set Reminders for their tasks.
   
For notifications, this project uses DWR-910 4G LTE USB Router to send sms to users.

## How to run

1. Make sure `python3` and `pip` are installed in your system.
2. clone the project and make the development environment ready:

```bash
git clone https://github.com/arianshnsz/Django-Task-Reminder.git
python -m venv .venv # create virtual environment called .venv
source .venv/bin/activate # activate the virtual environment
pip install -r requirements.txt # install the required packages
```
<details>

<summary> 
3. Generate the Django Secrete key (click to show the steps): 
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

4. Create database tables:
```bash
python manage.py migrate
```
5. Run the project and visit the following website.
```bash
python manage.py runserver
```

6. (Optional) Connect to DWR-910 device and run the sms script for sending sms to users:

```bash
python manage.py runscript task_notification
```
   This will run `scripts/task_notification.py`.
   
## TODO

- [ ] add SIM800 module
- [ ] accept request before assigning tasks
- [ ] international phone number check
