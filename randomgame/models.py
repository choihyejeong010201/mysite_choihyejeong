from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Content(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(default='')