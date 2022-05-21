from .seat import Seat


class EconomySeat(Seat):
    
    @property
    def seat_price(self):
        return 5000
    
    @property
    def aminities(self):
        return ["NewsPaper"]