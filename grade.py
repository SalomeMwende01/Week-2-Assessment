grade = int(input("provide your score (0-100): "))
if grade >= 80 and grade <= 100:
    print("Excellent")
elif grade >=50 and grade <= 79:
    print("Good")
elif grade >=0 and grade <= 49:
    print("Needs Improvement")
else:
    print("Invalid score entered.")