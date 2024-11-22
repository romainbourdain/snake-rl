from src.utils import Coordinate


class Snake:
    _body: list[Coordinate]
    _direction: Coordinate

    def __init__(self, grid_size: Coordinate):
        self._body = [(grid_size[0] // 2, grid_size[1] // 2)]
        self._direction = (0, -1)

    def move(self, grow: bool = False):
        head_x, head_y = self.head
        delta_x, delta_y = self._direction
        new_head = (head_x + delta_x, head_y + delta_y)

        self._body.insert(0, new_head)

        if not grow:
            self._body.pop()

    def is_head_colliding(self):
        return self.head in self._body[1:]

    def is_outside(self, grid_size: Coordinate):
        head_x, head_y = self.head
        return not (0 <= head_x < grid_size[0] and 0 <= head_y < grid_size[1])

    @property
    def head(self):
        return self._body[0]

    @property
    def body(self):
        return self._body

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, new_direction: Coordinate):
        opposite_direction = (-self._direction[0], -self._direction[1])
        if new_direction == (0, 0) or new_direction == opposite_direction:
            return

        self._direction = new_direction
