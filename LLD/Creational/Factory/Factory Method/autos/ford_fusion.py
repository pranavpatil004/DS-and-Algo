from .abstract_auto import AbstractAuto


class FordFusion(AbstractAuto):
    def start(self):
        print("Ford fusion started")
    
    def stop(self):
        print("Ford fusion stoped")
