def vuodenaika(kuukausi):
    kaudet = {
        1: "Talvi", 2: "Talvi", 3: "Kevät", 4: "Kevät", 5: "Kevät", 6: "Kesä", 7: "Kesä", 8: "Kesä", 9: "Syksy", 10: "Syksy", 11: "Syksy", 12: "Talvi"
    }
    return kaudet.get(kuukausi, "Virheellinen syöte!")

def main():
    kuukausi = int(input("Anna kuukauden numero: "))
    if kuukausi < 1 or kuukausi > 12:
        print("Virheellinen syöte!")
    else:
        kaudet = vuodenaika(kuukausi)
        print("Kuukausi", kuukausi, "on", kaudet)
        
if __name__ == "__main__":
    main()