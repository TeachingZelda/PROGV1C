bestand = open("V1C.txt", 'r')
mooibestand = bestand.read()
print(mooibestand)

regels = bestand.readlines()

print(len(regels))

for regel in regels:
    print(regel)

bestand.close()
