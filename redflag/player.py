from random import Random

from .rider import Rouler, Sprinter


class Player:
    def __init__(self, rng):
        self.sprinter = Sprinter(Random(rng.random()), self)
        self.rouler = Rouler(Random(rng.random()), self)
