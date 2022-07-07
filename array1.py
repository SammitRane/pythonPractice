from array import *

n = int(input("Please enter the length of the array>> "))
arr = array('i',[])

for i in range (n):
    x=int(input("Enter the element of the array>> "))
    arr.append(x)

largest=arr[0]

for i in range(n):
    if(arr[i]>largest):
        largest=arr[i]

print(largest)
print(arr)
