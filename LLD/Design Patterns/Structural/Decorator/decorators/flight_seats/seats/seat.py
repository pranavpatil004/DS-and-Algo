import abc

class Seat(abc.ABC):

    def seat_number(self):
        pass
    
    @abc.abstractproperty
    def seat_price(self):
        pass
    
    @abc.abstractproperty
    def aminities(self):
        pass