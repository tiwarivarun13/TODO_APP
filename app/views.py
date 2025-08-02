from django.shortcuts import render
from rest_framework import viewsets,permissions
from .models import Task
from .serializers import TaskSerializer
# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    queryset= Task.objects.all()
    serializer_class=TaskSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self,serializer):
            serializer.save(author=self.request.user)
