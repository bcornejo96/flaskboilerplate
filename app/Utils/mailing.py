from os import getenv
from app import mail
from flask_mail import Message
from flask import render_template


class Mailing:
    def __init__(self):
        self.sender = ('Flask Boilerplate', getenv('MAIL_USERNAME'))

    def email_reset_password(self, recipient, name, password):
        html = render_template(
            'reset_password.html', 
            name=name, password=password)
        return self.__sendMail(
            f'Reinicio de contraseña - {recipient}',
            [recipient],
            html
        )

    def __sendMail(self, subject, recipients, html):
        message = Message(
            subject=subject,
            sender=self.sender,
            recipients=recipients,
            html=html

        )
        return mail.send(message)

