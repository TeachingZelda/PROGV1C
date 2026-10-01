# De afstand tussen twee coördinaten kan je uitrekenen
# met de volgende formule:
# afstand = ((x2 - x1)**2 + (y2-y1)**2)**0.5
#
# Schrijf een programma waarin de gebruiker twee coördinaten
# moet invoeren. Print de afstand (afgerond op 4 decimalen).
# Let op: worteltrekken doe je met math.sqrt() of
# machtsverheffen met exponent 0.5!

x1 = int(input("Geef x1 "))
x2 = int(input("Geef x2 "))
y1 = int(input("Geef y1 "))
y2 = int(input("Geef y2 "))

afstand = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

print(f'De afstand is {afstand}')
