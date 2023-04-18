#War Game
import random

#52 cards in a deck
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,
          'King':13,'Ace':14}

suits = ('Hearts','Diamonds','Clubs','Spades')

ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)


    def shuffle(self):
        random.shuffle(self.all_cards)

        #in this piece of code we are assuming index -1 (or the last element) is the first in the deck instead of
        #what I thought which was have 0 as the top instead
    def deal_one(self):
        return self.all_cards.pop()


class Player:
    def __init__(self,name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)


    def __str__(self):
        return self.name + 'has ' + str(len(self.all_cards)) + ' number of cards.'

#Game Logic
deck1 = Deck()

player1 = Player('Tom')
player2 = Player('Jim')

deck1.shuffle()
deck1 = Deck()

for x in range(26):
    player1.add_cards(deck1.deal_one())
    player2.add_cards(deck1.deal_one())

game_on = True
round_num = 0

while game_on == True:
    round_num += 1
    print('Round: ' +  str(round_num))

    #Checks to see if the player is out of cards
    if len(player1.all_cards) == 0:
        print('Player One out of cards! Game Over')
        print('Player Two Wins!')
        game_on = False
        break


    if len(player2.all_cards) == 0:
        print('Player Two out of cards! Game Over')
        print('Player One Wins!')
        game_on = False
        break

    #Game keeps going after above are false
    player1_tablecards = []
    player1_tablecards.append(player1.remove_one())

    player2_tablecards = []
    player2_tablecards.append(player2.remove_one())

    at_war = True

    while at_war == True:
            if player1_tablecards[-1].value > player2_tablecards[-1].value:
                player1.add_cards(player1_tablecards)
                player1.add_cards(player2_tablecards)

            elif player1_tablecards[-1].value < player2_tablecards[-1].value:
                player2.add_cards(player1_tablecards)
                player2.add_cards(player2_tablecards)
            else:
                print('War!')








