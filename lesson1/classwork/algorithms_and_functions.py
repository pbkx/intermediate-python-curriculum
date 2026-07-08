numbers = [4, 10, 3, 8, 5]

# Sum algorithm
total = 0
for i in range(len(numbers)):
    item = numbers[i]
    total += item
print("Sum:", total)

# Count algorithm
count = 0
for i in range(len(numbers)):
    item = numbers[i]
    if item > 5:
        count += 1
print("Numbers above 5:", count)

# Biggest item algorithm
biggest = numbers[0]
for i in range(len(numbers)):
    if numbers[i] > biggest:
        biggest = numbers[i]
print("Biggest:", biggest)

# Search algorithm
found = False
for i in range(len(numbers)):
    if numbers[i] == 8:
        found = True
        break

if found == True:
    print("8 was found")
else:
    print("8 was not found")

# Functions help us reuse code
def add_numbers(a, b):
    total = a + b
    return total

answer = add_numbers(3, 5)
print("Answer:", answer)

# Local variables only exist inside the function
def double_number(num):
    result = num * 2
    return result

print(double_number(4))
