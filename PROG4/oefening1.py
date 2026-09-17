# Schrijf (en test) de functie gemiddelde() die 2 parameters heeft:
# 	getal1 en getal2. Print het gemiddelde van deze parameters!
#
# Voeg een extra parameter toe (getal3),
# 	bepaal het gemiddelde van de 3 parameters,
# 	en print weer het resultaat
#
# Schrijf een functie cirkel_oppervlakte() met 1 parameter: straal.
# 	Bereken en print vervolgens de oppervlakte en omtrek van een cirkel met de gegeven straal.
# 	Gebruik π uit de module ‘math’.

def gemiddelde(getal1, getal2):
    resultaat = (getal1 + getal2) / 2
    print(resultaat)


def gemiddelde(getal1, getal2, getal3):
    resultaat = (getal1 + getal2 + getal3) / 3
    print(resultaat)


def cirkel_oppervlakte(straal):
    print(math.pi * straal ** 2)


gemiddelde(42, 53)
gemiddelde(42, 53, 3)
cirkel_oppervlakte(32)
