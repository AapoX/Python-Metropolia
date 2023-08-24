sukupuoli = input("Anna sukupuoli (M/N): ")
hemoglo = int(input("Anna hemoglobiini: "))

if sukupuoli == "M":
    print("Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l")
    if hemoglo < 134:
        print("Hemoglobiiniarvo on liian pieni")
    elif hemoglo > 195:
        print("Hemoglobiiniarvo on liian suuri")
    else:
        print("Hemoglobiiniarvo on normaali")
        
if sukupuoli == "N":
    print("Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l")
    if hemoglo < 117:
        print("Hemoglobiiniarvo on liian pieni")
    elif hemoglo > 175:
        print("Hemoglobiiniarvo on liian suuri")
    else:
        print("Hemoglobiiniarvo on normaali")
        
