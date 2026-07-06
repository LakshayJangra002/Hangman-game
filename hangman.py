import random

#list of words
words = ["python", "apple", "school", "computer", "hangman"]

#Randomly choose one word
secret_word = random.choice(words)

#list of guessed letters
guessed_letters = []

#Set wrong guesses
wrong_guesses = 0
max_wrong_guesses = 6

print("===== Welcome to Hangman =====")

#playing until the game ends
while wrong_guesses < max_wrong_guesses:

    display = ""

    # guessed letters
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    # player guess the word
    if "_" not in display:
        print("\n🎉 Congratulations! You guessed the word:", secret_word)
        break

    # Take input from the player
    guess = input("Enter a letter: ")

    # input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.")
        continue

    # if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    # Store the guessed letter
    guessed_letters.append(guess)

    # the guess is correct or not
    if guess in secret_word:
        print("✅ Correct Guess!")
    else:
        wrong_guesses += 1
        print("❌ Wrong Guess!")
        print("Remaining Chances:", max_wrong_guesses - wrong_guesses)

# If chances are over
if wrong_guesses == max_wrong_guesses:
    print("\n💀 Game Over!")
    print("The correct word was:", secret_word)