import random

class Auto:
    def __init__(self, rekkari, nopeus, kmatka):
        self.rekkari = rekkari
        self.nopeus = nopeus
        self.kmatka = kmatka
        self.huippunopeus = random.randint(100, 200)
        self.kuljettu_matka = 0

    def kiihdyta(self, nmuutos):
        uusi_nopeus = self.nopeus + nmuutos
        self.nopeus = min(max(uusi_nopeus, 0), self.huippunopeus)

    def kulje(self):
        self.kuljettu_matka += self.nopeus

    def __str__(self):
        return f"{self.rekkari}\t{self.nopeus}\t{self.kmatka}\t{self.kuljettu_matka}"

class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            auto.kiihdyta(random.randint(-10, 15))
            auto.kulje()

    def tulosta_tilanne(self):
        print("Rekkari\tNopeus\tMatka\tKuljettu matka")
        for auto in self.autot:
            print(auto)

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus:
                return True
        return False

def main():
    autot = []
    for i in range(10):
        rekkari = f"ABC-{i+1}"
        nopeus = 0
        kmatka = 0
        auto = Auto(rekkari, nopeus, kmatka)
        autot.append(auto)

    kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

    tunti = 0
    while not kilpailu.kilpailu_ohi():
        kilpailu.tunti_kuluu()
        tunti += 1
        if tunti % 10 == 0:
            kilpailu.tulosta_tilanne()

    kilpailu.tulosta_tilanne()

if __name__ == "__main__":
    main()