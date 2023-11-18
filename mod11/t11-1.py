class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        print(f"Kirjan nimi: {self.nimi}\nKirjoittaja: {self.kirjoittaja}\nSivumäärä: {self.sivumaara}")

class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        print(f"Lehden nimi: {self.nimi}\nPäätoimittaja: {self.paatoimittaja}")

def main():
    lehti = Lehti("Aku Ankka", "Aki Hyyppä")
    lehti.tulosta_tiedot()

    kirja = Kirja("Hytti n:o 6", "Rosa Liksom", 200)
    kirja.tulosta_tiedot()

if __name__ == "__main__":
    main()