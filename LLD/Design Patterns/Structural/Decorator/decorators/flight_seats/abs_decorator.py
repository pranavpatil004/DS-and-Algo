import abc

class AbstractSeatDecorator(abc.ABC):
    def __init__(self, seat) -> None:
        self.__seat = seat
    
    @property
    def seat(self):
        return self.__seat


