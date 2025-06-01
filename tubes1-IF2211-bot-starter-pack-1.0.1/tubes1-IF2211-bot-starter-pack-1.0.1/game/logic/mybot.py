from game.logic.base import BaseLogic
from game.models import Board, GameObject

class Mybot(BaseLogic):
    def __init__(self):
        super().__init__()
        self.my_attribute = 0

    def next_move(self, board_bot: GameObject, board: Board):
        delta_x = 1
        delta_y = 0
        return delta_x, delta_y
