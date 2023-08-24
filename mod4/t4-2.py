while True:
    tuuma = int(input("Anna tuuma: "))
    cm = tuuma * 2.54
    if tuuma < 0:
        break
    print("Tuuma on", cm, "senttimetriä")