from .abstract_auto import AbstractAuto

class GMSports(AbstractAuto):
    def start(self):
        print("GM sport started")    
    
    def stop(self):
        print("GM sport stopped")