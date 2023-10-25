class Auto:
    def __init__(self, rekkari, nopeus, kmatka):
        self.rekkari = rekkari
        self.nopeus = nopeus
        self.kmatka = kmatka
        self.huippunopeus = 200
        self.kuljettu_matka = 0

    def kiihdyta(self, nmuutos):
        uusi_nopeus = self.nopeus + nmuutos
        self.nopeus = min(max(uusi_nopeus, 0), self.huippunopeus)

    def kulje(self, tuntimaara):
        self.kuljettu_matka += self.nopeus * tuntimaara

    def __str__(self):
        return f"Rekisteritunnus: {self.rekkari}\nAuton nopeus: {self.nopeus}\nMatkan pituus: {self.kmatka}\nKuljettu matka: {self.kuljettu_matka}"

def main():
    rekkari = input("Anna rekkari: ")
    nopeus = input("Anna nopeus: ")
    kmatka = input("Anna matkan pituus: ")

    auto = Auto(rekkari, int(nopeus), int(kmatka))

    print(auto)

    auto.kiihdyta(30)
    auto.kiihdyta(70)
    auto.kiihdyta(50)

    print(f"Uusi auton nopeus: {auto.nopeus}")

    auto.kulje(1.5)

    print(auto)

if __name__ == "__main__":
    main()