from django.shortcuts import render
from .models import ClientDtls
from KB.nowchat.models import Chats
import random
import re


def generate_session_token(length=10):
    return ''.join(random.SystemRandom().choice([chr(i) for i in range(97, 123)]+[str(i) for i in range(10)]) for _ in range(length))


def nowHelp(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        text = request.POST['ask']
        token = generate_session_token()
        cl = ClientDtls(name=name, email=email, question=text, token=token)
        cl.save()
        client = ClientDtls.objects.get(token=token)
        context = {
            'client': client
        }
        return render(request, 'clchat.html', context)
    else:
        context = {

        }
        return render(request, 'nowHelp.html', context)
