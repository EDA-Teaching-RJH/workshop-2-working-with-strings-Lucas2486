import random
secret_number = random.randint(1, 10)

b=int(input("What is your guest?"))
if b>secret_number:
    print("Too high")
elif b<secret_number:
    print("Too low")
else:
    print("You are correct") 
