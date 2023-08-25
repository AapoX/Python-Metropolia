
numcheck = False
while True:
    num = int(input("Anna luku: "))
    if num == 1:
        print(num, "Ei ole alkuluku")
    elif num > 1:
        for i in range (2, num):
            if (num % i) == 0:
                numcheck = True
                break
            
        if numcheck:
            print(num, "ei ole alkuluku")
            break
        else:
            print(num, "on alkuluku")
            break