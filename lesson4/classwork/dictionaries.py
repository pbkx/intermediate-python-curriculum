# A dictionary maps keys to values
person = {
    "name": "Max",
    "age": 17,
    "city": "Redmond"
}

print(person)
print("Name:", person["name"])
print("Age:", person["age"])

# Update a value
person["age"] = person["age"] + 1
print("New age:", person["age"])

# Add a new key
person["favorite_food"] = "pizza"
print(person)