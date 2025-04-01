#Games which are commented have not been implemented yet

#from games.Blackjack import Blackjack
#from games.Slot import Slot
#from games.Roulette import Roulette
from games.DiceGame import DiceGame
from Player import Player



class Casino:
    def __init__(self, balance:int, dicegame:DiceGame):
        self.balance = balance
        self.dicegame = dicegame
        #self.games = {}

    def __str__(self):
        return f"Welcome to casino, you have {self.balance} points in your balance"