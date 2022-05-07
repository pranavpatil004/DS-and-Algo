from .abstract_factory import AbstractFactory
import autos

class FordFactory(AbstractFactory):
    def create_economy(self):
        return autos.FordEconomy()
    def create_luxury(self):
        return autos.FordLuxury()
    def create_sport(self):
        return autos.FordSports()
