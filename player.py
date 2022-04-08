from card import Card
from deck import Deck

class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            # List of multiple card objects
            self.all_cards.extend(new_cards)
        else:
            # Single card object
            self.all_cards.append(new_cards)    

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'

def function():
    new_player = Player('Woz')
    print(new_player)

    new_deck = Deck()
    new_deck.shuffle()

    my_card = new_deck.deal_one()
    print(my_card)

    new_player.add_cards(my_card)
    print(new_player)

    new_player.remove_one()
    print(new_player)

if __name__ == "__main__":
    function()          