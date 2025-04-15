import random
from os import system
from Player import Player
import questionary

class BlackJack:
    def __init__(self, player: Player):
        self.cards = {
            '2': 2, '3': 3, 
            '4': 4, '5': 5, 
            '6': 6, '7': 7, 
            '8': 8, '9': 9, 
            '10': 10, 
            'J': 10, 'Q': 10, 
            'K': 10, 'A': 11}
        
        self.player = player
        self.dealer_hand = []

    def deal_card(self):
        card = random.choice(list(self.cards.keys()))
        return card

    def calculate_hand(self, hand):
        total = 0
        ace_count = hand.count('A')
        for card in hand:
            total += self.cards[card]
        while total > 21 and ace_count:
            total -= 10
            ace_count -= 1
        return total

    def place_bet(self):

        while True:
            try:
                player_bet_input = int(questionary.text("Place your bet:").ask())

                if player_bet_input <= 0:
                    print("Bet ~r~MUST~reset~ be geater than ~r~0!~reset~")

                elif player_bet_input > self.player.get_balance():
                    print("~r~You don't have enough balance!")
                else:
                    return player_bet_input
            except ValueError:
                print("~r~Invalid input!~reset~ Please enter ~g~a valid (NUMBER)~reset~ bet.\033")

    def choose_hit_or_stand(self):
        while self.calculate_hand(self.player.show_hand()) < 21:
            player_action = questionary.select("Do you want to hit or stand?",
            choices=[
                "Hit",
                "Stand",
            ]).ask()

            if player_action == "Hit":
                self.player.add_card(self.deal_card())
                print(f"{self.player.name}'s new hand: ~y~{self.player.show_hand()}~reset~ Total: {self.calculate_hand(self.player.show_hand())}")
            elif player_action == "Stand":
                return
            
    def print_blackjack_guide(self):
        guide_text = """
        ~b~How to Play Blackjack:~reset~

        ~c~1.~reset~ Place your bet.
        ~c~2.~reset~ Hit to draw a card or Stand to keep your hand.
        ~c~3.~reset~ The goal is to get as close to ~b~21~reset~ as possible without going over.
        ~c~4.~reset~ The dealer plays after you. If they go over ~b~21~reset~, you win.
        ~c~5.~reset~ Compare hands: The closest to ~b~21~reset~ wins.

        ~g~Enjoy and good luck!~reset~
        """

        print(guide_text)


    def play_game(self):
        system("cls")
        print("~g~Welcome to Blackjack!")
        self.print_blackjack_guide()
        print(f"Your balance: ~g~{self.player.get_balance()}")

        if self.player.get_balance() <= 0:
            print(f"~r~Not enough balance!")
            #return "BackToMainMenu"
            game_choice = play_again(self)

            if game_choice == "BackToMainMenu":
                return "BackToMainMenu"

        self.player.clear_hand()
        self.dealer_hand.clear()

        player_bet = self.place_bet()
        self.player.set_bet(player_bet)
        self.player.remove_balance(player_bet)

        # Deal cards to player and dealer
        self.player.add_card(self.deal_card())
        self.player.add_card(self.deal_card())
        self.dealer_hand.append(self.deal_card())
        self.dealer_hand.append(self.deal_card())

        # Player status
        print(f"\n{self.player.name}'s hand: ~y~{self.player.show_hand()}~reset~ Total: {self.calculate_hand(self.player.show_hand())}")
        print(f"Dealer's first card: ~y~{self.dealer_hand[0]}\n")

        # Player can choose "hit" or "stand"
        self.choose_hit_or_stand()

        # If player goes over 21, the game ends
        if self.calculate_hand(self.player.show_hand()) > 21:
            print(f"{self.player.name}'s went over 21! ~r~You lost!")
            game_choice = play_again(self)

            if game_choice == "BackToMainMenu":
                return "BackToMainMenu"
            
            return game_choice
        
        # Dealer plays its turn
        print(f"\nDealer's hand: ~y~{self.dealer_hand}~reset~ Total: {self.calculate_hand(self.dealer_hand)}")
        while self.calculate_hand(self.dealer_hand) < 17:
            print("Dealer hits...")
            self.dealer_hand.append(self.deal_card())
            print(f"Dealer's new hand: ~y~{self.dealer_hand}~reset~ Total: {self.calculate_hand(self.dealer_hand)}")

        # Game ends
        player_total = self.calculate_hand(self.player.show_hand())
        dealer_total = self.calculate_hand(self.dealer_hand)

        if dealer_total > 21:
            print("~g~Dealer went over 21! Player wins!~reset~\n")
            self.player.add_balance(self.player.get_bet() * 2)
        elif player_total > dealer_total:
            print(f"~g~{self.player.name} wins!~reset~\n")
            self.player.add_balance(self.player.get_bet() * 2)
        elif player_total < dealer_total:
            print("~r~Dealer wins!~reset~\n")
        else:
            print("~y~It's a tie!~reset~\n")

        # Play again?
        game_choice = play_again(self)

        if game_choice == "BackToMainMenu":
            return "BackToMainMenu"

        return game_choice


def play_again(self):
    play_again = questionary.select("Do you want to play again?",
    choices=[
        "Yes",
        "No",
        "Return to Game Selection",
    ]).ask()
    
    if play_again == "Yes":
        self.play_game()
        system("cls")
    elif play_again == "No":
        print("Thank you for playing!")
        return exit()
    elif play_again == "Return to Game Selection":
        system("cls")
        return "BackToMainMenu"
