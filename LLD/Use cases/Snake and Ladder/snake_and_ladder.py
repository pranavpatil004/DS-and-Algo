import abc
import random


class Cell(abc.ABC):
    @abc.abstractmethod
    def get_destination(self, current_position):
        pass

class StandardCell(Cell):
    def get_destination(self, current_position):
        return current_position
    def __repr__(self) -> str:
        return "Standard Cell"

class Ladder(Cell):
    def __init__(self, ladder_value) -> None:
        self.__ladder_value = ladder_value
    def get_destination(self, current_position):
        return current_position + self.__ladder_value
    def __repr__(self) -> str:
        return f"Ladder {self.__ladder_value}"

class Snake(Cell):
    def __init__(self, snake_value) -> None:
        self.__snake_value = snake_value
    
    def get_destination(self, current_position):
        print("Got snake", current_position, self.__snake_value)
        return current_position - self.__snake_value
    def __repr__(self) -> str:
        return f"Snake {self.__snake_value}"

class Board:
    def __init__(self, cells_dic) -> None:
        self.__cells_dic = cells_dic
    
    def get_position(self, position):
        return self.__cells_dic[position]
    
    @property
    def get_cells_dic(self):
        return self.__cells_dic
    
class BoardFactory:
    def get_board(self, N, ladder_count, snake_count):
        cells_dic = dict()
        for cell in range(1, N**2+1):
            cells_dic[cell] = StandardCell()
        ladder = 0
        
        while ladder < ladder_count:
            ladder_pos = random.randint(1, N**2-N)
            if type(cells_dic[ladder_pos]) == StandardCell:
                cells_dic[ladder_pos] = Ladder(random.randint(5, 8))
                ladder += 1

        snake = 0
        while snake < snake_count:
            snake_pos = random.randint(2*N, N**2-1)
            if type(cells_dic[snake_pos]) == StandardCell:
                cells_dic[snake_pos] = Snake(random.randint(5, 8))
                snake += 1
        
        board = Board(cells_dic)
        return board

# print(BoardFactory().get_board(10, 5, 5).get_cells_dic)

class Dice:
    @staticmethod
    def throw_dice():
        return random.randint(1, 6)

class Player:
    def __init__(self) -> None:
        self.__player_position = 0
    
    @property
    def player_position(self):
        return self.__player_position

    @player_position.setter
    def player_position(self, position):
        self.__player_position = position

    def __repr__(self) -> str:
        return str(self.__player_position)
class Game:
    def __init__(self) -> None:
        self.board = BoardFactory().get_board(10, 5, 15)
    def play(self, number_of_players):
        players = []
        for i in range(number_of_players):
            players.append(Player())
        player_index = 0
        while True:
            current_player = players[player_index]
            dice_val = Dice.throw_dice()
            next_destination = current_player.player_position + dice_val
            if next_destination == 100:
                return player_index
            if next_destination > 100:
                player_index += 1
                continue
            new_destination = self.board.get_position(next_destination).get_destination(next_destination)
            current_player.player_position = new_destination
            if dice_val == 6:
                continue
            player_index = (player_index + 1)%number_of_players
            print(players)

print("Winner is: ", Game().play(3))