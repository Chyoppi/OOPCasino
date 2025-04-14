from random import randint
import Player

class DiceGame:
    def __init__(self, player: Player):
        self.player = player
        self.dice = 0

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

    def decide_side(self):
        while True:
            self.player_choice = input("Higher (4,5,6) or Lower (1,2,3)? (H/L): ").upper()
            if self.player_choice in ["H", "L"]:
                break
            else:
                print("Invalid choice. Please enter 'H' for Higher or 'L' for Lower.")

    def roll_dice(self):
        self.dice = randint(1, 6)
        return self.dice
    
    def who_won(self):
        if self.dice in [4, 5, 6] and self.player_choice == "H":
            # Player wins
            self.player.add_balance(self.player.get_bet() * 2)
            return True
        elif self.dice in [1, 2, 3] and self.player_choice == "L":
            self.player.add_balance(self.player.get_bet() * 2)
            return True
        else:
            # Player loses
            return False
        
    def play_game(self):
        self.set_bet()
        self.decide_side()
        self.roll_dice()
        print(f"The dice rolled: {self.dice}")
        if self.who_won():
            print("You won!")
        else:
            print("You lost!")
        print(f"Your new balance is {self.player.get_balance()}.")

