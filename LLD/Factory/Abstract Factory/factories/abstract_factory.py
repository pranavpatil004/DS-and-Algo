import abc

class AbstractFactory(abc.ABC):
    
    @abc.abstractmethod
    def create_economy(self):
        pass
    
    @abc.abstractmethod
    def create_sport(self):
        pass

    @abc.abstractmethod
    def create_luxury(self):
        pass