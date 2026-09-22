import random

choices = ["rock", "paper", "scissors"]

player = input("Choose rock, paper or scissors : ").lower()

if player not in choices:
    print("Invalid choice! Please choose rock, paper or scissors.")
else:
    computer = random.choice(choices)

    if player == computer:
        print(f"It's a Tie. Both Choose {player}.")

    elif (player == "rock" and computer == "scissors") or \
        (player == "paper" and computer == "rock") or \
        (player == "scissors" and computer == "paper") :
        print(f"You Win! {player} beats {computer}")

    else:
        print(f"Computer Wins! {computer} beats {player}")

