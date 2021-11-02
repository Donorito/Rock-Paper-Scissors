import random

print("Welcome to Rock Paper Scissors!\n\n")
name = input("Who is challenging the computer today? ")

O_rock = "rock"
O_paper = "paper"
O_scissors = "scissors"
opponnent = O_rock, O_paper, O_scissors

P_rock = "rock"
P_paper = "paper"
P_scissors = "scissors"
Player = P_rock, P_paper, P_scissors

O_rock == P_rock
O_paper == P_paper
O_scissors == P_scissors
O_rock < P_paper
O_paper < P_scissors
O_scissors < P_rock


print("Welcome " + name + " \n\n")

player_throw = input("What would you like to throw? " + (P_rock) + " "  +  (P_paper) + " or " +  (P_scissors) + " ? " )
if player_throw == "rock":
    print("you threw " + (P_rock))
elif player_throw == "paper":
    print("You threw " + (P_paper))
elif player_throw == "scissors":
    print("you threw " + (P_scissors))


print("The computer throws")
throws_to_select = 1
opponnent_throw = random.sample(list(opponnent), throws_to_select)
print(opponnent_throw)

if opponnent_throw == ['rock'] and player_throw == "rock":
    print("it's a tie!")
elif opponnent_throw == ['paper'] and player_throw == "paper":
    print("It's a Tie!")
elif opponnent_throw == ['scissors'] and player_throw == "scissors":
    print("It's a Tie!")
elif opponnent_throw == ['rock'] and player_throw == "paper":
    print("YOU WIN!")
elif opponnent_throw == ['paper'] and player_throw == "scissors":
    print("YOU WIN!")
elif opponnent_throw == ['scissors'] and player_throw == "rock":
    print("you win!")

elif player_throw == "rock" and opponnent_throw == ['paper']:
    print("YOU LOSE!")
elif player_throw == "paper" and opponnent_throw == ["scissors"]:
    print("you lose!")
elif player_throw == "scissors" and opponnent_throw == ['rock']:
    print("you lose!")




