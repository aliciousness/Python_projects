import random
from hangman_art import *
from hangman_wordlist import word_list

chosen_word = random.choice(word_list)

for _ in range(len(chosen_word)):
        display.append("_")

def guess_letter():
    global lives
    if guess in a:
        print(f"sorry you already guessed {guess}, please try again")
    else:
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
                a.append(guess) 
                
        if guess not in chosen_word:
            lives -= 1
            print("Sorry that letter is not in the choosen word")
            a.append(guess)

print(logo)
while True:
    guess = input("Please guess a letter: ").lower()          
    guess_letter()
    print(display)
    print(STAGES[lives])
    if "_" not in display:
        print("YOU WIN!")
        break
    elif lives == 0:
        print("YOU LOSE!")
        print(f"Your word is {chosen_word}")
        break
    
    