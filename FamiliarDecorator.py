from ESDecorator import ESDecorator
from utils import *


class FamiliarDecorator(ESDecorator):
    def send(self):
        body = read_html('newsletter/familia.html')
        recipients = 'familia'
        return self._emailsender.send(body, recipients)
