import random

from src.utils import Coordinate


class Food:
    _position: Coordinate

    def __init__(self, grid_size: Coordinate, snake_body: list[Coordinate]):
        while True:
            self._position = self._generate_random_position(grid_size)
            if self._position not in snake_body:
                break

    def _generate_random_position(self, grid_size: Coordinate) -> Coordinate:
        return (
            random.randint(0, grid_size[0] - 1),
            random.randint(0, grid_size[1] - 1),
        )

    @property
    def position(self):
        return self._position
