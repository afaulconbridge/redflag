from random import Random

from .player import Player
from .rider import Rouler, Sprinter


class Game:
    def __init__(self, rng=Random(42)):
        self.board = [[None, None] for i in range(30)]  # TODO proper length
        self.startline = 6  # TODO proper length
        self.finishline = len(self.board) - 6  # TODO proper length

        self.players = []
        for p in range(4):
            player = Player(Random(rng.random()))
            self.players.append(player)
            # put the players on the track
            self.board[self.startline - p - 1][0] = player.sprinter
            self.board[self.startline - p - 1][1] = player.rouler

    def to_display_string(self):
        display = ""

        # markings
        for i in range(len(self.board)):
            if i < self.startline:
                display += "s"
            elif i >= self.finishline:
                display += "f"
            else:
                display += " "
        display += "\n"

        # racetrack
        lane = 0
        printed = True
        while printed:
            printed = False
            for row in self.board:
                if lane < len(row):
                    printed = True
                    if not row[lane]:
                        display += "."
                    elif isinstance(row[lane], Sprinter):
                        display += "ABCDEF"[self.players.index(row[lane].player)]
                    elif isinstance(row[lane], Rouler):
                        display += "abcdef"[self.players.index(row[lane].player)]
                    else:
                        raise ValueError()
                else:
                    display += " "
            display += "\n"
            lane += 1

        return display
