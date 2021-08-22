from django.shortcuts import render, redirect
from .models import Chats
from KB.nowhelp.models import ClientDtls


def nowChat(request):
    context = {
    }
    return render(request, 'clchat.html', context)


def addChat(request, who, clid):
    client = ClientDtls.objects.get(id=clid)
    if request.method == 'POST':
        if who == 'cl':
            chat = request.POST['typed']
            ch = Chats(client_dtls=client, chat=chat, ad_or_user=who)
            ch.save()
            ct = Chats.objects.filter(client_dtls=client).values()
            context = {
                'ct': ct,
                'client': client
            }
            return render(request, 'clchat.html', context)
        else:
            if who == 'ad':
                chat = request.POST['typed']
                ch = Chats(client_dtls=client, chat=chat, ad_or_user=who)
                ch.save()
                ct = Chats.objects.filter(client_dtls=client).values()
                context = {
                    'ct': ct,
                    'client': client
                }
                return render(request, 'clchat.html', context)
    else:
        ct = Chats.objects.filter(client_dtls=client).values()
        context = {
            'ct': ct,
            'client': client
        }
        return render(request, 'clchat.html', context)
