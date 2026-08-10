name = "Alex"  # String variable
age = 12  # Integer variable
height = 5.2  # Float variable
likes_python = True  # Boolean variable

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Likes Python:", likes_python)

# input() gives us a string
# int(input()) changes the string into an integer
num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")

# % gives us the remainder after division
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Logical operators let us combine conditions
if num > 0 and num < 100:
    print("The number is between 1 and 99")

if num < 0 or num > 100:
    print("Thle number is outside the normal range")