from .abstract_factory import AbstractFactory
import autos
class GMFactory(AbstractFactory):
    def create_economy(self):
        return autos.GMEconomy()
    
    def create_luxury(self):
        return autos.GMLuxury()
    
    def create_sport(self):
        return autos.GMSports()