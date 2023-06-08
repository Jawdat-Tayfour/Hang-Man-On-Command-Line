import random
import string 
from words import words 

def get_a_valid_word(words):
    word = random.choice(words)
    while " "  in word or  "-" in word:
        word = random.choice(words)
    return word.upper()
    
def hangman():
    lives = 6 
    word = get_a_valid_word(words)
    word_letters = set(word) #this is for the letters of the word we randomly picked 
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what did the user guessed already
    while len(word_letters) > 0 and lives > 0 :

        print('You have ', lives, 'lives. You have used these letters before', ' '.join(used_letters))
        
        word_list = [letter if letter in used_letters else ' - ' for letter in word]
        
        print("current word is : ", ' '.join(word_list))
        
        user_letter = input("Guess a letter : ").upper()
        
        if user_letter in alphabet - used_letters:
        
            used_letters.add(user_letter)
        
            if user_letter in word_letters:
        
                word_letters.remove(user_letter)
            else:
                print("You've used a live ")
                lives = lives -1 
        elif user_letter in used_letters:
        
            print("You have already guessed that letter, Try Again.")
        
        else:
        
            print("You have entered an invalid letter ! ")    
    if lives == 0:
        print("You're dead boy !")
    else:
        print("Congrats champ you just guessed, the word is  : ",word)    

hangman()            