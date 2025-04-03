import random
import Player

class slotMachine:
    def __init__(self, player: Player, symbols):
        self.player = player
        self.symbols = ["!", "£", "€", "$", "?"]
    
    def rules(self):
        print("Welcome to the slot machine game!")
        print("These are the rules:")
        print("If you get the 3 same symbols you win the jackpot")
        print("if you get 2 same symbols you win 10% more than your bet")
        print("if you get 3 different symbols you lose your bet")
        print("Good luck!")

    def bet(self):
        print(f"Your balance is {self.player.get_balance()}.")
        moneyBet = int(input("Bet amount: "))
        if moneyBet > self.player.get_balance():
            print("ERROR: You don't have enough money.")
            return
        elif moneyBet <= 0:
            print("ERROR: Invalid bet amount.")
            return
        else:
            self.player.remove_balance(moneyBet)
            print(f"Your balance is {self.player.get_balance()}.")

    def game(self):
        print("Clunk! Clunk! Clunk!")
        
        


        

