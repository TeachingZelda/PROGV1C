# 1. Laat de gebruiker een getal invoeren.
#       Als het getal positief is,
#       print je ‘Dit getal is positief’.
# 2. Vraag de leeftijd van de gebruiker.
#       Als deze 18 jaar of ouder is,
#       print dan: ‘Je bent volwassen’!
# 3. Laat de gebruiker een zin invoeren.
#       Print ‘Deze zin bevat de letter “a”!’
#       als dat zo is.

getal = int(input("Geef een getal "))
if getal > 0:
    print("het getal is positief")

leeftijd = int(input("Geef je leeftijd "))
if leeftijd > 18:
    print("Je bent volwassen")
if leeftijd < 18:
    print("Je bent niet volwassen")

zin = str(input("voer een zin in "))
if "a" in zin:
    print("Deze zin bevat een a")

