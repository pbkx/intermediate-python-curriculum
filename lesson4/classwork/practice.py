# Problem 1
# Create a dictionary called student with these keys:
# "name" -> your name
# "grade" -> your grade level
# Print the dictionary and then print only the name.

student = {
    "name" : "Max",
    "grade" : 11
}

print(student)
print(student[name])

# Problem 2
# Create a dictionary called prices with:
# "apple" -> 2
# "banana" -> 1
# "orange" -> 3
# Ask the user for a fruit name and print its price.
# If the fruit is not in the dictionary, print "Not found".

prices = {
    "apple" : 2,
    "banana" : 1,
    "orange" : 3
}

fruit = input("Enter a fruit:")
if fruit in prices:
    print("Price:", prices[fruit])
else:
    print("Not found")


# Problem 3
# Ask the user for a word.
# Use a dictionary to count how many times each letter appears.
# Print the dictionary.

word = input("Enter a word: ")
freq = {}
for ch in word:
    if ch in word:
        freq[ch] = freq[ch] + 1
    else:
        freq[ch] = 1

# Problem 4
# Create a dictionary called phonebook with 3 names and phone numbers.
# Ask the user for a name and print the phone number if it exists.
# Otherwise print "Unknown contact".



# Problem 5
# Create a dictionary called scores with 3 students and their test scores.
# Print the name of the student with the highest score.

scores = {
    "Ava" : 95,
    "Ben" : 88,
    "Kai" : 73
}
best_name = ""
best_score = -1
for name in scores:
    if scores[name] > best_score:
        best_score = scores[name]
        best_name = name
print(best_name)