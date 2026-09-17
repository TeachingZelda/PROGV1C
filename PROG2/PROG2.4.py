prijs = input("Wat is de prijs van het drankje?")
inworp = input("Wat is het betaalde bedrag?")

wisselgeld = int(inworp) - int(prijs)

type_munten = [50, 20, 10, 5, 2, 1]
aantal_munten = [0,0,0,0,0,0]

for i in range(0,len(type_munten)):
    aantal_munten[i] = wisselgeld // type_munten[i]
    wisselgeld = wisselgeld % type_munten[i]

for i in range(0,len(type_munten)):
    print("Aantal munten van " + str(type_munten[i]) + " cent: " + str(aantal_munten[i]))
