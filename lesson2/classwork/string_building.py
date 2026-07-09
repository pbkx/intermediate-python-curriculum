# Building a string with a loop (using +=)
name = "Max"
result = ""
for ch in name:
    result = result + ch + "-"
print(result)

# Building a string by collecting pieces in a list, the joining
letters = ["p", "y", "t", "h", "o", "n"]
built = "".join(letters)
print(built)

# Make a new string with only the even index characters
word = "computer"
new_word = ""
for i in range(len(word)):
    if i % 2 == 0:
        new_word = new_word + word[i]
print(new_word)