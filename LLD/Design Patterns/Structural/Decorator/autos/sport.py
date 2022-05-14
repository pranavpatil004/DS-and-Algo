from .auto_car import AutoCars

class Sport(AutoCars):
    @property
    def description(self):
        return "Sport"
    
    @property
    def price(self):
        return 3000