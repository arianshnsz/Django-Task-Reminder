from reminder.models import Task
import requests
import time
import urllib.parse


def run():
    while True:
        all_tasks = Task.objects.all()
        tasks_to_notify_ids = [
            task.id for task in all_tasks if task.has_expired() and task.is_notified is False]
        for task_id in tasks_to_notify_ids:
            task = Task.objects.get(id=task_id)
            task_description = task.description
            owner = task.owner
            number = task.owner.phone_number
            url = 'http://192.168.0.1/PostMessageList'
            value = '{"pnumber":"%s","content":"You have a reminder! \nTask: %s\nDescription: %s"}' % (
                number, task, task_description)
            payload = {
                'MessageList': value
            }
            requests.get(url, params=urllib.parse.urlencode(
                payload, quote_via=urllib.parse.quote))
            task.is_notified = True
            task.save()
            print(f'{owner} has been notified for task{task}')
        time.sleep(1)
