# Learn about nested if/else statements

print("Welcome to the rollercoaster!")
height = int(input("Enter your height in cm: "))  # get user height in cm


if height >= 120:
    print("\nYou are big enough to ride the rollercoaster!")
    age = int(input("Enter your age in years: "))  # get user age
    if age < 12:
        print("\nYour ticket cost is: $5.00")  # younger than 12

    elif age <= 18:
        print("\nYour ticket cost is: $7.00")  # between 12 - 18

    elif age > 18:
        print("\nYour ticket cost is: $12.00")  # over 18

else:
    print("You are too small to ride!")