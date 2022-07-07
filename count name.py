def countName(names):
    count = 0
    for name in names:
        if(len(name) > 5):
            count = count + 1
    return count


non = int(input("Please enter the number of names>> "))
names = []
for i in range(non):
    name = input("Please enter the name>> ")
    names.append(name)

print("{} name(s) have length greater than 5".format(countName(names)))
