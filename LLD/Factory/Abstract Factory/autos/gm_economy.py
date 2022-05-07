from .abstract_auto import AbstractAuto

class GMEconomy(AbstractAuto):
    def start(self):
        print("GM Economy started")
    
    def stop(self):
        print("GM Economy stopped")