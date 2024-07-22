from EmailSender import EmailSender
import sqlite3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class ConcreteEmailSender(EmailSender):
    def __init__(self, smtp_server='smtp.gmail.com', smtp_port=587, username='', password=''):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send(self, body, recipients):
        # Insira a lógica para enviar emails

        # Para usar os dados guardados da database, você precisa:
        # 1) Se conectar a ela (veja o exemplo no app.py);
        # 2) Usar o statement REQUEST. O site https://kb.iu.edu/d/ahux explica bem.

        # QUERY DB
        con = sqlite3.connect('database.db')
        c = con.cursor()
        c.excecute('SELECT email FROM user_info WHERE {recipients} = 1')
        emails = c.fetchall()
        con.close()
        email_list = [email[0] for email in emails]

        # SETUP MAIL MSG
        msg = MIMEMultipart()
        msg['From'] = self.username
        msg['Subject'] = 'lumiere {recipients}'
        msg.attach(MIMEText(body, 'plain'))

        # SETUP MAIL SERVER
        server = smtplib.SMTP(self.smtp_server, self.smtp_port)
        server.starttls()
        server.login(self.username, self.password)

        # SEND MAIL
        for email in email_list:
            msg['To'] = email
            text = msg.as_string()
            server.sendmail(self.username, email, text)

        server.quit()
        return
