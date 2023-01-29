import abc
from cell_type import CellType


class PlayingStrategy(abc.ABC):
    @abc.abstractmethod
    def execute(self, x, y, grid_cells):
        pass


# TODO
class MissileStrategy(PlayingStrategy):
    def execute(self, x, y, grid_cell_obj):
        score = 0
        grid_cells = grid_cell_obj.grid_cells
        if grid_cells[x][y] == CellType.EMPTY_CELL:
            grid_cells[x][y] = CellType.MISS
        elif grid_cells[x][y] == CellType.BATTLESHIP:
            grid_cells[x][y] = CellType.DEAD_BATTLESHIP
            score += 1
        return score


class PlayingStrategyFactory:
    def get_strategy(self, type):
        switcher = {"Missile": MissileStrategy()}
        return switcher.get(type, "Invalid strategy")
