scores = {
    "Ava" : 95,
    "Ben" : 88,
    "Kai" : 73
}

# Loop through keys
for name in scores:
    print(name, "scored", scores[name])

for name, score in scores.items():
    if score >= 90:
        print(name, "got an A")