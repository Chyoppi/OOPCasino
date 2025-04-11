#Games which are commented have not been implemented yet

#from games.Blackjack import Blackjack
#from games.Slot import Slot
#from games.Roulette import Roulette
from games.DiceGame import DiceGame
from games.Blackjack import BlackJack
from Player import Player

games_list = {
    1: ("Dice Game", DiceGame),
    2: ("Slot Machine", None),
    3: ("Blackjack", BlackJack),
    4: ("Roulette", None)
}


class Casino:
    def __init__(self, player: Player):
        self.player = player
        self.balance = player.balance
        self.game_controls = GameControls(self.player)
        self.start_casino()

    def __str__(self):
        return f"Welcome to the casino, you have {self.balance} points in your balance."

    def start_casino(self):
        self.game_controls.show_game_menu()
        self.game_controls.choose_game()


# Maybe use a package to incorporate arrows and create a cooler UI?
class GameControls:

    def __init__(self, player: Player):
        self.player = player

    def show_game_menu(self):
        print("Welcome to the CMR Casino!")
        for k, v in games_list.items():
            print(f"{k}. {v[0]}")

    def choose_game(self):
        while True:
            try:
                choice = int(input("Please choose a game: "))

                if choice in games_list:
                    game_choice = games_list[choice]
                    print(f"You have chosen {game_choice[0]}")
                    self.run_game(game_choice[1])
                    break
                
                else:
                    print("Invalid selection. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 5.")

    def run_game(self, game_class):
        game_instance = game_class(self.player)
        game_instance.play_game()

## MAIN
if __name__ == "__main__":
    player = Player("Test")
    casino = Casino(player)