from EmailSender import EmailSender


class ESDecorator(EmailSender):
    _emailsender: EmailSender = None

    def __init__(self, emailsender: EmailSender):
        self._emailsender = emailsender

    def emailsender(self):
        return self._emailsender

    def send(self):
        return self._emailsender.send()