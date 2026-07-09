# Count vowels in a word
word = "strawberry"
vowels = "aeiou"
count = 0
for ch in word:  # go through each character in the string
    if ch in vowels:  # check if the character is in the vowels string
        count = count + 1
print("Vowel count:", count)

# Check if a word is a palindrome
test = "racecar"
if test == test[::-1]:
    print(test, "is a palindrome")
else:
    print(test, "is not a palindrome")

# Build a new string without the letter a
fruit = "banana"
result = ""
for ch in fruit:
    if ch != "a":
        result = result + ch
print(result)