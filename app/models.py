from django.db import models
from django.contrib.auth import get_user_model
from .managers import SoftDeleteManager
from django.utils import timezone
# Create your models here.
User = get_user_model()

class Task(models.Model):
    STATUS=[
    ("Pending","pending"),
    ("Progress","in-progress"),
    ("Finished","finished"),
]
    title = models.CharField(max_length=255)
    description=models.TextField()
    status=models.CharField(max_length=50,choices=STATUS,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    due_date=models.DateTimeField(null=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    active=models.BooleanField(default=True)
    deleted_at=models.DateTimeField(null= True)

    objects = SoftDeleteManager()
    all_objects=models.Manager()

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def delete(self,*args,**kwargs):
        self.active=False
        self.deleted_at=timezone.now()
        self.save()

    def permanent_delete(self,*args,**kwargs):
        super().delete(*args,**kwargs)
    
    def restore_deleted(self,*args,**kwargs):
        self.active=True
        self.deleted_at=None
        self.save()

    


