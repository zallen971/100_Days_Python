# Type Error, Type Checking, Type Conversion

# type error
# len(12345) Type Error: object of type 'int' has no len()
len("Hello")  # changed 12345 to Hello to clear Type Error

print(type("Hello"))  # type <class 'str'>
print(type(12345))  # type <class 'int'>
print(type(3.1459))  # type <class 'float>
print(type(True))  # type <class 'bool'>


# type conversion
print("123" + "456")

print(int(123) + int(456))

# print(int("abc") + int("456")) ValueError: invalid literal for int() with base 10: 'abc'

# Make the below line of code to run without errors
#print("Number of letters in your name: " + (len(input("Enter your name"))))

user_name = input("Enter your name: ")
user_name_length = len(user_name)
print("Number of letters in your name: " + str(user_name_length))
