# Problem 1
# Create a tuple called colors with 3 colors.
# Print the first color and the last color.

colors = ("red", "green", "blue")
print(colors[0])
print(colors[-1])

# Problem 2
# Create a tuple called location with (city, state).
# Unpack it into city and state variables and print them.

location = ("Redmond", "WA")
city, state = location
print(city)
print(state)

# Problem 3
# Create a list of numbers.
# Sort the list and print it.

numbers = [8, 2, 10, 4, 1]
numbers.sort()
print(numbers)

# Problem 4
# Create a list of tuples called points with 3 points.
# Sort the list and print it.

points = [(3, 5), (1, 9), (1, 2)]
points.sort()
print(points)

# Problem 5
# Create a list of words.
# Sort the words by length and print the list.

words = ["python", "cat", "elephant", "gopher"]
words.sort(key=len)
print(words)