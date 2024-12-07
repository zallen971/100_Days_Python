# Task is to build an automatic pizza order program
# Small: $15
# Medium: $20
# Large: $25
# Add Pepperoni to S: +$2
# Add pepperoni to M or L: +$3
# Add extra cheese to any size: +$1
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# determine pizza size and add cost to it
pizza_cost = 0
if size == "S":  # size S
    pizza_cost += 15
elif size == "M":  # size M
    pizza_cost += 20
elif size == "L":  # size L
    pizza_cost += 25
else:
    print("Invalid size...")

# determine cost if adding pepperoni
if pepperoni == "Y":
    if size == "S":
        pizza_cost += 2
    else:
        pizza_cost += 3

# determine cost if adding extra cheese
if extra_cheese == "Y":
    pizza_cost += 1

# print total cost of pizza
print(f"Your total cost is: ${pizza_cost}")
