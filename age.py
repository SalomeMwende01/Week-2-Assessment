age = int(input("Please enter your age: "))
if age > 18:
    print("Access granted - you receive a complimentary drink!")
elif age >= 16 and age <= 18:
    print("Access granted - enjoy a juice a juice pack!")
elif age >=1 and age < 16:
    print("Acccess denied - you're too young!")
else:
    print("Invalid age entered!")
