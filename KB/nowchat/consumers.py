from channels.consumer import SyscConsumer


class EchoConsumer(SyscConsumer):
    def websocket_connect(self, event):
        print("Connect event is callsd")

    def websocket_receive(self, event):
        print("new event is received")
        print(event)
