from django.contrib import admin
from reminder.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'due_date', 'is_finished', 'is_notified', 'is_assigned', 'assigned_by',
                    'owner', 'has_alarm', 'has_expired']


admin.site.register(Task, TaskAdmin)
