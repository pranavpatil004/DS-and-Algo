from abs_decorator import AbstractSeatDecorator
from seats.seat import Seat

class DeltaAirlinesSeat(AbstractSeatDecorator):
    def __init__(self, seat: Seat) -> None:
        self.__seat = seat

    @property
    def aminities(self):
        return self.__seat.aminities + ["IceCream"]
    
    @property
    def seat_price(self):
        return self.__seat.seat_price  + 100