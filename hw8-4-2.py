# Author: CRS 12/09/21
from random import randint


def rock_paper_scissors(wins = 0, losses = 0, ties = 0, matches = 0):
        """Play rock paper scissors"""
        player = int(input("Enter 0 for rock, 1 for paper, and 2 for scissors: "))
        computer = randint(0, 2)
        looped = False

        # Check if the user or the computer won.
        if not looped:
            if player == computer:
                ties += 1
                print("It's a tie!")
        elif player == 0:
            if computer == 1:
                losses += 1
                print("You lose, paper covers rock.\n")
            else:
                losses += 1
                print("You win, rock crushes scissors!\n")
                wins += 1
        elif player == 1:
            if computer == 2:
                losses += 1
                print("You lose, scissors cuts paper.\n")
            else:
                wins += 1
                print("You win, paper covers rock!\n")
        elif player == 2:
            if computer == 0:
                losses += 1
                print("You lose, rock crushes scissors.\n")
            else:
                wins += 1
                print("You win, scissors cuts paper!\n")
        elif player >= 3 or player <= -1:
            print("Another round will start.")
            rock_paper_scissors()
        
        matches += 1
        again = input(" Play again?")
        if again.lower() == "yes":
                rock_paper_scissors(wins, losses, ties, matches)
        elif again.lower() == "no":
                print("Wins: " + wins + "Losses: " + losses + "Ties: " + ties + "Matches: " + matches)
rock_paper_scissors()