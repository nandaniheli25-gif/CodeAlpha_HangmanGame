import random

word_list = ["apple", "ball", "cat", "dog", "tiger", "banana"]

def instructions():

    print("----- Instructions -----")
    print("1. Guess the word letter by letter")
    print("2. You have 6 attempts")
    print("3. Correct letters will replace underscores")
    print("4. Guess the complete word before attempts end")


def word_prediction(word_list):

    word = random.choice(word_list)

    print("----- Welcome to the Hangman Game -----")
    print("The word contains", len(word), "letters")

    guess = ["_"] * len(word)

    attempts = 6

    while attempts > 0:

        show = ""

        for letter in guess:
            show += letter + " "

        print("Word :", show)

        letter = input("Enter a letter : ")

        if letter in word:

            print("Correct Guess")

            for i in range(len(word)):

                if word[i] == letter:
                    guess[i] = letter

        else:

            attempts -= 1

            print("Wrong Guess")
            print("Remaining attempts :", attempts)

        if "_" not in guess:

            print("You guessed the word!")

            final_word = ""

            for letter in guess:
                final_word += letter

            print("The word was :", final_word)

            break

    if attempts == 0:

        print("Game Over")
        print("Correct word was :", word)


while True:

    print("----- MENU -----")
    print("1. Instructions")
    print("2. Start Game")
    print("3. Exit")

    choice = input("Enter your choice : ")

    if choice == "1":

        instructions()

    elif choice == "2":

        word_prediction(word_list)

    elif choice == "3":

        print("Thank You")
        break

    else:

        print("Invalid Choice")
    