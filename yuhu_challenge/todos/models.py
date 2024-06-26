from django.contrib.auth.models import User
from django.db import models


class ToDoItem(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.CharField(max_length=500, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    due_date = models.DateTimeField(default=None, blank=True, null=True)
    is_done = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
