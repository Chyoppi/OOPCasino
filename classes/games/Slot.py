
import random 
from Player import Player

class slotMachine:

    def __init__(self, player: Player):
        self.player = player
        self.symbols = ["!", "£", "€", "$", "?"]  # Slot machine symbols
        
    def set_bet(self):
        if self.player.get_balance() <= 0:
            print("Not enough balance to play")
            return False
        while True:
            try:
                bet = int(input(f"Your current balance is {self.player.get_balance()}. Enter your bet: "))
                if 0 < bet <= self.player.get_balance():
                    self.player.remove_balance(bet)
                    self.player.set_bet(bet)
                    return True
                else:
                    print("Invalid bet amount. Please enter a positive number within your balance.")
            except ValueError:
                print("Invalid input. Please enter a number.") 
    
    # Explanation of the rules
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

    # Starts the game and add "clunk" sound effect
    def gameSoundFX(self):
        print("To start, pull the lever!")
        player_input = input("Press 'p' to pull the lever: ")
        if player_input == "p":
            print("Clunk! Clunk! Clunk!")
        else:
            print("ERROR")
        

    def jackpot(self, result):
        jackpot_symbols = ["!", "£", "€", "$"] #only these symbols are allowed in the jackpot

        if result[0] == result[1] == result[2] and result[0] in jackpot_symbols: #this makes sure that the symbols are the same and not including the "?" symbol
            print("You win the jackpot!")
            self.player.add_balance(1000) # If you win you get a lot of money
            print(f"Your balance is {self.player.get_balance()}.")
            return True
        return False
        
    def miniPot(self, result):
        
        minipot_symbols = ["!", "£", "€", "$"]
        
        if len(set(result)) == 2 and all(symbol in minipot_symbols for symbol in result):  # Check if there are 2 same symbols and 1 different symbol
            print("Cool! You won the mini POT!")
            self.player.add_balance(75)
            print(f"Your balance is {self.player.get_balance()}.")
            return True
        return False
        
    def lose(self, result):
        if len(set(result)) == 3 and all(symbol in self.symbols for symbol in result):  # this checks if all symbols are different
            print("You lose! Sorry...")
            print(f"Your balance is {self.player.get_balance()}.") # you win no omey
            return True
        return False
        
    def unfortunate(self, result):
        if result == ["?", "?", "?"]: # this checks if all symbols are "?" symbols
            print("You got the unfortunate combo...")
            self.player.remove_balance(130) # you lose unfortunate amount of money
            print(f"Your balance is unfortunately {self.player.get_balance()}.")
            return True
        
    # Ties everything together
    def play(self):
        self.rules()
        if not self.set_bet():
            return
        self.gameSoundFX()
        result = random.choices(self.symbols, k=3)
        print(f"Result: {result}")
        if self.jackpot(result):
            return
        if self.miniPot(result):
            return
        if self.unfortunate(result):
            return
        self.lose(result)
        
        
#TEST 
player = Player(1000)  # Example player with a balance of 1000
slot_machine = slotMachine(player)

# Play the game
slot_machine.play()