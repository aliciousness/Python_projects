'''
Black Jack game
'''
import random

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
    'Jack':10,
    'Queen':10,
    'King':10,
    'Ace':11
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
        # Note we remove one card from the list of all_cards
        return self.all_cards.pop()     
    
    
class Player():
    def __init__(self,name,bank=0):
        self.bank = bank
        self.name = name
        self.hand = []
    
    def hit(self,add):
        #dealing one card and removing it from the all cards list
        self.hand.append(add)
        
        
    
    def clear(self):
        return self.hand.clear()
    
   
    
    def stay(self):
        for x in self.all_cards:
           x+=x
        return x



new_deck = Deck()
new_deck.shuffle()
p1 = Player('Richard')
d = new_deck.deal_one()
p1.hit(d.value)
p1.hit(d.value)
p1.hit(d.value)
#stuck here keeps repeating the same card when dealt 

#p1.clear()
#print()
print(p1.hand)