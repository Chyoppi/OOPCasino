from random import randint
import questionary
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
                print(f"Your current balance is {self.player.get_balance()}.")
                bet = int(questionary.text("Place your bet:").ask())
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
            self.player_choice = questionary.select("Higher (4,5,6) or Lower (1,2,3)? (H/L)",
            choices=[
                "Higher",
                "Lower",
            ]).ask()
            if self.player_choice in ["Higher", "Lower"]:
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
        
        game_choice = self.play_again()
        if game_choice == "BackToMainMenu":
            return "BackToMainMenu"

