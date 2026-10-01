# Schrijf een programma waarin de gebruiker drie getallen kan
# invullen. Print vervolgens het middelste (qua grootte) getal.

getal1 = int(input("geef eerste getal "))
getal2 = int(input("geef tweede getal "))
getal3 = int(input("geef derde getal "))

lijst = [getal1, getal2, getal3]
lijst.sort()

print(f'het middelste getal is {lijst[1]}')


