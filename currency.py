'''
Emily, Grade 12 APCSP
Assignment: Currency Conversion

This program will prompt the user to input a number of US Dollars (USD)
and output the equivalent amount of Thai Baht.
'''

# stored input into a variable name 'usd_str'
usd_str = input("Enter currency amount in USD: ")

# using 'float' to make 'usd_str' able to represent a decimal and stored it in a variable name 'usd'
usd = float(usd_str)

# stored the formula of converting dollar to baht into a variable name 'baht'
baht = (usd * 33.6887)

# print the output of currency changing from dollar to baht
print("{:.2f} Thai Baht".format((baht)))