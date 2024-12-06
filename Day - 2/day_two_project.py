# Day 2: Tip Calculator Project
# if bill was $150.00, split between 5 people with 12% tip.
# After formatting the result to 2 decimal places

# greeting
print("Welcome to the tip calculator!")

# store total bill in a variable
bill = float(input("What was the total bill? $"))

# store tip amount in a variable
tip_amount = int(input("What is the tip amount you would like to give? 10, 12, or 15: "))
tip_percent = tip_amount / 100 # calculate tip percent
total_tip_calc = bill * tip_percent # calculate total tip
total_bill = bill + total_tip_calc # calculate total bill

# store amount of people in a variable
people = int(input("How many people to split the bill: "))

# calculates total for each person
calc_each_total = total_bill / people

# outputs what each person should pay rounds to 2 decimals
print(f"Each person should pay: ${round(calc_each_total, 2)}")
