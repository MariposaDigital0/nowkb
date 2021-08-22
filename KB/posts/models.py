from django.db import models
from django.db.models.fields import CharField, TextField
from KB.category.models import Category


class Posts(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    Keywords = models.TextField()
    # slug = models.CharField(max_length=100, null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
