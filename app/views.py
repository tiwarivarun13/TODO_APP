from django.shortcuts import render
from rest_framework import viewsets,permissions
from .models import Task
from .serializers import TaskSerializer
from rest_framework.pagination import PageNumberPagination
# Create your views here.

class StandardResultSetPagination(PageNumberPagination):
      page_size=5 #Number of record you want to see in a page
      page_size_query_param='page_size' #Here this attribute will be decided by User
      page_query_param='p'
      max_page_size=3 #Maximum page size user can give
      last_page_strings='end' # By default it is last and you can override it by using this attribute


class TaskViewSet(viewsets.ModelViewSet):
    queryset= Task.objects.all()
    serializer_class=TaskSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    pagination_class=StandardResultSetPagination

    def perform_create(self,serializer):
            serializer.save(author=self.request.user)
