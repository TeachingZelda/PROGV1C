telefoonboek = { "Zelda": "061234567"}

naam = input("Wie wilt u verwijderen? ")

if naam not in telefoonboek:
    print(f"{naam} staat er niet in")
else:
    telefoonboek.pop(naam)
    print(f"{naam} is verwijderd!")
