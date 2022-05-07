from .abstract_auto import AbstractAuto

class FordLuxury(AbstractAuto):
    def start(self):
        print("Ford luxury started")
    
    def stop(self):
        print("Ford luxury stopped")