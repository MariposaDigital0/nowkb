from django.db import models
from django.db.models.fields import files
from KB.articles.models import Articles


class Media(models.Model):
    file = models.URLField(max_length=200)
    articals = models.ForeignKey(
        Articles, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.file
