from abstract_computer_builder import AbstractComputerBuilder

class Director:
    def __init__(self, builder: AbstractComputerBuilder) -> None:
        self.builder = builder
    
    def build_computer(self):
        self.builder.new_computer()
        self.builder.build_motherboard()
        self.builder.install_motherboard()
        self.builder.install_hard_drive()
        self.builder.install_video_card()

    def get_computer(self):
        return self.builder.get_computer()