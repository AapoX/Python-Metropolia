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

class Talo:
    def __init__(self, alin_kerros, ylim_kerros, hissien_lkm):
        self.hissit = []
        for i in range(hissien_lkm):
            hissi = Hissi(alin_kerros, ylim_kerros)
            self.hissit.append(hissi)

    def aja_hissia(self, hissin_nro, kohde_kerros):
        hissi = self.hissit[hissin_nro-1]
        hissi.siirry_kerrokseen(kohde_kerros)

def main():
    talo = Talo(1, 10, 2)
    talo.aja_hissia(1, 5)
    talo.aja_hissia(2, 8)

if __name__ == "__main__":
    main()