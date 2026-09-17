afstand = float(input('Afstand (km)? '))
uren = int(input('Tijd (uren)? '))
snelheid = afstand/uren

if snelheid < 4:
    print('Rustig tempo')
elif snelheid <= 6:
    print('Gemiddeld tempo')
else:
    print('Vlot tempo')
