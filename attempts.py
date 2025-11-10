correct_password = "pass123"

attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input("Enter your password: ")

    if password == correct_password:
        print("Access granted")
        break
    else:
        attempts += 1
        if attempts < max_attempts:
            print("Wrong password, try again.")
        else:
            print("Account locked.")
