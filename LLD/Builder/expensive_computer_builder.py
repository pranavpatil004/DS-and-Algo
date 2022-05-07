from abstract_computer_builder import AbstractComputerBuilder

class ExpensiveComputerBuilder(AbstractComputerBuilder):
    def build_motherboard(self):
        self._computer.motherboard = "MSI"
        self._computer.cpu = "intel"
        self._computer.memory = "8 GB"
    def install_motherboard(self):
        pass
    def install_hard_drive(self):
        self._computer.hard_drive = "2 TB"
    def install_video_card(self):
        self._computer.video_card = "NVidia RT 3080 Ti"
    def get_case(self):
        self._computer.case = "Coolermaster"

