###################################################################################################

#Basic code

row1 = [' ',' ',' ']

row2 = [' ',' ',' ']

row3 = [' ',' ',' ']



################################################################################

def player_check():
    #check player has no doubles
    player1 = 'wrong'
    player2 = False
    
    while player2 == False:
        player1 = input('Please pick either X or O: ')
    
        if player1.upper() == 'X':
            player1 = 'X'
            player2 = 'O'
        elif player1.upper() == 'O':
            player1 = 'O'
            player2 = 'X'
        elif player1.upper not in ['X','O']:
            print("Sorry that is neither 'X' or 'O' please try again!")
            
    return [player1,player2]

players = player_check

 
    
def display(r1,r2,r3):
    print(row1)
    print(row2)
    print(row3)
    if r1 == r2 and r1 == r3:
        print("Lets play Tic Tac Toe!")
    else:
        pass

display(row1,row2,row3)

def user_choice():
    #variables
    
    #inti
    choice = "wrong"
    acceptable_range = range(0,4)
    acceptable_row = [1,2,3]
    within_range_choice = False
    within_range_row = False
    #Two conditions to check
    #digit or within_range == False
    while choice.isdigit() == False or row.isdigit() == False and within_range_choice == False and within_range_row == False:
        row = input('please pick row by entering 1 2 or 3: ')
        choice = input('please enter a number from 1-3: ')
        
        if choice.isdigit() == False and row.isdigit() == False:
            #digit check
            print('Sorry that is not a number')
            
            #range check
        if row.isdigit()==True:
            if int(row) in acceptable_row:
                within_range_row=True
            else:
                print('sorry that is not with row range 1-3')
                within_range_row = False
                
        if choice.isdigit() == True:       
            if int(choice) in acceptable_range:
                within_range_choice = True
                
            else:
                print('sorry that is not within 1-3')
                within_range_choice = False
    moves_choice = [int(choice),int(row)]
    
    return moves_choice

first_choice = user_choice


def move(choice,play):
    #moves on the board
    move_choice = choice[0]
    row_choice = choice[1]
    
    player1 = play[0]
    player2 = play[1]
    
    #replace moves on the board
    if row_choice ==1:
        row1[move_choice-1] = player1
    elif row_choice == 2:
        row2[move_choice-1] = player1
    elif row_choice == 3:
        row3[move_choice-1] = player1 
    else:
        pass
    
    
    #display new board
    return row1,row2,row3

def game_on_choice():
    choice = 'wrong'
    
    while choice.upper() not in ['Y','N']:
        choice = input("Would you like to keep play? (Y or N)")
        if choice.upper() not in ['Y','N']:
            print('Sorry i do not understand please input Y or N')
    if choice.upper() == 'Y':
        return True
    else:
        return False
   
game_on = True
game_list = row1,row2,row3
while game_on:
    
    
    
    game_list = move(first_choice(),players())
    
    # user_choice()
    
    display(row1,row2,row3)
    
    game_on = game_on_choice()
    
    print('\n'*100)
    
    

    

    

