class Event:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, func):
        self.subscribers.append(func)

    def notify(self, *args, **kwargs):
        for subscriber in self.subscribers:
            subscriber(*args, **kwargs)


# Define a handler for the event
def on_custom_event(data):
    print(f"Received event data: {data}")


# Create event
event = Event()
event.subscribe(on_custom_event)

# Trigger event
event.notify("Hello World")
