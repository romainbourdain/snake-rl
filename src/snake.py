from src.type import Position

class Snake:
  _body: list[Position]
  _direction: Position
  
  def __init__(self, initial_position: Position):
    self._body = [initial_position]
    self._direction = (0, 1)
    
  @property
  def head(self):
    return self._body[0]
  
  @property
  def body(self):
    return self._body
  
  @property
  def direction(self):
    return self._direction
    
  def move(self, grow=False):
    head_x, head_y = self.head
    delta_x, delta_y = self._direction
    new_head = (head_x + delta_x, head_y + delta_y)
    
    self._body.insert(0, new_head)
    if not grow:
      self._body.pop()
  
  @direction.setter
  def direction(self, new_direction: Position):
    opposite_direction = (-self._direction[0], -self._direction[1])
    if new_direction != opposite_direction:
      self._direction = new_direction
  
  def collide_with_self(self) -> bool:
    return self.head in self._body[1:]