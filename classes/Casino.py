#Games which are commented have not been implemented yet

from games.DiceGame import DiceGame
from games.Blackjack import BlackJack
from games.Slot import slotMachine
from Player import Player

import questionary # pip install questionary
import os

games_list = {
    1: ("Dice Game", DiceGame),
    2: ("Slot Machine", slotMachine),
    3: ("Blackjack", BlackJack)
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


class GameControls:

    def __init__(self, player: Player):
        self.player = player

    def show_game_menu(self):
        print("Welcome to the CMR Casino!")
        
        games_list_choices = [v[0] for v in games_list.values()]
        
        choice_menu = questionary.select(
            "Choose a game to play:", 
            choices=games_list_choices, 
            use_indicator=True
        ).ask()

        game_user_choice = None

        for v in games_list.values():
            if v[0] == choice_menu:
                game_user_choice = v
                break

        if game_user_choice:
            print(f"You have chosen {game_user_choice[0]}")
            self.run_game(game_user_choice[1])

    def run_game(self, game_class):

        if game_class is None:
            print("This game is not ready yet :(")
            self.show_game_menu()

        game_instance = game_class(self.player)
        game_status = game_instance.play_game()

        if game_status == "BackToMainMenu":
            self.show_game_menu()

    # Maybe use this when the game is done
    def return_to_menu(self, clear: bool):
        if clear:
            os.system("cls")

        self.show_game_menu()


## MAIN
if __name__ == "__main__":
    player = Player("Test")
    casino = Casino(player)