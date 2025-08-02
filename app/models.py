from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()
STATUS=[
    ("Pending","pending"),
    ("Progress","in-progress"),
    ("Finished","finished"),
]
class Task(models.Model):
    title = models.CharField(max_length=255)
    description=models.TextField()
    status=models.CharField(max_length=50,choices=STATUS,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    due_date=models.DateTimeField(null=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} by {self.author}"
