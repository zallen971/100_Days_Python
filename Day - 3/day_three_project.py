# Goal is to build a simple 'choose your own adventure game' for day 3 project

print("Welcome to Treasure Island")
print("Your mission is to find the treasure.\n")

print("As you're walking you come to a crossroad in the jungle...")
# get direction input from user
direction = input("Which way do you want to go? L or R: ")

# if direction is L, keep going
if direction == "L":
    print("You keep moving through the jungle...\n")
else:  # if direction is R or anything else, game over
    print("\nOh no, you fell into a giant hole. Game Over!!!")
    exit()

print("As you're walking you come across a river...")
# get swim input from user
swim = input("Do you want to swim through the current or wait it out? S or W: ")

# if swim choice is n
if swim == "W":
    print("\nYou decided to wait it out until the current dies down to continue...")
else:  # if swim choice is y or anything else, game over
    print("\nYou attempted to swim through the current and were attacked by a killer trout...Game Over!")
    exit()

print("\nYou arrive at a building, upon entering you see 3 doors to pick from.")
print("There is a Red door, a Blue door and a Yellow door...")
# get door choice from user
door_choice = input("\nWhich door do you want to pick? R, B or Y: ")

if door_choice == "R":  # if door picked is Red
    print("\nYou pick up the Red door...")
    print("You were burned by fire..Game Over")
    exit()

elif door_choice == "B":  # if door picked is Blue
    print("\nYou pick up the Blue door...")
    print("You were eaten by beasts..Game Over")
    exit()

elif door_choice == "Y":  # if door picked is Yellow
    print("\nYou pick up the Yellow door...")
    print("You found the treasure..You win!")

else:  # anything else
    print("Game Over")
    exit()
