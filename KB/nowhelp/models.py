from django.db import models


class ClientDtls(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=245)
    question = models.TextField()
    token = models.CharField(max_length=10)

    def __str__(self):
        return self.name
