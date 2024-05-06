from abc import ABC, abstractmethod


class INotification(ABC):
    @abstractmethod
    def sendNotification(self, user):
        pass