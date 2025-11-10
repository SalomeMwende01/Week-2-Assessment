colors = ["red", "green", "yellow"]
fruits = ["apple", "banana", "pear"]

count = 0

for color in colors:
    for fruit in fruits:
        print(f"{color} : {fruit}")
        count += 1

print(f"Total combinations printed: {count}")
