import random
from ascii import stages, logo
from hangman_words import word_list

print(logo)
print("Welcome to Hangman!")

# Choose a random word
chosen_word = random.choice(word_list)
lives = 6
game_over = False
correct_letters = []

# Create initial placeholder (e.g., "_____")
display = ""
for _ in chosen_word:
    display += "_"
print(f"Word to guess: {display}")

# Game loop
while not game_over:
    print(f"\n**************************** {lives}/6 LIVES LEFT ****************************")
    guess = input("Guess a letter: ").lower()

    new_display = ""
    for letter in chosen_word:
        if letter == guess:
            new_display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            new_display += letter
        else:
            new_display += "_"

    display = new_display
    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"'{guess}' is not in the word.")
        if lives == 0:
            game_over = True
            print(f"You lose! The word was {chosen_word}")

    if "_" not in display:
        print("You win!")
        game_over = True

    print(stages[lives])

