import random

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns:
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    for letters in secret_word:
        if letters in letters_guessed:
            continue
        else:
            return False

    return True

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    word_duet = ""
    for letter in secret_word:
        if letter in letters_guessed:
            word_duet += letter
        else:
            word_duet += "_ "
    return word_duet



def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    #TODO: check if the letter guess is in the secret word
    for letters in secret_word:
        if letters == guess:
            return True
    return False






def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''
    print("Welcome to Spaceman!")
    print("The secret word contains: {} letters".format(len(secret_word)))
    print("You have 7 guesses left, please enter one letter per round")
    print("---------------------------------------")
    guesses_left = 7

    letters_guessed = []

    while guesses_left > 0:

        #TODO: show the player information about the game according to the project spec
        player_input = input("Enter a letter:")


        #TODO: Ask the player to guess one letter per round and check that it is only one letter
        if len(player_input) > 1:
            print("Error Please enter one letter")



        #TODO: Check if the guessed letter is in the secret word or not and give the player feedback
        if is_guess_in_word(player_input,secret_word):
            print("Nice! You guessed a letter correctly")
            letters_guessed.append(player_input)


            if is_word_guessed(secret_word, letters_guessed):
                print("Congratulations! You guessed the secret word correctly")
                break


        else:
            print("Sorry! You guessed a letter wrong try again")
            guesses_left -=1
        print(get_guessed_word(secret_word, letters_guessed))
        print("guesses left, "+str(guesses_left))
    else:
        print("You lost! You guessed the secret word wrong")
        print("The correct word is, "+secret_word)
        #TODO: show the guessed word so far

    #TODO: check if the game has been won or lost
#These function calls that will star t the game
secret_word = load_word()
spaceman(secret_word)
