from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="note", null=True)
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=300)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
