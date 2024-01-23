import random
import time

# Initial steps to begin the game.

print("\nWelcome to HANGMAN\n")
name = input("Enter your name.\n")
print("Hello " + name + "! Good luck!")
time.sleep(2)
print("The game is about to start. Let's play Hangman!")
time.sleep(3)


def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words = ["december", "water", "juice", "promise", "movie", "phone", "tissue",
             "dinosaur", "encyclopedia", "tackle", "sabotage", "enormous", "thesaurus",
             "fridge", "microwave", "kettle", "cup", "mug", "knife", "guitar", "fork",
             "spoon", "code", "spatula", "executive", "student", "teacher", "pencil",
             "ruler", "rubber", "attack", "destroy", "hug", "kiss", "study", "eat",
             "drink", "build", "punch", "kill", "slap", "rub", "pet", "cat", "dog",
             "horse", "bird", "hamster", "pig", "cow", "chicken", "sheep", "classroom",
             "chair", "table", "door", "keyboard", "program", "television", "laptop"]
    word = random.choice(words)
    length = (len(word))
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""


# Loop to re-execute the game when the first round ends.

def play_loop():
    global play_game
    play_game = input("Do you want to play again?\nType either y or n.\ny = yes, n = no\n")
    while play_game not in ["y", "n", "Y", "N"]:
        play_game = input("ERROR: Do you want to play again?\nType either y or n.\ny = yes, n = no\n")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("\nThanks for playing Hangman! Hope to see you here again.")
        exit()


# Initializing all necessary conditions required for the game.

def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input("This is your hangman word: " + display + " Enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid input, try a letter.\n")
        hangman()
    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    elif guess in already_guessed:
        print("Try a different letter.\n")

    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining.\n")

        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining.\n")
        elif count == 3:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")
        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. You are hanged and have failed!!!\n")
            print("The word was:", already_guessed, word)
            play_loop()

    if word == '_' * length:
        print("Congratulations! You have guessed the word correctly!")
        play_loop()

    elif count != limit:
        hangman()


main()
hangman()
