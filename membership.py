cars = ["jeep", "suv", "sedan"]

car_name = input("Enter a car type: ").lower()

if car_name in cars:
    print("We have that car type!")
else:
    print("Sorry, not available.")
