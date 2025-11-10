
value = input("Enter any value: ")

print(f"Raw input: {value}")

if value.isdigit():
    typed_value = int(value)
elif value.replace('.', '', 1).isdigit() and value.count('.') < 2:
    typed_value = float(value)
else:
    typed_value = value

if isinstance(typed_value, int):
    print("Data type: int")
elif isinstance(typed_value, float):
    print("Data type: float")
else:
    print("Data type: str")
