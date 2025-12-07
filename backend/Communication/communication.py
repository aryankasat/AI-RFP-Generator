from abc import ABC, abstractmethod

class Communication (ABC):

    @abstractmethod
    def send_communication():
        pass

    @abstractmethod
    def receive_communication():
        pass