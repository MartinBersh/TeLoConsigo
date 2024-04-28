from abc import ABC

from INotification import INotification


class ScreenNotification(INotification, ABC):
    def sendNotification(self, user):
        print(f"(Mensaje en pantalla)\n'El usuario {user.name} fue registrado con éxito y tendrá acceso a la página pronto'")
