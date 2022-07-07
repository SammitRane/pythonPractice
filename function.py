def testFunction(name):
	print("Hello, "+name)
	print("How you doin")

def add(num1, num2):
	sum1 = num1+num2
	return sum1

name = input("Please enter your name >>")
testFunction(name)

sum = add(3,2)
print(sum)