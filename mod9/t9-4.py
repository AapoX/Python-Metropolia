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

def main():
    autot = []
    for i in range(10):
        rekkari = f"ABC-{i+1}"
        nopeus = 0
        kmatka = 0
        auto = Auto(rekkari, nopeus, kmatka)
        autot.append(auto)

    while True:
        for auto in autot:
            auto.kiihdyta(random.randint(-10, 15))
            auto.kulje()

            if auto.kuljettu_matka >= 10000:
                break

        if auto.kuljettu_matka >= 10000:
            break

    print("Rekkari\tNopeus\tMatka\tKuljettu matka")
    for auto in autot:
        print(auto)

if __name__ == "__main__":
    main()