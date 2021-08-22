from django.db import models
from django.db.models.fields import CharField
from KB.posts.models import Posts
from ckeditor.fields import RichTextField


class Articles(models.Model):
    title = models.CharField(max_length=225)
    body = RichTextField(null=True, blank=True)
    # keywords = models.TextField()
    # slug = models.CharField(max_length=10)
    post = models.ForeignKey(
        Posts, on_delete=models.SET_NULL, blank=True, null=True)
    published = models.BooleanField()

    def __str__(self):
        return self.title
