from .abstract_auto import AbstractAuto


class FordSports(AbstractAuto):
    def start(self):
        print("Ford sports started")
    
    def stop(self):
        print("Ford sports stopped")
        