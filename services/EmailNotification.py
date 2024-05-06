from abc import ABC

from services.INotification import INotification


class EmailNotification(INotification, ABC):
    def sendNotification(self, user):
        print(f"Email de beienvenida enviado a {user.email}");