import random
def makeRandomNumber():
    int_random = random.randint(1, 100)
    return int_random

def getUserInput():
    user_input = int(input("Guess a number :\n"))
    return user_input
def main():
    random_int = makeRandomNumber()
    keyboard = getUserInput()
    print()
    while (keyboard != int(-1)):
        attempts = []
        while (keyboard != random_int):
            if (str(keyboard) in attempts):
                print("ERROR: You already guessed that!")
            elif (keyboard < random_int):
                print("ERROR: Too Low!")
                attempts.append(str(keyboard))
            elif (keyboard > random_int):
                print("ERROR: Too High!")
                attempts.append(str(keyboard))
            keyboard = getUserInput()
            print()
        print("Congrats you guessed the right number")
        print("It took you ",len(attempts),"times to guess the right number")
        random_int = makeRandomNumber()
        keyboard = getUserInput()
        print()
    print("Game Over")

if __name__ == "__main__":
    main()
