print("Hello world!")

x = 5  # Integer variable
favorite_food = "pizza"  # String variable
height = 5.2  # Float variable
likes_python = True # Boolean variable

print("x:", x)
print("favorite food:", favorite_food)
print("height:", height)
print("likes python:", likes_python)

# input() gives a string
# int(input()) changes the string into a number
num = int(input("Enter a number:"))

if num > 0:
    print("The number is positive.")
elif num == 0:
    print("The number is zero.")
else:
    print("The number is negative.")

if num % 2 == 0:  # % gives remainder after division.
    print("The number is even.")
else:
    print("The number is odd.")

if num > 0 and num < 100:
    print("The number is between 1 and 99.")

if num < 0 or num > 100:
    print("The number is not between 1 and 99.")