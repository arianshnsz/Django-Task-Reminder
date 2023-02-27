from rest_framework import serializers
from reminder.models import Task


class ReminderCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date']


class ReminderAssignSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'owner']


class ReminderListSerializer(serializers.ModelSerializer):
    due_date = serializers.DateTimeField(format="%a, %b %d, %Y %H:%M")

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date',
                  'is_finished', 'has_expired', 'status', 'is_assigned', 'owner']


class ReminderDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['title', 'description',
                  'due_date', 'is_finished', 'is_notified']
