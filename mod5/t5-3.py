
numcheck = False
while True:
    num = int(input("Anna luku: "))
    if num == 1:
        print(num, "On alkuluku")
    elif num > 1:
        for i in range (2, num):
            if num % i == 0:
                numcheck = True
                break
            
    if numcheck:
        print(num, "ei ole alkuluku")
    else:
        print(num, "on alkuluku")