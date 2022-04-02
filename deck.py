from card import Card
from constant import Constant

class Deck:

    def __init__(self):
        self.all_cards = []

        for suit in Constant.SUITS:
            for rank in Constant.RANKS:
                created_card = Card(suit, rank)

                self.all_cards.append(created_card)

def function():
    new_deck = Deck()
    print(new_deck.all_cards)

if __name__ == "__main__":
    function()                