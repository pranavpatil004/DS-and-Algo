from .auto_car import AutoCars

class Luxury(AutoCars):
    @property
    def description(self):
        return "luxury"
    
    @property
    def price(self):
        return 2000