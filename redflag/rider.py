from abc import ABC


class Rider(ABC):
    def __init__(self, rng, player, cards):
        self.rng = rng
        self.player = player
        self.cards = tuple(sorted(cards))

        self.deck = list(cards)
        self.rng.shuffle(self.deck)
        self.hand = []
        self.discard = []
        self.removed = []
        self.chosen = None

    def draw(self):
        # shuffle discard pile if necessary
        if not self.deck:
            self.shuffle()
        self.hand.append(self.deck.pop())

    def discard_or_remove_hand(self):
        while self.hand:
            card = self.hand.pop()
            if card == self.chosen:
                self.removed.append(card)
            else:
                self.discard.append(card)

    def shuffle(self):
        assert not self.deck
        self.deck = self.discard
        self.rng.shuffle(self.deck)
        self.discard = []

    def choose(self, x):
        self.chosen = x


class Sprinter(Rider):
    def __init__(self, rng, player):
        super().__init__(rng, player, (2, 3, 4, 5, 9) * 3)


class Rouler(Rider):
    def __init__(self, rng, player):
        super().__init__(rng, player, (3, 4, 5, 6, 7) * 3)
