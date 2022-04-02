import random
from card import Card
from constant import Constant

class Deck:

    def __init__(self):
        self.all_cards = []

        for suit in Constant.SUITS:
            for rank in Constant.RANKS:
                created_card = Card(suit, rank)

                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

def function():
    new_deck = Deck()
    new_deck.shuffle()
    print(new_deck.all_cards[0])

if __name__ == "__main__":
    function()                