def code(invoerstring):
    resultaat = ""
    for teken in invoerstring:
        nummer = ord(teken)
        nummer = nummer + 3
        nieuw_teken = chr(nummer)
        resultaat = resultaat + nieuw_teken
    return resultaat


naam = input("Voer je naam in: ")
beginstation = input("Voer het beginstation in: ")
eindstation = input("Voer het eindstation in: ")

invoer = naam + beginstation + eindstation

print(code(invoer))