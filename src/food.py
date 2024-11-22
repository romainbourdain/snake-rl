import random

from src.type import Position

class Food:
  _position: Position
  
  def __init__(self):
    self._position = self._generate_food_position()
    
  @property
  def position(self) -> Position:
    return self._position
    
  def _generate_food_position(self):
    while True:
      position = (random.randint(0, self._board.width-1), 
                  random.randint(0, self._board.height-1))
      if position not in self._snake.body:
        return position