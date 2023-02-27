from django.urls import path
from reminder import views

app_name = 'reminder'
urlpatterns = [
    # urls for template
    path('', views.ReminderList.as_view(), name='tasks'),
    path('task/add/', views.ReminderCreate.as_view(), name='task_add'),
    path('task-update/<int:pk>/',
         views.ReminderUpdate.as_view(), name='task_update'),
    path('task/assign/', views.ReminderAssign.as_view(), name='task_assign'),
    path('task/<int:pk>/delete/',
         views.ReminderDelete.as_view(), name='task_delete'),
    path('task/<int:pk>/finish/',
         views.finish_task, name='finish_task'),
    # urls for API
    path('api/', views.ReminderListAPI.as_view()),
    path('api/<int:pk>/', views.ReminderDetailAPI.as_view()),
    path('api/add/', views.ReminderCreateAPI.as_view()),
    path('api/<int:pk>/finish/', views.finish_task_API),
]
