import abc


class CostStrategy(abc.ABC):
    @abc.abstractmethod
    def calculate_cost(self):
        pass

class Fedex(CostStrategy):
    def calculate_cost(self):
        return 8.0

class PostOffice(CostStrategy):
    def calculate_cost(self):
        return 5.0

class Amazon(CostStrategy):
    def calculate_cost(self):
        return 20.0