class Auto:
    def __init__(self, rekkari, huippunopeus):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def aseta_nopeus(self, nopeus):
        self.nopeus = min(max(nopeus, 0), self.huippunopeus)

    def aja(self, tunnit):
        self.matka += self.nopeus * tunnit

    def tulosta_tiedot(self):
        print(f"Rekisterinumero: {self.rekkari}\nNopeus: {self.nopeus} km/h\nMatka: {self.matka} km")

class Sahkoauto(Auto):
    def __init__(self, rekkari, huippunopeus, akkukapasiteetti):
        super().__init__(rekkari, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self, rekkari, huippunopeus, tankin_koko):
        super().__init__(rekkari, huippunopeus)
        self.tankin_koko = tankin_koko

def main():
    sahkoauto = Sahkoauto("ABC-15", 180, 52.5)
    sahkoauto.aseta_nopeus(120)
    sahkoauto.aja(3)
    sahkoauto.tulosta_tiedot()

    polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)
    polttomoottoriauto.aseta_nopeus(100)
    polttomoottoriauto.aja(3)
    polttomoottoriauto.tulosta_tiedot()

if __name__ == "__main__":
    main()