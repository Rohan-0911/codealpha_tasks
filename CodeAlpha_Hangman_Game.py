import random

words = ["dance", "drink", "house", "mango", "table"]
rules = ["1. You need to guess a five letter word","2. You need to guess a single letter at a time","3. You have 6 lives","4. You will lose 1 live for 1 incorrect guess","5. You can use hints, but it will cost 2 lives for 1 hint","6. ALL THE BEST\n"]
valid_input = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

random_num = random.randrange(0,5)
random_word = words[random_num]

attempts = []
wrong_attempts = [] 

display = ["_","_","_","_","_"]

def start():

    tot_lives = 6

    print("Let's start the game,")
    
    print("Guess the following Word:",end=" ")
    for i in display:
               print(i, end=" ")

    while tot_lives>0:
        
        letter = input("\nGuess a letter: \n")
        letter = letter.lower()

        if letter not in valid_input:
            print("Please enter a valid letter")

        elif letter in attempts:
             print("You have already gussed this letter, Try another one.")

        elif letter in wrong_attempts:
            print(f"You have already tried for letter '{letter}', try again for another letter")

        elif letter in random_word:
            print(f"\nCongratulations you guessed it right, Keep going!\n{letter} is present in the word")
            index = random_word.find(letter)

            display[index] = letter.upper()
                
            for i in display:
                print(i, end=" ")

            attempts.append(letter)
            print(f"\nLives reamining {tot_lives}\n")
    
        else:
            print(f"You missed it, Try again. {letter} is not present in the word")
            tot_lives -= 1
            print(f"Lives reamining {tot_lives}\n")

            wrong_attempts.append(letter)

        if len(attempts) == 5:
            print(f"Congratulations you guessed the word. {random_word.upper()} is the word")
            break            

    if tot_lives == 0:
            print(f"You lose, {random_word.upper()} was the word")

print("\nLets Start The Hagman Game :) \n")
dummy = input("  Press enter To Continue  ".center(50,"*"))

option = input('\n| Press "1" to start the Game with Instructions & Rules | or | Press "2" to start the Game | \n')

if option == "1":
    for i in rules:
        print(" \n",i)
    start()

else:
    start()