'''
Emily, Grade 12 APCSP
Assignment: Celcius to Fahrenheit

This program will prompt the user to input Celcius temperature 
and output the equivalent Fahrenheit temperature.
'''

# stored input into a variable name 'cel_str'
cel_str = input("Enter a Celcius temperature as a float: ")

# using 'float' to make 'cel_str' able to represent a decimal and stored it in a variable name 'cel'
cel = float(cel_str)

# stored the formula of converting celcius to fahrenheit into a variable name 'fahrenheit'
fahrenheit = (cel * 9/5) + 32

# print the output of celcius changing to fahrenheit
print("Temperature in Fahrenheit: {:.2f}".format((fahrenheit)))