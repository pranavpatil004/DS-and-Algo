from .seat import Seat

class FirstClassSeat(Seat):
    @property
    def seat_price(self):
        return 15000
    
    @property
    def aminities(self):
        return ["NewsPaper", "Business Magazines", "Cold Drink", "Food", "TV", "Icecream"]