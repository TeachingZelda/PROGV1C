# 1. Maak huisgenoten.txt aan.
# 2. Zet per regel een naam en leeftijd, gescheiden door een komma.
# 3. Lees het bestand en print per persoon:
#    NAAM: volwassen / kind / baby
# 4. Print het aantal huisgenoten en de som van hun leeftijden.

bestand = open("huisgenoten.txt", "r")
regels = bestand.readlines()
som_leeftijden = 0
aantal = len(regels)

for regel in regels:
    lijst = regel.split(",")
    naam = lijst[0].upper()
    leeftijd = int(lijst[1])
    som_leeftijden = som_leeftijden + leeftijd
    if leeftijd < 1:
        print(f'{naam}: Baby')
    elif leeftijd < 18:
        print(f'{naam}: Kind')
    else:
        print(f'{naam}: Volwassen')

print(f'aantal {aantal}, totale leeftijd {som_leeftijden}')

