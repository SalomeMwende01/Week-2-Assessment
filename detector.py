day_number = int(input("Enter a number between 1 and 7: "))

match day_number:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5 | 6 | 7:
        print("Looking forward to the weekend!")
    case _:
        print("Invalid day number.")
