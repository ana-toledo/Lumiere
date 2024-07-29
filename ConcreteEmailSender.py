from EmailSender import EmailSender
import sqlite3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sqlite3

class ConcreteEmailSender(EmailSender):
    def __init__(self, smtp_server='smtp.gmail.com', smtp_port=587, username='', password=''):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send(self, body, recipients):
        try:
            # Connect to the database
            with sqlite3.connect('database.db') as con:
                c = con.cursor()
                query = f'SELECT email FROM user_info WHERE {recipients} = 1'
                c.execute(query)
                emails = c.fetchall()

            email_list = [email[0] for email in emails]

            # Setup mail server
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.username, self.password)

            # Send mail to each recipient individually
            for email in email_list:
                msg = MIMEMultipart()
                msg['From'] = self.username
                msg['To'] = email
                msg['Subject'] = f'Lumiere {recipients}'
                msg.attach(MIMEText(body, 'plain'))
                text = msg.as_string()
                server.sendmail(self.username, email, text)

            server.quit()
            print("Emails sent successfully.")
        
        except smtplib.SMTPAuthenticationError:
            print("Failed to authenticate with the SMTP server. Check your username and App Password.")
        except smtplib.SMTPException as e:
            print(f"Failed to send email: {e}")

        return



