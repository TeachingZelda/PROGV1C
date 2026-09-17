# Schrijf Python-expressies om de volgende vragen te beantwoorden:
# a. Komt 'sch' voor in s1?
# b. Komt de spatie niet voor in s2?
# c. Wat is de gecombineerde tekst van s1, s2 en s3?
# d. Wat is de 13e letter van s2?
# e. Is de 13e letter van s1 gelijk aan de 9e letter van s3?
# f. Is de lengte van 20 keer s3 achter elkaar geplakt groter dan 200?

s1 = 'Hogeschool Utrecht'
s2 = 'Heidelberglaan'
s3 = 'Programming'

print( 'sch' in s1)
print( ' ' not in s2)
print(s1 + s2 + s3)
print(s1[12])
print(s1[12] == s2[8])
print(len(s3*20) > 200)