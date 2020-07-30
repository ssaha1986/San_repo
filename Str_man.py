str = input("Enter a string: ")

# Find the first character of the string
print("First character of the string is: {}".format(str[0]))

# Find the last character of the string
print("Last character of the string is: {}".format(str[-1]))

# Slicing of string
print("Slicing characters from 2nd to 5th index: {}".format(str[2:5]))

# Find length of the string
print("Length of the string is: {}".format(len(str)))

# Split string with space
print("The list after splitting the string with space: {}".format(str.split(' ')))

# Reverse a string
print("The string after reversal: {}".format(str[::-1]))
