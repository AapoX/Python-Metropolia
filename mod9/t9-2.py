class Auto:
    def __init__(self, rekkari, nopeus, kmatka):
        self.rekkari = rekkari
        self.nopeus = nopeus
        self.kmatka = kmatka
        self.huippunopeus = 200

    def kiihdyta(self, nmuutos):
        uusi_nopeus = self.nopeus + nmuutos
        self.nopeus = min(max(uusi_nopeus, 0), self.huippunopeus)


def main():
    rekkari = input("Anna rekkari: ")
    nopeus = input("Anna nopeus: ")
    kmatka = input("Anna matkan pituus: ")

    auto = Auto(rekkari, int(nopeus), kmatka)

    print(f"Rekisteritunnus:  {auto.rekkari}")
    print(f"Auton nopeus: {auto.nopeus}")
    print(f"Matkan pituus: {auto.kmatka}")

    auto.kiihdyta(30)
    auto.kiihdyta(70)
    auto.kiihdyta(50)

    print(f"Uusi auton nopeus: {auto.nopeus}")

if __name__ == "__main__":
    main()