import random

options = ("rock", "papper", "sissor")

player  = None

computer = random.choice(options)

choie = input("do you like to play")
ties = 0
win = 0
lose = 0

while choie == "y" :
    player = input("choose rock , papper , sissor")

    while player not in options:
        print("unvalid selection, please try again")
        player = input("choose rock , papper , sissor")

    if player == computer :
        print("it's a tie")
        choie = input("do you like to play again? ")
        ties += 1

    elif player == "rock" and computer == "sissor":
        print("YOU WON!")
        choie = input("do you like to play again? ")
        win +=1

    elif player == "sissor" and computer == "papper":
        print("YOU WON!")
        choie = input("do you like to play again? ")
        win +=1

    elif player == "papper" and computer == "rock":
        print("YOU WON!")
        choie = input("do you like to play again? ")
        win +=1

    else : 
        print("YOU LOSE!!")
        choie = input("do you like to play again? ")
        lose +=1


print("______________________")
print("_________ SCORES________")
print(f"you have won {win} times , lost {lose} times , and it was a tie {ties} times")
print()