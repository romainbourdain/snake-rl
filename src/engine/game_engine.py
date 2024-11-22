from src.engine.snake import Snake
from src.engine.food import Food
from src.utils import Coordinate, Action, Reward
from src.utils import Square


class GameEngine:
    _grid_size: Coordinate
    _snake: Snake
    _food: Food
    _score: int
    _game_over: bool

    def __init__(self, width: int, height: int):
        self._grid_size = (width, height)
        self.reset()

    def reset(self):
        self._snake = Snake(self._grid_size)
        self._food = Food(self._grid_size, self._snake.body)
        self._score = 0
        self._game_over = False

    def step(self, action: Action) -> Reward:
        self._snake.direction = action.to_coordinate()

        grow = self._snake.head == self._food.position
        self._snake.move(grow)

        if grow:
            self._food = Food(self._grid_size, self._snake.body)
            self._score += 1

        if self._snake.is_outside(self._grid_size) or self._snake.is_head_colliding():
            self._game_over = True
            return Reward.DEATH

        return Reward.FOOD if grow else Reward.MOVE

    def __str__(self) -> str:
        return "\n".join(
            "".join(str(square) for square in row) for row in zip(*self.state)
        )

    @property
    def state(self) -> list[list[Square]]:
        grid = [
            [Square.EMPTY for _ in range(self._grid_size[1])]
            for _ in range(self._grid_size[0])
        ]

        food_x, food_y = self._food.position
        grid[food_x][food_y] = Square.FOOD

        head_x, head_y = self._snake.head
        grid[head_x][head_y] = Square.SNAKE_HEAD

        for x, y in self._snake.body[1:]:
            grid[x][y] = Square.SNAKE

        return grid

    @property
    def game_over(self):
        return self._game_over
