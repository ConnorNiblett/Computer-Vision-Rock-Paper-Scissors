import random

from cv2 import repeat

import itertools

UserScore = 0
ComputerScore = 0

num = 20000000
for _ in itertools.repeat(None, num):
    possible_actions = ["Rock", "Paper", "Scissors"]
    user_action = random.choice(possible_actions)
    possible_actions = ["Rock", "Paper", "Scissors"]
    computer_action = random.choice(possible_actions)
    print (f"\nYou chose {user_action}, computer chose {computer_action}.\n")


    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "Rock":
        if computer_action == "Scissors":
            print ("Rock smashes Scissors! You win!")
            UserScore += 1
        else:
            print ("Paper covers Rock! You lose.")
            ComputerScore += 1
    elif user_action == "Paper":
        if computer_action == "Rock":
            print ("Paper covers Rock! You win!")
            UserScore += 1
        else:
            print ("Scissors cut Paper! You lose.")
            ComputerScore += 1
    elif user_action == "Scissors":
        if computer_action == "Paper":
            print ("Scissors cut Paper! You win!")
            UserScore += 1
        else:
            print ("Rock smashes Scissors! You lose.")
            ComputerScore += 1
print (UserScore)
print (ComputerScore)
if UserScore < ComputerScore:
    print ("You lose!")
elif UserScore == ComputerScore:
    print ("Tie game...")
else:
    print ("You win!")
         

