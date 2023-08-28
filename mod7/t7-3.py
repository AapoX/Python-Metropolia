dictio = {"lentoasemat":[], "icao":[]}



while True:
    
    task = input("Mitä haluaisit tehdä?: Haku[2], Lisäys[1] tai Lopetus[0]:")
    
    
    if task == "1":
        print("Anna tyhjä ICAO-koodi lopettaaksesi lisäyksen.")
        icaokoodi = input("Anna ICAO-koodi: ")
        
        if icaokoodi in dictio["icao"] or len(icaokoodi) > 4:
            print("Koodi on jo listalla tai ICAO-koodi ei toimi.")
        else:
            dictio["icao"].append(icaokoodi)
            lentoasema = input("Anna lentoaseman nimi: ")
            dictio["lentoasemat"].append(lentoasema)
            
        
        
    
    elif task == "2":
        print("Anna tyhjä ICAO-koodi lopettaaksesi haun.")
        icaokoodih = input("Anna ICAO-koodi: ")
        if icaokoodih in dictio["icao"]:
            print(dictio["lentoasemat"][dictio["icao"].index(icaokoodih)])
                
    elif task == "0":
        print("Kiitos käytöstä!")
        break
    
    if task == "":
        break

