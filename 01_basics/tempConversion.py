# Write a Python program that converts a temperature from Celsius to Fahrenheit. The program should prompt the user to enter a temperature in Celsius and then display the equivalent temperature in Fahrenheit.


# Taking input from the user
celsius = float(input("Enter temperature in Celsius: "))

# Converting Celsius to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Displaying the result
print("{} degrees Celsius is equal to {} degrees Fahrenheit.".format(celsius, fahrenheit))