from ESDecorator import ESDecorator
from utils import *

class ClassicoDecorator(ESDecorator):
    def send(self):
        body = read_html('newsletter/classicos.html')
        recipients = 'classico'
        return self._emailsender.send(body, recipients)
