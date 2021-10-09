from rest_framework import serializers
from todoApp.models import Task
from django.contrib.auth.models import User


class TodoSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')
    description = serializers.CharField(required=False)
    due_date = serializers.DateTimeField(required=False)


    class Meta:
        model = Task
        fields = ['id','username','title', 'description', 'date_created', 'due_date', 'status']
        read_only_fields = ['id','username']
        
    def get_username(self,task):
        return task.author.username

    def getid(self,task):
        return task.id

