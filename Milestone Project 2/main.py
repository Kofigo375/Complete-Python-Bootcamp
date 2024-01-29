import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

## converting ranks from str type to int by mapping them in a dict
values = {
    'Two': 2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,
    'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14
}

class Card:
    # a card should have a suit and a rank(and a corresponding int value)
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        # will be displayed when an instance of this class is printed
        return f"{self.rank} of {self.suit}"
    
class Deck:

    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                ## create the card object
                created_card = Card(suit, rank)

                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def del_one(self):
        return self.all_cards.pop()



class Player:

    def __init__(self,name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f"Player {self.name} had {len(self.all_cards)} cards"


## GAME SETUP
player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.del_one())
    player_two.add_cards(new_deck.del_one())

print(player_two.all_cards[0])


game_on = True

## while game_on
round_num = 0 
while game_on:

    round_num += 1
    print(f"Round {round_num}")

    if len(player_one.all_cards) == 0:
        print("Player One, out of cards! Player Two Wins!")
        game_on = False
        break
    if len(player_two.all_cards) == 0:
        print("Player Two, out of cards! Player One Wins!")
        game_on = False
        break

    ## START A NEW ROUND
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())





    # while at_war

        