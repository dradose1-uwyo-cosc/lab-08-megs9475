# Meghan Longua
# UWYO COSC 1010
# Submission Date: 11/10/2024
# Lab 08
# Lab Section:15
# Sources, people worked with, help given to: Emmanual Penkra
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

def check_string(string):
    if (string.isnumeric()):
        return int(string)
    if (string.count(".") == 1 and
        string.replace(".", "").isdigit()):
        return float(string)
    if (string[0] == "-" and 
        string.replace("-", "").isdigit()):
        return int(string)
    if (string[0] == "-" and
        string.replace("-", "") and 
        string[1:].count(".") == 1 and
        string[1:].replace(".", "").isdigit()):
        return float(string)
    return False

print("*" * 75)

# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false
# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

def slope_intercept(m, b, min_x, max_x):
    slope = check_string(m)
    y_int = check_string(b)
    lower = check_string(min_x)
    upper = check_string(max_x)
    if(not isinstance(min_x, int)):
        print("Lower bound (min_x) must be a whole number")
    if(not isinstance(max_x, int)):
        print("Upper bound (max_x) must be a whole number")
    if upper < lower:
        print("Lower bound must be equal to or less than upper bound")
    return False

while True:
    values = input("Enter values for m, b, min_x, and max_x for formula y = mx + b. Enter 'exit' to exit")
    inputs = values.split(",")
    if (len(inputs) != 4):
        print("Invalid format")
    if (values == 'exit'):
        break
for x in range(lower, upper + 1):
    y = slope * x + y_int

print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null

def quadratic_coefficients(A, B, C):
    a = check_string(A)
    b = check_string(B)
    c = check_string(C)

while True:
    numbers = input("Please input real numbers for A, B, and C")
    inputs = numbers.split(",")
    if (len(inputs) != 3):
        print("Invalid format")
    if (values == 'exit'):
        break

dis = b** - 4*a*c
if dis < 0:
    print("There are no real solutions")
elif dis == 0:
    x = (-b + dis.sqrt())/2 * a
    print(f"There is one real solution: x={x}")
else:
    y = (-b - dis.sqrt())/2 * a
    z = (-b + dis.sqrt())/2 * a
    print(f"There are two real solutions: x={y} and x={z}")