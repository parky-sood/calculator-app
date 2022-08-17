# This program will create a basic command line calculator to take user input and output the result
# Future iterations will add more functions and a GUI to create a more interactive experience

# Get operator numbers from user
num1 = int(input("Enter any number: "))
num2 = int(input("Enter another number: "))

# Ask user for operation
operator = input("What would you like to do to these numbers? ('+' for add, '-' for subtract, '*' for multiply, '/' for divide) ")

# Operate on num1 and num2 based on user input for 'operator'
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 / num2

# output result of operation
print("The result of the operation is", result)
