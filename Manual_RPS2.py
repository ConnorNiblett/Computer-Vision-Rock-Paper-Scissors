import random

print("Rock, Paper, Scissors")

listCh = ["Rock", "Paper", "Scissors"]

userScore = 0
computerScore = 0
i = 1

chance = int(input("How many time you want to play (no. of chances): "))

while i <= chance:
    computerCh = random.choice(listCh)
    
    userCh = input ("Enter Rock, Paper, Scissors")
    if userCh == computerCh:
        print("Tied Round")
    
    elif userCh == "Rock":
        print("Computer Enter: ", computerCh)
        if computerCh == "Paper":
            print("You lose! Paper covers Rock")
            computerScore += 1
        else:
            print("You win! Rock smashes Scissors")
            userScore += 1
    
    elif userCh == "Paper":
        print("Computer Enter: ", computerCh)
        if computerCh == "Scissors":
            print("You lose! Scissors cut Paper")
            computerScore += 1
        else:
            print("You win! Paper covers Rock")
            userScore += 1
    
    elif userCh == "Scissors":
        print("Computer Enter: ", computerCh)
        if computerCh == "Rock":
            print("You lose! Rock smashes Scissors")
            computerScore += 1
        else:
            print("You win! Scissors cut Paper")
            userScore += 1

    print("\n\t******ScoreBoard******")
    print(f"\t You: {userScore} | Computer: {computerScore}")
    print("\t**********************")
    print(f"Game No:[{i}]")
    print("========================================================")
    i += 1
print("\n\n##### Game Over #####")
print("*******************************************")
if userScore < computerScore:
    print("Sorry You lose the game \n computer win the game with score:", computerScore)
elif userScore == computerScore:
    print("Game is Tie Play Again")
else:
    print("You Win the Game with score:", userScore)