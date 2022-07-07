n = int(input("Enter the number to check>> "))
i = 2
flag = False
#while(i<n):
#	if(n%i==0):
#		flag = True
#		break
#	i=i+1

numbers = range(2,n)
for no in numbers:
	if(n%no==0):
		flag = True
		break;

if(flag):
	print("It is not a prime number")
else:
	print("It is a prime number")