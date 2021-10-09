from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView,ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from bootstrap_datepicker_plus import DateTimePickerInput



# Create your views here.
# @login_required
# def home(request):
#     context ={"tasks":request.user.task_set.all()}
#     return render(request,"todoApp/TaskDetail.html",context)



class TaskCreateView(CreateView):
    model = Task
    template_name ='todoApp/CreateTask.html'
    fields = ['title','description','due_date']

    def get_form(self):
        form = super().get_form()
        form.fields['due_date'].widget = DateTimePickerInput()
        return form

    # to redirect to home page:
    # success_url = "homepage url name" otherwise it will redirect to the task detailView
    #using the get_absolute_url method in the model
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class TaskUpdateView(UserPassesTestMixin,UpdateView):
    model = Task
    template_name = 'todoApp/CreateTask.html'
    fields = ['title','description','due_date','status']

    #check if user attempting to update task is the author of the task
    def test_func(self):
        task =self.get_object()
        if self.request.user == task.author:
            return True
        return False




class TaskDeleteView(UserPassesTestMixin,DeleteView):
    model = Task
    success_url = reverse_lazy('todoHome')

    def test_func(self):
        task =self.get_object()
        if self.request.user == task.author:
            return True
        return False

class TaskDetailView(UserPassesTestMixin,DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'todoApp/TaskDetail.html'

    def test_func(self):
        task =self.get_object()
        if self.request.user == task.author:
            return True
        return False

class TaskListView(ListView):
    model = Task
    template_name = 'todoApp/TaskListView.html'
    paginate_by = 2
    context_object_name = 'tasks'

    def get_queryset(self):
        return self.request.user.task_set.all().order_by('-date_created')

    # def get(self, request, *args, **kwargs):
    #     context ={"tasks":request.user.task_set.all().order_by('-date_created')}
    #     return render(request,"todoApp/TaskListView.html",context)