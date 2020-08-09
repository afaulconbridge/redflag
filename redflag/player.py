from random import Random

from .rider import Rouler, Sprinter


class Player:
    def __init__(self, rng):
        self.sprinter = Sprinter(Random(rng.random()), self)
        self.rouler = Rouler(Random(rng.random()), self)
        self.riders = (self.sprinter, self.rouler)
        self.ai = PlayerAI(Random(rng.random()))


class PlayerAI:
    def __init__(self, rng):
        self.rng = rng

    def choose_rider_order(self, riders):
        riders = list(riders)
        self.rng.shuffle(riders)
        return riders

    def choose_card(self, rider):
        return self.rng.choice(rider.hand)
