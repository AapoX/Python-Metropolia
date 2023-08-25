import math

def pizza(diameter, price):
    area = math.pi * (diameter / 2) ** 2
    return price / area


def main():
    p1 = float(input("Syötä pizzan halkaisija: "))
    p1h = float(input("Syötä pizzan hinta: "))
    
    p2 = float(input("Syötä pizzan halkaisija: "))
    p2h = float(input("Syötä pizzan hinta: "))
    
    p1 = pizza(p1, p1h)
    p2 = pizza(p2, p2h)
    
    if p1 < p2:
        print("Pizzan 1 hinta-laatu suhde on parempi")
    elif p1 > p2:
        print("Pizzan 2 hinta-laatu suhde on parempi")
    else:
        print("Pizzat ovat yhtä hyviä")
    
    
if __name__ == "__main__":
    main()