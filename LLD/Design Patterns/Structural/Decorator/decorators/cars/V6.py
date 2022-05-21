from .abs_decorator import AbstractDecorator

class V6(AbstractDecorator):
    def __init__(self, car) -> None:
        self.__car = car
    
    @property
    def description(self):
        return self.__car.description + " , V6"
    
    @property
    def price(self):
        return self.__car.price + 200