from select import select
from deck import Deck
from player import Player

class Game:

    def __init__(self):
        self.player_one = Player("One")
        self.player_two = Player("Two")

        new_deck = Deck()
        new_deck.shuffle()

        for x in range(26):
            self.player_one.add_cards(new_deck.deal_one())
            self.player_two.add_cards(new_deck.deal_one())

def function():
    game = Game()
    print(game.player_one)
    print(game.player_two)

    print(game.player_one.all_cards[0])
    print(game.player_two.all_cards[0])

if __name__ == "__main__":
    function()    