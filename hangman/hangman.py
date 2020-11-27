# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    while True:
      letter = input("Enter the letter: ")
      if letter.isalpha() == False:
        print("this is incorrect")
        continue
      elif len(letter) != 1:
        print("this is incorrect")
        continue
      elif letter.islower() == False:
        print("Letter must be lower")
        continue
      else:
        break
    k = 0
    is_in_letters_guessed = letter in letters_guessed
    if is_in_letters_guessed == False:
      letters_guessed += letter
    for element in secret_word:
      if letter == element:
        k += 1
      else:
        k += 0
    if k == 0:
      print("unfortunately you did not guess the letter")
      return False
    else:
      print("You guessed the letter")
      return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    adding_string = secret_word
    adding_string_1 = ""
    def changeword(word):
      for element in word:
        if element != "":
          word = word.replace(element,"_")
      return word
    adding_string = changeword(adding_string)
    for element in secret_word:
      k = 0
      for letter in letters_guessed:
        if element == letter:
          k += 1
          adding_string_1 += letter
          break
        else:
          k += 0
      if k == 0:
        adding_string_1 += "_"
    while len(secret_word) != len(adding_string_1):
      adding_string_1 += "_"
    return adding_string_1




def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    all_letters = list(string.ascii_lowercase)
    for element in letters_guessed:
      if element in all_letters:
        all_letters.remove(element)
    all_letters = str(all_letters)
    a = all_letters.replace("[", "")
    b = a.replace("]", "")
    c = b.replace(" ", "")
    d = c.replace(",", ", ")
    remaining_letters = d.replace("'", "")
    return remaining_letters
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print("Number of letters:", len(secret_word))
    letters_guessed = []
    n = 1
    while n < 7:
      if is_word_guessed(secret_word, letters_guessed) == True:
        my_word = get_guessed_word(secret_word, letters_guessed)
        print("This word:", my_word)
        k = 0
        for element in my_word:
          if element == "_":
            k += 1
          else:
            k += 0
        if k == 0:
          print("You guessed the word")
          break
        print("Available letters:", get_available_letters(letters_guessed))
      else:
        print("Remaining letters:", get_available_letters(letters_guessed))
        print("There are", 6 - n, "guesses left")
        n += 1
    print("unfortunately you did not guess the word")
    print("This word:", secret_word)




# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    k = 0
    if len(other_word) == len(my_word):
      for element in range(0, len(my_word)):
        if my_word[element] == other_word[element]:
          k += 1
    if k == len(my_word.replace("_", "")):
      return True
    



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    list_of_same_words = []
    for word in wordlist:
      if match_with_gaps(my_word, word) == True:
        list_of_same_words.append(word)
    print(list_of_same_words)


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print("Number of letters:", len(secret_word))
    letters_guessed = []
    n = 1
    while n < 7:
      if is_word_guessed(secret_word, letters_guessed) == True:
        my_word = get_guessed_word(secret_word, letters_guessed)
        print("This word:", my_word)
        k = 0
        for element in my_word:
          if element == "_":
            k += 1
          else:
            k += 0
        if k == 0:
          print("You guessed the word")
          break
        print("Hints:")
        show_possible_matches(my_word)
        print("Available letters:", get_available_letters(letters_guessed))
      else:
        print("Remaining letters:", get_available_letters(letters_guessed))
        print("There are", 6 - n, "guesses left")
        n += 1
    print("unfortunately you did not guess the word")
    print("This word:", secret_word)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    print("Hello. Do you want to play the gallows with me?")
    print("If you want to play with me, write 'yes', otherwise - 'no'")
    while True:
      text_1 = input()
      if text_1 == "yes":
        print("Good. Now choose which version of the game you will play: normal(1) or easy(2)")
        print("'Normal' is a traditional version of the game")
        print("'Easy' will show words in which the locations of the guessed letters are the same")
        print("1 or 2?")
        while True:
          text_2 = input()
          if text_2 == "1":
            secret_word = choose_word(wordlist)
            hangman(secret_word)
            break
          elif text_2 == "2":   
            secret_word = choose_word(wordlist)
            hangman_with_hints(secret_word)
            break
          else:
            print("What does it mean?")
        print("You are not a bad opponent. I really liked our game. Do you want to keep playing with me?('yes' or 'no')")
      elif text_1 == "no":
        print("bye(")
        break
      else:
        print("What does it mean?")