from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField()
    TASK_STATUS_CHOICES = [
        ("Pending", 'Pending'),
        ("Completed", 'Completed'),
    ]
    status = models.CharField(
        max_length=10,
        choices=TASK_STATUS_CHOICES,
        default="Pending",
    )

    #redirects to task detail after a successful creat/edit
    def get_absolute_url(self):
        return reverse('task-detail',kwargs={'pk':self.pk})





