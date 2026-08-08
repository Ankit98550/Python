# Check whether a year is a leap year.
def IsLeapYear():
    while True:
        try:
            year = int(input("Enter a year"))
            if(year not in range(1,10000)):
                print("Enter a Year range B/W 1 to 9999")
                False
            else:
                break
        except ValueError:
            print("Enter a Year range B/W 1 to 9999")

    if(year%4==0 or year%400==0):
        print(f"It is a Leap Year")
    else:
        print(f"It is not a leap year")

#IsLeapYear()

# Check whether a person is eligible to vote.
def EligibleVoter():
    while True:
        try:
            age = int(input("Enter your age : "))
            if age<0 or age >120:
                print("please Enter correct age")
                
        except ValueError:
            print("Please enter correct age")
    if(age>=18):
        print("You are eligible to Vote")
    else:
        print("You are not eligible to vote")

EligibleVoter()
