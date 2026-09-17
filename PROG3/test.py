cijfer = float(input("Geef het laatst behaalde cijfer [0-10]"))

if cijfer > 5.5:
	behaald = True
elif cijfer < 5.5:
	behaald = False

print("Behaald = "+str(behaald))