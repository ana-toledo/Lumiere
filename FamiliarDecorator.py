from ESDecorator import ESDecorator


class FamiliarDecorator(ESDecorator):
    def send(self):
        # Modifique a lógica para incluir conteúdo familiar
        body = ''
        recipients = 'familiar'
        return self._emailsender.send(body, recipients)
