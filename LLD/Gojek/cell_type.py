import enum


class CellType(enum.Enum):
    EMPTY_CELL, BATTLESHIP, DEAD_BATTLESHIP, MISS = "_", "B", "X", "O"
