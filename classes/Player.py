class Player:
    def __init__(self, name):
        self.name = name
        self.balance = 1000
        self.hand = []
        self.bet = 0

    def __str__(self):
        return f"{self.name} has a balance of {self.balance} €."

    def add_balance(self, amount):
        self.balance += amount

    def remove_balance(self, amount):
        self.balance -= amount

    def add_card(self, card):
        self.hand.append(card)

    def clear_hand(self):
        self.hand = []

    def show_hand(self):
        return self.hand

    def set_bet(self, bet):
        self.bet = bet

    def get_bet(self):
        return self.bet

    def get_balance(self):
        return self.balance

    def get_name(self):
        return self.name