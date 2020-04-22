import random


class Word:

    game_word = None
    __words = ("adult", "film", "calm", "doll", "wolf", "moon", "soap", "zebra", "letter", "havoc", "elephant", "tiger", "snake", "military")

    def __init__(self):
        index = random.randint(0, len(self.__words)-1)
        self.game_word = self.__words[index]




