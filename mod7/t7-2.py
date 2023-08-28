nimet = []
while True: 
    nimi = input("Nimi: ")
    
    if nimi[-1] == "":
        for i in range(len(nimet)):
            print(nimet[i])
            break

    if nimi in nimet:
        print(f"{nimi} on jo listalla.")
        
    else:
        print("Uusi nimi")
        nimet.append(nimi)

            
