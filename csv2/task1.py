# Stores names in a list
names = []

# Loop to get names from the user
for _ in range(3):
    names.append(input("What's your name? "))

# Loop to print greetings for each name in sorted order
for name in sorted(names):
    print(f"Hello, {name}")
