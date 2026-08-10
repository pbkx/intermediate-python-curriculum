# Problem 1
# Ask the user for their name and age.
# Print a sentence that uses both variables.

name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hello", name, "you are", age, "years old")

# Problem 2
# Ask the user for a number.
# Print "Positive" if it is more than 0.
# Print "Zero" if it is equal to 0.
# Otherwise print "Negative".

num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")

# Problem 3
# Create a list of 5 numbers.
# Print the sum of all numbers in the list.

numbers = [4, 10, 3, 5, 8]
total = 0
for i in range(len(numbers)):
    total = total + numbers[i]
print("Sum:", total)

# Problem 4
# Create a list of 5 animals.
# Count how many times "cat" appears in the list.

animals = ["cat", "dog", "cat", "bird", "cat"]
count = 0
for i in range(len(animals)):
    if animals[i] == "cat":
        count = count + 1
print("Cats:", count)

# Problem 5
# Create a function called bigger(a, b).
# It should return the bigger number.
# Call it and print the result.

def bigger(a, b):
    if a > b:
        return a
    else:
        return b