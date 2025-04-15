class Player:
    def __init__(self, name):
        self.name = name
        self.balance = 1000
        self.hand = []
        self.bet = 0

    def __str__(self):
        return f"{self.name} has a balance of {self.balance} €."

    def add_balance(self, amount: int):
        if amount <= 0:
            print("Cannot add a negative balance.")
            return False
        
        self.balance += amount

    def remove_balance(self, amount: int):
        if amount > self.balance:
            print("Cannot remove more than the current balance.")
            return False
        
        if amount == 0:
            print("Cannot remove a zero balance.")
            return False
        
        self.balance -= amount

    def add_card(self, card: str):
        if not card:
            print("Card cannot be empty.")
            return False
        
        self.hand.append(card)

    def clear_hand(self):
        self.hand = []

    def show_hand(self):
        return self.hand

    def set_bet(self, bet: int):
        if not bet:
            print("Bet cannot be empty or zero")
            return False
        
        self.bet = bet

    def get_bet(self):
        return self.bet

    def get_balance(self):
        return self.balance

    def get_name(self):
        return self.name
    
class VIP_Player(Player):
    __inti__ = Player.__init__
    def __init__(self, name):
        super().__init__(name)
        self.balance = 15000

    def __str__(self):
        return f"{self.name} has a balance of {self.balance} €."

    def add_balance(self, amount: int):
        if amount <= 0:
            print("Cannot add a negative balance.")
            return False
        
        self.balance += amount

    def remove_balance(self, amount: int):
        if amount > self.balance:
            print("Cannot remove more than the current balance.")
            return False
        
        if amount == 0:
            print("Cannot remove a zero balance.")
            return False
        
        self.balance -= amount

    def add_card(self, card: str):
        if not card:
            print("Card cannot be empty.")
            return False
        
        self.hand.append(card)

    def clear_hand(self):
        self.hand = []

    def show_hand(self):
        return self.hand

    def set_bet(self, bet: int):
        if not bet:
            print("Bet cannot be empty or zero")
            return False
        
        self.bet = bet

    def get_bet(self):
        return self.bet

    def get_balance(self):
        return self.balance

    def get_name(self):
        return self.name