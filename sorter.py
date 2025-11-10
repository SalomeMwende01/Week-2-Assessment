numbers = [3, 15, 7, 12, 20, 8, 11]

print("Numbers in the list:", numbers)

count = 0

for num in numbers:
    if num <= 10:
        continue
    print(f"Number greater than 10: {num}")
    count += 1

print(f"Total numbers greater than 10: {count}")
