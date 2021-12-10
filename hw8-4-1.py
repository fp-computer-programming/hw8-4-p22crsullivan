# Author: CRS 12/09/21
from random import randint as rand
def game():
    guessed_correctly = False
    random_number = str(rand(0, 15))
    while not guessed_correctly:
        player_input = input("What did I generate?")

        if player_input.lower() == "stop":
            print("The number was: " + random_number)
            break
        elif player_input > random_number:
            print("Guess lower.")
        elif player_input < random_number:
            print("Guess higher.")
        elif player_input == random_number:
            break


game()