class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.name = f"{self.rank} of {self.suit}"


    def get_card_name(self, deck):
        pass