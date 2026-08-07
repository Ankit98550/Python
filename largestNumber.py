# Find the largest number from three numbers
def LargestNumber():
    while True:
        try:
            a=int(input("Enter First Number : "))
            b=int(input("Enter Second Number : "))
            c=int(input("Enter Third Number : "))
            break
        except ValueError:
            print("Please Enter a Integer Value")
    if a==b==c: 
        print("All values are Equal")
    elif a>=b and a>=c:
        print(f"{a} is greater than {b} and {c}")
    elif b>=a and b>=c:
        print(f"{b} is greater than {a} and {c}")
    else:
        print(f"{c} is greater than {a} and {b}")

LargestNumber()