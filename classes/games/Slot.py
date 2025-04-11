
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
        print("Beware of the unfortunate symbol '?'...")
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

    def gameSoundFX(self):
        print("To start, pull the lever!")
        input("Press 'p' to pull the lever: ")
        if input == "p":
            print("Clunk! Clunk! Clunk!")

    def jackpot(self, symbols):
        if random.sample(self.symbols, 3) == symbols["!"] :
            print("You win the jackpot!")
            self.player.add_balance(1000)
            print(f"Your balance is {self.player.get_balance()}.")
            return True
        elif random.sample(self.symbols, 3) == symbols["€"]:
            print("You win the jackpot!")
            self.player.add_balance(1000)
            print(f"Your balance is {self.player.get_balance()}.")
            return True
        elif random.sample(self.symbols, 3) == symbols["£"]:
            print("You win the jackpot!")
            self.player.add_balance(1000)
            print(f"Your balance is {self.player.get_balance()}.")
            return True
        elif random.sample(self.symbols, 3) == symbols["$"]:
            print("You win the jackpot!")
            self.player.add_balance(1000)
            print(f"Your balance is {self.player.get_balance()}.")
            return True
        
    def miniPot(self, symbols):
        if random.sample(self.symbols, 3) == symbols["!"] and symbols["£"]:
            print("Cool! You won the mini POT!")
            self.player.add_balance(75)
            print(f"Your balance is {self.player.get_balance()}.")
            return True
        elif random.sample(self.symbols, 3) == symbols["$"] and symbols["€"]:
            print("Cool! You won the mini POT!")
            self.player.add_balance(75)
            print(f"Your balance is {self.player.get_balance()}.")
            return True
        elif random.sample(self.symbols, 3) == symbols["!"] and symbols["€"]:
            print("Cool! You won the mini POT!")
            self.player.add_balance(75)
            print(f"Your balance is {self.player.get_balance()}.")
            return True
        elif random.sample(self.symbols, 3) == symbols["$"] and symbols["!"]:
            print("Cool! You won the mini POT!")
            self.player.add_balance(75)
            print(f"Your balance is {self.player.get_balance()}.")
            return True
        elif random.sample(self.symbols, 3) == symbols["$"] and symbols["£"]:
            print("Cool! You won the mini POT!")
            self.player.add_balance(75)
            print(f"Your balance is {self.player.get_balance()}.")
            return True
        
    def lose(self, symbols):
        if random.sample(self.symbols, 3):
            print("You lose! Sorry...")
            self.player.remove_balance(50)
            print(f"Your balance is {self.player.get_balance()}.")
            return True
        
    def unfortunate(self,symbols):
        if random.sample(self.symbols, 3) == ["?", "?", "?"]:
            print("You got the unfortunate combo...")
            self.player.remove_balance(130)
            print(f"Your balance is unfortunately {self.player.get_balance()}.")
            return True


        

