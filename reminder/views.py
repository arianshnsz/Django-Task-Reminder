from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.db.models import F
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from reminder.models import Task
from reminder.forms import ReminderCreateForm, ReminderUpdateForm, ReminderAssignForm
from reminder import serializers

User = get_user_model()


# Views for template
class ReminderList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'all_tasks'
    template_name = 'reminder/task_list.html'

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user).order_by(F('due_date').asc(nulls_last=True))


class ReminderCreate(LoginRequiredMixin, CreateView):
    model = Task
    form_class = ReminderCreateForm
    template_name = 'reminder/task_add.html'
    success_url = reverse_lazy('reminder:tasks')

    def form_valid(self, form):
        # the authenticated user will be set as the owner of the task
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ReminderAssign(LoginRequiredMixin, CreateView):
    model = Task
    form_class = ReminderAssignForm
    template_name = 'reminder/task_assign.html'
    success_url = reverse_lazy('reminder:tasks')

    def form_valid(self, form):
        # authenticated user will be set as the person who assigned the task
        form.instance.is_assigned = True
        form.instance.assigned_by = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        # available owners to assign a task. all users are available expect for the person who is assigning
        context = super().get_context_data(**kwargs)
        context['form'].fields['owner'].queryset = User.objects.exclude(
            username=self.request.user)
        return context


class ReminderUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = ReminderUpdateForm
    template_name = 'reminder/task_update.html'
    success_url = reverse_lazy('reminder:tasks')


class ReminderDelete(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('reminder:tasks')


def finish_task(request, pk):
    task = Task.objects.get(id=pk)
    task.is_finished = True
    task.save()

    return redirect('reminder:tasks')


# views for API
class ReminderCreateAPI(generics.CreateAPIView):
    serializer_class = serializers.ReminderCreateSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ReminderAssignAPI(generics.CreateAPIView):
    serializer_class = serializers.ReminderAssignSerializer

    def perform_create(self, serializer):
        serializer.save(is_assigned=True)
        serializer.save(assigned_by=self.request.user)


class ReminderListAPI(generics.ListAPIView):
    serializer_class = serializers.ReminderListSerializer

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user).order_by(F('due_date').asc(nulls_last=True))


class ReminderDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = serializers.ReminderDetailSerializer


@api_view(['GET'])
def finish_task_API(request, pk):

    task = Task.objects.get(id=pk)
    task.is_finished = True
    task.save()

    context = {
        'code': 'task_finished'
    }
    return Response(context)
