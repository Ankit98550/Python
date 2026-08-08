# Grade calculator (A/B/C/D/F).
def gradeCalc():
    try:
        number = int(input("Enter your Marks : "))
        if(number >100):
            print("Marks are not greater than 100")
        elif number >=90 :
            print("Your grade is A")
        elif number >70 and number <91:
                print("Your grade is b")
        elif number >50 and number <71 :
                print("Your grade is c")
        elif number > 40 and number <51:
              print("Your grade is D")
        else:
             print("Your grade is F")
    except ValueError:
        print("Please Enter Correct Marks")

gradeCalc()