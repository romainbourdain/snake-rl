from src.engine.game_engine import GameEngine
from src.interfaces.terminal_interface import TerminalInterface


def main():
    game_engine = GameEngine(10, 10)
    terminal_interface = TerminalInterface(game_engine)
    terminal_interface.run()


if __name__ == "__main__":
    main()
