# Learn to use the modulo operator


# Pause 1
print(10 % 3) # output is 1, remainder of 1

# Pause 2: Check odd or even
number = int(input("What number do you want to check: "))  # ask user for number

if number % 2 == 0:
    print(number, "is an even number.")  # if number is even
else:
    print(number, "is an odd number.")  # if number is odd
