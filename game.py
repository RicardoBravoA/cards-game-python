from select import select
from deck import Deck
from player import Player

class Game:

    def __init__(self):
        self.player_one = Player("One")
        self.player_two = Player("Two")
        self.game_on = True
        self.round_number = 0

        new_deck = Deck()
        new_deck.shuffle()

        for x in range(26):
            self.player_one.add_cards(new_deck.deal_one())
            self.player_two.add_cards(new_deck.deal_one())

    def play(self):
        while self.game_on:
            self.round_number += 1
            print(f'Round {self.round_number}')

            if len(self.player_one.all_cards) == 0:
                print(f'Player {self.player_two.name} wins!')
                self.game_on = False
                break

            if len(self.player_two.all_cards) == 0:
                print(f'Player {self.player_one.name} wins!')
                self.game_on = False
                break

            # Start a new round
            player_one_cards = []
            player_one_cards.append(self.player_one.remove_one())

            player_two_cards = []
            player_two_cards.append(self.player_two.remove_one())

            at_war = True
            
            while at_war:

                if player_one_cards[-1].value > player_two_cards[-1].value:
                    self.player_one.add_cards(player_one_cards)
                    self.player_one.add_cards(player_two_cards)

                    at_war = False

                elif player_one_cards[-1].value < player_two_cards[-1].value:
                    self.player_two.add_cards(player_two_cards)
                    self.player_two.add_cards(player_one_cards)

                    at_war = False
                else:
                    print('War')    

                    if len(self.player_one.all_cards) < 5:
                        print(f'Player {self.player_one.name} unable to declare war')
                        print(f'{self.player_two} wins!')
                        self.game_on = False
                        break

                    elif len(self.player_two.all_cards) < 5:
                        print(f'Player {self.player_two.name} unable to declare war')
                        print(f'{self.player_one} wins!')
                        self.game_on = False
                        break

                    else:
                        for num in range(5):
                            player_one_cards.append(self.player_one.remove_one())
                            player_two_cards.append(self.player_two.remove_one())
                




def function():
    game = Game()
    print(game.player_one)
    print(game.player_two)

    print(game.player_one.all_cards[0])
    print(game.player_two.all_cards[0])

    game.play()

if __name__ == "__main__":
    function()    