# import modules
import random
import hangman_art
import hangman_words

# print logo
print(hangman_art.logo)

# generate random word
choose_word = random.choice(hangman_words.word_list)

word_len = len(choose_word)
game_over = False
# default lives
lives = 6


display = []
# generates blanks 
for blank in range(word_len):
    display += "_"

print(choose_word)

# start the game
while not game_over:
    # user guess letter
    guess = input("Guess the letter? ").lower()

    # check if user already give right answer multiple times
    if guess in display:
        print(f"Your've already guessed {guess} ")

    # check if the guessed letter same with choose word
    for position in range(word_len):
        if choose_word[position] == guess:
            display[position] = guess

    # lose a life if guessed wrong
    if guess not in choose_word:
        lives -= 1 
        print(f"You guessed {guess}, word. You lose one life")
        if lives == 0:
            game_over = True
            print("You lose.")

    # print list but remove "quotation mark"
    print(f"{' '.join(display)}")

    # check are all blank filled?
    if "_" not in display:
        game_over = True
        print("You win the game!")
    
    # print ascii art
    print(hangman_art.stages[lives])

