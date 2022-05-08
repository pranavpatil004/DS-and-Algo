from director import Director
from expensive_computer_builder import ExpensiveComputerBuilder
from cheap_computer_builder import CheapComputerBuilder

if __name__ == "__main__":
    for builder in [ExpensiveComputerBuilder(), CheapComputerBuilder()]:
        director = Director(builder)
        director.build_computer()
        computer = director.get_computer()
        computer.display()