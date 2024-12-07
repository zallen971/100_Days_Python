# Learn about multiple if/else statements

print("Welcome to the rollercoaster!")
height = int(input("Enter your height in cm: "))  # get user height in cm


if height >= 120:
    print("\nYou are big enough to ride the rollercoaster!")
    age = int(input("Enter your age in years: "))  # get user age
    if age < 12:
        ticket = 5
        print("\nChild ticket cost is: $5")  # younger than 12

    elif age <= 18:
        ticket = 7
        print("\nYouth ticket cost is: $7")  # between 12 - 18

    elif age > 18:
        ticket = 12
        print("\nAdult ticket cost is: $12")  # over 18

    wants_photo = input("Would you like to see a photo? (y/n): ")
    if wants_photo == "y":

        # Add $3 to bill
        ticket += 3
        print(f"\nYour total bill is: ${ticket}")
    else:
        print(f'\nYour total bill is: ${ticket}')


else:
    print("You are too small to ride!")