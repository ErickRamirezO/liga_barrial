# myapp/observer.py

class Observer:
    def update(self, message):
        pass

class User(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f'Notification for {self.name}: {message}')

class MatchSubscriber:
    def update(self, message):
        print(f"Notificación recibida: {message}")

class NotificationManager:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        if subscriber not in self.subscribers:
            self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        if subscriber in self.subscribers:
            self.subscribers.remove(subscriber)

    def notify(self, message):
        for subscriber in self.subscribers:
            subscriber.update(message)
