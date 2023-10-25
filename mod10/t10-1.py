class Hissi:
    def __init__(self, alin_kerros, ylim_kerros):
        self.kerros = alin_kerros
        self.alin_kerros = alin_kerros
        self.ylim_kerros = ylim_kerros

    def siirry_kerrokseen(self, kohde_kerros):
        if kohde_kerros < self.alin_kerros:
            self.kerros_alas(kohde_kerros)
        elif kohde_kerros > self.ylim_kerros:
            self.kerros_ylos(kohde_kerros)
        else:
            while self.kerros != kohde_kerros:
                if self.kerros < kohde_kerros:
                    self.kerros_ylos()
                else:
                    self.kerros_alas()

    def kerros_ylos(self, kohde_kerros=None):
        if kohde_kerros is None:
            kohde_kerros = self.kerros + 1
        if kohde_kerros <= self.ylim_kerros:
            self.kerros = kohde_kerros
            print(f"Hissi on kerroksessa {self.kerros}")
        else:
            print("Hissi ei voi nousta ylemmäs")

    def kerros_alas(self, kohde_kerros=None):
        if kohde_kerros is None:
            kohde_kerros = self.kerros - 1
        if kohde_kerros >= self.alin_kerros:
            self.kerros = kohde_kerros
            print(f"Hissi on kerroksessa {self.kerros}")
        else:
            print("Hissi ei voi laskea alemmas")

def main():
    hissi = Hissi(1, 5)
    hissi.siirry_kerrokseen(3)
    hissi.siirry_kerrokseen(5)
    hissi.siirry_kerrokseen(1)

if __name__ == "__main__":
    main()