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
    'Ace':1
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
                self.all_cards.append(Card(suit,rank))
    
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n'+ card.__str__()
        return 'The deck has: '+ deck_comp
                   
                
        
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
        n=0
        for x in self.hand:
           n+=x
        print(n)
        return n
        
        
    
    def clear(self):
        return self.hand.clear()
    
   
    
    def stay(self):
        n=0
        for x in self.hand:
           n+=x
        print(n)
        return n
        


'''
new_deck = Deck()
new_deck.shuffle()
p1 = Player('Richard')
d = new_deck.deal_one()
a = new_deck.deal_one()
p1.hit(d.value)
p1.hit(a.value)
# print(len(new_deck.all_cards))
print(p1.hand)
#stuck here keeps repeating the same card when dealt 
p1.stay()
#p1.clear()
#print()
print(p1.hand)
'''




'''
l = 0
to = [1,2,3]

for t in to:
    l+=t
    
print(l)
'''
new_deck = Deck()
new_deck.shuffle()

p1 = Player('Richard')
p2 = Player('Computer')

game_round = 0
game_on = True

# for x in new_deck.all_cards:
#     print(x.value)            #checking cards and the value contributed to it

while game_on:
    comp_turn = True
    player_turn = True
    cal_player = True
    cal_sum = True
    g=0 
    comp_hand = 0
    
    while player_turn:
        d = new_deck.deal_one() 
        cur_hand = 0
        choice1 = input(f'You have a new card would you like to hit or stay? ')
        if choice1 == 'hit':
            p1.hit(d.value)
            continue
        elif choice1 =='stay':
            p1.stay()
            player_turn = False
            break
        else:
            print('Sorry that is not one of the options, please try again')
            print(p1.hand)
    
    while cal_sum:
            
        for x in p1.hand:
            g+=x
        print(g)
        
        if g > 21:
            print('Bust Sorry you have lost his round')
            game_round += 1
            cal_sum = False
            comp_turn = False
            p1.clear()
            break
        elif g <= 21:
            cur_hand = g
            game_round += 1
            print(f'Your total is {g}')
            p1.clear()
            cal_sum = False
            
            break
    
    while comp_turn:
        
        if comp_hand == 0:
            comp_hand += p2.hit(d.value)
            
        if comp_hand < 21 and comp_hand < g:
            comp_hand += p2.hit(d.value)
            print(p2.hit(d.value),'hti')
            
        elif comp_hand > g and comp_hand <= 21:
            p2.stay()
            print(f'the house got {comp_hand}, and the house has won')
            p2.clear()
            
            break
        elif comp_hand > 21:
            print(f'You have beaten the house, the house total {comp_hand}')
            p2.clear()
            
            break
        
            
    print(f'game round: {game_round}')
    print(f'There are {len(new_deck.all_cards)} cards left')
    if len(new_deck.all_cards) == 0:
        print('Game is over we are out of cards')
        game_on = False
        break       
           
        
        
        
        
        
    # game_on = False
    # break
        
