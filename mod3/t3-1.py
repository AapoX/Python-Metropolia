plength = int(input("Enter the length of the pike in cm: "))

minlength = 37

if plength < minlength:
    print("The pike is too small. release back to water.")
    print (f"It's {minlength - plength} cm too short.")
else:
    print("The pike is big enough. Keep it if u want.")
