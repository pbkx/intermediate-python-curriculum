text = "   Hello world   "
print("Raw text is:", text)

print("Length:", len(text))  # includes spaces

print(text.lower())  # make everything lowercase
print(text.upper())  # make everything uppercase
print(text.title())  # make everything titlecase

print(text.strip())  # remove spaces on the left and right
print(text.strip().upper())

message = "banana bread"
print("Count of a:", message.count("a"))
print("Find 'bread':", message.find("bread"))  # index of first match (or -1)

print(message.replace("banana", "pumpkin"))

print(message.startswith("ban"))
print(message.endswith("bread"))