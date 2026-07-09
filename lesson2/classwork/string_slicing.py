word = "pineapple"
print("Word is:", word)

# Strings are 0 indexed (first character is index 0)
print("First letter:", word[0])
print("Second letter:", word[1])

# Negative indexing starts from the end
print("Last letter:", word[-1])
print("Second to last letter:", word[-2])

# Slicing: word[start:stop]  (start is inclusive, stop is exclusive: [start, stop)
print(word[0:4])   # 'pine'
print(word[4:9])   # 'apple'

# Shortcuts: you can leave start or stop blank
print(word[:4])
print(word[4:])

print(word[::-1])  # reverse the string

# Error: index out of range
# print(word[100])