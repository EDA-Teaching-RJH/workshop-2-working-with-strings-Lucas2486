grade = int(input("What is your grade?, from 0-100:"))

if 100>=grade>=90:
    print("You got an A")
elif 89>=grade>=80:
    print("You got an B")
elif 79>=grade>=70:
    print("You got an C")
elif 69>=grade>=60:
    print("You got an D")
elif 60>grade>=0:
    print("You got an F")
else:
    print("Error")