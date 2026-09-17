maand = int(input("Wat is het maandnummer? "))

if maand < 3 or maand > 11:
    print("Het is winter")
elif maand >= 3 and maand <= 5:
    print("Het is lente")
elif maand >= 6 and maand <= 8:
    print("Het is zomer")
elif maand >= 9 and maand <= 11:
    print("Het is herfst")
elif maand < 1 or maand >= 13:
    print("ongeldig")
