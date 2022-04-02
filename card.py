from constant import Constant

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = Constant.VALUES[rank]

    def __str__(self):
        return self.rank + " of " + self.suit    

def function():
    two_hearts = Card("Hearts", "Two")
    three_clubs = Card("Clubs", "Three")
    print(two_hearts.value < three_clubs.value)

if __name__ == "__main__":
    function()