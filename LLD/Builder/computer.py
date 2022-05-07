class Computer(object):
    def __init__(self) -> None:
        self.case = self.memory = self.cpu = self.motherboard = self.hard_drive = self.video_card = ""

    def display(self):
        print("Custom computer")
        print(self.case, self.memory, self.cpu, self.motherboard, self.hard_drive, self.video_card)




