from random import randint

num = randint(0, 10)

while True:
    guess = int(input("Arvaa numero 0-10 välillä: "))
    
    if guess < num:
        print("Liian pieni arvaus.")
    elif guess > num:
        print("Liian suuri arvaus.")
    else:
        print("oikein.")
        break