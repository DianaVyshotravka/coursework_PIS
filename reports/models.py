from django.contrib.auth.models import User
from django.db import models


class Report(models.Model):
    name = models.CharField(max_length=255)
    project = models.CharField(max_length=255)
    file = models.FileField(upload_to='reports')
    description = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)