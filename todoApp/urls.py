from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views


urlpatterns = [
    #path('',views.home,name="todoHome"),
    path('',login_required(views.TaskListView.as_view()),name='todoHome'),
    path('task/add/',login_required(views.TaskCreateView.as_view()),name='create-task'),
    path('task/<int:pk>/edit/', views.TaskUpdateView.as_view(), name='task-update'),
    path('task/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task-delete'),
    path('task/<int:pk>/', views.TaskDetailView.as_view(), name='task-detail'),
]