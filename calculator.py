a=float(input("Enter the first number >>"))
b=float(input("Enter the second number >>"))
operation=input("Choose the operation among +,-,*,/ >>")

if operation=="+":
	print("Addition is ",(a+b))
elif operation=="-":
	print("Subtraction is ",(a-b))
elif operation=="*":
	print("Multiplication is ",(a*b))
elif operation=="/":
	print("Divison is ",(a/b))
else:
	print("Invalid choice!")
