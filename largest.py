a = float(input("Enter the first number>> "))
b = float(input("Enter the second number>> "))
c = float(input("Enter the third number>> "))

if(a>b):
	if(a>c):
		print("Largest number is ",a)
	else:
		print("Largest number is ",c)
else:
	if(b>c):
		print("Largest number is ",b)
	else:
		print("Largest number is ",c)	
