from random import randint
summa = 0
i = 0
num = int(input("Anna arpakuutioiden määrä: "))

for i in range(num):
    arpa = randint(0, 6)
    print(arpa)
    summa += arpa
    i += 1
print(" ")
print(summa)
    
    