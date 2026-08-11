# Find Maximum and Minimum in a list
numlst =[5,10,25,15,20]
# Sort Method sorts the list in place, meaning it modifies original list directly and returns None
numlst.sort()
print(numlst[-1])

x = [2,4,10,6,8]
# sorted methods takes arguments in method.
y=sorted(x)
print(y)

# Calculate Sum
x=[2,4,6,8,10]
i=0
for y in x:
     i+=y
print(x, "sum of the list is ",i)

# Count Even and Odd numbers
lst =[2,3,6,8,9,10]
odd=0;even=0
for x in lst:
     if x%2==0:
          odd+=1
     else:
          even+=1
print(lst, f"Odd numbers are {odd} and even number are {even}")

# Reverse a list
def reverseList(lst):
    y=[]
    for x in range((len(lst)-1),-1,-1):
        y.append(lst[x])
    print(y)
# reverseList(lst)

# Remove Duplicates
lst2=[2,4,2,4,2,6,8,4]
lst1=set(lst2)    
print("Duplicates item removed",lst1)

# search for an element
searchNum = int(input("Enter element to search : "))
lst=[10,4,8,13,15]
if searchNum in lst:
    print(searchNum, f"is present")
else:
    print("Element not found")