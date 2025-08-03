from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    author=serializers.CharField(source='author.username')
    class Meta:
        model=Task
        fields=["title","description","status","due_date","author"]
        
        