class Auto:
    def __init__(self, rekkari, nopeus, kmatka):
        self.rekkari = rekkari
        self.nopeus = nopeus
        self.kmatka = kmatka

def main():
    rekkari = input("Anna rekkari: ")
    nopeus = input("Anna nopeus: ")
    kmatka = input("Anna matkan pituus: ")

    auto = Auto(rekkari, nopeus, kmatka)

    print(f"Rekisteritunnus: {rekkari}")
    print(f"Auton nopeus: {nopeus}")
    print(f"Matkan pituus: {kmatka}")

if __name__ == "__main__":
    main()