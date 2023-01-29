from cell_type import CellType
from playing_strategy import PlayingStrategyFactory
from players import PlayerFactory


class Grid:
    def __init__(self, x, y) -> None:
        self.__grid_cells = [
            [CellType.EMPTY_CELL for col in range(y)] for row in range(x)
        ]

    @property
    def grid_cells(self):
        return self.__grid_cells

    def set_grid_cell_value(self, x, y, value: CellType):
        self.__grid_cells[x][y] = value

    def print_grid(self) -> None:
        for row in range(len(self.__grid_cells)):
            for col in range(len(self.__grid_cells[row])):
                print(CellType(self.__grid_cells[row][col]).value, end=" ")
            print("\n")


class GridFactory:
    @staticmethod
    def get_grid(x, y):
        return Grid(x, y)


class Game:
    def __init__(self, player_grids, strategy) -> None:
        self.player_grids = player_grids
        self.playing_strategy = strategy

    def add_battleship_positions(self, player, positions):
        player_grid = self.player_grids[player]
        for x, y in positions:
            player_grid.set_grid_cell_value(x, y, CellType.BATTLESHIP)

    def execute_playing_strategy(self, opponent, missiles):
        player_score = 0
        for x, y in missiles:
            player_score += self.playing_strategy.execute(
                x, y, self.player_grids[opponent]
            )
        return player_score

    def print_grids(self):
        for player, grid in self.player_grids.items():
            # print(player.player_id)
            grid.print_grid()


class GameFactory:
    def get_game(self, playing_strategy, players, grid_x, grid_y):
        player_grids = {}
        for player in players:
            player_grids[player] = GridFactory.get_grid(grid_x, grid_y)
        strategy = PlayingStrategyFactory().get_strategy(playing_strategy)
        game = Game(player_grids, strategy)
        return game
