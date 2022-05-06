from .abstract_auto import AbstractAuto

class ChevyVolt(AbstractAuto):
    def start(self):
        print("Chevy volt started correctly")
    
    def stop(self):
        print("Chevy volt stopped")


