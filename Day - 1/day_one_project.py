# Band Name Generator
# Create a greeting for the program
# Ask user for the city they grew up in and store it in a variable
# Ask user for the name of a pet and store in a variable
# Combine the city and name of the pet and output their band name

# greeting
print("Hello and welcome to the Band Name Generator!")

# get user city and store in a variable
user_city = input("The city you grew up in: ")

# get user pet name and store in a variable
user_pet_name = input("The name of a pet you have or had: ")

# combine the two variables for the band name
band_name = user_city + " " + user_pet_name

# output the band name
print(f"\nYour band name is: {band_name}")