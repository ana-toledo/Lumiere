from ESDecorator import ESDecorator


class ClassicoDecorator(ESDecorator):
    def send(self):
        body = ' clássico '
        recipients = 'classico'
        return self._emailsender.send(body, recipients)
