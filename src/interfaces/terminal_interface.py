from src.engine.game_engine import GameEngine
from src.utils import Action


class TerminalInterface:
    _engine: GameEngine

    def __init__(self, engine: GameEngine):
        self._engine = engine

    def __str__(self) -> str:
        return str(self._engine)

    def get_input(self) -> Action:
        direction = input("Enter direction: ")
        match direction:
            case "z":
                return Action.UP
            case "s":
                return Action.DOWN
            case "q":
                return Action.LEFT
            case "d":
                return Action.RIGHT
            case _:
                return Action.NONE

    def run(self):
        while not self._engine.game_over:
            print(self)
            self._engine.step(self.get_input())

        print("Game Over!")
