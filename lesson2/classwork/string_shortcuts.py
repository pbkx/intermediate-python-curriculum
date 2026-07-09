first = "Pineapple"
last = "Pizza"

# String concatenation
full = first + " " + last
print(full)

# Repeat a string
print("ha" * 3)  # 'hahaha'

# 'in' checks if something appears inside a string
sentence = "I like python"

if "python" in sentence:
    print("There is python in the sentence.")
if "java" in sentence:
    print("There is java in the sentence.")

# Escape characters
print("\"hello\"")
print("\\world")

print("Line 1\nLine 2")

# You can turn non-strings into strings using str()
age = 16
print("Age is: " + str(age))