from ESDecorator import ESDecorator


class FamiliarDecorator(ESDecorator):
    def send(self):
        body = ' familiar'
        recipients = 'familia'
        return self._emailsender.send(body, recipients)
