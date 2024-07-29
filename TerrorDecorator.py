from ESDecorator import ESDecorator
from utils import *

class TerrorDecorator(ESDecorator):

    def send(self):
        body = read_html('newsletter/terror.html')
        recipients = 'terror'
        return self._emailsender.send(body, recipients)