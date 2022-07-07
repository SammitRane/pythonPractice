#Understanding for loop
table = int(input("Enter the number whose table you want>> "))

tables = range(1,table+1)
numbers = range(1,11)
#languages = ["Java", "Python","C++"]
#sum=0
#for language in languages:
#	print(language)
for iteration in tables:
	for number in numbers:
		print(iteration," * ",number,"= ",(iteration*number))
