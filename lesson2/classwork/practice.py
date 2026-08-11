# Problem 1
# Ask the user for a word.
# Print the first 3 letters, and then print the last 3 letters.

word = input("Enter a word: ")
print("First 3:", word[:3])
print("Last 3:", word[-3:])

# Problem 2
# Ask the user for a sentence.
# Print it in all caps, then print it in all lowercase.

sentence = input("Enter a sentence: ")
print(sentence.upper())
print(sentence.lower())

# Problem 3
# Ask the user for a word.
# Print how many vowels it has (a, e, i, o, u).

word = input("Enter a word: ")
vowels = "aeiou"
count = 0
for ch in word.lower():
    if ch in vowels:
        count = count + 1
print("Vowels:", vowels)

# Problem 4
# Ask the user for a phrase.
# Build a new string that removes all spaces.

phrase = input("Enter a phrase: ")
result = ""
for ch in phrase:
    if ch != " ":
        result = result + ch
print(result)

# Problem 5
# Ask the user for a word.
# Print "Palindrome" if it reads the same backwards, otherwise print "Not palindrome".

word = input("Enter a word: ")
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")