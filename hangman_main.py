import random
from random_word import RandomWords

word_list = ["laptop", "magazine", "phone", "clarify", "abbreviate", "lucky", "luxury", "example", "absurd",
             "subway", "syndrome"]


stages =  [ '''
   +---+
  |   |
  O   |
 /|\  |
 / \   |
      |
========= 
''' , '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
========= 
''' , '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
========= 
''' , '''

  +---+
  |   |
  O   |
  |   |
      |
      |
========= 
''' , '''

  +---+
  |   |
  O   |
      |
      |
      |
========= 
''' , '''

  +---+
  |   | 
      |
      |
      |
      |
========= 
''']
# Choosing random word from word list


def blanks_(word_length):
    display_blanks = []
    for _ in range(word_length):
        display_blanks += "_"
    return display_blanks


# Ask user to guess a letter

def user_guess():
    user_guess_ = input("Guess a letter: ")
    return user_guess_.lower()

# Check if user guessed word matches the chosen word


def main():
   #  r = RandomWords()
   # word_list = r.get_random_words()
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)
    blanks = blanks_(word_length)
    print(blanks)
    lives = 6
    word_guess_end = False

    while not word_guess_end:
        guess = user_guess()
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                blanks[position] = letter
        print(blanks)

        if guess not in chosen_word:
            lives = lives - 1
            print(stages[lives])
            if lives == 0:
                word_guess_end = True
                print("You lose")
                print("The word is : ", chosen_word)

        if "_" not in blanks:
            word_guess_end = True
            print("You win!!")


if __name__ == "__main__":
    print( ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                   
'''   )

    print("You have 6 lives")
    main()
