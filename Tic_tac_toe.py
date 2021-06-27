###################################################################################################

#Basic code

row1 = [' ',' ',' ']

row2 = [' ',' ',' ']

row3 = [' ',' ',' ']



################################################################################

def player_check():
    #check player has no doubles
    player1 = input('Please player 1 pick either X or O: ')
    player2 = False
    
    while player2 == False:
        if player1.upper() == 'X':
            player2 = 'O'
        elif player1.upper() == 'O':
            player2 = 'X'
        else:
            print("Sorry that is neither 'X' or 'O' please try again!")
            break
    return [player1,player2]

players = player_check()

print(players) 
    
def display(r1,r2,r3):
    print(row1)
    print(row2)
    print(row3)
    if r1 == r2 and r1 == r3:
        print("Lets play Tic Tac Toe!")
    else:
        pass

dipslay_board = display(row1,row2,row3)

def user_choice():
    #variables
    
    #inti
    choice = "wrong"
    acceptable_range = range(0,10)
    within_range = False
    
    #Two conditions to check
    #digit or within_range == False
    while choice.isdigit() == False or within_range == False:
        choice = input('From left to right and from top to bottom please enter a number from 0-9 : ')
        
        
        if choice.isdigit() == False:
            #digit check
            print('Sorry that is not a number')
            
            #range check
        if choice.isdigit() == True:
            
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print('sorry that is not within 0-9')
                within_range = False
    return int(choice)

first_choice = user_choice()



    

