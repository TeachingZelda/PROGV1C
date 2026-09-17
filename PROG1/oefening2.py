# 1. Definieer drie numerieke variabelen: var1, var2 en var3.
#    Bereken het gemiddelde en sla dit op in de variabele gemiddelde.
#    Toon het gemiddelde.
#
# 2. Bepaal met de functies max() en min() wat de grootste
#    en kleinste waarden zijn. Toon beide waarden.
#
# 3. Print het gemiddelde, afgerond op 3 decimalen.

var1 = 30
var2 = 40.5
var3 = 50

gemiddelde = (var1 + var2 + var3) / 3
print(gemiddelde)

print(max(var1, var2, var3))

print(min(var1, var2, var3))

print(round(gemiddelde, 3))
