from thespian.actors import Actor


class TicketCounter(Actor):
    def __init__(self, *args, **kwargs):
        self.count = 1
        super().__init__(*args, **kwargs)

    def receiveMessage(self, message, sender):
        if isinstance(message, str) and message == "What's my count?":
            msg = "Actor Ticket is: " + str(self.count)
            self.count += 1
            self.send(sender, msg)
