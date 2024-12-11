suits = ('clubs', 'hearts', 'diamonds', 'spades')
ranks = ('ace', 'king', 'queen', 'jack', '10', '9', '8', '7', '6', '5', '4', '3', '2')
def main():

    deck = get_full_deck(suits, ranks)
    print(deck)
    
    
def get_full_deck(suits, ranks):
    deck = ()
    for suit in suits:
        for rank in ranks:
            #current_rank = (rank,)
            #current_suit = (suit,)
            current_card = (rank, suit)
            deck = deck + (current_card,)
    return deck


def shuffle():
    pass

def take_bet():
    pass

def deal_cards():
    pass







if __name__=='__main__':
    main()