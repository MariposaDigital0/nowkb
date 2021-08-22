from django.urls import path
from KB.nowchat.consumers import EchoConsumer

application = ProtocolTypeRouter({
    'websocket': URLRouter([
        path('ws/chat/', EchoConsumer)
    ])
})
