numbers = [4, 10, 3, 8, 5]

# Sum algorithm
total = 0
for i in range(len(numbers)):
    total = total + numbers[i]
print("Sum:", total)

# Count algorithm
count = 0
for i in range(len(numbers)):
    if numbers[i] > 5:
        count = count + 1
print("Numbers above 5:", count)

# Biggest item algorithm
biggest = numbers[0]
for i in range(len(numbers)):
    if numbers[i] > biggest:
        biggest = numbers[i]
print("Biggest:", biggest)

# Functions help us reuse code
def add_numbers(a, b):
    return a + b

answer = add_numbers(3, 7);
print("Answer:", answer)

# Local variables only exist inside the function
def double_number(num):
    result = num * 2
    return result

print(double_number(6))