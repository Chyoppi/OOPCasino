from random import randint
import Player

class DiceGame:
    def __init__(self, player: Player):
        self.player = player
        self.dice = 0

    def roll_dice(self):

        self.dice = randint(1, 6)
        return self.dice
    
    def who_won (self, player, house):
        if player > house:
            return "Player"
        elif player < house:
            return "House"
        else:
            return "Tie"
