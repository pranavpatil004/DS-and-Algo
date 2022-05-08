from .abstract_auto import AbstractAuto

class GMLuxury(AbstractAuto):
    def start(self):
        print("GM luxury started")
    
    def stop(self):
        print("GM luxury stopped")