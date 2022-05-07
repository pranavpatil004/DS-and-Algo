from abstract_computer_builder import AbstractComputerBuilder

class CheapComputerBuilder(AbstractComputerBuilder):
    def build_motherboard(self):
        self._computer.motherboard = "MSI Old"
        self._computer.cpu = "AMD"
        self._computer.memory = "4 GB"
    
    def get_case(self):
        self._computer.case = "Corsair"
    
    def install_motherboard(self):
        pass
    
    def install_hard_drive(self):
        self._computer.hard_drive = "1 TB"
    
    def install_video_card(self):
        self._computer.video_card = "RTX 2080"