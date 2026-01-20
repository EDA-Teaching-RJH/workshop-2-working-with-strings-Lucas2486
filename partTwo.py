import math  

def main():
    A = int(input("What is length A?"))
    B = int(input("What is length B?"))
    C = pythag(A,B)
    print(C)

def pythag(A,B):
    return math.sqrt(A**2 + B**2)

main()
