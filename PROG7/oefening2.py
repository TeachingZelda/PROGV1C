telefoonboek = { "Zelda": "061234567"}

naam = input("Wie zoekt u? ")
nummer = telefoonboek.get(naam, 'werd niet gevonden')
print(f"Het nummer van {naam}: {nummer}")

nummer = input("Bij welk nummer zoekt u een naam? ")
if nummer not in telefoonboek.values():
    print("Nope")
else:
    for key,value in telefoonboek.items():
        if value == nummer:
            print("De naam is", key)
