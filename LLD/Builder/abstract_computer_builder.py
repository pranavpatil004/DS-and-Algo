import abc
from computer import Computer

class AbstractComputerBuilder(abc.ABC):
    def get_computer(self):
        return self._computer
    def new_computer(self):
        self._computer = Computer()
    @abc.abstractmethod
    def get_case(self):
        pass
    @abc.abstractmethod
    def build_motherboard(self):
        pass
    @abc.abstractmethod
    def install_motherboard(self):
        pass
    @abc.abstractmethod
    def install_hard_drive(self):
        pass
    @abc.abstractmethod
    def install_video_card(self):
        pass
