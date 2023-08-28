dictio = {"lentoasemat":[], "icao":[]}



while True:
    
    task = input("Mitä haluaisit tehdä?: Haku, Lisäys tai Lopetus:")
    
    
    if task == "Lisäys":
        print("Anna tyhjä ICAO-koodi lopettaaksesi lisäyksen.")
        while True:
            icaokoodi = input("Anna ICAO-koodi: ")
            dictio["icao"].append(icaokoodi)
            lentoasema = input("Anna lentoaseman nimi: ")
            if icaokoodi or lentoasema == "":
                break
            dictio["lentoasemat"].append(lentoasema)
        
    
    elif task == "Haku":
        print("Anna tyhjä ICAO-koodi lopettaaksesi haun.")
        while True:
            icaokoodih = input("Anna ICAO-koodi: ")
            if icaokoodih in dictio["icao"]:
                print(dictio["lentoasemat"][dictio["icao"].index(icaokoodih)])
                
            elif icaokoodih == "":
                break
    
    elif task == "Lopetus":
        print("Kiitos käytöstä!")
        break
    
    if task == "":
        break

