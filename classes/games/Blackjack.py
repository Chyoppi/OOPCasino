import random
import Player

class BlackJack:
    def __init__(self, player: Player):
        self.player = player
        self.player_deck = self.create_deck()
        self.player_hand = []
        self.dealer_hand = []

    def play_game(self):
        print("Blackjack game is still under development!")
        return "BackToMainMenu"


    def create_deck(self):
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

        deck = []
        for value in values:
            for suit in suits:
                deck.append(f'{value} of {suit}')
     
        random.shuffle(deck)
        return deck
    
    def deal_card(self):
        print("Deal card")

    def who_won(self, player):
        print("Winner")
    

class Dealer(BlackJack):
    def __init(self):
        super().__init__()

    def dealer_turn(self):
        print("Dealer's Turn!")

    def dealer_show_hand(self):
        print("Show Dealer's hand!")