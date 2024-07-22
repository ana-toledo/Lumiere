from ESDecorator import ESDecorator


class TerrorDecorator(ESDecorator):
    def send(self):
        # Modifique a lógica para incluir conteúdo de terror
        body = ''
        recipients = 'terror'
        return self._emailsender.send(body, recipients)