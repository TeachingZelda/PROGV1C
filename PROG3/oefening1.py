# 1. Laat de gebruiker een getal invoeren.
#       Als het getal positief is,
#       print je ‘Dit getal is positief’.
# 2. Vraag de leeftijd van de gebruiker.
#       Als deze 18 jaar of ouder is,
#       print dan: ‘Je bent volwassen’!
# 3. Laat de gebruiker een zin invoeren.
#       Print ‘Deze zin bevat de letter “a”!’
#       als dat zo is.




getal = input("Geef een getal")
if int(getal) >= 0:
    print("Dit getal is positief")

leeftijd = input("Wat is je leeftijd")
if int(leeftijd) >= 18:
    print("Je bent volwassen!")

zin = input("Geef een zin")
if "a" in zin:
    print("Deze zin bevat de letter a")