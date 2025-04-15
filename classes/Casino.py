#Games which are commented have not been implemented yet
from utils.colors import CPrint
from games.DiceGame import DiceGame
from games.Blackjack import BlackJack
from games.Slot import slotMachine
from Player import Player, VIP_Player

import questionary # pip install questionary

games_list = {
    1: ("Dice Game", DiceGame),
    2: ("Slot Machine", slotMachine),
    3: ("Blackjack", BlackJack),
    4: ("Reset Balance", "reset_balance"),
    5: ("Exit", None)
}

class Casino:
    def __init__(self, player: Player):
        self.player = player
        self.balance = player.balance
        self.game_controls = GameControls(self)
        self.start_casino()

    def __str__(self):
        return f"Welcome to the casino, you have {self.balance} points in your balance."

    def start_casino(self):
        self.game_controls.show_game_menu()

    def reset_balance(self):
        if self.player.get_balance() == 0:
            print("~y~You don't have enough money? Let's reset your balance.")
            self.player.add_balance(1000)
        else:
            print("~y~You still have money...")

        self.start_casino()


class GameControls:

    def __init__(self, casino: Casino):
        self.player = casino.player
        self.casino = casino

    def show_game_menu(self):
        print("Welcome to the CMR Casino!\n")
        
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

            if game_user_choice[0] == "Exit":
                exit()
            elif game_user_choice[0] == "Reset Balance":
                self.casino.reset_balance()
                self.show_game_menu()
            
            self.run_game(game_user_choice[1])

    def run_game(self, game_class):

        if game_class is None:
            self.show_game_menu()

        game_instance = game_class(self.player)
        game_status = game_instance.play_game()

        if game_status == "BackToMainMenu":
            self.show_game_menu()


## MAIN

if __name__ == "__main__":
    player = Player("Test")
    casino = Casino(player)

#Added VIP_Player class, using inheritance from Player
"""
if __name__ == "__main__":
    vip_player = VIP_Player("VIPTest")
    casino = Casino(vip_player)

"""


"""
## TEST FUNCTIONS
test_player = Player("Test Player")
#test_casino = Casino(test_player)

# Add Balance
test_player.add_balance(500)
test_player.add_balance(0) # Cannot add a negative balance

# Remove Balance
test_player.remove_balance(500)
test_player.remove_balance(0) # Cannot remove a zero balance

# Set Bet
test_player.set_bet(100)
test_player.set_bet(0) # Bet cannot be empty or zero

# Add Card
test_player.add_card("Ace of Spades")
test_player.add_card() # missing 1 required positional argument: 'card'
"""