# Reverse a String using for loop
def reverseString():
    k=''
    string = input("Enter a String : ")
    for x in range((len(string)-1),-1,-1):
        k=k+string[x]
    print(k)

#reverseString()

# Reverse a String using for without loop
def ReverseString():
    string = input("Enter you String you want to reverse : ")
    k=list(string)
    print("".join(k[::-1]))
#ReverseString()

# Check Palindrome
def checkPalindrome():
    string = input("Enter String : ")
    k=string[::-1]
    print(string, "is a palindrom" if k==string else "it is not a palindrome")

# checkPalindrome()

# Count Vowels:
def countVowels():
    vowels = ['A','E','I','O','U','a','e','i','o','u']
    i=0
    string = input("Enter a string : ")
    for x in string:
        if(x in vowels):
            i+=1
    print(i)
# countVowels()

# Convert Upper Case or Lower case
string =input("Enter a string : ")
print("Press 1 for Upper Case string")
print("Press 2 for Lower Case string")
opt =input("Enter integer as mention above : ")
print(string.upper() if opt == "1" else string.lower() if opt == "2" else "Invalid entry")
