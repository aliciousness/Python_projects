'''
war game, if you dont know the rules or how to play war, here is a link on the game https://en.wikipedia.org/wiki/War_(card_game)

'''
#card class
    #understand Suit and Rank and easy correspondant to int value  
    
#Deck class

#Player

#logic
from hashlib import new
from math import atan
import random
import pdb

values = {
    'One':1,
    'Two': 2,
    'Three':3,
    'Four':4,
    'Five':5,
    'Six':6,
    'Seven':7,
    'Eight':8,
    'Nine':9,
    'Ten':10,
    'Jack':11,
    'Queen':12,
    'King':13,
    'Ace':14
    }

suits = ('Hearts','Diamonds','Spades','Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __str__(self):
        '''
        when print class will show 'whatever rank' of 'whatever suit' ie. Two of Hearts
        '''
        return self.rank + ' of ' + self.suit
    
class Deck:
    
    def __init__(self):
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                #create the card object, to create each card and place it in the all cards att
                create_card = Card(suit,rank)
                self.all_cards.append(create_card)
                   
                
        
    def shuffle(self):
        #shuffles the deck when called. 
        random.shuffle(self.all_cards)  
    
    def deal_one(self):
        #dealing one card and removing it from the all cards list
        return self.all_cards.pop()

class Player:
    
    def __init__(self,name):
        self.name = name
        self.all_cards = []
    
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            #list of multiple Card objects
            self.all_cards.extend(new_cards)
        else:
            #single Card object
            self.all_cards.append(new_cards)
    
    def __str__(self):
        return f'{self.name} has {len(self.all_cards)} card(s)'




'''
Game Setup
'''

player_one = Player(input('Player one please enter your name '))
player_two = Player(input('Player two please enter your name '))


new_deck = Deck()
new_deck.shuffle()

#split deck
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())
    
game_on = True
    
# while game_on
round_num = 0

while game_on:
    round_num += 1
    print(f'Round {round_num}')
    
    #check if players have card
    if len(player_one.all_cards) == 0:
        print(f'{player_one} out of cards {player_two} wins! ')
        game_on = False
        break
    
    if len(player_two.all_cards) == 0:
        print(f'{player_two} out of cards {player_one} wins! ')
        game_on = False
        break
    
    #game still on, Start new round
    player_one_cards = []       #the card in play
    player_one_cards.append(player_one.remove_one())
    
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())
    
    

    #while at_war
    at_war = True

    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
           player_one.add_cards(player_one_cards)
           player_one.add_cards(player_two_cards)
           at_war = False
           break
        elif player_one_cards[-1].value < player_two_cards[-1].value:
           player_two.add_cards(player_one_cards)
           player_two.add_cards(player_two_cards)
           at_war = False
           break
        else:
            print('WAR!')
            if len(player_one.all_cards) < 5:
              print(f'{player_one} unable to declare war')
              print(f'{player_two} wins')
              game_on = False
              break
            elif len(player_one.all_cards) < 5:
              print(f'{player_two} unable to declare war')
              print(f'{player_one} wins')
              game_on = False
              break 
            else:
                for num in range(3):
                    player_one_cards.append(player_one.remove_one())
                    player_one_cards.append(player_one.remove_one())
    


