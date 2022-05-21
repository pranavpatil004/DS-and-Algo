from .auto_car import AutoCars

class Economy(AutoCars):
    @property
    def description(self):
        return "Economy"
    
    @property
    def price(self):
        return 1000