from django.db import models
from django.db.models.query import QuerySet

class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active=True)