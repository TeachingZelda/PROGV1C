# Schrijf booleaanse expressies die met de variabelen uit
# oefening PROG1.3 evalueren of:
#
# 1. 6.75 groter is dan a en kleiner is dan b.
#
# 2. De lengte van mijnnaam gelijk is aan de som van de lengtes
#    van voornaam, tussenvoegsel en achternaam.
#
# 3. De lengte van mijnnaam minstens 5 keer zo groot is
#    als de waarde van variabele c.
#
# 4. De waarde van variabele tussenvoegsel voorkomt
#    in de waarde van variabele achternaam.

a = 6
b = 7
c = (a + b)/2

voornaam = "Zelda"
tussenvoegsel = ""
achternaam = "Zeegers"
mijnnaam = voornaam + " " + tussenvoegsel + " " + achternaam

print(6.75 > a and 6.75 < b)
print(len(mijnnaam) == len(voornaam) + len(tussenvoegsel) + len(achternaam))
print(len(mijnnaam) > 5*c)
print(tussenvoegsel in mijnnaam)