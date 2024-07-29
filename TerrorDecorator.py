from ESDecorator import ESDecorator


class TerrorDecorator(ESDecorator):

    def send(self):
        body = ' terror'
        recipients = 'terror'
        return self._emailsender.send(body, recipients)