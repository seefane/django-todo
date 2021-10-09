from django.shortcuts import get_object_or_404
from django.http import HttpResponse, Http404
from rest_framework import status, filters, viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.views import APIView
from todoApp.models import Task
from .serializers import TodoSerializer


def is_author(obj, req):
    if req.user == obj.author:
        return True
    return False

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
def api_task_list(request):

        tasks = Task.objects.all()
        serializer = TodoSerializer(tasks, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
def api_task_view(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return HttpResponse(status=404)
    if is_author(task,request):
            serializer = TodoSerializer(task)
            return Response(serializer.data)
    else:
        return Response({'response':'You are not allowed to view this task'})


@api_view(['PUT'])
def api_task_update(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return HttpResponse(status=404)
    if is_author(task,request):

        serializer = TodoSerializer(task,data=request.data)
        data={}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "Update completed successfully"
            return Response(data=data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'response':'You are not allowed to edit this task'})

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
def api_task_delete(request, pk):

    task = get_object_or_404(Task,pk=pk)
    if is_author(task,request):

            deletion = task.delete()
            message = {}
            if deletion:
                message['success'] = 'task successfully deleted'
            else:
                message['failure'] = 'task deletion failed'
            return Response(data=message)
    else:
        return Response({'response':'You are not allowed to delete this task'})

class ApiUserTasksList(ListAPIView):

    authentication_classes = [TokenAuthentication,SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class =  TodoSerializer
    # pagination_class = PageNumberPagination
    filter_backends = [filters.OrderingFilter]
    filterset_fields = ['title', 'description','author__username']


    def get_queryset(self):
        return self.request.user.task_set.all().order_by('-date_created')

class ApiCreateTask(CreateAPIView):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TodoSerializer

    def post(self, request, *args, **kwargs):
        user = request.user
        task = Task(author=user)

        serializer = TodoSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ApiDeleteTask(DestroyAPIView):
    queryset = Task.objects.all()
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    serializer_class = TodoSerializer
    lookup_field = 'pk'

    def get(self,request,pk):
        task = get_object_or_404(Task,pk=pk)
        task.delete()
        return Response('Task Deleted',status=status.HTTP_200_OK)

class ApiUpdateTask(APIView):

    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TodoSerializer



    def put(self, request, pk, format=None):
        task = get_object_or_404(Task,pk=pk)
        serializer = TodoSerializer(task, data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


