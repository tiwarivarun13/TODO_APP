from django.shortcuts import render
from rest_framework import viewsets,permissions
from .models import Task
from .serializers import TaskSerializer
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .filters import TaskFilter
# import django_filters.rest_framework

# Create your views here.

class StandardResultSetPagination(PageNumberPagination):
      page_size=5 #Number of record you want to see in a page
      page_size_query_param='page_size' #Here this attribute will be decided by User
      page_query_param='p'
      max_page_size=3 #Maximum page size user can give
      last_page_strings=('end',)  # By default it is last and you can override it by using this attribute


class TaskViewSet(viewsets.ModelViewSet):
    queryset= Task.objects.all().order_by("due_date")
    serializer_class=TaskSerializer
    permission_classes=[permissions.IsAuthenticated]
    pagination_class=StandardResultSetPagination
    filter_backends=[DjangoFilterBackend]
    filterset_class= TaskFilter
    # filter_backends=[filters.SearchFilter]
    # search_fields=['author__username','status']

    def perform_create(self,serializer):
            serializer.save(author=self.request.user)

    def get_queryset(self):
          user=self.request.user
          task=Task.objects.filter(author=user)
          return task