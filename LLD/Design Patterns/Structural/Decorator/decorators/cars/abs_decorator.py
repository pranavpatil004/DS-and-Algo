from autos.auto_car import AutoCars
import abc

class AbstractDecorator(abc.ABC):
    def __init__(self, car) -> None:
        self.__car = car
    
    @property
    def car(self):
        return self.__car