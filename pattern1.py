from re import A


i = 1
while i < 5:
    print("#", end="")
    j = 1
    while j <= 4:
        print("#", end="")
        j += 1
    i += 1
    print()
    
    a=2
    b=a
    
    print(id(a))
    print(id(b))