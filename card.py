import random

values = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Eleven': 11, 'Twelve': 12, 'Thirtheen': 13}

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirtheen')

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit    

def function():
    two_hearts = Card("Hearts", "Two")
    three_clubs = Card("Clubs", "Three")
    print(two_hearts.value < three_clubs.value)

if __name__ == "__main__":
    function()