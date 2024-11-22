from enum import Enum

Coordinate = tuple[int, int]


class Square(Enum):
    EMPTY = "0"
    SNAKE = "S"
    SNAKE_HEAD = "H"
    FOOD = "F"

    def __str__(self) -> str:
        return self.value


class Reward(Enum):
    FOOD = 1
    MOVE = 0
    DEATH = -1


class Action(Enum):
    UP = "UP"
    DOWN = "DOWN"
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    NONE = "NONE"

    def to_coordinate(self) -> Coordinate:
        return {
            Action.UP: (0, -1),
            Action.DOWN: (0, 1),
            Action.LEFT: (-1, 0),
            Action.RIGHT: (1, 0),
            Action.NONE: (0, 0),
        }[self]
