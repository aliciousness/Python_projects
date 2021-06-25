###################################################################################################
from IPython.display import clear_output
#Basic code

row1 = [' ',' ',' ']

row2 = [' ',' ',' ']

row3 = [' ',' ',' ']

player1 = input('Please player 1 please pick either X or O: ')

player2 = input('Please player 2 please pick either X or O: ')




######################################################################################################
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
idk = user_choice()

# if choice.isdigit():
    
#     for num in numbers:
    
   
#         if num == 1 or num == 2 or num == 3:
#            row1[first_move-1] = 'X'
#            numbers.remove(first_move)
#            break
#         if num == 4 or num == 5 or num == 6:
#             row2[first_move-1] = 'X'
#             numbers.remove(first_move)
#             break
#         if num == 7 or num == 8 or num == 9:
#             row3[first_move-1] = 'X'
#             numbers.remove(first_move)
#             break
# else:
#          print('number not allowed, need to fix this BUG')
    

