import abc

class AbstractAdapter(abc.ABC):
    def __init__(self, adaptee) -> None:
        self._adaptee = adaptee
    @abc.abstractmethod
    def request(self, data):
        pass