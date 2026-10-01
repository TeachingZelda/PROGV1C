# Schrijf een programma waarin een gebruiker getallen moet
# invoeren. Dit gaat door totdat de gebruiker ‘stop’ intoetst.
# De getallen moeten met elkaar vermenigvuldigd worden.
# Print het resultaat.

getal = 1
while True:
    invoer = input("Voer een getal in ")
    if invoer == "stop":
        break
    getal = getal * int(invoer)

print(getal)


