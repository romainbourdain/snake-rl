from enum import Enum
from src.snake import Snake
from src.food import Food
from src.type import Position

class Square(Enum):
  EMPTY = " "
  SNAKE = "S"
  SNAKE_HEAD = "H"
  FOOD = "F"

class Board:
  _width: int
  _height: int
  _board: list[list[Square]]
  
  def __init__(self, width: int, height: int):
    self._width  = width
    self._height = height
    self._board = [[Square.EMPTY for _ in range(self._width)] for _ in range(self._height)]
    
  def update(self, snake: Snake, food: Food):
    self.grid = [[Square.EMPTY for _ in range(self._width)] for _ in range(self._height)]
    
    head_x, head_y = snake.head
    self.grid[head_y][head_x] = Square.SNAKE_HEAD
    
    for x, y in snake.body[1:]:
      self.grid[y][x] = Square.SNAKE
      
    food_x, food_y = food.position
    self.grid[food_y][food_x] = Square.FOOD
  
  def is_inside(self, position: Position) -> bool:
    x, y = position
    return 0 <= x < self._width and 0 <= y < self._height
  
  def display(self):
    pass