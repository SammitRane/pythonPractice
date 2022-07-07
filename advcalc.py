def add(num1,num2):
	return num1+num2

def subtract(num1,num2):
	return num1-num2

def multiply(num1,num2):
	return num1*num2

def divide(num1,num2):
	return num1/num2	

flag = True

while(flag):
	op = int(input('''Choose the operation>>\n 1. Addition\n 2. Subtraction\n 3. Multiplication\n 4.Divison\n'''))
        a = int(input("Enter the first number >>"))
        b = int(input("Enter the second number"))


	if (op==1):
		print("Addition is ",add(a,b))
		cont = input("Do you want to continue? Press (Y/N) >>")
		if(cont = "Y"):
			flag = True
		else:
			flag = False
	elif(op==2):
		print("Subtraction is ",subtract(a,b))
		cont = input("Do you want to continue? Press (Y/N) >>")
		if(cont = "Y"):
			flag = True
		else:
			flag = False		
	elif(op==3):
		print("Multiplication is ",multiply(a,b))
		cont = input("Do you want to continue? Press (Y/N) >>")
		if(cont = "Y"):
			flag = True
		else:
			flag = False		
	elif(op==4):
		print("Division is ",divide(a,b))
		cont = input("Do you want to continue? Press (Y/N) >>")
		if(cont = "Y"):
			flag = True
		else:
			flag = False		
	else:
		print("!!!INVALID CHOICE!!!")	


