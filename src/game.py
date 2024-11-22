import random

from src.board import Board
from src.snake import Snake
from src.food import Food

class Game:
  _width: int
  _height: int
  _board: Board
  _snake: Snake
  _food: Food
  _score: int
  
  def __init__(self, width, height):
    self._width = width
    self._height = height
    self.reset()
    
  def reset(self):
    self._board = Board(self._width, self._height)
    self._snake = Snake(initial_position=(self._width//2, self._height//2))
    self._food = Food()
    self._score = 0
      
  def step(self):
    if self._snake.head() == self._food.position:
      self._snake.move(grow=True)
      self._food = Food()
      self._score += 1
    else:
      self._snake.move()
    
    if (not self._board.is_inside(self._snake.head)) or self._snake.collide_with_self():
      return False
    
    self._board.update(self._snake, self._food)
    return True