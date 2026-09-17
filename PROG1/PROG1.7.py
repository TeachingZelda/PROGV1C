# De tuple letters kan in willekeurige volgorde
# de letters A, B en C bevatten.
#
# Bijvoorbeeld:
#
# letters = ('A', 'C', 'B', 'B', 'C', 'A', 'C', 'C', 'B')
#
# Neem deze tuple over en schrijf code waarmee je een nieuwe lijst
# maakt met het aantal voorkomens van de letters A, B en C,
# in alfabetische volgorde.
#
# In het bovenstaande voorbeeld bevat letters:
# - 2 keer 'A'
# - 3 keer 'B'
# - 4 keer 'C'
#
# De lijst die het programma maakt en print is dan:
#
# [2, 3, 4]

letters = ('A', 'C', 'B', 'B', 'C', 'A', 'C', 'C', 'B')

hoeveelheid = [letters.count('A'), letters.count('B'), letters.count('C')]
print(hoeveelheid)