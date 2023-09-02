import math
import random

class Player:
    def __init__(self, marker) -> None:
        self.marker = marker
    
    def get_move(self, game):
        pass

class Computer(Player):
    def __init__(self, marker) -> None:
        super().__init__(marker)

    def get_move(self, game):
        pass



class Human(Player):
    def __init__(self, marker) -> None:
        super().__init__(marker)

    def get_move(self, game):
            pass
