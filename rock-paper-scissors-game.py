import random

player_score = 0
computer_score = 0


# Checking the winner
def check_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors")
        or (player_choice == "Paper" and computer_choice == "Rock")
        or (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"
        
#Written by Krishna Chandel

#Game Logic
def play_game(player_choice):
    global player_score, computer_score
    computer_choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(computer_choices)
    
    result = check_winner(player_choice, computer_choice)
    print(f"\nComputer chose {computer_choice}\n{result}")
    
    if result == "You win!":
        player_score += 1
    elif result == "Computer wins!":
        computer_score += 1
    
    print(f"\nPlayer: {player_score} | Computer: {computer_score}")

# Rock Paper Scissors ASCII Art - https://gist.github.com/wynand1004/b5c521ea8392e9c6bfe101b025c39abe

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

#Taking input from user
while True:
    print("\n------ Welcome to Rock, Paper & Scissors Game ------")
    print("\n Choose Rock, Paper, or Scissors (or 'Exit'):")
    user_choice = input().capitalize()
    if user_choice == 'Exit':
        break
    elif user_choice not in ["Rock", "Paper", "Scissors"]:
        print("Invalid choice. Please choose Rock, Paper, or Scissors.")
    else:
        play_game(user_choice)
        
    if user_choice == "Rock":
        print("\n",rock)
    elif user_choice == "Paper":
        print("\n",paper)
    elif user_choice == "Scissors":
        print("\n",scissors)

