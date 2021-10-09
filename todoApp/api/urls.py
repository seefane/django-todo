
from django.urls import path
from . import views


urlpatterns = [
    # path('tasks/',views.api_task_list,name='task-list'),
    path('user-tasks/',views.ApiUserTasksList.as_view(),name='api-user-task-list'),
    path('task/create/',views.ApiCreateTask.as_view(),name='api-task-create'),
    path('task/<int:pk>/',views.api_task_view,name='api-task-detail'),
    path('task/<int:pk>/edit/',views.ApiUpdateTask.as_view(),name='api-task-edit'),
    path('task/<int:pk>/delete/',views.ApiDeleteTask.as_view(),name='api-task-delete'),
]

