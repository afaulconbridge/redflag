# this is what is imported with import * from redflag
__all__ = ()


class Game:
    def __init__(self):
        self.players = []
        for _ in range(4):
            player = Player()
            self.players.append(player)


class Player:
    def __init__(self):
        pass
