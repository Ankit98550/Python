def OddEvenTest():
    try:
        num = int(input("Please Enter Number"))
        if type(num)==int:
            if num%2==0:
                print(f"Number is {num} even")
            else:
                print(f"Number is {num} odd.")
    except ValueError:
        print("Please enter an Integer")
#OddEvenTest()

# If you dont want to stop the program after wrong entry use While loop

def ContOddEvenTest():
    while True:
        try:
            num= int(input("Enter an Integer Value"))
            break
        except ValueError:
            print("Please Enter a Integer Value")
    if num%2==0:
        print(f"Number is {num} Even")
    else:
        print(f"Number is {num} Odd")
ContOddEvenTest()