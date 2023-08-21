import math

massa = 0
leivisko = float(input("Anna massa leivisköinä:"))
naula = float(input("Anna massa nauloina:"))
luoti = float(input("Anna massa luoteina:"))

luotip = 13.3
naulap = luotip * 32
leiviskop = naulap * 20


leivisko = leivisko * leiviskop
naula = naula * naulap
luoti = luoti * luotip

total = leivisko + naula + luoti
gr, kg = math.modf(total)






print("Massa nykymittojen mukaan:")

print(round(kg / 1000, 0), "kilogrammaa")
print(round(gr, 5), "grammaa")