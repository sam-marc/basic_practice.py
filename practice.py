import math

# Variables and Data Types:

# Declare three variables: num1 (an integer), num2 (a float), and name (a string).
num1 = 10
num2 = 5.5
name = "Samuel"

# Print the values and types of these variables.
print("num1:", num1, "Type:", type(num1))
print("num2:", num2, "Type:", type(num2))
print("name:", name, "Type:", type(name))
print()

# User Input:

# Prompt the user to enter their age.
age = int(input("Enter your age: "))

# Print a message based on the age:
if age < 18:
    print("You are a minor.")
elif 18 <= age <= 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
print()

# Conditional Statements:

def check_number(num):
    """Function to check if a number is positive, negative, or zero."""
    if num > 0:
        print("Positive number.")
    elif num < 0:
        print("Negative number.")
    else:
        print("Zero.")

# Call this function with different integer values to test it.
check_number(5)   # Positive number
check_number(-3)  # Negative number
check_number(0)   # Zero
print()

# Loops:

# Write a loop that prints all even numbers from 0 to 20 (inclusive).
print("Even numbers from 0 to 20:")
for i in range(0, 21, 2):
    print(i, end=" ")
print("\n")

# Functions:

def calculate_circle_area(radius):
    """Function to calculate the area of a circle."""
    area = math.pi * radius ** 2
    return area

# Call this function with different values of radius and print the results.
radii = [2, 3, 4.5]
for r in radii:
    print("Radius:", r, "Area:", calculate_circle_area(r))
