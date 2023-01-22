import random

player1 = input("select Rock, Paper, or Scissors :").lower()
player2 = random.choice(["Rock","Paper","Scissor"]).lower()
print("Player 2 Selected:", player2)

if player1 == "rock" and player2 == "paper":
    print("Player 2 won")
elif player1 == "Paper" and player2 == "Scissor":
    print("Player 2 won")
elif player1 == "Scissor" and player2 == "rock":
    print("Player 2 won")
elif player1 == player2:
    print("Tie")
else:
    print("Player 1 won")


