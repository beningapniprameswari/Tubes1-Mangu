import random
from typing import Optional

from game.logic.base import BaseLogic
from game.models import GameObject, Board, Position
from ..util import get_direction

class RandomLogic(BaseLogic):
    def __init__(self):
        super().__init__()
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.goal_position: Optional[Position] = None
        self.current_direction = 0

    def next_move(self, board_bot: GameObject, board: Board):
        props = board_bot.properties
        if props.diamonds == 5:
            self.goal_position = props.base
        else:
            self.goal_position = None

        current_position = board_bot.position

        if self.goal_position:
            delta_x, delta_y = get_direction(
                current_position.x,
                current_position.y,
                self.goal_position.x,
                self.goal_position.y,
            )
        else:
            delta_x, delta_y = self.directions[self.current_direction]
            if random.random() > 0.6:
                self.current_direction = (self.current_direction + 1) % len(self.directions)

        return delta_x, delta_y
