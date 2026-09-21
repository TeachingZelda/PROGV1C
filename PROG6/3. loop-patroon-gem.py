teller = 0
totaal = 0

while teller < 5:
    totaal = totaal + int(input("Geef een nummer: "))
    teller += 1

print("Gemiddelde is", totaal/teller)
