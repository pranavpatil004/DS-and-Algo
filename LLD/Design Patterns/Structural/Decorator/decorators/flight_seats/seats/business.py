from .seat import Seat

class BusinessSeat(Seat):
    @property
    def seat_price(self):
        return 10000
    
    @property
    def aminities(self):
        return ["NewsPaper", "Business Magazines", "Cold Drink"]