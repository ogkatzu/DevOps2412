import random


class Game:
    def __init__(self, name):
        self.name = name
        self.difficulty = None

    def play(self):
        pass


class MemoryGame(Game):
    def __init__(self):
        super().__init__("Memory Game")

    def play(self):
        pass


class GuessGame(Game):
    def __init__(self):
        super().__init__("Guess game")

    def play(self):
        pass


class CurrencyRoulette(Game):
    def __init__(self):
        super().__init__(Game)

    def play(self):
        pass
