myFamily = {
    "father": {"name": "John", "year": 1985},
    "mother": {"name": "Jane", "year": 1990}
}

member = input("Enter 'father' or 'mother': ").lower()

if member in myFamily:
    print(f"Name: {myFamily[member]['name']}")
    print(f"Birth Year: {myFamily[member]['year']}")
else:
    print("Family member not found.")
