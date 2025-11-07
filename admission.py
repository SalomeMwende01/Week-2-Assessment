age = input("Please provide your age: ")
user = input("Please provide your username: ")
if int(age) < 12:
    fee = 100
elif int(age) >= 12 and int(age) <= 18:
    fee = 200
elif int(age) > 18:
    fee = 300
print(f"{user} pays {fee} KES for admission.")