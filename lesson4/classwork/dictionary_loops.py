scores = {
    "Ava": 95,
    "Ben": 88,
    "Kai": 73
}

# Loop through keys
for name in scores:
    print(name, "scored", scores[name])

# Print scores greater than 90
for name in scores:
    score = scores[name]
    if score >= 90:
        print(name, "got an A")

# Loop through keys and values
for name, score in scores.items():  # key, value
    print(name, "scored", score)

# Loop through values
for score in scores.values():
    print(score)