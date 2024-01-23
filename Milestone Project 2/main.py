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


new_deck = Deck()
print(new_deck.all_cards)
first_card = new_deck.all_cards[0]
last_card = new_deck.all_cards[-1]
print(first_card)
print(last_card)

for card_object in new_deck.all_cards:
    print(card_object)

new_deck.shuffle()
last_card = new_deck.all_cards[-1]
print(last_card)

my_card = new_deck.del_one()
print(my_card)
print(len(new_deck.all_cards))