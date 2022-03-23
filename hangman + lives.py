import random
import string

from words import words

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    #getting user input
    while len(word_letters) > 0 and lives> 0:
        # letters used
        # ''.join(['a','b','cd']) ----> 'a b cd'
        print('You have', lives,'lives left and You have used these letters:', ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('current word:',' '.join(word_list))

        user_letter = input('guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1  #take away a life if wrong
                print('letter is not in the word. ')
        elif user_letter in user_letter:
            print('You have already used that character, please try again. ')

        else:
            print('Invalid character. Please try again. ')
    if lives == 0:
        print('You died, sorry the word was', word)
    else:
        print('You guesses the word', word, '!!')
print(hangman())