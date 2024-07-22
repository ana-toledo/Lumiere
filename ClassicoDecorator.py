from ESDecorator import ESDecorator


class ClassicoDecorator(ESDecorator):
    def send(self):
        # Modifique a lógica para incluir conteúdo clássico
        body = ''
        recipients = 'classico'
        return self._emailsender.send(body, recipients)
