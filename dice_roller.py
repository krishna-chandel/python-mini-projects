import random

print("------- Welcome to Dice Rolling Simulation Game -------\n")

while True:
    choice = int(input("Choose an option:\n1. Roll the dice\n2. Exit\n"))

    if choice == 1:
        dice_roll = random.randint(1, 6)
        print(f"You rolled: {dice_roll} \n")
	#written by Krishna Chandel
    elif choice == 2:
        break
    else:
        print("Invalid entry. Please select 1 to roll the dice or 2 to exit.\n")
