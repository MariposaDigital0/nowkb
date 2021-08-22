from django.db import models
from KB.nowhelp.models import ClientDtls


class Chats(models.Model):
    client_dtls = models.ForeignKey(ClientDtls, on_delete=models.CASCADE)
    chat = models.CharField(max_length=1000)
    ad_or_user = models.CharField(max_length=10)

    def __str__(self):
        return self.chat
