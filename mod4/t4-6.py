import random

def plikiarvo(pisteet):
    x = random.uniform(1, -1)
    y = random.uniform(1, -1)
    
    i = 0
    
    if x**2 + y**2 <= 1:
        i += 1
        
    plikiarvo = 4 * i / pisteet
    return plikiarvo

def main():
    pisteet = int(input("Montako pistettä? "))
    
    if pisteet <= 0:
        print("Virheellinen syöte!")
        
    else:
        print("Piin likiarvo on", plikiarvo(pisteet))
        
        
if __name__ == "__main__":
    main()
