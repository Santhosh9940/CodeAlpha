import random as rd

words = ["apple", "table", "chair", "plant", "house"]
word = rd.choice(words)
hidden = ["_"] * len(word)
guesses = 6

print("Welcome to Hangman!")

while guesses > 0 and "_" in hidden:
    print("\nWord:", " ".join(hidden))
    letter = input("Guess a letter: ")

    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                hidden[i] = letter
        print("Correct!")
    else:
        guesses -= 1
        print("Wrong! Tries left:", guesses)

if "_" not in hidden:
    print("\nYou won the game! The word was:", word)
else:
    print("\nYou lost the game! The word was:", word)
