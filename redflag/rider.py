from abc import ABC


class Rider(ABC):
    def __init__(self, rng, player, cards):
        self.rng = rng
        self.player = player
        self.cards = tuple(sorted(cards))

        self.deck = self.rng.shuffle(list(cards))


class Sprinter(Rider):
    def __init__(self, rng, player):
        super().__init__(rng, player, (2, 3, 4, 5, 9) * 3)


class Rouler(Rider):
    def __init__(self, rng, player):
        super().__init__(rng, player, (3, 4, 5, 6, 7) * 3)
