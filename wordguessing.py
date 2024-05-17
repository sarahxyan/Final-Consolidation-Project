# Consolidation project
# set the game to two person players
# create word bank as a list of words
# Pick a word from the list randomly 
# Loop through each letter in the chosen word
# Make the players take turns to enter a letter or word (make sure they only have three word guesses)
# Display the number of times the letter appears in the word
# Count the letter and word guesses for each player
# after the player guesses a letter, they have an option to guess the word
# track the score for each player (score is the number of turns they made before guessing correctly)
# when the right word is guessed, the loop stops and displays the scores of each player and says who wins

import random 

def pick_letter():
    letter = input("Please enter a letter : ")
    if len(letter) != 1:
        return pick_letter()
    return letter

player_count = 2

word_bank = ["River", "Ocean", "Beach", "Stone", "Earth"]
scores = [0,0]
word_guess_counts = [0,0]
secret_word = random.choice(word_bank).lower()
print("Theme of the word is nature, and the word is five letters long")
game_is_completed = False
while True:  
    for y in range (2):
        print ("Person Number: ", y)
        letter = pick_letter()
        print("The letter appears this many times in the word: ", secret_word.count(letter))
        scores[y] = scores[y] + 1
        word = input("Guess the word (press enter if you would like to skip): ")
        print(word)
        if word != "": 
            if word == secret_word:
                print("Congradulations! You guessed the word!")
                game_is_completed = True
                break
            else:
                print("Sorry, that is not the correct answer.")
            word_guess_counts[y] = word_guess_counts[y] + 1 
            if word_guess_counts[y] == 3:
                print("You have guessed the word 3 times, you lose :(")
                game_is_completed = True
                break 
            
    if game_is_completed: 
        break    
print("Amount of times the word has been guessed: ", word_guess_counts)
print("score: ", scores)