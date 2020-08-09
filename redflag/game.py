from random import Random

from .player import Player


class Game:
    def __init__(self, rng=Random(42), startline=6):
        self.board = Board(30, startline, 30 - 6)  # TODO proper lengths

        self.players = []
        for p in range(4):
            player = Player(Random(rng.random()))
            self.players.append(player)
            # put the players on the track
            self.board.set_rider_position(player.sprinter, startline - p - 1, 0)
            self.board.set_rider_position(player.rouler, startline - p - 1, 1)

    def is_race_finished(self):
        return self.board.is_race_finished()

    def move_rider(self, row_number, lane_number, steps):
        rider = self.board[row_number][lane_number]
        assert rider, (rider, row_number, lane_number)
        assert steps > 0, steps
        row_target = row_number + steps

        # if it would move beyond end of board, cap it
        if row_target >= len(self.board):
            return self.move_rider(
                row_number, lane_number, len(self.board) - row_number - 1
            )

        # move to innermost lane if possible
        for lane_target, lane in enumerate(self.board[row_target]):
            if not self.board[row_target][lane_target]:
                self.board[row_target][lane_target] = rider
                self.board[row_number][lane_number] = None
                return steps

        # target lane all full, try moving one less
        return self.move_rider(row_number, lane_number, steps - 1)

    def run(self):
        while not self.is_race_finished():
            self.step()

    def run_and_display(self):
        while not self.is_race_finished():
            yield self.board.to_display_string()
            self.step()
        yield self.board.to_display_string()

    def step(self):
        # pick cards
        for player in self.players:
            for rider in player.ai.choose_rider_order(player.riders):
                # draw a hand of cards
                while len(rider.hand) < 4:
                    rider.draw()
                # ask the AI to pick a card
                rider.choose(player.ai.choose_card(rider))
                # discard or remove the hand
                rider.discard_or_remove_hand()

        # move riders based on card chosen in position order descending
        for rider in self.board.get_riders_positionally():
            self.board.move_rider(rider, rider.chosen)

        # self.board.apply_slipstream()

        # self.board.apply_exhaustion()


class Board:
    def __init__(self, length, startline, finishline):
        # TODO hills
        self.riders = []
        self.players = []
        self.rider_positions = {}
        self.length = length
        self.startline = startline
        self.finishline = finishline

    def set_rider_position(self, rider, pos, lane):
        assert rider not in self.riders
        self.riders.append(rider)

        if rider.player not in self.players:
            self.players.append(rider.player)

        rider_id = id(rider)
        assert rider_id not in self.rider_positions
        self.rider_positions[rider_id] = (pos, lane)

    def get_rider_position(self, rider):
        assert rider in self.riders

        rider_id = id(rider)
        assert rider_id in self.rider_positions
        return self.rider_positions[rider_id]

    def get_position_rider(self, pos, lane):
        assert pos >= 0
        assert lane in (0, 1)
        assert pos < self.length

        for key, value in self.rider_positions.items():
            if value[0] == pos and value[1] == lane:
                # key is id(rider)
                for rider in self.riders:
                    if id(rider) == key:
                        return rider

        # no rider at that position
        return None

    def get_riders_positionally(self):
        rider_ids = tuple(
            rider
            for rider, _ in sorted(
                self.rider_positions.items(), key=lambda x: (-x[1][0], x[1][1])
            )
        )
        # TODO make this faster?
        reversed_riders = []
        for rider_id in rider_ids:
            for rider in self.riders:
                if id(rider) == rider_id:
                    reversed_riders.append(rider)
        return tuple(reversed_riders)

    def is_race_finished(self):
        for pos, _ in self.rider_positions.values():
            if pos >= self.finishline:
                return True
        return False

    def move_rider(self, rider, steps):
        rider_id = id(rider)
        assert rider in self.riders
        assert rider_id in self.rider_positions

        pos, _ = self.get_rider_position(rider)

        pos_target = pos + steps

        # if it would move beyond end of board, cap it
        if pos_target >= self.length:
            return self.move_rider(rider, self.length - pos - 1)

        # move to innermost lane if possible
        # TODO relax assumption always 2 wide
        for lane_target in (0, 1):
            if not self.get_position_rider(pos_target, lane_target):
                self.rider_positions[rider_id] = (pos_target, lane_target)
                return steps

        # target lane all full, try moving one less
        return self.move_rider(rider, steps - 1)

    def apply_slipstream(self):
        # TODO
        raise NotImplementedError

    def apply_exhaustion(self):
        # TODO
        raise NotImplementedError

    def get_player_character(self, player):
        assert player in self.players
        return

    def to_display_string(self):
        display = ""

        # markings
        for i in range(self.length):
            if i < self.startline:
                display += "s"
            elif i >= self.finishline:
                display += "f"
            else:
                display += " "
        display += "\n"

        # racetrack
        # TODO relax assumption always 2 wide
        for j in range(2):
            for i in range(self.length):
                rider = self.get_position_rider(i, j)
                if rider:
                    player_char = "abcdefghijklmnopqrstuvwxyz"[
                        self.players.index(rider.player)
                    ]
                    if rider is rider.player.sprinter:
                        player_char = player_char.upper()
                    elif rider is rider.player.rouler:
                        player_char = player_char.lower()
                    else:
                        raise RuntimeError(f"Unrecognized rider {rider}")
                    display += player_char
                else:
                    # no rider, empty track
                    display += "."
            # next lane on new line
            display += "\n"

        return display
