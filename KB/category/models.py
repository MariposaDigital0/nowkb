from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    # description = models.TextField()
    # keywords = models.TextField()
    # slug = models.CharField(max_length=100)
    parent = models.ForeignKey(
        'Category', on_delete=models.SET_NULL, blank=True, null=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
