number1 = int(input("Enter the 1st number >> "))
number2 = int(input("Enter the 2nd number >> "))
number3 = int(input("Enter the 3rd number >> "))

if number1 == number2 == number3:
    print("All numbers are equal")
else:
    if (number1 > number2) and (number1 > number3):
        print(number1, " is the greatest number")
    elif (number2 > number1) and (number2 > number3):
        print(number2, " is the greatest number")
    else:
        print(number3, " is the greatest number")
