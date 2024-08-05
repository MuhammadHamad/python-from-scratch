# Write a Python program that takes two numbers as input from the user and performs the following operations:
# Addition
# Subtraction
# Multiplication
# Division
# The program should display the results of each operation.

# Taking input from the user
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

# Performing the arithmetic operations
addition = first_number + second_number
subtraction = first_number - second_number
multiplication = first_number * second_number
division = first_number / second_number

# Displaying the results
print("Addition: {} + {} = {}".format(first_number, second_number, addition))
print("Subtraction: {} - {} = {}".format(first_number, second_number, subtraction))
print("Multiplication: {} * {} = {}".format(first_number, second_number, multiplication))
print("Division: {} / {} = {}".format(first_number, second_number, division))