from django.db import models
from django.conf import settings
from django.utils import timezone


class Task(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    is_finished = models.BooleanField(default=False)
    is_notified = models.BooleanField(default=False)
    is_assigned = models.BooleanField(default=False)
    assigned_by = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='item_assigned')
    owner = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='item_created')

    class Meta:
        ordering = ('due_date',)

    def __str__(self):
        return self.title

    def has_alarm(self):
        return self.due_date is not None

    def has_expired(self):
        if self.has_alarm():
            return timezone.now() > self.due_date
        else:
            return False

    def status(self):
        if self.is_finished:
            return 'is_finished'
        elif self.has_expired():
            return 'Expired'
        else:
            return 'In progress'
