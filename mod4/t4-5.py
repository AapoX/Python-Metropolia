user = "python"
passw = "rules"
i = 0
while i <= 5:
    username = input("Anna käyttäjätunnus: ")
    passg = input("Anna salasanasi: ")
    
    
    if username != user or passg != passw:
        print("Pääsy evätty.")
    else:
        print("Tervetuloa!")
        break
    i+=1
