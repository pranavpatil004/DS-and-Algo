from .abstract_auto import AbstractAuto

class FordEconomy(AbstractAuto):
    def start(self):
        print("Ford economy started")
    
    def stop(self):
        print("Ford economy stopped")
        