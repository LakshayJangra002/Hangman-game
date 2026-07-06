import random

# Step 1: Create a list of predefined words
words = ["python", "apple", "school", "computer", "hangman"]

# Step 2: Randomly choose one word
secret_word = random.choice(words)

# Step 3: Create an empty list to store guessed letters
guessed_letters = []

# Step 4: Set the maximum number of wrong guesses
wrong_guesses = 0
max_wrong_guesses = 9

print("===== Welcome to Hangman =====")

# Step 5: Keep playing until the game ends
while wrong_guesses < max_wrong_guesses:

    display = ""

    # Step 6: Show guessed letters and hide others with "_"
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    # Step 7: Check if the player has guessed the whole word
    if "_" not in display:
        print("\n🎉 Congratulations! You guessed the word:", secret_word)
        break

    # Step 8: Take input from the player
    guess = input("Enter a letter: ")

    # Step 9: Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.")
        continue

    # Step 10: Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    # Step 11: Store the guessed letter
    guessed_letters.append(guess)

    # Step 12: Check whether the guess is correct
    if guess in secret_word:
        print("✅ Correct Guess!")
    else:
        wrong_guesses += 1
        print("❌ Wrong Guess!")
        print("Remaining Chances:", max_wrong_guesses - wrong_guesses)

# Step 13: If all chances are over
if wrong_guesses == max_wrong_guesses:
    print("\n💀 Game Over!")
    print("The correct word was:", secret_word)