from re import S


class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        pass

    def add_cards(self, new_cards):
        pass

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'

def function():
    new_player = Player('Woz')
    print(new_player)

if __name__ == "__main__":
    function()          