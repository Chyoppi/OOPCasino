
import random 
import time
import questionary
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
        rules = """
        Welcome to the slot machine game!
        These are the rules:

        If you get the 3 same symbols you win the jackpot
        If you get 2 same symbols you win 10% more than your bet
        If you get 3 different symbols you lose your bet
        Beware of the unfortunate symbol '?'...

        Good luck!
        """
        print(rules)

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
            self.player.add_balance(self.player.get_bet() * 15) # If you win you get a lot of money
            print(f"Your balance is {self.player.get_balance()}.")
            return True
        return False
        
    def miniPot(self, result):
        
        minipot_symbols = ["!", "£", "€", "$"]
        
        if len(set(result)) == 2 and all(symbol in minipot_symbols for symbol in result):  # Check if there are 2 same symbols and 1 different symbol
            print("Cool! You won the mini POT!")
            self.player.add_balance(self.player.get_bet() + 150)
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
        
    def play_again(self):
        play_again = questionary.select("Do you want to play again?",
            choices=[
                "Yes",
                "No",
                "Return to Game Selection",
            ]).ask()
        
        if play_again == "Yes" and self.player.get_balance() > 0:
            return self.play_game()
        elif play_again == "No":
            print("Thanks for playing!")
            return False
        elif play_again == "Return to Game Selection":
            print("Returning to game selection")
            return "BackToMainMenu"
        else:
            print("You don't have enough balance to play again.")
            return False
        
    # Ties everything together
    def play_game(self):
        self.rules()
        if not self.set_bet():
            return
        self.gameSoundFX()
        time.sleep(1) # Waits for 1 second before showing results
        result = random.choices(self.symbols, k=3)
        print(f"Result: {result}")
        if self.jackpot(result):
            return
        if self.miniPot(result):
            return
        if self.unfortunate(result):
            return
        self.lose(result)

        game_choice = self.play_again()
        if game_choice == "BackToMainMenu":
            return "BackToMainMenu"
        