import random
import hangman_words

import hangman_art


# words_list = ["aardvark","camel","baboon"]

word = random.choice(hangman_words.words_list)
# print(word)

size =len(word)
live = 6
placeholder =""

for letter in range(size):
    placeholder += "_ "

print(placeholder)

game_over = False

correct_letter =[]


while not game_over:

    display =""
    print(live,"lives left")


    guess = input("guess the letter for the given word :-").lower()
    print("Guess letter is :-",guess)

    if guess in correct_letter:
        print("Already guessed by you ")
        continue
    
    for letter in word:
        if(letter == guess):
            display += guess
            correct_letter.append(letter)
        elif letter in correct_letter:
            display += letter
        else:
            display +=" _ "
    
    print(display)

    if guess not in word:
        print(f"you guessed the letter $ {guess} $ not in word")
        live -=1
        
        if live == 0:
            game_over = True
            print("\n*******************You Lose****************")

        
    
    
    print(hangman_art.stages[live])

    if "_" not in display:
        game_over == True
        print("******************You Win***********************")
        exit()
    

    
