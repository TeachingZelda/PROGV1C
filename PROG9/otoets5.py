# Schrijf een functie isPositiefEnKleinerDan(x, y)
# waarin je bepaalt of gegeven getal ‘x’ een positief getal
# is, en kleiner dan getal ‘y’.
# De parameters x en y zijn van het type int.
# De functie geeft True terug als dat zo is,
# anders False.

def isPositiefEnKleinerDan(x,y):
    if (x > 0) and (x < y):
        resultaat = True
    else:
        resultaat = False
    return resultaat

print(isPositiefEnKleinerDan(-2,-3))